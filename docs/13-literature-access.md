# Literature access & discovery

Part of [research-vault](../README.md). 74 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (2) · [Software](#software) (11) · [Literature](#literature) (43) · [Publishing](#publishing) (6) · [Funding](#funding) (2) · [Learning](#learning) (6) · [Community](#community) (4)

## Data

### [OpenCitations](https://opencitations.net)

`Free` · beginner 3/5 · open citation index

Open citation data infrastructure run by the Research Centre for Open Scholarly Metadata at the University of Bologna. Provides the OpenCitations Index of citation links and OpenCitations Meta of bibliographic metadata, with all data released under CC0.

**Access.** REST API, no key: `https://opencitations.net/index/api/v2/citation-count/doi:10.1038/nature12373` returns a citation count; also citations, references and metadata endpoints. SPARQL endpoint and full data dumps available.

**Caveats.** The reason it matters is licensing: citation counts from Scopus and Web of Science cannot be redistributed, and Crossref's reference data is only open where publishers opted in. OpenCitations is CC0 with no strings, so you can publish derived analyses without a rights problem. Coverage is narrower than Scopus and skewed towards publishers who open their references — do not treat counts as complete. Data is served from a nonprofit on modest infrastructure; be gentle with request rates.

*Also listed under: publishing.*

### [Retraction Watch Database (via Crossref)](https://api.labs.crossref.org/data/retractionwatch)

`Free` · beginner 3/5 · retraction and correction records

The Retraction Watch database, acquired by Crossref in 2023 and released as public data: 72,060 records as of 2026-08-28, each with the retracted work's DOI, title, journal, publisher, country, author, retraction date, retraction DOI, article type and reason. Updated daily.

**Access.** Direct CSV download: `https://api.labs.crossref.org/data/retractionwatch?you@example.org` (about 63 MB). Source and daily updates mirrored at gitlab.com/crossref/retraction-watch-data. Retraction status is also surfaced in Crossref and OpenAlex work records.

**Caveats.** Released under CC0 — a genuine change from the pre-2023 situation where the database was licensed. Run your reference list against it before submitting; citing retracted work is embarrassing and increasingly caught by reviewers. The download is slow (it took over two minutes on a home connection) and the file is a flat CSV, so load it with pandas rather than a spreadsheet. Coverage is good but not exhaustive, and reasons are curator-assigned.

*Also listed under: publishing.*

## Software

### [ASReview LAB](https://github.com/asreview/asreview)

`Free` · beginner 3/5 · systematic review screening

Open-source active-learning tool from Utrecht University for title-and-abstract screening: you label records, the model re-ranks what is left, and relevant records surface early — an approach validated in a Nature Machine Intelligence paper. Apache-2.0 licensed and runs entirely on your own machine, with no data leaving it.

**Access.** `pip install asreview` then `asreview lab` opens a local web app in your browser. Import a CSV, RIS, XLSX or TSV export from any database, screen interactively, export the labelled dataset. A simulation mode replays an already-completed review to estimate how much screening effort the model would have saved.

**Caveats.** It reorders the screening queue; it does not decide inclusion, and stopping early is a methodological choice you must justify and report in your PRISMA flow. Needs Python and a records export, so there is a setup step that a hosted tool like Rayyan avoids. Screening only — no search building, no full-text stage, no data extraction. Recent major releases changed the interface and project format, so older tutorials may not match your install.

### [bibliometrix](https://cran.r-project.org/package=bibliometrix)

`Free` · beginner 3/5 · science mapping in R

R package implementing a full bibliometric and science-mapping workflow — co-citation, coupling, co-word and collaboration networks, thematic maps, Lotka's law — with importers for OpenAlex, Dimensions, PubMed, Cochrane, Scopus and Web of Science exports. Ships with the Biblioshiny point-and-click web interface.

**Access.** `install.packages("bibliometrix")` in R, then `library(bibliometrix); biblioshiny()` opens the GUI in a browser; or `convert2df()` then `biblioAnalysis()` for scripted use.

**Caveats.** Biblioshiny means you can do serious bibliometrics without writing R, which matters if you are coming from a non-computational field. Crucially for this audience it reads OpenAlex and PubMed, so you do not need a Scopus or Web of Science subscription to use it. Runs fine on a laptop for datasets up to tens of thousands of records; larger corpora need memory care.

### [CORE Discovery](https://core.ac.uk/services/discovery)

`Free` · beginner 5/5 · browser extension for OA copies

Free browser extension that finds free copies of papers when you hit a paywall, backed by CORE's 57M+ full texts plus external sources. Unlike DOI-keyed tools it can also resolve documents that have no DOI, which matters for theses, reports and repository items.

**Access.** Install from the Chrome Web Store, Firefox Add-ons or Opera; a repository plugin and an API are also offered. Free to install, no account.

**Caveats.** Worth running alongside Unpaywall rather than instead of it: the two use different source sets and each finds copies the other misses. CORE's own coverage claims are self-reported. The API for third-party integration is a separate arrangement — contact CORE.

### [EndNote Click](https://click.endnote.com)

`Free (registration), email` · beginner 4/5 · one-click PDF retrieval extension

Free Chrome and Firefox extension (the former Kopernio, now Clarivate) that resolves the full-text PDF of the article you are viewing in one click, routing through your library's subscriptions where you have them and falling back to open-access copies. Claims over 750,000 users.

**Access.** Install from the Chrome Web Store or Firefox Add-ons and create a free account; optionally connect an institutional login. PDFs are saved to a personal cloud locker.

**Caveats.** Be clear about who this helps. Most of its value comes from proxying your institutional subscriptions — if you have no institution, it falls back to the same open-access sources Unpaywall and CORE Discovery already cover, and those need no account. Worth installing if you have any affiliation at all (including alumni or public-library access); otherwise skip it. Clarivate-owned and account-gated, unlike the nonprofit alternatives, and it is used to market EndNote.

### [habanero](https://pypi.org/project/habanero/)

`Free` · beginner 3/5 · Python client for Crossref

Low-level Python client for the Crossref REST API (version 2.9.2 on PyPI) from rOpenSci, covering works, members, journals, funders, prefixes and types, with cursor paging and content negotiation for formatted citations.

**Access.** `pip install habanero`, then `from habanero import Crossref; cr = Crossref(mailto="you@example.org"); cr.works(query="deep learning", limit=100)`. `cn.content_negotiation(ids="10.1038/nature12373", format="bibtex")` turns a DOI into a BibTeX entry.

**Caveats.** Always pass `mailto` — without it you are in the anonymous Crossref pool, which throttles hard. The content-negotiation helper is the cleanest way to turn a list of DOIs into a bibliography without any GUI. rOpenSci maintains an equivalent R package, `rcrossref`.

### [JabRef](https://www.jabref.org)

`Free` · beginner 4/5 · BibTeX reference manager

Free and open-source reference manager storing everything in plain BibTeX/BibLaTeX text files with no vendor lock-in. Founded in 2003, maintained by a volunteer team of researchers, with desktop apps and browser extensions.

**Access.** Download for Windows, macOS and Linux from jabref.org. Fetches metadata by DOI, ISBN, arXiv ID or PubMed ID; browser extensions for capture.

**Caveats.** The right choice if you write in LaTeX and want your bibliography under version control alongside your manuscript — the .bib file is the database, so git diffs are meaningful and no service can hold your data. Less polished than Zotero for PDF reading and annotation, and no hosted sync (use your own git repo or file sync). 100% free and open source with no paid tier at all.

*Also listed under: workflow-tools.*

### [Publish or Perish](https://harzing.com/resources/publish-or-perish)

`Free` · beginner 4/5 · citation retrieval and metrics

Free desktop application by Anne-Wil Harzing that retrieves citations from multiple backends (Google Scholar, Crossref, OpenAlex, Semantic Scholar, PubMed and others) and computes citation metrics including the h-index and its variants for individual academics, journals or research areas. The current release is version 8, issued 1 November 2021; the product page itself was last updated 1 July 2026.

**Access.** Download for Windows and macOS from harzing.com; runs on Linux under Wine or CrossOver. Results copy to the clipboard or export to several formats.

**Caveats.** Explicitly designed for people making a case for research impact with few citations and no institutional subscription — the use case this catalogue exists for. Its Google Scholar backend is the most complete but is scraped, so heavy use triggers blocking; the Crossref, OpenAlex, Semantic Scholar and PubMed backends are API-based and reliable. Metrics from different backends are not comparable; always state which source you used.

### [pyalex](https://pypi.org/project/pyalex/)

`Free` · beginner 3/5 · Python client for OpenAlex

Maintained Python client for the OpenAlex API (version 0.21 on PyPI) covering all entity types, filtering, grouping, paging and cursor-based bulk retrieval, with automatic handling of the polite-pool and API-key parameters.

**Access.** `pip install pyalex`, then `import pyalex; pyalex.config.email = "you@example.org"; from pyalex import Works; Works().filter(publication_year=2024).group_by("open_access.oa_status").get()`.

**Caveats.** Set `pyalex.config.api_key` to your free OpenAlex key or you will be running on the $0.10/day anonymous budget. Use `paginate(per_page=200)` for large pulls — page size directly determines how far your daily dollar goes. For anything above a few hundred thousand records, download the free CC0 snapshot instead of hammering the API.

### [Rayyan](https://www.rayyan.ai)

`Freemium, email` · beginner 5/5 · systematic review screening

Hosted screening tool for systematic reviews with blinded multi-reviewer workflows, duplicate detection, exclusion reasons and AI relevance ranking. The free plan allows 3 active reviews, 2 invited reviewers and 1 sample; paid plans start at $4.99/user/month billed annually (pricing page, 2026-08-28).

**Access.** Free account at rayyan.ai; import RIS, CSV or EndNote exports, screen title/abstract with include/exclude/maybe labels and reasons, resolve conflicts between reviewers, then export decisions. Mobile app available, with limited access on the free plan.

**Caveats.** Rayyan was effectively unlimited for years and is now capped; 3 active reviews and 2 collaborators is the constraint that bites on a real project. PRISMA flow diagrams, auto-resolve duplicates and unlimited samples are paid (Essential $4.99/month billed annually or $8.33/month quarterly; Advanced $8.33/month annually; Business $41.67 per licence/month with a five-licence minimum, i.e. $2,500/year). Your records sit on their servers, which some ethics approvals do not permit — ASReview runs locally if that matters.

*Also listed under: medicine, workflow-tools.*

### [VOSviewer](https://www.vosviewer.com)

`Free` · beginner 4/5 · bibliometric network visualisation

Free desktop tool from CWTS at Leiden University for constructing and visualising bibliometric networks — co-authorship, co-citation, bibliographic coupling and term co-occurrence maps. Version 1.6.21 (12 June 2026) imports records from OpenAlex, Crossref, Europe PMC, Semantic Scholar, Lens, PubMed, Scopus and Web of Science, and can query OpenAlex and Europe PMC directly from inside the application.

**Access.** Download for Windows, macOS (native Apple Silicon) and Linux from vosviewer.com; requires Java. Either load an exported records file (RIS, CSV, BibTeX) or use the built-in API connections, then export the map as an image or publish it through VOSviewer Online.

**Caveats.** Free of charge, but it is a GUI application rather than a scriptable library — for reproducible pipelines use bibliometrix in R and keep VOSviewer for the figure. Because it now queries OpenAlex, Crossref and Europe PMC directly, you can produce a publishable science map with no Scopus or Web of Science subscription, which was not true a few years ago. Large corpora need generous Java heap settings, and cluster labels always need human interpretation.

*Also listed under: workflow-tools.*

### [Zotero](https://www.zotero.org)

`Freemium, email` · beginner 5/5 · reference manager

Free, open-source reference manager from the nonprofit Corporation for Digital Scholarship. Captures references and PDFs from the browser in one click, reads and annotates PDFs, syncs across devices, generates citations in thousands of styles, and integrates with Word, LibreOffice and Google Docs.

**Access.** Download the desktop app for Windows, macOS and Linux plus the Zotero Connector browser extension. Free account for syncing. Web API at api.zotero.org; `pip install pyzotero` for scripting. Group libraries for collaboration.

**Caveats.** The software is free and unlimited forever; only cloud file storage is metered — 300 MB free, then $20/year for 2 GB, $60/year for 6 GB, $120/year for unlimited. Two ways around this entirely: sync metadata only (unlimited and free) and keep PDFs local, or point file syncing at your own WebDAV server. Group library files draw on the group owner's quota. Beyond citation formatting, Zotero is the practical hub of a no-institution workflow: it stores the PDFs you legally obtain, and its saved searches and RSS reader make it a discovery tool as well.

*Also listed under: physics, mathematics, neuro-psych, social, humanities, publishing, workflow-tools.*

## Literature

### [African Journals Online (AJOL)](https://www.ajol.info)

`Free` · beginner 5/5 · African journal aggregator

Non-profit platform founded in 1998 hosting 977 African-published peer-reviewed journals from 40 countries (370 Nigeria, 115 South Africa, 82 Kenya), with 288,357 full-text articles of which 172,840 are open access and 51,307 sit in journals that charge authors nothing. Counts read from the AJOL site on 2026-08-28.

**Access.** Free web search and browse at ajol.info by journal, country, subject or keyword; open-access articles download as PDF with no account. Journals run on OJS with per-journal tables of contents and RSS.

**Caveats.** Only 459 of the 977 journals are fully open access (283 of those charge no author fee); for the rest AJOL lists abstracts and full text must be requested or purchased. Coverage of African scholarship is far better than Scopus or Web of Science, but indexing elsewhere is thin, so this literature is easy to miss entirely if you search only the big indexes. No documented public API — plan on browsing or harvesting the OJS endpoints.

### [arXiv](https://arxiv.org)

`Free` · beginner 5/5 · preprint server

Open-access archive of nearly 2.4 million scholarly articles in physics, mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical engineering and economics. Now operated as an independent nonprofit. In several of these fields arXiv, not the journal, is where research is actually read.

**Access.** Free reading and download, no account. Metadata API: `https://export.arxiv.org/api/query?search_query=all:...&max_results=100` (Atom, includes opensearch totals). Daily new-submission listings, RSS feeds and email subscriptions per category. Bulk full text via a requester-pays S3 bucket; OAI-PMH for metadata harvesting.

**Caveats.** Reading is unconditional and unregistered. Submitting requires an account and, for a first submission in a category, endorsement by an established author — a real barrier for unaffiliated researchers, though endorsement is usually granted on request with a reasonable draft. Nothing on arXiv is peer reviewed by arXiv. The daily category listing plus its RSS feed is the cheapest current-awareness tool in existence for these fields.

### [BASE (Bielefeld Academic Search Engine)](https://www.base-search.net)

`Free, application` · beginner 4/5 · repository search engine

One of the largest search engines for academic web resources, operated by Bielefeld University Library, harvesting institutional and subject repositories worldwide via OAI-PMH. Strong on grey literature, theses and non-English material that Google Scholar indexes poorly.

**Access.** Web interface at base-search.net with fielded search and filters for document type, licence and access level. An HTTP search API exists at `api.base-search.net/cgi-bin/BaseHttpSearchInterface.fcgi`.

**Caveats.** The API is IP-whitelisted: an unregistered request returns 'Access denied for IP address ... and user agent', so scripted use requires applying to Bielefeld first and is granted for non-commercial purposes. The public website is now behind an Anubis proof-of-work bot check, which blocks scripted fetching but is invisible to ordinary browser users. I could not verify current document or provider counts because both the about page and the API refused automated access — treat any figure you see quoted elsewhere as unconfirmed.

### [bioRxiv](https://www.biorxiv.org)

`Free` · beginner 5/5 · life-sciences preprint server

Preprint server for the life sciences, operated by the non-profit openRxiv and founded at Cold Spring Harbor Laboratory. OpenAlex indexes 341,681 bioRxiv preprints as of 2026-08-28, with 45,182 posted in 2025 alone; posting is free and every preprint is free to read from the day it appears.

**Access.** Free reading and PDF download with no account at biorxiv.org. JSON API with no key: `https://api.biorxiv.org/details/biorxiv/2026-08-01/2026-08-28` for metadata by date range, or `/details/biorxiv/{DOI}` for one preprint. Per-subject RSS feeds and email alerts; records are also searchable in Europe PMC with `SRC:PPR`.

**Caveats.** Screening covers scope, plagiarism, non-scientific content and dual-use concerns — not validity. Nothing here is peer reviewed, and a substantial share of preprints never reach a journal, so check for a published version before citing. Authors pick from six licences, several of which forbid reuse, so check the licence before text mining. Posting requires an account. api.biorxiv.org refused connections from the network used for this check on 2026-08-28; the website and the Europe PMC route both worked, so have a fallback if you script against it.

*Also listed under: biology, neuro-psych, publishing.*

### [Connected Papers](https://www.connectedpapers.com)

`Freemium, email` · beginner 5/5 · citation similarity graphs

Generates a visual graph of papers similar to a seed paper, using co-citation and bibliographic coupling rather than direct citation, so it surfaces relevant work that never cites the seed. Also produces 'prior works' and 'derivative works' views.

**Access.** Paste a title, DOI or arXiv ID at connectedpapers.com and a graph builds in seconds. No install.

**Caveats.** Verified free-tier limits, read from the site's own application code on 2026-08-28: 2 graphs per month without an account, 5 graphs per month with a free account. All features are included in the free tier — only the volume is capped. Premium (Academic and Business tiers, priced per region and billed quarterly or annually) removes the cap. Five graphs a month is enough for orienting yourself in a new field but not for systematic work; use Inciteful, which is uncapped, for heavy use.

### [CORE](https://core.ac.uk)

`Free tier, email` · beginner 4/5 · open-access full-text aggregator

Not-for-profit aggregator hosted by The Open University indexing 452 million searchable research papers with more than 57 million full texts, harvested from over 15,000 repositories and journals across 150+ countries. The largest single collection of open-access full text, as opposed to metadata alone.

**Access.** Web search at core.ac.uk/search; REST API at `https://api.core.ac.uk/v3/search/works?q=...`; bulk Dataset download; R client via rOpenSci. Register an email for a key at core.ac.uk/services/api.

**Caveats.** The API is documented as usable without registration but capped at one batch request or five single requests per 10 seconds; note that on 2026-08-28 an unauthenticated call to `https://api.core.ac.uk/v3/search/works` returned HTTP 403, as did core.ac.uk itself, so plan on registering for a free key rather than assuming anonymous access works. Registered organisational keys get faster rates but those are 'typically not free'; free licences are assessed case by case at registration, and Supporting/Sustaining Members get the fast rate as a benefit. FastSync and bespoke contracts are commercial. Because CORE harvests repositories, records include preprints, theses and accepted manuscripts alongside published versions — check the version before citing. The 452M papers / 57M full texts figures could not be re-verified in this check because the site blocks automated access.

*Also listed under: social, publishing.*

### [Crossref REST API](https://api.crossref.org)

`Free` · beginner 4/5 · DOI metadata registry

Authoritative metadata for 185,908,779 registered DOIs from about 25,000 member publishers: titles, authors, ORCIDs, references, funder data, licences, abstracts where deposited, and links to preprints, peer reviews, grants and retraction notices.

**Access.** Open REST API, no key: `https://api.crossref.org/works?query.bibliographic=...&rows=100`. Python `pip install habanero`, then `from habanero import Crossref; Crossref(mailto="you@example.org").works(query="...")`. Full metadata torrents/snapshots also published annually.

**Caveats.** No registration, but the shared anonymous pool is aggressively throttled — I hit HTTP 429 repeatedly from a single laptop during this sweep. Put a real mailto in your User-Agent or the `mailto` parameter to enter the 'polite pool', which is markedly more reliable. Crossref only knows what publishers deposit: abstracts and references are missing for many records, and it holds no full text. Metadata Plus (guaranteed throughput, snapshots) is a paid membership service. Content Registration fees for members drop, and back-year record fees are removed, on 1 January 2027.

*Also listed under: publishing.*

### [dblp computer science bibliography](https://dblp.org)

`Free` · beginner 5/5 · computer science bibliography

Curated computer-science bibliography run by Schloss Dagstuhl – Leibniz Center for Informatics: 8,733,004 publications, 4,184,231 authors, 7,150 conferences and 1,901 journals as of 2026-08-28, with hand-maintained author disambiguation. All metadata is CC0.

**Access.** Web search at dblp.org; search API with no key — `https://dblp.org/search/publ/api?q=transformer&format=json&h=100` plus `/search/author/api` and `/search/venue/api`. One-click BibTeX on every record, monthly XML and RDF dumps, and a SPARQL endpoint at sparql.dblp.org.

**Caveats.** Metadata only: no abstracts, no citation counts and no full text, though records link out to DOIs and open versions. Scope is computer science and immediate neighbours; anything else is out of scope by design. The curated author pages are the reason to prefer dblp over Google Scholar for CS publication lists and co-authorship analysis, but homonyms still need checking. For bulk work use the dumps rather than hammering the API.

*Also listed under: cs-ml.*

### [Dimensions (free version)](https://www.dimensions.ai/products/free/)

`Free tier, email` · beginner 4/5 · linked research index

Free tier of Digital Science's Dimensions covering more than 140 million publications and 29 million datasets, linked to grants, patents, clinical trials and policy documents, with citation indicators and Altmetric attention scores.

**Access.** Register a free account at app.dimensions.ai; full-text search with filters, analytical views, export, and ORCID linking.

**Caveats.** Free for personal, non-commercial use only. The distinctive free feature is linkage from a paper to the grant that funded it, the clinical trials that reference it and the policy documents that cite it — hard to get elsewhere without paying. The Dimensions Analytics platform, the DSL API and bulk data are commercial; free API access is granted only by application for scientometric research. Do not build a pipeline assuming API access comes with the free account.

### [DOAB (Directory of Open Access Books)](https://www.doabooks.org)

`Free` · beginner 5/5 · open-access monograph index

Discovery service indexing over 108,500 peer-reviewed open-access scholarly books and chapters from vetted publishers, with the PRISM service recording each publisher's peer-review process. Free of charge with all metadata openly available.

**Access.** Web search by keyword, subject, publisher, collection or language, linking through to the full text on the publisher's or OAPEN's platform. Metadata available for harvest (OAI-PMH, exports) for library systems.

**Caveats.** The single most useful resource for humanities and social science researchers without library access, where the monograph is the unit of scholarship and journal-focused tools are useless. Coverage is only books their publishers chose to make OA — most academic monographs are still closed. Quality varies; check the PRISM peer-review record.

*Also listed under: social, humanities, publishing.*

### [DOAJ (Directory of Open Access Journals)](https://doaj.org)

`Free` · beginner 5/5 · vetted OA journal and article index

Community-curated whitelist of 23,371 open-access journals from 141 countries in 92 languages, of which 14,433 charge authors no fees at all, plus 13,512,244 article records (figures from the DOAJ homepage, 2026-08-28). Independent, donation-funded, no publisher pays for inclusion.

**Access.** Web search of journals and articles; free REST API with no key: `https://doaj.org/api/search/journals/{query}?pageSize=100` and `/api/search/articles/{query}`; journal CSV, OAI-PMH feed, and a full public data dump.

**Caveats.** DOAJ inclusion is the practical test for whether an OA journal is legitimate rather than predatory — its criteria cover peer review, editorial process, licensing and transparency. Article-level coverage is partial: only some member journals deposit article metadata, so the 13.5M article records are far from all articles in the 23,371 journals. 'Premium Mode' is a paid convenience layer; all the data and APIs remain free.

*Also listed under: chemistry, medicine, neuro-psych, social, publishing.*

### [Elicit](https://elicit.com)

`Freemium, email` · beginner 4/5 · AI literature review assistant

Searches across more than 138 million papers and extracts structured data from them into a table — populations, methods, outcomes, sample sizes — for screening and evidence synthesis. Built for systematic-review-style workflows rather than chat.

**Access.** Free Basic account at elicit.com. Import from Zotero; export is a paid feature.

**Caveats.** Verified on the public pricing page, 2026-08-28: Basic (free) gives unlimited search across 138M+ papers, unlimited summaries, unlimited chat with papers including full text, source display and Zotero import, but only 'limited usage' of the Research Agent and Research Reports. The paid ladder is now Pro at $49/user/month (billed annually as $588), Scale at $169/user/month ($2,028/year) and Enterprise on request — the $11 Plus tier and $39 Pro price quoted earlier no longer appear, and no academic price list is shown publicly. Export (RIS/CSV/BIB/PDF/DOCX) is not listed among Basic features, so treat export as paid and confirm before building a workflow on it. As with all LLM extraction, verify every extracted value against the paper before it enters your analysis.

### [Emailing the corresponding author](https://orcid.org)

`Free` · beginner 5/5 · direct author request

Ask the author for a copy. Authors are legally entitled to share their own manuscripts for personal scholarly use, response rates are high, and it costs nothing. ORCID is the reliable way to find a current identity and contact page when the paper's listed address is a decade stale.

**Access.** Look up the author in ORCID (`https://orcid.org/{id}`, or the free public API at pub.orcid.org) or OpenAlex to find their current affiliation and website; take the corresponding-author email from the paper. A three-sentence email naming the paper and why you want it is enough.

**Caveats.** Say this plainly because newcomers do not believe it: this works, often within a day, and researchers are generally pleased to be asked. It works best for papers less than about 15 years old where the author is still contactable. It does not scale to a systematic review of 400 papers, and do not ask for a PDF the publisher has already made open — check Unpaywall first. ORCID itself is free, registration is optional for lookups, and the public API needs no key for basic record retrieval.

*Also listed under: publishing, funding, workflow-tools.*

### [ERIC (Education Resources Information Center)](https://eric.ed.gov)

`Free` · beginner 5/5 · education literature index

US Department of Education index of 2,139,548 education research records — journal articles, reports, conference papers, dissertations and grey literature — many with free full text hosted directly on ERIC. Indexed with a controlled education thesaurus.

**Access.** Web search with peer-reviewed and full-text-available filters. Free API with no key: `https://api.ies.ed.gov/eric/?search=...&format=json&rows=200`. Bulk metadata download offered.

**Caveats.** The API works with no registration and no rate-limit friction, which makes ERIC one of the easiest fielded corpora to script against. Coverage is US-centric and English-language; non-US education research is patchy. Full text is available for the ED-numbered documents but usually not for indexed journal articles, where you still need an OA route.

### [Europe PMC](https://europepmc.org)

`Free` · beginner 5/5 · life-sciences literature database

EMBL-EBI's life-sciences literature database: 48,779,933 abstracts, 12,103,215 full-text articles, 8,054,743 open-access articles and 1,226,926 preprints indexed as of 2026-08-28. Adds text-mined annotations (genes, diseases, accession numbers) and links to underlying data records.

**Access.** Free REST API, no key: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json&pageSize=100`, with cursorMark paging for large result sets. Bulk OA full text via FTP and an annotations API. Web search with saved-query email alerts.

**Caveats.** The API needs no key and imposes no registration, which makes it the easiest large biomedical corpus to script against. Preprints from bioRxiv, medRxiv and others are included and flagged `SRC:PPR` — useful, but check peer-review status before citing. Full text is only downloadable for the open-access subset; the rest is abstract-only.

### [Google Scholar](https://scholar.google.com)

`Free` · beginner 5/5 · general academic search

The broadest academic index available free, covering journal and conference papers, theses, books, preprints, abstracts, technical reports and court opinions, with citation counts and 'cited by' chaining. Its Library Links feature can route you through a public or alumni library you already belong to.

**Access.** Web search only. Email alerts via the envelope icon on any search or author profile. Citation export to BibTeX, EndNote, RefMan and RefWorks. Free author profiles. Set Settings > Library links to connect a library you have a card for.

**Caveats.** Limits confirmed from Google's own help pages: there is no API and no bulk access ('Sorry, we're unable to provide bulk access'), automated downloading gets your IP blocked and they will not raise the limit, and no query returns more than 1,000 results. That makes it unusable for systematic reviews requiring reproducible, exportable result sets — use OpenAlex, Europe PMC or Lens for that and Google Scholar for serendipity and citation chasing. Coverage is undocumented and unauditable, and includes records from commercial subscription services you cannot read. The `scholarly` Python package exists but scraping violates the terms and gets blocked quickly.

### [HAL (Hyper Articles en Ligne)](https://hal.science)

`Free` · beginner 3/5 · national open repository (France)

France's national open archive, run by the CNRS Centre for Direct Scientific Communication: 4,644,610 records as of 2026-08-28, of which 1,787,345 carry a deposited full-text file. All disciplines, and the default deposit route for French public research, so it holds French-language scholarship, theses and grey literature that Anglophone indexes miss.

**Access.** Free web search at hal.science. Solr-backed API with no key: `https://api.archives-ouvertes.fr/search/?q=apprentissage+profond&fq=submitType_s:file&rows=100&wt=json&fl=title_s,uri_s,fileMain_s`; OAI-PMH at api.archives-ouvertes.fr/oai/hal. Depositing your own work needs a free account.

**Caveats.** The web front end sits behind an Anubis proof-of-work bot check and refused an automated fetch on 2026-08-28, while the API answered normally — script against the API, browse in a browser. Only about 38% of records carry full text; the rest are metadata-only references. Interface and much of the metadata are in French, so French-language query terms materially change what you retrieve.

### [HathiTrust Digital Library](https://www.hathitrust.org)

`Free tier` · beginner 3/5 · digitised book corpus

Large-scale collaborative digital library of volumes digitised from research library collections. Full-text search runs across the entire corpus for anyone; public-domain volumes can be read and downloaded page by page by anyone with no affiliation.

**Access.** Free full-text search and public-domain reading at babel.hathitrust.org; free account for building collections. The HathiTrust Research Center offers computational access to derived datasets.

**Caveats.** The key affordance for an unaffiliated reader is search-inside on in-copyright books you cannot read: it tells you the page numbers where your term appears, which is often enough to justify an interlibrary loan request or a targeted purchase. Reading in-copyright volumes requires membership through a partner institution. Full-volume PDF download of public-domain works is restricted to affiliated users at some partner libraries. The site is behind a bot filter and could not be verified programmatically for this entry, so no volume counts are quoted here.

*Also listed under: humanities.*

### [Inciteful](https://inciteful.xyz)

`Free` · beginner 4/5 · citation network exploration

Builds a citation network from one or more seed papers and ranks the most important connected works, with a separate 'Literature Connector' tool that finds the citation paths between two papers. Built on open citation data.

**Access.** Paste a DOI, title, arXiv ID or PubMed ID at inciteful.xyz; use 'Paper Discovery' for one seed or 'Literature Connector' for two. No account, no install.

**Caveats.** The genuinely free alternative in this category — no monthly graph cap, no account, no paid tier pushing at you. The Literature Connector is unusual and useful: give it a paper from each of two fields and it shows you the works that bridge them. The interface is a JavaScript app, so it cannot be scripted. Small independent project; treat availability as best-effort.

### [INSPIRE-HEP](https://inspirehep.net)

`Free` · beginner 4/5 · high-energy physics literature

Literature database for high-energy physics operated jointly by CERN, DESY, Fermilab and SLAC: 1,881,232 literature records as of 2026-08-28, linked to curated author profiles, institutions, experiments, conferences, jobs and data. Records merge arXiv e-prints, journal versions, reports and theses into one entry.

**Access.** Web search at inspirehep.net; open REST API with no key — `https://inspirehep.net/api/literature?q=dark+matter&fields=titles,arxiv_eprints&size=25` returns JSON, and appending `?format=bibtex` to any record URL gives a ready citation. Metadata is CC0 and bulk records are downloadable.

**Caveats.** Scope is strictly high-energy physics and its neighbours — astronomy is better served by NASA ADS and general physics by arXiv. The curated author profile is the accepted way to present a HEP publication record, but claiming yours requires an ORCID login. The API is unmetered on a small publicly funded service, so throttle voluntarily and cache.

*Also listed under: physics.*

### [Internet Archive Scholar](https://scholar.archive.org)

`Free` · beginner 4/5 · preserved OA full-text search

Full-text search across 85,899,891 academic papers preserved by the Internet Archive, built on the Fatcat bibliographic catalogue. Its distinctive value is long-tail and at-risk content: small journals, non-English titles and papers whose original publisher website has disappeared.

**Access.** Web search at scholar.archive.org with full-text queries; Fatcat catalogue and its API at fatcat.wiki; bulk metadata dumps published by the Internet Archive.

**Caveats.** Search this when a DOI resolves to a dead link — it is the best chance of recovering a paper from a defunct journal. Contrary to earlier reports, scholar.archive.org served full content to an automated fetch on 2026-08-28 and the stated corpus (85,899,891 papers) was confirmed on the page; there is still no documented public search API, so use the Fatcat catalogue API at fatcat.wiki or the bulk metadata dumps for anything systematic. Development has been quiet for some time and metadata quality is uneven compared with Crossref or OpenAlex, but the archive itself is live and searchable.

### [JSTOR free read-online access](https://about.jstor.org/whats-in-jstor/)

`Free (registration), email` · beginner 5/5 · humanities and social science archive

A free personal JSTOR account lets anyone read up to 100 articles every 30 days online, plus unlimited access to open-access books and journals and public-domain Early Journal Content. JSTOR's archive is the backbone of humanities and social science back-run literature.

**Access.** Register a free account at jstor.org, then use the 'read online' option on participating publishers' articles; items save to a personal Workspace.

**Caveats.** Read-online only — the 100-article allowance does not include PDF downloads, and not every article participates. Downloading requires JPASS, a personal subscription at $19.50/month or $199/year, which caps downloads at 10 PDFs/month or 120/year respectively across 2,400+ journals. Open-access and public-domain content on JSTOR is downloadable without any of this. For most unaffiliated readers the free 100/30 days is genuinely enough.

*Also listed under: humanities.*

### [Lens.org](https://www.lens.org)

`Freemium, email` · beginner 3/5 · scholarly and patent search

Search and analysis platform from Cambia, a non-profit, that uniquely links scholarly works to the patent literature — the only free tool that lets you see which patents cite a given paper. Useful for technology transfer, prior art and innovation research.

**Access.** Free scholarly and patent search at lens.org/lens/search/scholar/list; register a free account to save queries, build collections and export. API and bulk data are separately licensed products.

**Caveats.** Honest caveat: I could not verify Lens's current free-tier limits. The pricing pages are JavaScript-only and returned no readable content to either of my fetch tools, and the URLs commonly cited for them now 404. Anonymous scholarly search does load. Historically Lens has offered free individual and academic use with paid tiers for institutional and commercial users, and API/bulk access has always been a paid subscription — confirm current caps on the site before you build a workflow on it.

### [Litmaps](https://www.litmaps.com)

`Freemium, email` · beginner 4/5 · citation mapping and alerts

Builds interactive citation maps from seed papers and monitors them, emailing you when new work connects to your map. Emphasis is on ongoing literature monitoring rather than one-off exploration.

**Access.** Free account at litmaps.com; seed a map from a DOI, title or an imported reference library, then let it alert you.

**Caveats.** Verified free-tier limits from the pricing page on 2026-08-28: monthly (not weekly or daily) alerts, basic search only, up to 20 inputs, 2 Litmaps, 100 articles per map, no collaboration. Pro is $10/month with an academic email ($120/year) and removes all those caps; country-parity discounts are offered. The free tier is workable for one focused project, not for a whole thesis. Litmaps Ltd also now owns ResearchRabbit.

### [medRxiv](https://www.medrxiv.org)

`Free` · beginner 5/5 · health-sciences preprint server

Preprint server for clinical and public-health research, run by openRxiv with BMJ and Yale. OpenAlex indexes 86,455 medRxiv preprints as of 2026-08-28, 84,273 of them open access; epidemiological and trial results frequently appear here months before journal publication.

**Access.** Free reading, no account. Same API shape as bioRxiv: `https://api.biorxiv.org/details/medrxiv/{start-date}/{end-date}`. Subject RSS feeds and email alerts; indexed in Europe PMC under `SRC:PPR`.

**Caveats.** Screening is stricter than bioRxiv's because of clinical risk, but nothing is peer reviewed and medRxiv itself warns that preprints must not guide clinical practice or be reported as established information. Case reports and anything with identifiable patient data are rejected. Same six-licence choice as bioRxiv, so check reuse terms before mining.

*Also listed under: medicine, publishing.*

### [NASA ADS (Astrophysics Data System)](https://ui.adsabs.harvard.edu)

`Free (registration), api-key` · beginner 4/5 · astronomy and physics literature

NASA-funded literature index for astronomy, astrophysics, planetary science and physics, covering journal articles, arXiv e-prints, conference proceedings, theses and scanned historical literature, with full-text search, citation and reference links, and links out to observational data archives. It is the field-standard discovery tool in astronomy.

**Access.** Free web search at ui.adsabs.harvard.edu (no account needed to search). For the API, create a free account, generate a token under user settings, then `curl -H 'Authorization: Bearer <token>' 'https://api.adsabs.harvard.edu/v1/search/query?q=exoplanet&fl=bibcode,title'`. Python client `pip install ads`. Endpoints for search, metrics, BibTeX export and personal libraries.

**Caveats.** Rate limits are per endpoint per day and reported in the `X-RateLimit-Limit` response header — the documented example is 5,000 queries/day — resetting at UTC midnight; email adshelp@cfa.harvard.edu for details or a raise. Browsing and exporting citations in the web interface need no token at all. Use is governed by the ADS terms of use, which restrict redistribution of the holdings. Coverage falls away sharply outside astronomy and physics.

*Also listed under: physics, earth.*

### [Open Knowledge Maps](https://openknowledgemaps.org)

`Free` · beginner 5/5 · visual topic mapping

Charitable non-profit search service that turns a query into a clustered visual map of the most relevant results, drawn from BASE (over 400 million outputs from more than 11,000 sources in 400+ languages) and from PubMed, covering 25 output types including datasets and software. Free, no account, supported by library and institutional memberships.

**Access.** Enter a query at openknowledgemaps.org, choose the BASE or PubMed base index, and a map builds in about a minute; clusters expand into the underlying records with links to open-access full text. Each map gets a permanent URL you can cite or share; institutions can embed components in their own discovery systems.

**Caveats.** Best used at the very start of an unfamiliar topic to see the shape of a literature. It is not a systematic search tool: a map covers a top-ranked slice of results, not the full result set, so never report it as your search. Cluster labels are generated automatically and are sometimes vague or misleading. Throughput is best-effort on donation funding.

### [Open Library and Internet Archive](https://openlibrary.org)

`Free (registration), email` · beginner 5/5 · book catalogue and lending library

Open, editable catalogue of books run by the Internet Archive, linked to a lending collection of 4,196,072 items as of 2026-08-28. Public-domain texts are downloadable outright; many in-copyright books can be borrowed one reader at a time under controlled digital lending.

**Access.** Free account at archive.org to borrow; search and public-domain downloads need no account. Open Library has a free JSON API (`https://openlibrary.org/search.json?q=...`) and publishes bulk data dumps.

**Caveats.** Honest caveat: the lending programme was substantially curtailed by the outcome of Hachette v. Internet Archive, and several hundred thousand in-copyright titles were removed from lending. What remains available is real and legal, but do not assume a given modern book is borrowable. Public-domain material (pre-1930 in the US, broadly) is unrestricted and is where most of the research value sits — historical journals, government reports, out-of-print monographs. Borrow periods are typically one hour or 14 days.

### [OpenAIRE Graph](https://graph.openaire.eu)

`Free` · beginner 3/5 · European OA aggregator

EU-funded open research graph linking 237,289,559 publications, 106,541,040 datasets, 961,040 software entries and 41,871,152 other research products to 3,924,606 funded projects and 376,499 organisations, harvested from 157,198 data sources (counts checked 2026-08-28).

**Access.** Free REST API without a key: `https://api.openaire.eu/graph/v1/researchProducts?search=...&pageSize=50`; also filterable by `type=publication|dataset|software|other`. Web search at https://explore.openaire.eu. Full graph dumps published on Zenodo.

**Caveats.** Anonymous API access works but is rate-limited; registering an OpenAIRE account and using a token raises the ceiling. The unique value is the funding layer — tracing a paper back to the grant that paid for it — which most other indexes lack. Deduplication across 157k sources is imperfect, so expect some duplicate records. explore.openaire.eu blocked scripted requests during this sweep; use a browser.

### [OpenAlex](https://openalex.org)

`Free tier, email` · beginner 4/5 · open bibliographic graph

Open catalogue of the scholarly record run by the OurResearch nonprofit: 322,147,582 works (121,778,297 flagged open access), 126,053,818 authors, 255,810 sources and 134,448 institutions as of 2026-08-28, plus a cached archive of 50M+ open-access PDFs and ~43M Grobid TEI XML parses. Successor to Microsoft Academic Graph.

**Access.** REST API at https://api.openalex.org/works?filter=... ; Python `pip install pyalex`, then `from pyalex import Works; Works()["doi:10.1038/nature12373"]`. Full CC0 snapshot free from the S3 bucket `s3://openalex` (JSONL and, newly, hive-partitioned Parquet under data/parquet/), refreshed quarterly; latest release 2026-06-25.

**Caveats.** IMPORTANT CHANGE: the API is now metered in dollars, not calls. A free account key gets $1 of usage per day (resets midnight UTC); with no key you get $0.10/day. Rates: single-entity lookups by ID or DOI are free and unlimited; list+filter $0.10 per 1,000 calls; keyword or semantic search $1 per 1,000 calls; cached PDF download $10 per 1,000. So $1/day buys roughly 10,000 filter calls (1M results) or ~1,000 searches or 100 PDFs. Browsing openalex.org draws on the same budget (~1.8x costlier per search than a direct API call). Overflow needs prepaid credit in $1 increments (expires after 3 months) or an annual plan (Member $5,000/yr, Member+ $10,000/yr, Partner from $20,000/yr). The data itself stays CC0 and the whole snapshot remains a free download — only serving and freshness are billed. The snapshot is quarterly, so it lags the live API by up to three months.

*Also listed under: physics, chemistry, medicine, mathematics, cs-ml, neuro-psych, social, publishing, workflow-tools.*

### [OpenReview](https://openreview.net)

`Free` · beginner 3/5 · open peer review records

Non-profit peer-review platform built by Andrew McCallum's lab at UMass Amherst that publishes submissions together with their reviews, rebuttals, meta-reviews and decisions — at many venues including rejected papers. It runs review for ICLR, NeurIPS, ACL-family and many other machine-learning venues, with no fee to submit or to read.

**Access.** Free browsing and search at openreview.net. Public REST API v2: `https://api2.openreview.net/notes?content.venueid=ICLR.cc/2025/Conference&limit=1000`; Python client `pip install openreview-py`, then `openreview.api.OpenReviewClient(baseurl='https://api2.openreview.net')`. Web interface source is AGPL-3.0.

**Caveats.** The reviews themselves are the point: reading accepted and rejected papers' reviews is the cheapest available training in how a field actually judges work, which matters most for someone with no local mentor. What is public depends on each venue's configuration — some hide reviews, some hide rejected submissions. A raw unauthenticated API call was diverted to a bot-check challenge on 2026-08-28, so use openreview-py with a free account rather than plain HTTP fetches. Older venues (mostly pre-2024) still sit on API v1 at api.openreview.net.

*Also listed under: cs-ml, publishing.*

### [OSF Preprints](https://osf.io/preprints/)

`Free` · beginner 4/5 · multidisciplinary preprint aggregator

Center for Open Science aggregator searching across dozens of community-run preprint servers (PsyArXiv, SocArXiv, EdArXiv, AfricArXiv, MetaArXiv and others) alongside its own OSF Preprints service, with DOIs assigned to deposits.

**Access.** Web search across all providers at osf.io/preprints. Free public API: `https://api.osf.io/v2/preprints/?filter[q]=...` returning JSON:API records with DOIs, dates and download links. Free deposit with an OSF account.

**Caveats.** Reading and the API need no account; depositing needs a free one. This is the main preprint route for psychology, education, sociology and other social sciences that have no arXiv. Preprints are not peer reviewed and quality is uneven — check whether a published version exists. Some partner servers have shut down or moved over the years, so older links can rot.

### [PubMed and PubMed Central (E-utilities)](https://pubmed.ncbi.nlm.nih.gov)

`Free` · beginner 5/5 · biomedical index and full-text archive

PubMed holds 41,074,375 citation records (verified 2026-08-28 with `esearch.fcgi?db=pubmed&term=all[sb]`); PubMed Central holds roughly 12.3 million full-text articles, about 8.2 million of them inside the open-access filter. MeSH indexing makes PubMed the most precisely searchable biomedical corpus in existence.

**Access.** Web search, plus the free E-utilities API: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...&retmode=json`, then efetch for records. Python `pip install pymed-paperscraper`. Saved searches and email alerts via a free My NCBI account. PMC OA subset available in bulk over FTP.

**Caveats.** E-utilities work with no key at 3 requests/second; a free NCBI API key raises this to 10/second. PMC's 'open access subset' is the only part you may bulk-download and text-mine — the wider PMC archive is free to read but not to redistribute, and the commercial-use subset is narrower still. Coverage is biomedicine and adjacent fields only.

*Also listed under: biology, medicine.*

### [RePEc / IDEAS](https://ideas.repec.org)

`Free` · beginner 4/5 · economics literature index

Volunteer-run decentralised bibliography of economics: over 5,400,000 items of research indexed, of which over 4,800,000 can be downloaded in full text. Covers working papers, journal articles, books, chapters and software components, with author rankings and citation analysis via CitEc.

**Access.** Web search at ideas.repec.org, or the sibling interface EconPapers. Free author registration (RePEc Author Service) builds a profile and a public research record. Email 'new research' subscriptions by subject. MPRA (Munich Personal RePEc Archive) accepts self-deposits.

**Caveats.** The unusually high full-text ratio is because economics circulates via working-paper series that are open by default — this is the field where an unaffiliated researcher is least disadvantaged. The interface is dated and metadata quality varies by contributing archive. Rankings are widely used in economics hiring but are volunteer-computed and should not be treated as authoritative.

*Also listed under: social, econ-finance.*

### [Research4Life](https://www.research4life.org)

`Free tier, application` · beginner 2/5 · country-based access programme

Public-private partnership giving institutions in eligible low- and middle-income countries free or very low-cost access to paywalled journals, books and databases across five programmes: Hinari (health), AGORA (agriculture), OARE (environment), ARDI (applied science and technology) and GOALI (law and social science).

**Access.** Institutional registration through research4life.org; once an institution is registered, staff and students log in with institutional credentials. Country eligibility is published as Group A (free) and Group B (low annual fee) lists.

**Caveats.** This is an institutional programme, not an individual one — an unaffiliated researcher cannot register alone, and a researcher at an eligible institution that has not registered gets nothing until a librarian applies. Eligibility is determined by country group, so a poorly resourced institution in a high-income country is excluded entirely. Group A countries get free access; Group B institutions pay an annual fee. The same Group A/B lists are reused by many publishers to set APC waivers, so knowing your country's group is worth doing. Their website is behind a bot filter that blocked automated verification of current title counts, so I have not quoted any.

*Also listed under: chemistry, medicine, social, publishing.*

### [ResearchGate](https://www.researchgate.net)

`Free (registration), email` · beginner 4/5 · author-shared copies

Academic social network where authors post copies of their own papers and where a 'Request full-text' button emails the author directly. For many papers this is the fastest legal route to a PDF, because the person who wrote it is entitled to share it.

**Access.** Free account to search, download author-posted PDFs and send full-text requests. Google indexes many ResearchGate PDFs, so they often surface without an account.

**Caveats.** Grey but not piracy, and the distinction matters. Authors sharing their own accepted manuscript is usually permitted; authors uploading the publisher's typeset PDF often is not, and publishers have repeatedly forced bulk takedowns, so links rot. Availability is unpredictable and there is no coverage guarantee. Registration is pushy and the notification volume is high. Academia.edu is the comparable site but paywalls basic features behind a subscription and is harder to recommend. Both are commercial companies, not scholarly infrastructure — prefer a repository copy found via Unpaywall or CORE when one exists.

### [ResearchRabbit](https://www.researchrabbit.ai)

`Freemium, email` · beginner 5/5 · iterative literature discovery

Recommendation engine that learns from the papers you add to a collection and suggests related work, similar authors and emerging topics across 310+ million papers, with a configurable citation graph view. Claims over 1,000,000 users.

**Access.** Free account at researchrabbit.ai; seed a collection manually or import a Zotero library, then iterate on recommendations.

**Caveats.** STATUS CHANGE worth knowing: ResearchRabbit was famously 'free forever' but introduced a premium tier in 2025 and is now operated by Litmap Ltd, the same company as Litmaps. The free tier is still substantial — unlimited searches, unlimited library and collections, collaboration by sharing collections, library uploads, and up to 50 seed articles. RR+ ($10/month annual, $12.50 monthly, with country-parity discounts) raises seed articles to 300 and adds advanced search, multiple projects and alerts. The 50-seed cap is the one that bites on a large review.

### [SciELO](https://www.scielo.org)

`Free` · beginner 4/5 · Latin American and Iberian OA network

Open-access publishing and indexing network for Latin America, the Caribbean, Spain, Portugal and South Africa: 2,274 journals and 1,427,429 articles in the ArticleMeta index as of 2026-08-28, all free to read, mostly in Spanish and Portuguese alongside English. Also runs SciELO Preprints and SciELO Data.

**Access.** Web search at search.scielo.org and per-country collections (scielo.br, scielo.org.mx and others). Machine access via the ArticleMeta API with no key: `https://articlemeta.scielo.org/api/v1/article/identifiers/?collection=scl&limit=100`, plus per-collection OAI-PMH. Records also flow into Crossref, DOAJ and OpenAlex.

**Caveats.** The largest body of research on Latin American health, agriculture, education and social policy, much of it invisible in Anglophone indexes — but interface and content are Spanish/Portuguese first, so English-only keyword searches will badly under-retrieve. search.scielo.org and analytics.scielo.org both returned HTTP 403 to automated fetches on 2026-08-28 while the ArticleMeta API answered normally; script against ArticleMeta, browse in a browser. Metadata completeness varies by national collection.

*Also listed under: medicine, publishing.*

### [Semantic Scholar Academic Graph API](https://www.semanticscholar.org/product/api)

`Free tier, api-key` · beginner 3/5 · bibliographic API and bulk datasets

Allen Institute for AI's graph of roughly 214 million papers, 2.49 billion citations and 79 million authors, with citation contexts and intents, TLDR one-line summaries, and SPECTER embeddings. Bulk datasets are refreshed weekly; the latest release when checked was 2026-08-18.

**Access.** REST: `https://api.semanticscholar.org/graph/v1/paper/search?query=...`. Bulk: `https://api.semanticscholar.org/datasets/v1/release/latest` lists downloadable datasets — papers, abstracts, authors, citations, publication-venues, tldrs, embeddings-specter_v1/v2, s2orc and s2orc_v2 (full text).

**Caveats.** The unauthenticated pool is nominally 1,000 requests/second shared across every anonymous user worldwide, which in practice means constant throttling — a single test call returned HTTP 429 during this sweep. Request a free key via the form on the product page; the introductory key rate is 1 request/second, which is slow but reliable. S2ORC full text is restricted to open-access papers and carries its own terms. Abstracts are omitted for some publishers for licensing reasons.

*Also listed under: cs-ml, neuro-psych.*

### [SSRN](https://www.ssrn.com)

`Free (registration), email` · beginner 4/5 · social science preprint repository

Preprint and working-paper repository owned by Elsevier (RELX), strongest in law, economics, finance, management and accounting. OpenAlex indexes 1,667,992 SSRN works as of 2026-08-28 (source S4210172589), effectively all free to read; in law and finance this is where working papers circulate first and get cited for years before journal publication.

**Access.** Free full-text PDF from ssrn.com; a free account is needed for some downloads and for posting. Because SSRN blocks scripted access, find papers through Google Scholar or OpenAlex (`https://api.openalex.org/works?filter=locations.source.id:S4210172589`) and follow the link out.

**Caveats.** Commercial and Elsevier-owned, unlike arXiv or OSF Preprints: there is no open API and no bulk download, and an unauthenticated fetch of ssrn.com returned HTTP 403 on 2026-08-28. Nothing is peer reviewed, and papers can be withdrawn by the author or removed by the platform, so archive a copy of anything you cite. Series curated by sponsoring institutions are a weak quality signal at best.

*Also listed under: social, econ-finance, publishing.*

### [The Wikipedia Library](https://wikipedialibrary.wmflabs.org)

`Free (registration), credentialing` · beginner 3/5 · paywalled database access for editors

Gives active Wikipedia editors free access to over 100 paywalled content collections in more than 30 languages, including JSTOR, ProQuest Central, Cambridge University Press, Elsevier, Sage, Gale, the Wall Street Journal and the Telegraph. Wikimedia does not buy these — publishers donate access in exchange for citation visibility.

**Access.** Log in with your Wikimedia account at wikipedialibrary.wmflabs.org. Bundle collections give immediate web-proxy access with no application; limited-seat collections need an individual application that can take weeks.

**Caveats.** Eligibility is strict and verified automatically: at least 6 months of editing history, more than 500 edits across Wikimedia projects, at least 10 edits in the last 30 days, and no active block (block exemptions can be requested). That means it is not an on-demand solution — you have to have been a genuine contributor for months first. Access is granted for the purpose of improving Wikimedia content; bulk downloading violates the publisher agreements and can lose access for everyone. Still the single largest legal route into paywalled databases for an unaffiliated researcher who is willing to edit.

*Also listed under: chemistry, neuro-psych, social.*

### [Unpaywall](https://unpaywall.org)

`Free, email` · beginner 5/5 · legal OA copy finder

Given a DOI, returns whether a legal free-to-read copy exists and where, distinguishing publisher and repository copies, version (published/accepted/submitted) and licence. The browser extension turns a green tab when the paywalled article you are looking at has a free copy elsewhere.

**Access.** Browser extension for Chrome and Firefox — the single highest-value install for an unaffiliated reader. API: `https://api.unpaywall.org/v2/{DOI}?email=you@example.org`, then read `best_oa_location.url_for_pdf`. Simple Query Tool: paste up to 1,000 DOIs and get results emailed, no code required.

**Caveats.** The `email` parameter is mandatory — omit it and the API returns HTTP 422. Coverage is Crossref DOIs only: DataCite DOIs are deliberately excluded (nearly all are OA anyway), and a non-Crossref DOI returns 404. Since OurResearch's 'Walden' rewrite, Unpaywall is no longer a separate database — it is a legacy-compatible format served from the same OpenAlex pipeline, kept stable for the ecosystem built on it. For new code, query OpenAlex directly. The daily Data Feed is a paid subscription; the per-DOI API, extension and Simple Query Tool remain free.

*Also listed under: physics, chemistry, medicine, neuro-psych, social, publishing, workflow-tools.*

### [WorldCat](https://www.worldcat.org)

`Free` · beginner 5/5 · global library catalogue

OCLC's union catalogue of library holdings worldwide: 405 million books, 440 million articles, 30 million theses and dissertations, 25 million sound recordings, 10 million musical scores and 6 million maps. Shows which libraries near you hold a given item.

**Access.** Free web search at worldcat.org, no account needed; free account adds lists, citation export and saved searches. Enter a postcode to see nearby holding libraries.

**Caveats.** The practical route for an unaffiliated researcher to books and dissertations: find which library holds it, then request it through your public library's interlibrary loan service. Most public library systems will borrow from academic libraries on your behalf, sometimes free and sometimes for a small fee — this is a legal, underused route that works. The catalogue tells you what exists and where, not whether you can read it online. The site requires JavaScript and cannot be scripted; the WorldCat Search API is a paid OCLC product.

## Publishing

### [Free Journal Network](https://freejournals.org)

`Free` · beginner 4/5 · diamond open-access journal network

Non-profit membership network of scholar-controlled journals operating on the Fair Open Access model: no charges to readers and no charges to authors. 99 member journals are listed as of 2026-08-28 — 37 in mathematical sciences, 27 in natural sciences, medicine and engineering, 16 in social sciences and 15 in humanities and law.

**Access.** Browse the member journal list at freejournals.org/current-member-journals/ and submit directly to the journal. Membership is free for qualifying journals.

**Caveats.** The practical use is as a shortlist of venues where an unfunded author can publish at zero cost without the predatory-journal risk — every member is community-governed and vetted against published acceptance criteria. The list skews heavily towards mathematics and theoretical fields; some disciplines have almost no members. The organisation's blog has not posted since 2022, so it is more a curated directory than an active programme; the journal list itself remains current. DOAJ's no-fee filter covers far more journals if you need breadth.

*Also listed under: mathematics, publishing.*

### [Open Policy Finder (formerly Sherpa Romeo)](https://openpolicyfinder.jisc.ac.uk)

`Free` · beginner 4/5 · publisher self-archiving policy database

Jisc's database of publisher and funder open-access policies: for a given journal it tells you which version (submitted, accepted, published) you may deposit, where, after what embargo, and under which licence. Also covers funder OA compliance and transitional agreements.

**Access.** Web lookup by journal title or ISSN at openpolicyfinder.jisc.ac.uk; an API is available for programmatic checks.

**Caveats.** This is the successor to Sherpa Romeo — old sherpa.ac.uk links and bookmarks point at a renamed service, which trips up a lot of older guidance. The API is mid-migration to a new platform; Jisc extended the migration window to July 2026, so verify which endpoint you are calling. Site content is licensed CC BY-NC-ND. Policies are as reported by publishers and can lag actual contract terms — for a specific paper, your signed agreement wins.

### [ShareYourPaper](https://shareyourpaper.org)

`Free` · beginner 5/5 · assisted green OA self-archiving

OA.Works tool that takes a DOI, checks the journal's copyright and self-archiving terms, confirms whether a free copy already exists, tells you which version you are allowed to post, and deposits it into Zenodo for you. Built by an academia-owned non-profit funded by libraries and foundations.

**Access.** Go to `https://shareyourpaper.org/{DOI}` and follow the prompts. Open source, with an open API.

**Caveats.** Solves the actual blocker in green open access, which is not motivation but not knowing which version of your own paper you may legally post. Note that the sibling OA.Works products — the Open Access Button and InstantILL — were permanently switched off on 18 November 2025; ShareYourPaper and OA.Report are the two the organisation is continuing. It is a tool for authors depositing their own work, not a way to obtain someone else's paper.

### [SPARC Author Addendum](https://sparcopen.org/our-work/author-rights/)

`Free` · beginner 3/5 · author rights instrument

A free legal addendum you attach to a publisher's copyright transfer agreement to retain the right to post your own accepted manuscript, reuse it in teaching, and make it openly available. Produced by SPARC with accompanying plain-language guidance on author rights.

**Access.** Download the addendum PDF from sparcopen.org, complete it, and submit it with your signed publishing agreement.

**Caveats.** Publishers are not obliged to accept it and some will refuse or ignore it; you need to check that it was actually countersigned rather than assume. It works best when combined with a funder rights-retention policy that already requires it. If you sign a standard transfer without it, your self-archiving rights are whatever Open Policy Finder says the publisher grants — which is often less than you would like.

### [Think. Check. Submit.](https://thinkchecksubmit.org)

`Free` · beginner 5/5 · venue vetting checklist

Free checklist for deciding whether a journal or book publisher can be trusted with your manuscript, run by a cross-sector coalition of ALPSP, AUP, COPE, DOAJ, ISSN, LIBER, OAPEN, OASPA, STM and UKSG. Separate checklists for journals and for book publishers, with translations including Japanese, Spanish and Portuguese.

**Access.** Work through the journal or book checklist at thinkchecksubmit.org against the venue's own website; downloadable PDFs, posters and videos are provided for reuse in training and are openly licensed.

**Caveats.** It is a procedure, not a blacklist — deliberately, since blacklists are contested and go stale. Working through it honestly takes about fifteen minutes and requires you to actually check things (DOAJ indexing, editorial board affiliations, a real postal address, transparent fees). It tells you whether a venue is legitimate and transparent, not whether it is any good scholarly company for your paper.

*Also listed under: publishing.*

### [Zenodo](https://zenodo.org)

`Free, email` · beginner 5/5 · general-purpose repository

CERN-hosted open repository holding 7,191,588 records as of 2026-08-28. Accepts papers, preprints, datasets, software, posters and slides from anyone in any field, mints a DOI for each deposit, and versions records. Funded by CERN and the EU, not by deposit fees.

**Access.** Web upload at zenodo.org, or the REST API with a personal access token. GitHub integration mints a DOI for each software release automatically. Free deposit up to 50 GB per record by default; larger by request.

**Caveats.** The default answer to 'where do I put this so it has a permanent identifier and someone can cite it' when you have no institutional repository. Anyone can deposit, so Zenodo carries no quality signal — that is a feature for self-archiving and a caveat for readers. Check your publisher's self-archiving policy (Open Policy Finder) before depositing an accepted manuscript; ShareYourPaper automates that check and deposits into Zenodo for you.

*Also listed under: physics, chemistry, mathematics, cs-ml, social, compute, publishing, workflow-tools.*

## Funding

### [DOAJ APC and waiver metadata](https://doaj.org/api/)

`Free` · beginner 3/5 · no-fee and waiver journal finder

Every DOAJ journal record carries structured fields for whether the journal charges an APC (`apc.has_apc`, with maximum price and currency) and whether it operates a waiver policy (`waiver.has_waiver`, with a URL). 14,433 of the 23,371 indexed journals charge authors nothing at all.

**Access.** Query the free API, e.g. `https://doaj.org/api/search/journals/bibjson.apc.has_apc:false%20AND%20bibjson.subject.term:...`, or filter by 'Without APCs' in the web interface. Also available in the journal CSV and public data dump.

**Caveats.** The most concrete answer to 'where can I publish this if nobody will pay an APC': filter DOAJ to no-fee journals in your subject before you look anywhere else. Fields are self-reported by publishers and can be stale — check the journal's own site before submitting. A no-fee journal is not automatically a good journal; combine with the DOAJ seal, indexing and editorial-board checks.

### [PLOS Publication Fee Assistance and country waivers](https://plos.org/publish/fees/)

`Free tier, application` · beginner 3/5 · APC waiver programme

PLOS waives fees on a country basis and on demonstrated need. Authors without external funding in Research4Life Group A countries publish free in any PLOS journal; Group B authors publish free in PLOS Biology, Medicine and Sustainability & Transformation and pay $940 elsewhere. Publication Fee Assistance is open to any author who can demonstrate financial need.

**Access.** Apply for PFA at submission through the PLOS submission system; decisions typically arrive within 10 business days. Country eligibility follows the Research4Life Group A/B lists.

**Caveats.** Fee-assistance applications are kept confidential from editors and reviewers, and PLOS states that publication decisions are made on editorial criteria alone — so applying does not prejudice your paper. Standard APCs are substantial if you do not qualify: PLOS ONE ranges $1,088–$2,477 depending on article type and other PLOS journals $2,596–$6,460. The same Research4Life country lists drive waiver schemes at Springer Nature, Wiley, Elsevier, BMJ and others, so check your country's group once and reuse it.

## Learning

### [Aaron Tay, Musings about librarianship](https://musingsaboutlibrarianship.blogspot.com)

`Free` · beginner 3/5 · practitioner analysis of search tools

Long-running blog by an academic librarian that tests and compares scholarly search and discovery tools in detail — OpenAlex versus Scopus coverage, how Semantic Scholar's citation data differs from Crossref's, what AI literature tools actually do and where they fail.

**Access.** Free to read, no registration; RSS feed available.

**Caveats.** The most reliable independent source on what these tools really cover, written by someone who runs the tests rather than repeating vendor claims — the antidote to listicles. Blog posts date quickly in a field where free tiers change every few months, so check the post date. One person's perspective, mostly from a Singapore academic library context.

### [Cochrane Handbook for Systematic Reviews of Interventions](https://training.cochrane.org/handbook)

`Free` · beginner 2/5 · systematic search methodology

The reference methodology text for systematic reviews, free to read online in full. Its chapters on searching for studies define how to build, document and report a reproducible database search — the skill that separates a literature review from a list of papers you happened to find.

**Access.** Free web version at training.cochrane.org/handbook, chapter by chapter. Cochrane also publishes free interactive learning modules.

**Caveats.** Written for health interventions, but the search-strategy chapters transfer to any field: block structure, controlled vocabulary versus free text, sensitivity versus precision, and how to record a search so someone else can rerun it. Dense and long — read the searching chapters, not the whole thing. Pair it with the PRISMA statement for the reporting side.

*Also listed under: medicine.*

### [Library Carpentry](https://librarycarpentry.org/lessons/)

`Free` · beginner 4/5 · data skills for literature work

Free, openly licensed lesson materials from The Carpentries aimed at people working with library and bibliographic data: shell basics, regular expressions, OpenRefine for messy metadata, SQL, Git, and working with web APIs and structured data formats.

**Access.** All lessons are free to read and work through self-paced at librarycarpentry.org/lessons/, CC-BY licensed. Instructor-led workshops are run worldwide, sometimes for a fee.

**Caveats.** The OpenRefine and regular-expressions lessons are the highest-value hours here: deduplicating and normalising a few thousand exported bibliographic records is the actual bottleneck in most literature projects, and these teach exactly that. Self-study works fine — the lessons are written to be followed without an instructor. Not research-methods training; it is data-handling craft.

### [Peter Suber, Open Access (MIT Press)](https://cyber.harvard.edu/hoap/Open_Access_(the_book))

`Free` · beginner 5/5 · foundational text

The standard short book explaining what open access is, the difference between gratis and libre, green and gold routes, licences, embargoes, and the economics of the system. Written by the field's most careful thinker and made openly available by the author and MIT Press.

**Access.** Free full text linked from the Harvard Open Access Project page, in multiple formats. Around 200 pages; readable in an afternoon.

**Caveats.** Read this before you form opinions about APCs, Plan S or predatory publishing — almost every confused argument on those topics is resolved in it. Published in 2012 with later updates and supplements, so specific policies and figures are dated; the conceptual framework is not. The companion Open Access Tracking Project provides current news.

### [PRISMA statement](https://www.prisma-statement.org)

`Free` · beginner 4/5 · review reporting standard

The reporting standard for systematic reviews and meta-analyses: a checklist and a flow diagram specifying what a review must disclose about its search, screening, inclusion and exclusion. Freely available with extensions for scoping reviews, network meta-analyses and other designs.

**Access.** Download the checklist and flow-diagram templates free from prisma-statement.org; no registration.

**Caveats.** Increasingly demanded by journals well outside medicine, and following it makes your search auditable, which is exactly what an unaffiliated author needs when reviewers wonder whether you had access to the literature. Filling in the flow diagram honestly also exposes to you how much you missed. It is a reporting standard, not a method — it tells you what to disclose, not how to search.

### [The Turing Way](https://book.the-turing-way.org)

`Free` · beginner 4/5 · open and reproducible research handbook

Large, community-written, openly licensed handbook on reproducible, ethical and collaborative research, with guides covering open access, preprints, licensing, research data management, version control and collaboration practices.

**Access.** Free online book at book.the-turing-way.org; CC-BY licensed and openly developed on GitHub, so you can file an issue or contribute a chapter.

**Caveats.** Use it as a reference rather than reading it cover to cover — it is very large. The open-access and licensing chapters are a practical complement to Suber's book, covering what to actually do rather than why. Being community-written, depth varies between chapters and some are stubs.

## Community

### [Academia Stack Exchange](https://academia.stackexchange.com)

`Free` · beginner 5/5 · academic practice Q&A

Q&A site covering the practice of academic life, with a large accumulated archive on exactly this catalogue's questions: getting papers without institutional access, publishing as an independent researcher, emailing authors, arXiv endorsement, and choosing venues without funding.

**Access.** Free reading with no account; free account to ask or answer. Search the existing archive first — most access questions are already answered in depth.

**Caveats.** Answers skew towards North American and Western European STEM norms and towards people who do have institutional affiliations, so weigh advice about 'just ask your librarian' accordingly. Requests for copyrighted PDFs are off-topic and get closed; questions about legal routes are welcome. Voting-based, so accepted answers can be dated — check the timestamps on anything about tools or services.

*Also listed under: publishing.*

### [Crossref Community Forum](https://community.crossref.org)

`Free, email` · beginner 3/5 · scholarly metadata practitioners

Crossref's public Discourse forum where staff, publishers, repository managers and developers discuss metadata, DOIs, the REST API and scholarly infrastructure. Crossref staff answer technical API questions directly.

**Access.** Free reading with no account; free account to post.

**Caveats.** The right place for 'why does this DOI's metadata look wrong' and API behaviour questions — you get an answer from people who run the service rather than speculation. It is an infrastructure forum, so it assumes you know what a DOI prefix is. For running a small journal, the discussions on membership, fees and deposit workflows are directly useful.

### [PubPeer](https://pubpeer.com)

`Free` · beginner 4/5 · post-publication peer review

Post-publication peer review platform run by the PubPeer Foundation, a US 501(c)(3) nonprofit, where researchers comment on published papers. In practice it is where image duplication, statistical impossibilities and data fabrication surface years before a formal retraction.

**Access.** Free search and reading with no account; commenting needs a free account and can be done anonymously. Browser extension for Chrome and Firefox flags any paper you view that has PubPeer comments.

**Caveats.** Install the extension and it costs you nothing thereafter — it will silently warn you when a paper you are reading has been questioned. Comments are user-generated and unrefereed; the Foundation itself says they are 'sources of potentially useful information whose veracity readers must evaluate for themselves'. Some comments are wrong or vexatious. Absence of comments means nothing.

### [Zotero Forums](https://forums.zotero.org)

`Free, email` · beginner 5/5 · reference management support

Official support forum for Zotero, staffed by the core developers alongside experienced users. In practice it is also the best public venue for questions about citation styles, metadata capture from awkward sources, and bibliographic data wrangling generally.

**Access.** Free reading; free account to post. Search before posting — most problems have been answered.

**Caveats.** Responses come from actual maintainers, often the same day, and the archive goes back well over a decade. Scope is Zotero-specific: general 'how do I find this paper' questions belong elsewhere. CSL citation-style problems are handled here and in the citation-style-language GitHub repositories.

*Also listed under: workflow-tools.*
