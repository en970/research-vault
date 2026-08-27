#!/usr/bin/env python3
"""Check every URL in the canonical data files.

Concurrent GET requests with a browser-like User-Agent. Sites that block
automated clients (403/405/429, TLS quirks) are reported as `manual`, not
failures — the point is to catch genuinely dead links, not to fight WAFs.

Run from the repository root:  python3 scripts/check_links.py [--timeout 20]
Writes data/link-report.json and prints a summary.
"""

import argparse
import concurrent.futures
import json
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
MANUAL_CODES = {401, 403, 405, 406, 429, 503}


def check(entry: tuple[str, str, str], timeout: int) -> dict:
    unit, name, url = entry
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return {"unit": unit, "name": name, "url": url,
                    "status": resp.status, "verdict": "ok"}
    except urllib.error.HTTPError as e:
        verdict = "manual" if e.code in MANUAL_CODES else "dead"
        return {"unit": unit, "name": name, "url": url,
                "status": e.code, "verdict": verdict}
    except ssl.SSLError:
        return {"unit": unit, "name": name, "url": url,
                "status": None, "verdict": "manual", "error": "ssl"}
    except Exception as e:  # timeout, DNS, connection refused
        return {"unit": unit, "name": name, "url": url,
                "status": None, "verdict": "dead", "error": type(e).__name__}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()

    entries = []
    for path in sorted(DATA.glob("*.json")):
        if path.name in ("link-report.json",):
            continue
        unit = json.loads(path.read_text())
        if "resources" not in unit:
            continue
        for r in unit["resources"]:
            entries.append((unit["unit"], r["name"], r["url"]))

    print(f"Checking {len(entries)} URLs ({args.workers} workers)…")
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(check, e, args.timeout) for e in entries]
        for i, f in enumerate(concurrent.futures.as_completed(futures), 1):
            results.append(f.result())
            if i % 100 == 0:
                print(f"  …{i}/{len(entries)}")

    by_verdict: dict[str, list] = {"ok": [], "manual": [], "dead": []}
    for r in results:
        by_verdict[r["verdict"]].append(r)

    (DATA / "link-report.json").write_text(
        json.dumps(sorted(results, key=lambda r: (r["verdict"], r["unit"], r["name"])),
                   indent=2, ensure_ascii=False) + "\n")

    print(f"\nok: {len(by_verdict['ok'])}   manual-check: {len(by_verdict['manual'])}   "
          f"dead: {len(by_verdict['dead'])}")
    for r in by_verdict["dead"]:
        print(f"  DEAD [{r['unit']}] {r['name']}: {r['url']} "
              f"({r.get('status') or r.get('error')})")
    for r in by_verdict["manual"]:
        print(f"  manual [{r['unit']}] {r['name']}: {r['url']} ({r.get('status') or r.get('error')})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
