# research-vault

**Browse the catalogue:** https://en970.github.io/research-vault/ · **From the terminal:** [`rv`](#the-command-line-tool)

A catalogue of the free and open resources a researcher needs in order to actually do
research — open data archives, literature access, free compute, software, publication
pathways, funding, and learning materials — organised by field, with a concrete access
method for every entry and an honest label for what is free and what is gated.

It is written for three readers: the graduate student whose library subscription does not
cover the thing they need, the researcher at an institution that cannot afford those
subscriptions at all, and the person working without any affiliation.

<!-- STATS:START -->
**1,154 resources** across **18 fields** — 895 free outright, 738 usable with no account at all. Verified 2026-08-28.
<!-- STATS:END -->

## Guiding principle

A list of links answers the question *what exists*. The harder question — the one that
costs an afternoon each time it goes unanswered — is *what can I reach from where I am
sitting*. A database that turns out to need an institutional login, a free tier that stops
at the first real query, a grant that quietly requires a university appointment: each of
those is discovered late, and only by the person least able to afford the time.

So the rule the catalogue is built on is:

> Include a resource only where a meaningful free route exists, and state exactly what that
> route is — the package to install, the endpoint that needs no key, the registration hoop,
> the quota. Where a resource is free only in part, say which part. Where the wall is
> institutional, say so plainly instead of listing it as free. Prefer a number that can be
> checked at the source over an adjective that cannot.

The consequence is that the caveats are not an appendix to the catalogue; they are half of
what it is for. MIMIC-IV is free, but only after a credentialing course — and that course
is itself free if you register under the right affiliation, which most write-ups omit.
UK Biobank charges, but has a £500 concession for students and LMIC applicants. Rubin's
DP1 pixels are locked to data-rights holders while its alert stream is world-public within
sixty seconds. Those distinctions are the content.

## What is inside

<!-- FIELDS:START -->
| Field | Entries | The deepest part of it |
|---|---|---|
| [Physics](docs/01-physics.md) | 87 | software (28), data (20), learning (11) |
| [Astronomy & space science](docs/02-astronomy.md) | 83 | data (39), software (20), learning (6) |
| [Chemistry & materials science](docs/03-chemistry.md) | 87 | software (29), data (25), literature (9) |
| [Biology & life sciences](docs/04-biology.md) | 87 | data (38), software (20), learning (6) |
| [Medicine & health sciences](docs/05-medicine.md) | 76 | data (26), software (16), literature (11) |
| [Earth, climate & environmental science](docs/06-earth.md) | 88 | data (38), software (18), learning (8) |
| [Mathematics](docs/07-mathematics.md) | 86 | software (20), publishing (15), data (13) |
| [Computer science & machine learning](docs/08-cs-ml.md) | 86 | software (21), data (15), literature (14) |
| [Neuroscience & psychology](docs/09-neuro-psych.md) | 94 | software (39), data (22), literature (10) |
| [Social sciences](docs/10-social.md) | 87 | data (37), software (16), literature (12) |
| [Economics & finance](docs/11-econ-finance.md) | 80 | data (38), software (14), literature (8) |
| [Linguistics & humanities](docs/12-humanities.md) | 76 | data (30), software (22), publishing (7) |
| [Literature access & discovery](docs/13-literature-access.md) | 74 | literature (43), software (11), publishing (6) |
| [Free compute & storage](docs/14-compute.md) | 62 | compute (36), data (10), publishing (6) |
| [Publishing, identity & preservation](docs/15-publishing.md) | 73 | publishing (43), literature (13), software (5) |
| [Funding, grants & recognition](docs/16-funding.md) | 68 | funding (63), learning (2), community (2) |
| [Learning materials](docs/17-learning.md) | 73 | learning (62), funding (3), compute (2) |
| [Research workflow software](docs/18-workflow-tools.md) | 76 | software (44), literature (7), publishing (6) |

The first 12 are fields of study. The rest cut across all of them: the parts of research that are the same whatever you work on.
<!-- FIELDS:END -->

Each entry carries a category (`data`, `software`, `literature`, `compute`, `publishing`,
`funding`, `learning`, `community`), a free-status label (`free`, `free-registration`,
`free-tier`, `freemium`), the heaviest registration hoop between a stranger and the
resource (`none`, `email`, `api-key`, `application`, `credentialing`), and a
beginner-friendliness rating from 1 to 5, where 5 means a newcomer gets something useful
out of it in ten minutes.

