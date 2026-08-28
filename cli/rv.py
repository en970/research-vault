#!/usr/bin/env python3
"""rv — search the research-vault catalogue from the terminal.

Standard library only. Reads the canonical data files (data/*.json) from,
in order: --data, $RESEARCH_VAULT_DATA, or the repository this file sits in.

Examples:
  rv search eeg                          # full-text search
  rv search "light curve" -u astronomy   # restrict to one unit
  rv search gpu -c compute --no-signup   # free compute, no account needed
  rv show zenodo                         # full card for one resource
  rv units                               # list units with entry counts
  rv random                              # one serendipitous entry
"""

import argparse
import json
import os
import random
import re
import sys
from pathlib import Path

FREE_LABELS = {
    "free": "free",
    "free-registration": "free, registration",
    "free-tier": "free tier",
    "freemium": "freemium",
}

# ── terminal formatting ────────────────────────────────────────────────────────

USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


def c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text


def bold(t): return c("1", t)
def dim(t): return c("2", t)
def green(t): return c("32", t)
def yellow(t): return c("33", t)
def cyan(t): return c("36", t)


def stars(n: int) -> str:
    return "●" * n + "○" * (5 - n)


def free_tag(r: dict) -> str:
    label = FREE_LABELS.get(r["free"], r["free"])
    if r.get("registration") not in ("", "none", None) and "registration" not in label:
        label += f" ({r['registration']})"
    return green(label) if r["free"] == "free" else yellow(label)


# ── data loading ───────────────────────────────────────────────────────────────

def find_data_dir(explicit: str | None) -> Path:
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    if os.environ.get("RESEARCH_VAULT_DATA"):
        candidates.append(Path(os.environ["RESEARCH_VAULT_DATA"]))
    here = Path(__file__).resolve()
    candidates.append(here.parent.parent / "data")   # repo checkout: cli/../data
    candidates.append(Path.cwd() / "data")
    for cand in candidates:
        if cand.is_dir() and any(cand.glob("*.json")):
            return cand
    sys.exit(
        "rv: no data directory found.\n"
        "Clone the repository (https://github.com/en970/research-vault) and run rv\n"
        "from inside it, or point --data / $RESEARCH_VAULT_DATA at its data/ folder."
    )


def load_units(data_dir: Path) -> list[dict]:
    units = []
    for path in sorted(data_dir.glob("*.json")):
        try:
            u = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        if isinstance(u, dict) and "resources" in u and "unit" in u:
            units.append(u)
    if not units:
        sys.exit(f"rv: no unit files in {data_dir}")
    return units


def all_resources(units: list[dict]):
    for u in units:
        for r in u["resources"]:
            yield u, r


# ── commands ───────────────────────────────────────────────────────────────────

def score(r: dict, tokens: list[str], unit: dict | None = None) -> int:
    name = r["name"].lower()
    sub = r.get("subcategory", "").lower()
    fields = ("summary", "notes", "access", "url", "category", "free", "registration")
    body = " ".join(str(r.get(k, "")) for k in fields)
    if unit:
        body += " " + unit.get("unit", "") + " " + unit.get("title", "")
    body = body.lower()
    total = 0
    for t in tokens:
        s = 0
        if t in name:
            s += 3
        if t in sub:
            s += 2
        if t in body:
            s += 1
        if s == 0:
            return 0  # every token must match somewhere
        total += s
    return total


def apply_filters(pairs, args):
    for u, r in pairs:
        # A resource written up in several fields is shown once unless you
        # ask for a field, where its field-specific write-up is the point.
        if not args.unit and not r.get("canonical", True):
            continue
        if args.unit and u["unit"] != args.unit:
            continue
        if args.category and r["category"] != args.category:
            continue
        if args.free and r["free"] != args.free:
            continue
        if args.no_signup and r.get("registration") not in ("", "none"):
            continue
        if args.min_beginner and r.get("beginner", 0) < args.min_beginner:
            continue
        yield u, r


