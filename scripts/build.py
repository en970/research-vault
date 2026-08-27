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


def esc(text: str) -> str:
    """Escape pipes/newlines for markdown table cells."""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def render_unit_md(unit: dict) -> str:
    lines = [
        f"# {unit['title']}",
        "",
        f"Part of [research-vault](../README.md). {len(unit['resources'])} entries, "
        f"verified {unit.get('generated', '')} — free status and limits change, so "
        "check the source before you depend on it.",
        "",
        "Beginner rating: 5/5 means a newcomer gets value in ten minutes; 1/5 means "
        "specialist tooling and patience.",
        "",
    ]
    by_cat: dict[str, list] = {}
    for r in unit["resources"]:
        by_cat.setdefault(r["category"], []).append(r)
    for cat in CATEGORY_TITLES:
        rows = by_cat.pop(cat, [])
        if not rows:
            continue
        lines += [f"## {CATEGORY_TITLES[cat]}", ""]
        lines += [
            "| Resource | What it is | Access | Free | Beginner |",
            "|---|---|---|---|---|",
        ]
        for r in rows:
            what = esc(r["summary"])
            if r["notes"]:
                what += f" *{esc(r['notes'])}*"
            free = FREE_LABELS.get(r["free"], r["free"])
            if r["registration"] not in ("", "none"):
                free += f", {r['registration']}"
            lines.append(
                f"| [**{esc(r['name'])}**]({r['url']}) | {what} | {esc(r['access'])} "
                f"| {free} | {r['beginner']}/5 |"
            )
        lines.append("")
    # Any non-enum categories at the end so nothing silently disappears.
    for cat, rows in by_cat.items():
        lines += [f"## {cat}", ""]
        for r in rows:
            lines.append(f"- [**{esc(r['name'])}**]({r['url']}) — {esc(r['summary'])}")
        lines.append("")
    return "\n".join(lines)


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

    total = sum(len(u["resources"]) for u in units)
    print(f"Build complete: {len(units)} units, {total} entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
