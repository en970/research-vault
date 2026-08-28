#!/usr/bin/env python3
"""Check every URL in the canonical data files.

Two passes: everything that is not plainly fine on the first pass is retried
once, more slowly and alone, because a catalogue this size trips rate limits
and transient 5xx on its own. Verdicts are deliberately conservative — the
point is to catch genuinely dead links, not to fight bot protection:

  ok         2xx, or a redirect that resolved
  manual     alive but refusing an automated client (401/403/405/406/429/503)
  unreachable  timed out, TLS or DNS failure, or 5xx twice — recheck by hand
  dead       404/410, or a redirect loop — almost certainly gone

Run from the repository root:  python3 scripts/check_links.py
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
    "Accept-Encoding": "identity",
    "Connection": "close",
}
MANUAL_CODES = {401, 403, 405, 406, 429, 503}
DEAD_CODES = {404, 410}


def fetch(url: str, timeout: int) -> dict:
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return {"status": resp.status, "verdict": "ok", "final": resp.url}
    except urllib.error.HTTPError as e:
        if e.code in DEAD_CODES:
            verdict = "dead"
        elif e.code in MANUAL_CODES:
            verdict = "manual"
        elif 300 <= e.code < 400:
            # urllib raises rather than following only when the redirect is
            # unusable — a loop, or a Location it will not follow.
            verdict = "redirect"
        else:
            verdict = "unreachable"
        return {"status": e.code, "verdict": verdict}
    except ssl.SSLError as e:
        return {"status": None, "verdict": "unreachable", "error": f"ssl: {e.reason}"}
    except Exception as e:
        return {"status": None, "verdict": "unreachable", "error": type(e).__name__}


def check(entry: tuple[str, str, str], timeout: int) -> dict:
    unit, name, url = entry
    res = fetch(url, timeout)
    return {"unit": unit, "name": name, "url": url, **res}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--retry-timeout", type=int, default=45)
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()

    entries = []
    for path in sorted(DATA.glob("*.json")):
        if path.name == "link-report.json":
            continue
        unit = json.loads(path.read_text())
        if "resources" not in unit:
            continue
        for r in unit["resources"]:
            entries.append((unit["unit"], r["name"], r["url"]))

    print(f"Pass 1: {len(entries)} URLs ({args.workers} workers)…")
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = [ex.submit(check, e, args.timeout) for e in entries]
        for i, f in enumerate(concurrent.futures.as_completed(futures), 1):
            results.append(f.result())
            if i % 200 == 0:
                print(f"  …{i}/{len(entries)}")

    suspect = [r for r in results if r["verdict"] != "ok"]
    print(f"\nPass 2: retrying {len(suspect)} slowly (4 workers, "
          f"{args.retry_timeout}s timeout)…")
    fixed = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        futures = {
            ex.submit(check, (r["unit"], r["name"], r["url"]), args.retry_timeout): r["url"]
            for r in suspect
        }
        for f in concurrent.futures.as_completed(futures):
            res = f.result()
            fixed[res["url"]] = res
    results = [fixed.get(r["url"], r) for r in results]

    order = ["dead", "redirect", "unreachable", "manual", "ok"]
    by_verdict: dict[str, list] = {v: [] for v in order}
    for r in results:
        by_verdict.setdefault(r["verdict"], []).append(r)

    (DATA / "link-report.json").write_text(
        json.dumps(sorted(results, key=lambda r: (order.index(r["verdict"])
                                                  if r["verdict"] in order else 9,
                                                  r["unit"], r["name"])),
                   indent=2, ensure_ascii=False) + "\n")

    print("\n" + "  ".join(f"{v}: {len(by_verdict[v])}" for v in order))
    for v in ("dead", "redirect", "unreachable"):
        for r in by_verdict[v]:
            print(f"  {v.upper():12s} [{r['unit']}] {r['name']}: {r['url']} "
                  f"({r.get('status') or r.get('error')})")
    print(f"\n{len(by_verdict['manual'])} alive but blocking automated clients "
          f"(403 and friends) — listed in data/link-report.json, no action needed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
