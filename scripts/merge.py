#!/usr/bin/env python3
"""Merge raw sweep + critic files into canonical per-unit data files.

Reads  data/raw/<unit>.sweep.json  and  data/raw/<unit>.critic.json,
applies the critic's corrections/removals/additions, normalises and
validates every entry, and writes  data/<unit>.json.

Run from the repository root:  python3 scripts/merge.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data"

# Display titles and site order: disciplines first, cross-cutting after.
UNITS = [
    ("physics", "Physics"),
    ("astronomy", "Astronomy & space science"),
    ("chemistry", "Chemistry & materials science"),
    ("biology", "Biology & life sciences"),
    ("medicine", "Medicine & health sciences"),
    ("earth", "Earth, climate & environmental science"),
    ("mathematics", "Mathematics"),
    ("cs-ml", "Computer science & machine learning"),
    ("neuro-psych", "Neuroscience & psychology"),
    ("social", "Social sciences"),
    ("econ-finance", "Economics & finance"),
    ("humanities", "Linguistics & humanities"),
    ("literature-access", "Literature access & discovery"),
    ("compute", "Free compute & storage"),
    ("publishing", "Publishing, identity & preservation"),
    ("funding", "Funding, grants & recognition"),
    ("learning", "Learning materials"),
    ("workflow-tools", "Research workflow software"),
]
CROSS_CUTTING = {
    "literature-access", "compute", "publishing",
    "funding", "learning", "workflow-tools",
}

CATEGORIES = [
    "data", "software", "literature", "compute",
    "publishing", "funding", "learning", "community",
]
FREE_LEVELS = ["free", "free-registration", "free-tier", "freemium"]
REGISTRATION = ["none", "email", "api-key", "application", "credentialing"]


def norm_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def norm_url(url: str) -> str:
    u = url.strip().rstrip("/")
    u = re.sub(r"^http://", "https://", u)
    u = re.sub(r"^https://www\.", "https://", u)
    return u.lower()


def clean_resource(r: dict, unit: str, problems: list) -> dict | None:
    required = ["name", "url", "category", "summary", "access", "free"]
    for f in required:
        if not str(r.get(f, "")).strip():
            problems.append(f"[{unit}] '{r.get('name', '?')}': missing field '{f}' — dropped")
            return None
    out = {
        "name": str(r["name"]).strip(),
        "url": str(r["url"]).strip(),
        "category": str(r["category"]).strip().lower(),
        "subcategory": str(r.get("subcategory", "")).strip(),
        "summary": str(r["summary"]).strip(),
        "access": str(r["access"]).strip(),
        "free": str(r["free"]).strip().lower(),
        "registration": str(r.get("registration", "none")).strip().lower(),
        "beginner": r.get("beginner", 3),
        "notes": str(r.get("notes", "")).strip(),
    }
    if not out["url"].startswith(("http://", "https://")):
        problems.append(f"[{unit}] '{out['name']}': bad URL '{out['url']}' — dropped")
        return None
    if out["category"] not in CATEGORIES:
        problems.append(f"[{unit}] '{out['name']}': category '{out['category']}' not in enum — kept, flag for review")
    if out["free"] not in FREE_LEVELS:
        problems.append(f"[{unit}] '{out['name']}': free '{out['free']}' not in enum — kept, flag for review")
    if out["registration"] not in REGISTRATION:
        problems.append(f"[{unit}] '{out['name']}': registration '{out['registration']}' not in enum — kept, flag for review")
    try:
        out["beginner"] = max(1, min(5, int(out["beginner"])))
    except (TypeError, ValueError):
        out["beginner"] = 3
    return out


def merge_unit(key: str, title: str, problems: list) -> dict | None:
    sweep_path = RAW / f"{key}.sweep.json"
    critic_path = RAW / f"{key}.critic.json"
    if not sweep_path.exists():
        problems.append(f"[{key}] no sweep file — unit skipped")
        return None
    sweep = json.loads(sweep_path.read_text())
    resources = list(sweep.get("resources", []))

    corrections = removals = additions = 0
    if critic_path.exists():
        critic = json.loads(critic_path.read_text())
        by_key = {norm_key(r.get("name", "")): r for r in resources}
        for c in critic.get("corrections", []):
            target = by_key.get(norm_key(c.get("name", "")))
            if target is not None and c.get("field") in (
                "name", "url", "category", "subcategory", "summary",
                "access", "free", "registration", "beginner", "notes",
            ):
                target[c["field"]] = c.get("new_value")
                corrections += 1
        removed_keys = {norm_key(r.get("name", "")) for r in critic.get("removals", [])}
        before = len(resources)
        resources = [r for r in resources if norm_key(r.get("name", "")) not in removed_keys]
        removals = before - len(resources)
        existing = {norm_key(r.get("name", "")) for r in resources}
        existing_urls = {norm_url(r.get("url", "")) for r in resources}
        for a in critic.get("additions", []):
            if norm_key(a.get("name", "")) in existing:
                continue
            if norm_url(a.get("url", "")) in existing_urls:
                continue
            resources.append(a)
            existing.add(norm_key(a.get("name", "")))
            existing_urls.add(norm_url(a.get("url", "")))
            additions += 1
    else:
        problems.append(f"[{key}] no critic file — sweep used as-is")

    # Clean, then dedupe within the unit by name and by URL.
    cleaned, seen_names, seen_urls = [], set(), set()
    for r in resources:
        c = clean_resource(r, key, problems)
        if c is None:
            continue
        nk, uk = norm_key(c["name"]), norm_url(c["url"])
        if nk in seen_names or uk in seen_urls:
            problems.append(f"[{key}] duplicate within unit: '{c['name']}' — dropped")
            continue
        seen_names.add(nk)
        seen_urls.add(uk)
        cleaned.append(c)

    cat_order = {c: i for i, c in enumerate(CATEGORIES)}
    cleaned.sort(key=lambda r: (cat_order.get(r["category"], 99), r["name"].lower()))

    unit = {
        "unit": key,
        "title": title,
        "kind": "cross-cutting" if key in CROSS_CUTTING else "discipline",
        "generated": sweep.get("generated", ""),
        "resources": cleaned,
    }
    (OUT / f"{key}.json").write_text(json.dumps(unit, indent=2, ensure_ascii=False) + "\n")
    print(f"  {key:20s} {len(cleaned):4d} entries  (+{additions} critic adds, "
          f"{corrections} corrections, -{removals} removals)")
    return unit


def main() -> int:
    problems: list[str] = []
    units = []
    print("Merging units:")
    for key, title in UNITS:
        u = merge_unit(key, title, problems)
        if u:
            units.append(u)

    # Cross-unit URL overlap: allowed, but reported for review.
    seen: dict[str, str] = {}
    overlaps = 0
    for u in units:
        for r in u["resources"]:
            uk = norm_url(r["url"])
            if uk in seen and seen[uk] != u["unit"]:
                overlaps += 1
            else:
                seen.setdefault(uk, u["unit"])

    total = sum(len(u["resources"]) for u in units)
    print(f"\nTotal: {total} entries across {len(units)} units; "
          f"{overlaps} cross-unit URL overlaps (allowed, review if odd).")
    if problems:
        report = ROOT / "data" / "merge-report.txt"
        report.write_text("\n".join(problems) + "\n")
        print(f"{len(problems)} problems logged to {report.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