A resource that matters to several fields is written up once per field, each time in that
field's terms. The unfiltered views show it once; select a field and you get that field's
write-up.

## What is deliberately not here

- **Piracy.** No Sci-Hub, LibGen, Anna's Archive, or their equivalents. The catalogue
  documents legal routes only — including the ones people forget, such as Unpaywall, the
  Wikipedia Library, public-library access, and writing to the author, which works.
- **Paid tools with a free demo.** If the free tier exists to sell the paid one, it is out.
  Where a field's standard tool is genuinely paid (Stata, MATLAB, Scopus, CRSP), the entry
  that replaces it says so, so that you stop looking.
- **Padding.** Entries a researcher in that field would not actually recommend were cut,
  even where it left a section short. The funding sections are the honest example: routes
  genuinely open to unaffiliated researchers are scarce, and the catalogue says so rather
  than filling the space.

## The command-line tool

`rv` is a single Python file with no dependencies beyond the standard library. It reads the
same data the website does.

```bash
git clone https://github.com/en970/research-vault && cd research-vault
python3 cli/rv.py search "light curve"
```

Or install it, and run `rv` from anywhere with `RESEARCH_VAULT_DATA` pointing at the
`data/` directory:

```bash
pipx install .
```

```bash
rv search eeg                        # full-text search across every field
rv search gpu -c compute             # free compute, GPU-related
rv search archive --no-signup        # only things usable with no account at all
rv search "open access" -u medicine  # inside one field
rv show zenodo                       # the full card for one resource
rv units                             # fields and entry counts
rv random -c funding                 # one funding route you had not considered
```

Filters combine: `-u/--unit`, `-c/--category`, `--free`, `--no-signup`,
`--min-beginner N`, `-n/--limit`, and `--json` for piping into something else.

## How it is built

The catalogue lives in `data/<field>.json`. Everything else is generated from it: the
per-field documents under `docs/`, the website, and the CLI's index. To change an entry,
edit the JSON and rebuild — never edit a generated file.

```bash
python3 scripts/build.py         # regenerate docs/ and index.html
python3 scripts/check_links.py   # verify every URL still resolves
```

```
research-vault/
  data/                  the catalogue — one JSON file per field, the single source of truth
    raw/                 per-field research output the catalogue was merged from
  docs/                  generated: one readable document per field
  cli/rv.py              the command-line tool (standard library only)
  scripts/
    merge.py             raw research output -> canonical data files
    build.py             canonical data -> docs/ and index.html
    check_links.py       concurrent link checker
  web/template.html      the site, before the data is injected into it
  index.html             generated: the complete site, self-contained
```

The website is a single static page with the whole dataset inlined. There is no build step
beyond `build.py`, no external requests, no analytics, and no cookies; a strict
Content-Security-Policy meta tag (`default-src 'none'`) means no remote script, style, or
connection can load, every outbound link carries `rel="noopener noreferrer nofollow"`, and
URLs are sanitised to `http(s)` at render time so that a bad `url` in a pull request cannot
become a `javascript:` injection.

## A note on accuracy

Every entry was checked against the resource's own pages on the date shown at the top of
each field document, with numbers taken from primary sources — several were pulled live
from the resources' own APIs — rather than from secondary write-ups. Where a figure could
not be verified it was left out rather than guessed, and where a resource's status is
changing the entry says so.

That does not make the catalogue durable. Free tiers shrink, archives migrate, grant
programmes skip a year, and services close. Check the source before you build on it, and
please [open a pull request](CONTRIBUTING.md) when you find something that has moved —
status changes are the one thing a catalogue cannot notice by itself.

## Contributing

Additions, corrections, and dead-link reports are all welcome; the bar for an entry, the
field reference, and the house style are in [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

The curation, the code, and the written material are released under the MIT Licence (see
[`LICENSE`](LICENSE)). Every linked resource carries its own separate licence and terms —
check those before you build on, redistribute, or commercialise anything found through here.

---

<sub>topics: `research` `open-science` `open-data` `open-access` `awesome-list` `free-resources` `academia` `independent-research` `preprints` `open-source` `datasets` `scientific-computing`</sub>
