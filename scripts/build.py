#!/usr/bin/env python3
"""Generate docs/<unit>.md and index.html from the canonical data files.

The catalogue lives in data/<unit>.json (produced by scripts/merge.py).
This script renders (a) one markdown catalogue per unit in the style of
space-ml-lab's data-sources document, and (b) the self-contained web
page, by injecting the full dataset into web/template.html.

Run from the repository root:  python3 scripts/build.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"

UNIT_ORDER = [
    "physics", "astronomy", "chemistry", "biology", "medicine", "earth",
    "mathematics", "cs-ml", "neuro-psych", "social", "econ-finance", "humanities",
    "literature-access", "compute", "publishing", "funding", "learning",
    "workflow-tools",
]

CATEGORY_TITLES = {
    "data": "Data",
    "software": "Software",
    "literature": "Literature",
    "compute": "Compute",
    "publishing": "Publishing",
    "funding": "Funding",
    "learning": "Learning",
    "community": "Community",
}

FREE_LABELS = {
    "free": "Free",
    "free-registration": "Free (registration)",
    "free-tier": "Free tier",
    "freemium": "Freemium",
}


def flat(text: str) -> str:
    return " ".join(str(text).split())


def free_line(r: dict) -> str:
    label = FREE_LABELS.get(r["free"], r["free"])
    if r["registration"] not in ("", "none"):
        label += f", {r['registration']}"
    return label


def render_entry(r: dict) -> list[str]:
    lines = [
        f"### [{flat(r['name'])}]({r['url']})",
        "",
        f"`{free_line(r)}` · beginner {r['beginner']}/5"
        + (f" · {flat(r['subcategory'])}" if r.get("subcategory") else ""),
        "",
        flat(r["summary"]),
        "",
        f"**Access.** {flat(r['access'])}",
        "",
    ]
    if r.get("notes"):
        lines += [f"**Caveats.** {flat(r['notes'])}", ""]
    if r.get("also_in"):
        lines += [f"*Also listed under: {', '.join(r['also_in'])}.*", ""]
    return lines


def render_unit_md(unit: dict) -> str:
    by_cat: dict[str, list] = {}
    for r in unit["resources"]:
        by_cat.setdefault(r["category"], []).append(r)
    present = [c for c in CATEGORY_TITLES if by_cat.get(c)]

    lines = [
        f"# {unit['title']}",
        "",
        f"Part of [research-vault](../README.md). {len(unit['resources'])} entries, "
        f"verified {unit.get('generated', '')}. Free status and limits change; check "
        "the source before you build on it.",
        "",
        "Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it "
        "in ten minutes, 1 means a specialist toolchain and patience.",
        "",
        "**Contents:** "
        + " · ".join(
            f"[{CATEGORY_TITLES[c]}](#{CATEGORY_TITLES[c].lower()}) ({len(by_cat[c])})"
            for c in present
        ),
        "",
    ]
    for cat in present:
        lines += [f"## {CATEGORY_TITLES[cat]}", ""]
        for r in by_cat.pop(cat):
            lines += render_entry(r)
    # Any non-enum categories at the end so nothing silently disappears.
    for cat, rows in by_cat.items():
        lines += [f"## {cat}", ""]
        for r in rows:
            lines += render_entry(r)
    return "\n".join(lines)


def replace_block(text: str, marker: str, body: str) -> str:
    """Swap the content between <!-- MARKER:START --> and <!-- MARKER:END -->."""
    start, end = f"<!-- {marker}:START -->", f"<!-- {marker}:END -->"
    i, j = text.find(start), text.find(end)
    if i == -1 or j == -1:
        return text
    return text[: i + len(start)] + "\n" + body + "\n" + text[j:]


def refresh_readme(units: list[dict]) -> None:
    """Keep the README's counts true to the data rather than to a memory of it."""
    readme = ROOT / "README.md"
    if not readme.exists():
        return
    canon = [r for u in units for r in u["resources"] if r.get("canonical", True)]
    dates = sorted({u.get("generated", "") for u in units if u.get("generated")})
    stats = (
        f"**{len(canon):,} resources** across **{len(units)} fields** — "
        f"{sum(1 for r in canon if r['free'] == 'free'):,} free outright, "
        f"{sum(1 for r in canon if r.get('registration') == 'none'):,} usable with no account "
        f"at all. Verified {dates[0] if len(dates) == 1 else f'{dates[0]} – {dates[-1]}'}."
    )

    rows = ["| Field | Entries | The deepest part of it |", "|---|---|---|"]
    for u in units:
        by_cat: dict[str, int] = {}
        for r in u["resources"]:
            by_cat[r["category"]] = by_cat.get(r["category"], 0) + 1
        top = sorted(by_cat.items(), key=lambda kv: -kv[1])[:3]
        deepest = ", ".join(f"{CATEGORY_TITLES.get(c, c).lower()} ({n})" for c, n in top)
        doc = f"docs/{UNIT_ORDER.index(u['unit']) + 1:02d}-{u['unit']}.md"
        rows.append(f"| [{u['title']}]({doc}) | {len(u['resources'])} | {deepest} |")
    disciplines = sum(1 for u in units if u.get("kind") != "cross-cutting")
    rows += [
        "",
        f"The first {disciplines} are fields of study. The rest cut across all of them: "
        "the parts of research that are the same whatever you work on.",
    ]

    text = readme.read_text()
    text = replace_block(text, "STATS", stats)
    text = replace_block(text, "FIELDS", "\n".join(rows))
    readme.write_text(text)
    print("  refreshed README counts")


def main() -> int:
    units = []
    for key in UNIT_ORDER:
        path = DATA / f"{key}.json"
        if not path.exists():
            print(f"  (missing {path.name} — skipped)")
            continue
        units.append(json.loads(path.read_text()))

    DOCS.mkdir(exist_ok=True)
    for i, unit in enumerate(units, 1):
        out = DOCS / f"{i:02d}-{unit['unit']}.md"
        out.write_text(render_unit_md(unit))
        print(f"  wrote {out.relative_to(ROOT)} ({len(unit['resources'])} entries)")

    template = ROOT / "web" / "template.html"
    if template.exists():
        payload = json.dumps(units, ensure_ascii=False, separators=(",", ":"))
        payload = payload.replace("</", "<\\/")  # keep inline <script> safe
        html = template.read_text().replace("/*__DATA__*/[]", payload, 1)
        (ROOT / "index.html").write_text(html)
        size_kb = len(html.encode()) / 1024
        print(f"  wrote index.html ({size_kb:.0f} KB)")
    else:
        print("  (web/template.html not found — site not built)")

    refresh_readme(units)

    total = sum(len(u["resources"]) for u in units)
    print(f"Build complete: {len(units)} units, {total} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