def print_row(u: dict, r: dict):
    head = f"{bold(r['name'])}  {free_tag(r)}  {dim(stars(r.get('beginner', 3)))}"
    print(head)
    print(f"  {r['summary']}")
    print(f"  {cyan('access:')} {r['access']}")
    if r.get("notes"):
        print(f"  {yellow('note:')} {r['notes']}")
    print(f"  {dim(r['url'])}  {dim('[' + u['unit'] + ' / ' + r['category'] + ']')}")
    print()


def cmd_search(units, args):
    tokens = " ".join(args.query).lower().split()
    hits = []
    for u, r in apply_filters(all_resources(units), args):
        s = score(r, tokens, u) if tokens else 1
        if s > 0:
            hits.append((s, u, r))
    hits.sort(key=lambda h: (-h[0], h[2]["name"].lower()))
    hits = hits[: args.limit]
    if args.json:
        print(json.dumps([r | {"unit": u["unit"]} for _, u, r in hits],
                         indent=2, ensure_ascii=False))
        return
    if not hits:
        print("no matches — try fewer words, or `rv units` to browse")
        return
    for _, u, r in hits:
        print_row(u, r)
    print(dim(f"{len(hits)} result(s). Filters: -u UNIT -c CATEGORY --free LEVEL "
              f"--no-signup --min-beginner N"))


def cmd_show(units, args):
    want = " ".join(args.name).lower()
    best = None
    for u, r in all_resources(units):
        name = r["name"].lower()
        if name == want:
            best = (u, r)
            break
        if want in name and best is None:
            best = (u, r)
    if not best:
        sys.exit(f"rv: nothing named like '{want}' — try `rv search {want}`")
    u, r = best
    print()
    print_row(u, r)
    if r.get("subcategory"):
        print(dim(f"  subcategory: {r['subcategory']}"))


def cmd_units(units, _args):
    total = 0
    for u in units:
        n = len(u["resources"])
        total += n
        kind = dim(" (cross-cutting)") if u.get("kind") == "cross-cutting" else ""
        name_col = "{:<24s}".format(u["unit"])
        print(f"  {bold(name_col)} {n:4d}  {u['title']}{kind}")
    print(dim(f"\n  {total} entries in {len(units)} units"))


def cmd_categories(units, _args):
    counts: dict[str, int] = {}
    for _u, r in all_resources(units):
        counts[r["category"]] = counts.get(r["category"], 0) + 1
    for cat, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        cat_col = "{:<16s}".format(cat)
        print(f"  {bold(cat_col)} {n:4d}")


def cmd_random(units, args):
    pool = list(apply_filters(all_resources(units), args))
    if not pool:
        sys.exit("rv: nothing matches those filters")
    u, r = random.choice(pool)
    print()
    print_row(u, r)


# ── entry point ────────────────────────────────────────────────────────────────

def add_filters(p):
    p.add_argument("-u", "--unit", help="restrict to one unit (see `rv units`)")
    p.add_argument("-c", "--category",
                   choices=["data", "software", "literature", "compute",
                            "publishing", "funding", "learning", "community"])
    p.add_argument("--free", choices=["free", "free-registration",
                                      "free-tier", "freemium"])
    p.add_argument("--no-signup", action="store_true",
                   help="only resources usable with no account at all")
    p.add_argument("--min-beginner", type=int, metavar="N",
                   help="minimum beginner-friendliness (1-5)")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="rv", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", help="path to the data/ directory")
    sub = ap.add_subparsers(dest="cmd")

    p = sub.add_parser("search", help="full-text search")
    p.add_argument("query", nargs="*")
    p.add_argument("-n", "--limit", type=int, default=10)
    p.add_argument("--json", action="store_true")
    add_filters(p)

    p = sub.add_parser("show", help="full card for one resource")
    p.add_argument("name", nargs="+")

    sub.add_parser("units", help="list units")
    sub.add_parser("categories", help="list categories")

    p = sub.add_parser("random", help="one serendipitous entry")
    add_filters(p)

    args = ap.parse_args(argv)
    if not args.cmd:
        ap.print_help()
        return 0
    units = load_units(find_data_dir(args.data))
    {"search": cmd_search, "show": cmd_show, "units": cmd_units,
     "categories": cmd_categories, "random": cmd_random}[args.cmd](units, args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
