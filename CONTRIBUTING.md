# Contributing

Additions, corrections, and dead-link reports are all welcome. The catalogue is only useful
if it stays true, and it goes stale on its own.

## The bar for an entry

A resource belongs here if a researcher **without institutional access** can get real value
from it for free. Concretely:

- **A meaningful free route exists.** Not a trial, not a demo. If the free tier is a teaser
  for a paid product, leave it out. If a resource is partly free, include it and say precisely
  which part.
- **It is legal.** No Sci-Hub, LibGen, Anna's Archive, or similar. This catalogue documents
  legal routes only, including the ones people forget — Unpaywall, the Wikipedia Library,
  public-library access, and writing to the author.
- **You would recommend it to a colleague.** Thirty entries someone actually uses beat sixty
  that pad a list.

## Adding or fixing an entry

The canonical data lives in `data/<unit>.json`. Everything else — the per-field documents in
`docs/`, the web page, the CLI's index — is generated from it. **Edit the JSON, not the
generated files.**

1. Find the right unit file (`rv units`, or the list in the README).
2. Add your entry to the `resources` array:

```json
{
  "name": "Open Babel",
  "url": "https://openbabel.org",
  "category": "software",
  "subcategory": "file conversion",
  "summary": "Open-source toolbox that interconverts on the order of 100 chemical file formats, with fingerprints and 3D coordinate generation.",
  "access": "`conda install -c conda-forge openbabel`; CLI: `obabel input.smi -O output.sdf --gen3d`",
  "free": "free",
  "registration": "none",
  "beginner": 4,
  "notes": "Development pace has slowed; RDKit covers much of the same ground with a more active community."
}
```

3. Rebuild and check nothing broke:

```bash
python3 scripts/build.py          # regenerates docs/ and index.html
python3 scripts/check_links.py    # optional; verifies every URL still resolves
```

4. Commit the JSON **and** the regenerated files, and open a pull request.

## Field reference

| Field | Values | Notes |
|---|---|---|
| `category` | `data`, `software`, `literature`, `compute`, `publishing`, `funding`, `learning`, `community` | Where it sits in the catalogue. |
| `subcategory` | free text | Short, e.g. `"preprint server"`, `"particle-physics data"`. |
| `summary` | 1–2 sentences | Concrete and verifiable — sizes, counts, coverage, dates. No marketing adjectives. |
| `access` | free text | How a practitioner actually reaches it: the pip/CRAN package with a usage hint, the API endpoint, "web interface", "direct download". |
| `free` | `free`, `free-registration`, `free-tier`, `freemium` | What is actually free. |
| `registration` | `none`, `email`, `api-key`, `application`, `credentialing` | The heaviest hoop between a stranger and the data. |
| `beginner` | 1–5 | 5 = a newcomer gets value in ten minutes; 1 = specialist toolchain and patience. |
| `notes` | free text | The honest caveats: rate limits, what is *not* free, institutional gates, licence restrictions, eligibility. Empty string if there genuinely are none. |

## Style

Write the way the rest of the catalogue is written: plain, specific, no hype. "Roughly 119
million compounds and 322 million substances" is useful; "a comprehensive chemical database"
is not. If you know a limitation, put it in `notes` — the caveats are half of what makes an
entry worth reading.

Numbers should be checkable at the source, and the source should be primary: the resource's
own page, not a blog post about it. If you cannot verify a number, leave it out rather than
guess.

## Reporting something broken

Open an issue with the entry name and what you found — a 404, a free tier that closed, a
registration wall that appeared. Status changes are the most valuable contribution here,
because they are the thing a catalogue cannot notice by itself.
