# Publishing, identity & preservation

Part of [research-vault](../README.md). 77 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (3) · [Software](#software) (5) · [Literature](#literature) (13) · [Publishing](#publishing) (46) · [Funding](#funding) (3) · [Learning](#learning) (2) · [Community](#community) (5)

## Data

### [figshare](https://figshare.com/)

`Free tier, email` · beginner 5/5 · general-purpose repository with DOI minting

General-purpose repository that mints DataCite DOIs for datasets, figures, posters, preprints, theses and software. A free figshare.com account is documented as getting 20 GB of private storage, individual files up to 20 GB, a maximum of 500 items, 500 files per item, and 100 projects and 100 collections.

**Access.** Web upload at figshare.com after signing up. Public REST API needs no key for reads: curl 'https://api.figshare.com/v2/articles?page_size=1'; deposits use a personal token (Applications settings). OAI-PMH endpoint at https://api.figshare.com/v2/oai?verb=Identify; a GitHub integration archives a tagged release and mints a DOI for it.

**Caveats.** Anything larger than the 20 GB quota or a 20 GB file needs paid Figshare+ or an institutional repository (Amazon S3 caps any single file at 5 TB regardless). Published items are permanent — a public DOI cannot simply be deleted. figshare is a Digital Science (Holtzbrinck) product, so this is corporate rather than community-governed infrastructure; Zenodo is the non-profit equivalent with a larger 50 GB per-record allowance.

*Also listed under: compute.*

### [re3data](https://www.re3data.org/)

`Free` · beginner 4/5 · registry of research data repositories

Global registry describing 3,521 research data repositories as of 2026-08-31, managed and operated by Karlsruhe Institute of Technology and Purdue University Libraries. Each entry records subject coverage, accepted content types, access and upload conditions, licences, persistent identifier schemes, certificates such as CoreTrustSeal, and policies.

**Access.** Browse or filter at re3data.org by subject, country, content type, PID scheme, certificate and access type; every repository has a stable re3data ID. An open API returns the same records (documentation at re3data.org/api/doc), and all registry metadata is released under CC0.

**Caveats.** It describes repositories, not datasets — use it to choose where to deposit, then search inside the repository you pick. Entries are curated by an editorial board and can lag reality, so confirm current size limits, fees and licence options on the repository's own page before uploading. Listing implies no quality judgement: the certificate, policy and PID fields are the signal. Answers the concrete question funders now ask — 'a discipline-specific repository, or a general one like Zenodo?' — with a filterable list instead of guesswork.

### [Zenodo](https://zenodo.org/)

`Free (registration), email` · beginner 5/5 · general-purpose repository with DOI minting

CERN-operated catch-all repository that mints a DataCite DOI for anything — data, code, slides, posters, theses, negative results — and holds 7,193,352 records as of 2026-08-28. Each record allows up to 100 files and 50 GB (50,000,000,000 bytes), with up to 200 GB available on request.

**Access.** Web upload at zenodo.org/uploads/new, or REST API with a personal token (Settings > Applications). One-click code archiving: enable a GitHub repository under zenodo.org/account/settings/github, then cut a GitHub release and Zenodo deposits the tarball and mints a version DOI plus a concept DOI that always points at the newest version.

**Caveats.** Registration is open to anyone worldwide with no affiliation check — the single most useful fact in this section for unaffiliated researchers. Records are versioned and DOIs are permanent, so you cannot silently delete a published record; plan for that before uploading. Zenodo does not curate or peer-review, so a DOI here signals preservation and citability, not validation.

## Software

### [Janeway](https://janeway.systems/)

`Free` · beginner 2/5 · journal and preprint publishing platform

Open-source (Python/Django) publishing platform built by the Open Library of Humanities team at Birkbeck, University of London, and used by OLH journals and by EarthArXiv via the California Digital Library. Handles journals, repositories and preprint servers in one codebase.

**Access.** Source and installation docs at janeway.systems (link through to the public repositories); self-host, or use the team's hosting service. Supports Crossref DOI deposit, OAI-PMH and typesetting workflows out of the box.

**Caveats.** Smaller community and thinner documentation than OJS, so self-hosting expects more Django familiarity. Hosting from the Janeway team is a paid service. Best treated as an option when you are already in the OLH/CDL orbit or need repository plus journal in one system.

### [Open Journal Systems (OJS) / Public Knowledge Project](https://pkp.sfu.ca/software/ojs/)

`Free` · beginner 2/5 · journal publishing platform

Free, open-source journal management and publishing software from the Public Knowledge Project, used by thousands of small and scholar-run journals worldwide. It covers submissions, peer review, editing, issue publication, DOI registration plugins and OAI-PMH metadata export.

**Access.** Download and self-host from pkp.sfu.ca/software/ojs (PHP + MySQL/PostgreSQL; a modest shared-hosting account is enough for a small journal). Companion products: OPS for preprint servers, OMP for monographs. PKP Publishing Services offers paid hosting if you would rather not run a server.

**Caveats.** The software is free; hosting, a domain, DOI registration (Crossref membership) and long-term preservation are not. Running a journal on OJS is a real sysadmin and editorial commitment — upgrades between major versions require care. PKP's Preservation Network offers free archiving for qualifying OJS journals.

### [Overleaf](https://www.overleaf.com/)

`Free tier, email` · beginner 5/5 · collaborative LaTeX writing

Browser-based collaborative LaTeX editor with a free plan at $0/month allowing 1 collaborator per project and unlimited projects, plus a large template gallery covering most journal and conference styles. It removes the local TeX-installation barrier entirely.

**Access.** Web interface at overleaf.com; start from a journal template in the gallery, or import a .zip / link a GitHub repo (Git integration is a paid feature). Several publishers, including IEEE and Springer, offer direct submission from Overleaf.

**Caveats.** The free tier limits you to one collaborator per project (different people per project is fine) and imposes a shorter compile timeout, which bites on long documents with many figures — the usual workaround is to precompile figures to PDF or move to a local TeX Live install, which is free and unlimited. Git/Dropbox sync, track changes and full document history are paid. Overleaf is owned by Digital Science.

### [Quarto](https://quarto.org/)

`Free` · beginner 3/5 · manuscript authoring and publishing

Open-source scientific publishing system from Posit (v1.9.38, released 2026-05-25) that renders one .qmd or notebook source into a journal-ready PDF/LaTeX, MS Word, a website and a MECA submission package, with executable Python, R, Julia and Observable code blocks and BibTeX citations.

**Access.** Install the platform package from quarto.org/docs/download (or 'brew install quarto'), then 'quarto render paper.qmd'. Journal formats come from 'quarto use template <org>/<template>' (community-maintained templates for ACM, Elsevier, AGU and others); works from VS Code, RStudio, Jupyter or a plain text editor. Manuscript projects are documented at quarto.org/docs/manuscripts.

**Caveats.** PDF output needs a TeX installation — 'quarto install tinytex' handles that. Journal templates are community-maintained and can lag publisher style changes, so check the target journal's own class file before submitting. It is an authoring toolchain, not a reference manager: pair it with Zotero plus Better BibTeX for the .bib file. Overleaf remains easier for co-authors who will not install anything.

*Also listed under: workflow-tools.*

### [Zotero](https://www.zotero.org/)

`Free tier, email` · beginner 5/5 · reference manager

Free, open-source reference manager from the non-profit Corporation for Digital Scholarship: a browser Connector saves citations plus PDFs from journal pages, and word-processor plugins insert citations and bibliographies in any CSL style. Library metadata syncing is free and unlimited; attached files use 300 MB of free Zotero Storage, above which plans cost $20/year for 2 GB, $60/year for 6 GB or $120/year unlimited (prices listed 2026-08-28).

**Access.** Download the desktop app for macOS/Windows/Linux at zotero.org/download plus the browser Connector; cite while writing with the Word, LibreOffice or Google Docs plugin. Local use needs no account; sync needs a free account, and attachments can go to your own WebDAV server instead of Zotero Storage. Web API with a key from Settings > Security: curl 'https://api.zotero.org/users/<userID>/items?limit=5'

**Caveats.** Data syncing (items, notes, tags) is free and unlimited — only file attachments count against the 300 MB, so a PDF-heavy library hits the cap fast; WebDAV avoids paying but you must supply the server. Group-library file storage is billed to the group owner, not the members. Automatic metadata capture is imperfect for scanned PDFs and small publishers, so audit imported records before submission.

## Literature

### [CORE](https://core.ac.uk/)

`Free (registration), api-key` · beginner 3/5 · open access full-text aggregator

The largest aggregation of open access full texts harvested from institutional and subject repositories worldwide, offering search, a recommender, an OAI resolver and bulk datasets for text and data mining.

**Access.** Web search at core.ac.uk; API at api.core.ac.uk/v3 requires a free key (register at core.ac.uk/services/api) — curl -H 'Authorization: Bearer $CORE_KEY' 'https://api.core.ac.uk/v3/search/works?q=title:reproducibility'. Full dataset downloads and FastSync are available for research use.

**Caveats.** The free API key carries rate limits; heavy or commercial use is expected to go through a paid membership or bespoke contract. Because it harvests repositories, you get many versions of the same paper (submitted, accepted, published) and deduplication is imperfect. Metadata quality inherits whatever the source repository supplied.

### [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)

`Free` · beginner 3/5 · DOI metadata registry

The metadata behind most journal-article DOIs: 185,913,541 records on 2026-08-28, covering titles, authors, ORCID iDs, funder IDs, licences, references and retraction notices. It is the substrate almost every other discovery tool is built on.

**Access.** REST API, no key: curl 'https://api.crossref.org/works/10.1371/journal.pone.0000308' or search with 'https://api.crossref.org/works?query.bibliographic=...&mailto=you@example.com'. Python: pip install habanero. Full metadata dumps are released annually as a torrent.

**Caveats.** Reading metadata is free and open; registering DOIs is not — that requires Crossref membership paid by a publisher, so an individual cannot mint a Crossref DOI directly (use Zenodo/OSF/Figshare for a DataCite DOI instead). Reference lists are only present when the publisher deposited them, so citation coverage is uneven.

### [DataCite Commons](https://commons.datacite.org/)

`Free` · beginner 3/5 · DOI metadata for data, software and preprints

Search and API over DOIs registered through DataCite — datasets, software, preprints, theses and other non-article outputs; the API reported 133,810,957 DOIs on 2026-08-28. This is where a Zenodo, OSF or institutional-repository DOI becomes machine-findable.

**Access.** Web interface at commons.datacite.org; REST API with no key: curl 'https://api.datacite.org/dois?query=creators.nameIdentifiers.nameIdentifier:*0000-0002-1825-0097*'. GraphQL endpoint at api.datacite.org/graphql for linked queries across works, people and organisations.

**Caveats.** Like Crossref, reading is free but registering DOIs requires a paying DataCite member — which is exactly why an individual routes through Zenodo or OSF, both of which mint DataCite DOIs for free. Metadata completeness varies a lot by repository.

### [Directory of Open Access Books (DOAB)](https://www.doabooks.org/)

`Free` · beginner 4/5 · open access book directory

Discovery service for peer-reviewed open access academic books and chapters from vetted publishers, with the PRISM service recording each title's peer review procedure. The companion OAPEN Library (oapen.org) hosts and preserves the full texts.

**Access.** Web search at doabooks.org, with links straight to publisher-hosted or OAPEN-hosted full texts; metadata is downloadable in bulk and exposed via OAI-PMH for library systems.

**Caveats.** A directory of books that are already open — it is not a route to publish one. Strongest in humanities and social sciences and in European publishing; English-language North American university presses are less consistently represented. Licences vary by title, so check before reusing content.

### [Europe PMC](https://europepmc.org/)

`Free` · beginner 4/5 · biomedical literature database and deposit route

Free database of life-science and biomedical literature including abstracts, open access full texts, preprints and grant-linked records, with a REST API that needs no key. It is also a deposit route: authors funded by participating funders can submit accepted manuscripts through Europe PMC plus to satisfy open access mandates.

**Access.** Web search at europepmc.org; REST API, no key: curl 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=cancer&format=json&pageSize=1'. Author manuscript deposit via plus.europepmc.org for eligible funders; the US equivalent is PubMed Central's NIHMS system.

**Caveats.** The manuscript deposit route works only if one of the participating funders supported the work, so it is not a general-purpose repository. Full text is available only where the publisher or author made it open; abstracts are universal. Preprint indexing includes bioRxiv and medRxiv but is not exhaustive.

*Also listed under: chemistry, biology, medicine, neuro-psych, literature-access.*

### [Google Scholar profiles](https://scholar.google.com/citations)

`Free (registration), email` · beginner 5/5 · author profile and citation metrics

Free author profile with automatic publication matching, citation counts, h-index and i10-index, plus per-paper citation alerts. It covers preprints, theses, book chapters and conference papers that Scopus and Web of Science ignore, which makes it the most inclusive metrics source for people outside well-indexed venues.

**Access.** Web interface: sign in with any Google account at scholar.google.com/citations, click 'My profile', confirm the papers it proposes, and set the profile to public so it appears in search. Set up 'Follow' alerts for new citations to your work and for other authors.

**Caveats.** Any Google account works — an institutional email only adds a 'verified email at' line, it is not required to have a profile. There is no API and scraping is blocked, so metrics cannot be pulled programmatically; use OpenAlex for that. Automatic matching pulls in wrong papers and merges distinct authors, so audit the list. Citation counts include non-peer-reviewed sources and are inflated relative to Scopus/WoS — say which source you used when you quote a number.

### [OpenAIRE Explore](https://explore.openaire.eu/)

`Free` · beginner 3/5 · open science aggregator and funder linking

EU-funded aggregator that links publications, datasets, software and projects harvested from thousands of repositories; its public API reported 237,292,434 publications on 2026-08-28. Its distinctive use is showing a funder that a given output is open and connected to a specific grant.

**Access.** Search at explore.openaire.eu. Free REST API, no key: curl 'https://api.openaire.eu/search/publications?title=reproducibility&size=1&format=json'; a newer Graph API and bulk dumps are documented at graph.openaire.eu. Claiming links between a paper, a dataset and a project is done from a free account.

**Caveats.** Metadata quality is inherited from source repositories, so duplicates and thin records are common and author disambiguation is weaker than OpenAlex's. Project linking is built around EU grant identifiers; other funders are covered unevenly. The legacy search API coexists with the newer Graph API — check the developer docs before building anything long-lived on an endpoint.

### [OpenAlex](https://openalex.org/)

`Free` · beginner 4/5 · open bibliographic database

Fully open index of scholarly works and their metadata, successor to Microsoft Academic Graph. On 2026-08-28 the API reported 322,147,582 works, 126,053,818 authors, 255,810 sources, 136,136 institutions and 45,639 funders. Author pages give a free, no-paywall alternative to Scopus/Web of Science profiles.

**Access.** REST API, no key: curl 'https://api.openalex.org/works?filter=author.orcid:0000-0002-1825-0097&mailto=you@example.com'. Python client: pip install pyalex. Whole-corpus snapshots are downloadable from an S3 bucket for local analysis.

**Caveats.** Adding &mailto= puts you in the faster 'polite pool'; anonymous use is rate-limited. Author disambiguation is automated and imperfect — you can claim and correct your own author record, which is the practical fix. Institution and funder coverage is thinner outside Europe and North America.

### [OpenCitations](https://opencitations.net/)

`Free` · beginner 3/5 · open citation data

CC0 citation infrastructure from the Research Centre for Open Scholarly Metadata at the University of Bologna: the INDEX holds citation links between works and META holds the bibliographic records behind them, both queryable per DOI with no key — a free stand-in for Scopus or Web of Science citation counts.

**Access.** REST API, no key: curl 'https://api.opencitations.net/index/v2/citation-count/doi:10.1186/1756-8722-6-59' (returned 217 on 2026-08-28) and 'https://api.opencitations.net/meta/v1/metadata/doi:10.1186/1756-8722-6-59'. Also SPARQL endpoints (sparql.opencitations.net), an OCI resolver, and complete CC0 dumps at download.opencitations.net.

**Caveats.** Coverage depends on publishers depositing open references in Crossref, so counts run lower than Scopus in fields whose publishers keep references closed — say which source a number came from when you quote it. Use the api.opencitations.net host and the v2 index paths; the older opencitations.net/index/api/... URLs redirect. Bulk dumps are very large; query the API for one-off lookups.

### [PubMed Central (PMC) and NIHMS](https://pmc.ncbi.nlm.nih.gov/)

`Free` · beginner 4/5 · biomedical full-text archive and funder deposit route

The US National Library of Medicine's free full-text archive of biomedical and life-science literature — over 11.3 million articles as of FY2025 — and the mandated destination for manuscripts from NIH and partner-funder awards, deposited through the NIH Manuscript Submission system (NIHMS). Some content is released only after a publisher embargo.

**Access.** Search and read at pmc.ncbi.nlm.nih.gov. Programmatic access via E-utilities with no key: curl 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term=reproducibility&retmode=json&retmax=2', then efetch for full records; the OA subset is downloadable in bulk over FTP/S3 for text mining. Authors (or their journals) deposit accepted manuscripts at nihms.nih.gov.

**Caveats.** Reading is open to everyone, but depositing is not a general-purpose route — NIHMS only accepts manuscripts attached to a participating funder's award, so unfunded or unaffiliated authors use a preprint server or Zenodo instead. Only the OA subset may be redistributed or text-mined; the rest is free to read only. Europe PMC covers the same literature with a European funder deposit route.

*Also listed under: medicine, neuro-psych.*

### [Retraction Watch Database (via Crossref)](https://api.labs.crossref.org/data/retractionwatch)

`Free` · beginner 4/5 · retraction and correction records

The Retraction Watch Database, acquired by Crossref in 2023 and released openly, downloadable as a single CSV with fields including title, journal, publisher, country, article type, retraction date and DOI, original paper DOI, retraction nature and reason. Record IDs run past 72,000.

**Access.** Direct download, no key: curl 'https://api.labs.crossref.org/data/retractionwatch?you@example.com' > retractions.csv, then load with pandas. Retraction notices are also surfaced in the standard Crossref API 'update-to' field on affected DOIs.

**Caveats.** The file is large; expect a slow download and do it once rather than in a loop. Reasons are free text drawn from multiple curators, so normalise before counting. Presence in the database is not proof of misconduct — many entries are honest-error retractions or publisher-initiated corrections. Check your own reference list against it before submitting; citing retracted work is embarrassing and increasingly flagged automatically.

### [ROR (Research Organization Registry)](https://ror.org/)

`Free` · beginner 4/5 · institution identifier

Open, CC0 registry of research organisation identifiers — 134,298 organisations on 2026-08-28 — increasingly required by publishers and funders in affiliation fields. It includes an 'independent researcher' path only indirectly, which matters when you have no institution to name.

**Access.** Web search at ror.org/search; REST API with no key: curl 'https://api.ror.org/v2/organizations?query=Birkbeck'. Full data dumps are published on Zenodo under CC0.

**Caveats.** ROR IDs exist for organisations, not people — an unaffiliated author simply leaves the ROR field empty or uses 'Independent Researcher', which most submission systems accept as free text. New organisations can be requested via a public curation process, but a one-person consultancy is unlikely to qualify.

### [Unpaywall](https://unpaywall.org/)

`Free` · beginner 5/5 · legal open access full-text locator

Database of legally posted open access copies harvested from repositories, preprint servers and publisher sites, delivered as a browser extension and an API. It is the legal way to get past a paywall when an author or repository copy exists.

**Access.** Browser extension for Chrome and Firefox: a green tab appears on paywalled article pages when a free version exists. API keyed on DOI, no signup but your real email is mandatory: curl 'https://api.unpaywall.org/v2/10.1038/nature12373?email=you@example.com' (a placeholder address returns HTTP 422). Bulk data snapshots are available for download.

**Caveats.** Only finds copies that someone posted legally — it will not help with an article that has no open version anywhere. The Open Access Button, long recommended alongside it, shut down on 18 November 2025 and its own site now points users here. For requesting a copy directly, email the corresponding author; that remains legal and works surprisingly often.

## Publishing

### [African Journals Online (AJOL)](https://www.ajol.info/)

`Free` · beginner 5/5 · African-published journal platform

Non-profit platform operating since 1998 that indexes and hosts African-published peer-reviewed journals: the site reported 977 journals on 2026-08-28, of which 459 are open access and 283 charge authors nothing, across 288,357 full-text articles (172,840 open access, 51,307 in no-fee open access journals). Each partner journal carries a JPPS (Journal Publishing Practices and Standards) rating.

**Access.** Web search and browse at ajol.info by subject, country, JPPS rating, or the 'No fee Open Access (Free To Read & Free for Authors)' list — that list is the practical shortlist of diamond venues published in Africa. Submission goes through each journal's own site; reading open access titles needs no account.

**Caveats.** Not everything indexed is free to read: 459 of the 977 journals are open access and the rest show abstracts only. The JPPS rating is AJOL's own assessment of publishing practice and is not equivalent to DOAJ indexing — check both before submitting. Coverage is African-published journals specifically, so a Nigerian author publishing in a European title will not appear here. The service is donation-funded.

*Also listed under: medicine, literature-access.*

### [arXiv](https://arxiv.org/)

`Free (registration), email` · beginner 3/5 · preprint server (physics, maths, CS, quantitative biology, economics)

The oldest and most consequential preprint server, now run by arXiv as an independent non-profit. Posting is free, papers get a permanent identifier and are announced daily; in maths, physics and machine learning the arXiv version is often the version people actually read and cite.

**Access.** Web submission at arxiv.org/submit (LaTeX source strongly preferred over PDF). Full-text and metadata harvesting via the free API: curl 'http://export.arxiv.org/api/query?search_query=all:transformer&max_results=5'. Bulk metadata via OAI-PMH; full-text bulk via a requester-pays S3 bucket.

**Caveats.** The real barrier for unaffiliated authors is endorsement: first-time submitters and anyone posting to a new category need at least one positive endorsement per category. Authors with a recognised institutional email who have claimed their co-authored papers are usually auto-endorsed; without that, you must ask an established author in the field — find candidates by checking who can endorse on recent papers you cite, and send them the endorsement link arXiv emails you when you start a submission. Cold-emailing strangers works, but slowly. Moderators also reclassify or decline submissions on scope and scholarly-standards grounds with limited appeal.

*Also listed under: physics, cs-ml, literature-access.*

### [AsPredicted](https://aspredicted.org/)

`Free (registration), email` · beginner 5/5 · lightweight preregistration

Minimal preregistration service built around eight fixed questions, producing a time-stamped one-page PDF with a unique verification URL. Designed to take minutes rather than hours, which is why it gets used in practice in experimental psychology and behavioural economics.

**Access.** Web interface at aspredicted.org: click 'CREATE', answer the eight questions, and all listed co-authors must confirm by email before the preregistration is finalised. Keep it private and share the PDF with reviewers, or make it public later.

**Caveats.** Deliberately shallow — no file attachments, no analysis code, no versioning — so it is not a substitute for an OSF registration when you need to preregister a full analysis pipeline. Preregistrations stay private by default, which some journals and reviewers now consider insufficient; make it public when you publish. Run from a single university group, with correspondingly modest infrastructure guarantees.

### [bioRxiv](https://www.biorxiv.org/)

`Free (registration), email` · beginner 4/5 · preprint server (life sciences)

Free preprint archive for the life sciences, founded by Cold Spring Harbor Laboratory in 2013 and now operated by the non-profit openRxiv. Preprints are not peer-reviewed, edited or typeset, but every submission is screened for offensive or non-scientific content, dual-use risk and plagiarism.

**Access.** Web submission at biorxiv.org/submit-a-manuscript; most major journals accept direct transfer from bioRxiv. Free metadata API documented at api.biorxiv.org: curl 'https://api.biorxiv.org/details/biorxiv/2026-08-01/2026-08-02/0'. That API returned HTTP 500 on every documented endpoint when checked on 2026-08-28, so for a working feed in the meantime use the RSS at https://connect.biorxiv.org/biorxiv_xml.php?subject=all or query bioRxiv DOIs (prefix 10.1101) through the Crossref API.

**Caveats.** No endorsement system, but screening can reject work judged non-scientific, and there is no formal appeal path. Posting a preprint is compatible with almost all life-science journals, but check the target journal first — a small number still treat it as prior publication. Once posted, a preprint cannot be deleted, only withdrawn with a public notice.

### [ChemRxiv](https://chemrxiv.org/)

`Free (registration), email` · beginner 4/5 · preprint server (chemistry)

Free preprint server for chemistry and related sciences, operated by the American Chemical Society with partner chemistry societies. Submissions receive a DOI and are moderated for scope and basic scientific content rather than peer-reviewed.

**Access.** Web submission at chemrxiv.org/engage/chemrxiv/public-dashboard (create an account, then 'Submit'). Metadata is exposed through the Cambridge Open Engage API used by the platform, and preprints are indexed in Crossref, so a Crossref query on the DOI prefix also works.

**Caveats.** The site sits behind bot protection, so scripted access is unreliable; use the browser. Posting is free and open to anyone, but moderation turnaround varies and off-scope submissions are declined. Verify the current partner list on the site rather than relying on secondhand descriptions — governance of chemistry preprint servers has changed more than once.

*Also listed under: chemistry.*

### [ClinicalTrials.gov](https://clinicaltrials.gov/)

`Free, application` · beginner 3/5 · clinical trial registry

The US NLM trial registry, holding 600,762 registered studies as reported by its own API on 2026-08-28. ICMJE member journals require prospective registration in a WHO-recognised registry such as this one before the first participant is enrolled, and US-regulated trials must also post summary results here.

**Access.** Search free at clinicaltrials.gov; REST API v2, no key: curl 'https://clinicaltrials.gov/api/v2/studies?query.cond=asthma&pageSize=1' and 'https://clinicaltrials.gov/api/v2/stats/size' for corpus statistics. Registering a study requires a PRS (Protocol Registration and Results System) account, applied for through the PRS site; individual investigator accounts exist for those without a sponsoring organisation.

**Caveats.** Reading and the API need nothing; registering does — PRS accounts are normally issued to organisations and an individual account has to be applied for and approved, which takes days, so start before you enrol anyone. Registration must be prospective: registering after enrolment begins will not satisfy ICMJE and many journals will refuse the paper outright. Results-reporting duties under FDAAA carry legal penalties for covered US trials. Researchers elsewhere can use their national WHO primary registry instead — several (for example ANZCTR, CTRI) charge nothing, while ISRCTN charges a fee.

*Also listed under: medicine.*

### [cOAlition S Journal Checker Tool and Rights Retention Strategy](https://journalcheckertool.org/)

`Free` · beginner 3/5 · OA compliance and author rights

Free tool that tells you, for a given journal + funder + institution combination, which routes give Plan S-compliant open access. The associated Rights Retention Strategy is a standard licence statement you put in the manuscript to retain the right to make the accepted version openly available immediately.

**Access.** Web interface at journalcheckertool.org: enter journal, funder and institution to get the compliant routes. The Rights Retention wording and guidance are at coalition-s.org/rights-retention-strategy/ — add the prescribed CC BY statement to your submitted manuscript and funding acknowledgement before you submit, not after.

**Caveats.** Built around cOAlition S funders, so it is far less useful if your funder is not in the coalition, and it assumes you have a funder at all. Rights retention is legally contested by some publishers; a few respond by desk-rejecting manuscripts carrying the statement. It is a legitimate route, but know that it can cost you a venue.

### [COPE (Committee on Publication Ethics)](https://publicationethics.org/)

`Free` · beginner 4/5 · publication ethics guidance, flowcharts and cases

Publisher-neutral guidance on publication ethics. The guidance search listed 37 flowcharts (paper mills, authorship disputes, plagiarism, concerns raised on social media, data concerns), 835 anonymised member cases with discussion and outcomes, 36 COPE positions and 16 guidelines on 2026-08-31.

**Access.** Web interface at publicationethics.org/guidance, no login: filter by type (Flowchart, Case, Guideline, COPE position, Endorsed guidance) and by topic (authorship, peer review, data, conflicts of interest); flowcharts download as PDFs.

**Caveats.** Written for editors, which is exactly why it is useful to an author: the flowcharts show what a journal is supposed to do when you report a co-authorship problem, request a correction or raise a concern about a published paper. Membership is a paid subscription for journals, publishers, institutions and individuals, and the guidance carries no enforcement — 'follows COPE guidelines' on a journal's website is a claim, not a certification, so check the member directory. The case database is anonymised, so it shows precedent rather than named outcomes.

### [Creative Commons licence chooser](https://creativecommons.org/chooser/)

`Free` · beginner 5/5 · licensing

Step-by-step tool that walks you to the right Creative Commons licence and emits ready-to-paste attribution HTML and plain text. For scholarly work the defaults worth knowing are CC BY 4.0 for papers and text, and CC0 for datasets, where attribution stacking otherwise becomes unworkable.

**Access.** Web interface at chooser-beta.creativecommons.org; answer the questions and copy the generated licence notice into your paper, repository README or dataset metadata. Full legal texts at creativecommons.org/licenses/.

**Caveats.** A licence chooser cannot tell you whether you hold the rights to license — if you signed copyright over to a publisher, or your funder/employer claims ownership, decide that first. NC and ND variants are not considered open access under most funder policies and block reuse in many contexts; think hard before picking them. For software, use choosealicense.com instead, since CC licences are not designed for code.

### [CRediT (Contributor Roles Taxonomy)](https://credit.niso.org/)

`Free` · beginner 5/5 · contributor role taxonomy

Community-owned taxonomy of 14 contributor roles — Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing – original draft, Writing – review & editing — approved in 2022 as an ANSI/NISO standard and licensed CC-BY 4.0. Translations into several languages are published on the site.

**Access.** Read the role definitions and the summary table of roles with examples at credit.niso.org, then write the contributions statement with them. Many submission systems now collect CRediT roles per author at submission, and publishers record them in article XML so they travel with the metadata.

**Caveats.** A vocabulary, not a settlement mechanism: it says nothing about author order, corresponding authorship or who qualifies as an author, so it complements ICMJE-style authorship criteria rather than replacing them. Its value is procedural — agreeing roles in writing at the start of a project is what prevents the dispute. If your target journal does not collect CRediT, put the same statement in the manuscript's contributions section; the CC-BY licence permits it.

### [DMPTool](https://dmptool.org/)

`Free (registration), email` · beginner 4/5 · data management plans

Free, community-supported service for writing machine-actionable data management and sharing plans against specific funder templates, with published example plans you can read and adapt.

**Access.** Web interface at dmptool.org: sign up, choose your funder's template, and answer the guided questions with the built-in prompts and sample text; export to PDF/DOCX for grant submission. Browse the 'Public Plans' library for real funded examples. European equivalents: DMPonline (dmponline.dcc.ac.uk) and Argos (argos.openaire.eu).

**Caveats.** You can sign up without an institutional login, though institutional accounts unlock member-specific templates and internal review workflows. Template coverage is best for US federal funders; check DMPonline or Argos for UK and EU funders. It structures the plan for you but does not know your data — the substance is still yours to write.

### [DOAJ (Directory of Open Access Journals)](https://doaj.org/)

`Free` · beginner 5/5 · vetted OA journal directory with no-APC filter

Community-curated whitelist of vetted open access journals: 23,372 indexed on 2026-08-28, of which 14,658 charge no article processing charge and 8,714 do. Being in DOAJ is the single best quick signal that a journal is legitimate rather than predatory.

**Access.** Web interface: search at doaj.org/search/journals and narrow with the sidebar filters (subject, licence, and the article-processing-charge facet) to isolate no-fee titles. Verified API route, no key: curl 'https://doaj.org/api/search/journals/bibjson.apc.has_apc:false?pageSize=100' — combine with a subject term, e.g. .../bibjson.apc.has_apc:false%20AND%20bibjson.subject.term:Medicine

**Caveats.** API is rate-limited to two requests per second. 'No APC' does not always mean no cost — check the separate other_charges field, which flags submission or page charges some journals levy instead. DOAJ indexes journals, not articles' quality, and inclusion is not an endorsement of any individual paper. Journals can be and are removed.

### [EarthArXiv](https://eartharxiv.org/)

`Free (registration), email` · beginner 4/5 · preprint server (Earth and planetary science)

Community-run, free preprint server for the Earth, planetary and environmental sciences, now hosted by the California Digital Library on the open-source Janeway platform after moving off OSF. Preprints get DOIs and are moderated against a published moderation policy.

**Access.** Web submission at eartharxiv.org — register, then 'Start New Submission'. Preprints and postprints (where the publisher permits) are both accepted; RSS feed and Crossref-indexed DOIs for downstream discovery.

**Caveats.** Volunteer-moderated, so posting is not instant. Because it accepts accepted-manuscript versions too, check publisher self-archiving terms with Open policy finder before depositing a postprint.

*Also listed under: earth.*

### [Engineering Archive (engrXiv)](https://engrxiv.org/)

`Free (registration), email` · beginner 4/5 · preprint server (engineering)

Free engineering preprint server launched in 2016 and operated by Open Engineering Inc., a 501(c)(3) non-profit. It accepts both preprints submitted in parallel with journal submission and previously published articles the author is entitled to make open access.

**Access.** Web submission at engrxiv.org (register, then 'Submit'). Runs on PKP preprint-server software; all submissions go through a basic moderation check against the posted guidelines.

**Caveats.** Migrated off OSF, so older engrXiv records may need a legacy-account claim to manage. Small volunteer operation: moderation is not fast. For the second use case (posting an already-published article) confirm your rights first — the server points authors at self-archiving policy lookups for this reason.

### [Episciences](https://www.episciences.org/)

`Free, email` · beginner 3/5 · overlay journal platform (diamond OA)

Diamond open access publishing platform hosting 46 overlay journals across all disciplines, with close to 8,000 published articles. An overlay journal organises peer review on top of preprints already deposited in arXiv, HAL or Zenodo, so it carries no production or hosting cost and charges authors nothing.

**Access.** Submit by giving a journal the identifier of a preprint you have already deposited (arXiv ID, HAL ID or Zenodo DOI) at episciences.org; the journal handles review and, on acceptance, publishes the overlay record with its own DOI. Institutions and communities can also apply to launch a new journal on the platform.

**Caveats.** Funded through French national infrastructure and OpenAIRE Nexus; no author charges anywhere. You must deposit the preprint first — the platform does not host manuscript files itself. Journal coverage is uneven: mathematics and computer science are well served, some fields have no relevant title. Discrete Analysis (discreteanalysisjournal.com) is the best-known independent example of the same overlay model.

*Also listed under: mathematics.*

### [Free Journal Network](https://freejournals.org/)

`Free` · beginner 4/5 · directory of scholar-controlled, fee-free journals

Non-profit association of journals that meet Fair Open Access criteria: scholar-controlled editorial boards, free to read, and no author-facing charges. It is a curated shortlist of venues you can submit to with no money involved at all.

**Access.** Browse the member journal list at freejournals.org/journals to find a fee-free venue in your field, then submit through that journal's own site. Editors of qualifying journals can apply for membership and for FJN funding.

**Caveats.** A directory, not a publisher — it does not host anything. Membership is concentrated in mathematics, linguistics and parts of physics and psychology; many fields have thin or no coverage. Use it alongside the DOAJ no-APC filter rather than instead of it, since DOAJ is far larger.

### [HAL](https://hal.science/)

`Free (registration), email` · beginner 3/5 · national open archive (multidisciplinary)

France's national open archive, run by CCSD/CNRS: the API reported 4,644,665 records on 2026-08-28, of which 1,787,362 carry a deposited full text. It accepts preprints, accepted manuscripts, theses, conference papers, software and datasets, and is the deposit layer that Episciences overlay journals publish on top of.

**Access.** Web deposit at hal.science after creating an account; SWORD and API deposit are supported for bulk work. Free search API, no key: curl 'https://api.archives-ouvertes.fr/search/?q=title_t:reproducibility&rows=5&wt=json'. Every deposit gets a HAL identifier with version history, and can be pushed to arXiv or given a DOI on request.

**Caveats.** The documentation frames HAL as being for researchers affiliated with an academic institution, French or foreign — there is no automated affiliation check, but an unaffiliated depositor is outside the stated audience. Every deposit is moderated before going live, so posting is not instant, and a deposited file cannot be withdrawn on a whim. The web interface is French-first and sits behind an Anubis proof-of-work challenge that blocks plain HTTP clients; the search API is unaffected.

*Also listed under: mathematics, literature-access.*

### [JMLR and TMLR](https://jmlr.org/)

`Free, email` · beginner 3/5 · diamond OA machine-learning journals

The Journal of Machine Learning Research has published free-to-read, free-to-publish machine-learning papers since 2000. Its companion Transactions on Machine Learning Research runs rolling submissions with double-blind review on OpenReview and judges technical correctness rather than perceived significance.

**Access.** JMLR: submit LaTeX via the JMLR submission system at jmlr.org/author-info.html. TMLR: submit through OpenReview at openreview.net/group?id=TMLR — no deadlines, decisions target a short fixed review window. Both publish PDFs openly with no paywall and no fee.

**Caveats.** No charges to authors or readers in either venue. TMLR rejects any submission with overlap to previously published work, including your own conference papers. Neither venue offers copy-editing or typesetting, so camera-ready quality is entirely on you. Acceptance rates are not generous.

*Also listed under: cs-ml.*

### [Journal of Open Source Software (JOSS)](https://joss.theoj.org/)

`Free` · beginner 4/5 · software paper journal (diamond OA)

Diamond open access journal (ISSN 2475-9066) that publishes short papers about research software, with the actual peer review conducted on the software itself in public GitHub issues. Free to publish, free to read, and widely accepted as a citable credit for research code.

**Access.** Write a ~250–1000 word paper.md plus paper.bib in your repository, then submit the repository URL at joss.theoj.org/papers/new. Review happens in an open GitHub issue against a public checklist; on acceptance the paper gets a Crossref DOI and the software is archived (usually via Zenodo).

**Caveats.** Requires an OSI-approved licence, a feature-complete package with meaningful research impact, and at least six months of public development history — thin wrappers and single-function utilities are rejected at pre-review. Authors must disclose generative-AI use. Everything, including rejection, is public, which some authors dislike. A GitHub account is effectively required.

*Also listed under: physics, astronomy, chemistry, earth, cs-ml, neuro-psych, workflow-tools.*

### [Keepers Registry](https://keepers.issn.org/)

`Free` · beginner 3/5 · digital preservation status of journals

Run by the ISSN International Centre, it reports which archiving agencies hold a preserved copy of a serial with a given ISSN. The agency tables behind the site (updated 2026-08-28/29) cover 20 Keepers — CLOCKSS, LOCKSS, Portico, PKP PLN, Internet Archive, HathiTrust, Library of Congress, Gallica, the National Digital Preservation Program of China, several national libraries and subject archives — and list 119,977 ISSNs archived by at least one agency, of which 21,113 are held by three or more.

**Access.** Web interface, no login: search by ISSN or title at keepers.issn.org to see which Keepers hold which years and volumes, or browse by agency. The homepage counters are computed from agency tables the site publishes as TSV/CSV under /sites/default/files/keepers/.

**Caveats.** Scope is continuing resources with an ISSN — no books, datasets or preprint servers. Absence is not proof of neglect: an agency has to report its holdings for them to appear. And being 'kept' by a dark archive such as CLOCKSS or Portico means the content is released only if the publisher fails, not that you can read it there today. The practical use is a pre-submission check on a small or new journal: if nobody is preserving it, your article disappears with the website.

### [Language Science Press](https://langsci-press.org/)

`Free` · beginner 2/5 · diamond OA scholarly book publisher (linguistics)

Community-supported open access book publisher in linguistics with 35 series and over 500 editorial board members from more than 55 countries. Books are peer-reviewed, published under CC BY with authors retaining copyright, and free to download; there are no book processing charges.

**Access.** Submit a proposal to the relevant series at langsci-press.org/about/submissions. Authors work in a LaTeX/XML pipeline (templates provided) and community proofreading is part of the process; printed copies are sold at cost through print-on-demand.

**Caveats.** Funded by a library consortium, so nothing is charged to authors — genuinely unusual for monographs. Authors are expected to do more typesetting work than with a commercial press, and the production pipeline assumes some LaTeX comfort. Scope is strictly linguistics.

*Also listed under: humanities.*

### [medRxiv](https://www.medrxiv.org/)

`Free (registration), email` · beginner 4/5 · preprint server (clinical and health sciences)

Free preprint server for medical, clinical and health-sciences research, run by openRxiv alongside bioRxiv. It applies stricter screening than bioRxiv because of the risk of clinical harm from unreviewed findings.

**Access.** Web submission at medrxiv.org/submit-a-manuscript. Same metadata API family as bioRxiv (curl 'https://api.biorxiv.org/details/medrxiv/2026-08-01/2026-08-02/0'), but that API returned HTTP 500 on all endpoints on 2026-08-28 — fall back to the medRxiv RSS feeds at connect.medrxiv.org or to Crossref queries on the 10.1101 DOI prefix.

**Caveats.** Submissions must carry ethics-approval and trial-registration statements where applicable, and some categories (for example single case reports and work implying immediate clinical action) are restricted or refused. Screening is slower than bioRxiv and rejection is more common; budget days, not hours.

### [MPRA (Munich Personal RePEc Archive)](https://mpra.ub.uni-muenchen.de/)

`Free (registration), email` · beginner 4/5 · working-paper repository (economics)

Repository run by the University Library of LMU Munich holding 61,601 records on 2026-08-28, created specifically for economists who want their work in the RePEc network but are not affiliated with an institution that runs a working-paper series. Deposits propagate into RePEc, so they surface in IDEAS and EconPapers, where economists actually search and where NEP subject mailings are generated.

**Access.** Web deposit at mpra.ub.uni-muenchen.de after free registration (EPrints software); papers appear in RePEc within about a day and get a RePEc handle. OAI-PMH endpoint available for harvesting; browse and download need no account.

**Caveats.** The single most useful venue in economics for an unaffiliated author — it exists for exactly that case. Screening is light but submissions must be scholarly economics, and papers already published elsewhere can be removed on a publisher's request. Papers are identified by RePEc handles, not DOIs, so deposit a copy in Zenodo as well if you need a DOI. Deposits are versioned and superseded versions stay visible.

*Also listed under: econ-finance.*

### [Open Library of Humanities](https://www.openlibhums.org/)

`Free, email` · beginner 3/5 · diamond OA humanities journal platform

Library-consortium-funded publisher of humanities and social science journals with no author-facing article processing charges; its titles, including the linguistics journal Glossa, are recorded in DOAJ as having no APC. Costs are covered by supporting libraries rather than authors.

**Access.** Pick a journal from the OLH portfolio at openlibhums.org/journals and submit through its own editorial system (most run on Janeway). Everything is CC-licensed and free to read.

**Caveats.** The main site sits behind a JavaScript proof-of-work challenge, so scripted access fails; use a browser. DOAJ flags 'other charges' for some OLH-published titles, so read the individual journal's author page before assuming zero cost in every case. Editorial standards and turnaround vary by journal, as with any multi-title platform.

*Also listed under: humanities.*

### [Open policy finder (formerly Sherpa Romeo)](https://openpolicyfinder.jisc.ac.uk/)

`Free` · beginner 4/5 · publisher self-archiving policy lookup

Jisc-run database of publisher and journal open access policies: which version (submitted, accepted, published) you may deposit where, under what licence, and after what embargo. The essential check before putting a manuscript in a repository.

**Access.** Web interface at openpolicyfinder.jisc.ac.uk — search by journal title or ISSN and read the per-version deposit conditions. A free API is available for programmatic lookups after requesting a key.

**Caveats.** Rebranded from Sherpa Romeo; old sherpa.ac.uk/romeo links and any guide that still calls it Sherpa Romeo point at the same service. The API is being migrated to a new platform — the site's own updates (07/05/2026) record the migration window being extended to July 2026 — so an old Sherpa API key or integration may need moving; request a new key from the site. It records what the publisher states, which is not always what an individual contract says: the signed publishing agreement wins in a dispute. Coverage of small and non-English publishers is patchy.

*Also listed under: literature-access.*

### [Open Research Europe](https://open-research-europe.ec.europa.eu/)

`Free tier, email` · beginner 3/5 · funder-run open publishing platform

European Commission publishing platform using the post-publication open peer review model: manuscripts appear within days with a DOI, then named referee reports are published against them and the article is indexed once it passes. Publishing costs are met by the Commission rather than the author.

**Access.** Web submission at open-research-europe.ec.europa.eu; all article versions, referee reports and referee names are public, and underlying data must be deposited openly.

**Caveats.** Eligibility is the whole story: the free route is for work acknowledging Horizon 2020 / Horizon Europe funding, and eligibility rules have been revised more than once — check the current criteria on the site before assuming you qualify. If you have no EU grant, this is not a route for you. The site is JavaScript-heavy and will not render in a plain HTTP client.

### [OpenReview](https://openreview.net/)

`Free (registration), email` · beginner 4/5 · open peer review platform

Free, open-source platform that hosts the peer review process for major machine-learning venues (ICLR, NeurIPS, TMLR and many workshops), publishing reviews, author rebuttals and decisions openly alongside submissions. It is also a public, queryable archive of what reviewers actually said.

**Access.** Web interface at openreview.net with a free account; submissions go through whichever venue's page is open. Programmatic reads now go through the Python client rather than plain curl: pip install openreview-py, then openreview.api.OpenReviewClient(baseurl='https://api2.openreview.net', username=..., password=...) and client.get_notes(content={'venue': 'ICLR 2025 poster'}). An unauthenticated curl to api2.openreview.net/notes returns HTTP 403 'Challenge verification required'.

**Caveats.** Whether reviews stay public and whether rejected submissions remain visible is set per venue, not by OpenReview. Signing up without an institutional address is possible but moderated: the documentation says personal-email profiles are all moderated, that 'Independent Researcher' must be entered as the current position (which locks the institution domain), and that a profile whose Education and Career History lists only 'Independent Researcher' will be rejected until another institution record is added — so expect delay and have a past affiliation ready.

### [ORCID](https://orcid.org/)

`Free (registration), email` · beginner 5/5 · persistent researcher identifier

Free persistent identifier for researchers, used by most publishers and funders to disambiguate authors; the public registry search returned 29,337,299 records on 2026-08-28. An iD is issued to anyone who registers, with no institutional affiliation required.

**Access.** Web interface: register at orcid.org/register (email + password), then add works manually, from a DOI/PubMed search, or by authorising Crossref and DataCite auto-update so new publications land on your record automatically. Public API needs no key: curl -H 'Accept: application/json' 'https://pub.orcid.org/v3.0/0000-0002-1825-0097/record'

**Caveats.** Registration is free and open to unaffiliated people; only organisations pay (ORCID membership). Fields you mark private are invisible to the public API, so set employment/works to 'everyone' if you want them to show on your public page. Auto-update only fires when a publisher passes your iD through to Crossref/DataCite, so older and smaller-press works still need manual entry.

### [OSF (Open Science Framework)](https://osf.io/)

`Free (registration), email` · beginner 4/5 · project repository, preregistration and DOI

Free project workspace from the Center for Open Science combining file storage, version history, wikis, preprints, preregistration and DOI minting. OSF Storage caps are 5 GB per private project or component and 50 GB per public one, with individual files limited to 5 GB.

**Access.** Web interface at osf.io; sign up with any email or ORCID. Components let you split a project so each gets its own quota. REST API with no key for reads: curl 'https://api.osf.io/v2/nodes/?filter[title]=...'; write access uses a personal access token. Add-ons connect Google Drive, Dropbox, GitHub and S3 for storage OSF does not host itself.

**Caveats.** The caps are per project/component, not per user, so large projects get split across components — awkward but workable. Files stored via third-party add-ons live with that provider and are not preserved by OSF. Making a project public is irreversible in practice; DOIs are only minted for public projects and registrations.

### [OSF Preprints](https://osf.io/preprints/)

`Free (registration), email` · beginner 5/5 · preprint server network (social sciences, humanities and more)

Free preprint hosting for 32 community-branded servers as of 2026-08-28, including PsyArXiv (psychology), SocArXiv (sociology), EdArXiv (education), MetaArXiv (metascience), EcoEvoRxiv, AfricArXiv, Law Archive, SportRxiv and Thesis Commons. Each preprint gets a DOI and is indexed in Crossref, Google Scholar and OpenAlex.

**Access.** Web submission: pick a server (e.g. osf.io/preprints/psyarxiv) and choose 'Add a preprint'; an OSF account covers all of them. Enumerate providers via the free API: curl 'https://api.osf.io/v2/providers/preprints/?page[size]=100' (32 providers on 2026-08-28). The older /v2/preprint_providers/ route still answers but returns a deprecation warning: 'This route is deprecated and will be unavailable after version 2.7'.

**Caveats.** The provider list includes legacy servers that have gone quiet or migrated elsewhere — EarthArXiv and engrXiv, for instance, still appear in the API but now run on their own platforms. Check that a server has recent postings before choosing it. Moderation is per-server: some pre-moderate, some post-moderate, and a few accept almost anything in scope.

*Also listed under: literature-access.*

### [OSF Registries](https://osf.io/registries)

`Free (registration), email` · beginner 4/5 · preregistration and Registered Reports

Free preregistration service: you complete a template (including Registered Report, clinical-trial-style and open-ended templates), freeze it, and get a time-stamped, DOI-bearing, read-only registration that cannot be edited afterwards.

**Access.** Web interface: from an OSF project choose 'Registrations' > 'New registration', pick a template, then submit. Embargo up to four years is available if you need the content hidden while the study runs — the existence and date of the registration stay public.

**Caveats.** A registration is permanent; withdrawal leaves a public tombstone with the justification, by design. Reviewers only check administrative completeness, not scientific quality. For clinical trials in humans this does not replace a WHO-recognised trial registry such as ClinicalTrials.gov, which most medical journals require.

*Also listed under: social.*

### [Peer Community In (PCI) and Peer Community Journal](https://peercommunityin.org/)

`Free, email` · beginner 3/5 · free peer review and recommendation of preprints

Non-profit network of 21 thematic communities that organise free peer review of preprints and publish a public recommendation for those that pass. Recommended preprints can then be submitted to a PCI-friendly journal, or published as-is in Peer Community Journal, a diamond OA multidisciplinary journal with no author fees and CC BY licensing.

**Access.** Deposit your preprint on any server with a DOI (bioRxiv, arXiv, OSF, Zenodo), then submit its DOI to a thematic PCI at peercommunityin.org; at least two reviewers plus a recommender handle it. On recommendation you may accept publication in Peer Community Journal at no charge, or take the recommendation to a journal that recognises it.

**Caveats.** Free for authors, reviewers and readers, with reviews and editorial decisions published openly. The 21 communities are concentrated in ecology, evolution, genomics, archaeology, neuroscience and registered reports; many fields have no PCI. Review can be slow because recommenders are volunteers, and a fair number of submissions are rejected without a recommendation.

*Also listed under: biology.*

### [Preprints.org](https://www.preprints.org/)

`Free (registration), email` · beginner 4/5 · multidisciplinary preprint server

Free multidisciplinary preprint platform that assigns a DOI and a version history, useful for fields with no dedicated server of their own. Submissions are screened before posting and remain permanently available.

**Access.** Web submission at preprints.org (account required); choose a subject area, upload, and the preprint is posted after screening, typically within a few working days.

**Caveats.** Operated by MDPI, which some communities associate with aggressive solicitation and variable editorial standards in its journals — the preprint server itself is free and does not obligate you to submit to an MDPI journal, but expect marketing email. The site returns HTTP 403 to command-line clients (bot protection), so use a browser. It is genuinely active: DOI prefix 10.20944 holds 135,665 records with new ones registered the same day it was checked (2026-08-28). Prefer a field-specific server (arXiv, bioRxiv, an OSF server) when one exists; use this as the fallback.

### [PROSPERO](https://www.crd.york.ac.uk/prospero/)

`Free (registration), email` · beginner 3/5 · systematic review protocol registration

International register of systematic review protocols, run by the Centre for Reviews and Dissemination at the University of York. Registration is free and produces a public, date-stamped record with a CRD42-prefixed number that journals, PRISMA reporting and Cochrane-style methods sections expect to see cited.

**Access.** Web interface only: create an account at crd.york.ac.uk/prospero, complete the structured protocol form, and CRD staff check it before the record is published (usually days rather than hours). Records are publicly searchable and are updated as the review progresses, with an audit trail of changes.

**Caveats.** Scope is limited to reviews with a health-related outcome, and registration must be prospective — submissions from reviews that have already finished data extraction are refused, so register before you start screening. Reviews outside health belong in OSF Registries instead. The site is a JavaScript application with no usable public API, so records cannot be harvested from a plain HTTP client and the policy pages are not machine-readable; confirm current scope rules in the browser before relying on them.

*Also listed under: medicine.*

### [protocols.io](https://www.protocols.io/)

`Free tier, email` · beginner 5/5 · methods and protocol publishing

Platform for writing, versioning and publishing step-by-step research protocols. The 'Open Research' plan is $0 forever and allows unlimited public protocols with DOIs plus up to 2 private protocols, with long-term preservation via CLOCKSS and mirroring to the Internet Archive and GitHub.

**Access.** Web interface at protocols.io: create a protocol, then 'Publish' to mint a DOI and make it citable and forkable. REST API and mobile apps available; many journals accept a protocols.io DOI in place of a long methods section.

**Caveats.** The free tier is designed around publishing openly — private/unpublished work is capped at 2 protocols, and features aimed at labs and companies (unlimited private protocols, extra storage, SSO, compliance features) are paid. Publishing a protocol is permanent, like any DOI. The site is behind bot protection, so command-line fetching of pages fails.

### [Quantum](https://quantum-journal.org/)

`Freemium, email` · beginner 3/5 · community-run OA journal (quantum science)

Non-profit, CC BY open access journal for quantum science run by a researcher association, publishing on top of arXiv. From 1 January 2024 the standard publication fee is €600, with an explicit €100 discount option and a complete waiver available to any author who needs it, with no justification required.

**Access.** Post the paper to arXiv (quant-ph, or cross-listed there), then submit the arXiv identifier at quantum-journal.org — no fee at submission. On acceptance the final arXiv version becomes the published version and Quantum registers the DOI.

**Caveats.** Not diamond OA: there is a real fee, but the waiver policy is unconditional and self-declared, which makes it usable by unaffiliated and unfunded authors — be honest with yourself, and tell them, since they track waivers for accounting. Fees have been revised before, so check the payment page rather than this entry. arXiv deposit is mandatory, which means the arXiv endorsement problem applies here too.

*Also listed under: physics.*

### [ReScience C](https://rescience.github.io/)

`Free` · beginner 3/5 · replication journal for computational research

Platinum open access, GitHub-based journal that publishes explicit replications of already-published computational research using new, open-source implementations. Both successful and failed replications are publishable, which is unusual and useful.

**Access.** Fork the submission template, write the replication and its code, then open a public GitHub issue at github.com/ReScience/submissions to start review; reviewers run your code and the whole exchange is public. Accepted articles get a DOI and are archived on Zenodo.

**Caveats.** No fees for authors or readers. Volume is low and review depends on volunteers, so timelines are unpredictable. Scope is strictly replication of computational work — not new results — and you must produce a genuinely independent implementation, not rerun the original authors' code.

*Also listed under: cs-ml.*

### [Research Square](https://www.researchsquare.com/)

`Free (registration), email` · beginner 4/5 · multidisciplinary preprint platform

Free multidisciplinary preprint platform with DOIs and public commenting, plus an 'In Review' option that shows the peer-review status of a manuscript under consideration at participating journals.

**Access.** Web submission at researchsquare.com ('Submit a Preprint'); or opt into In Review when submitting to a participating journal, which posts the preprint automatically and exposes review milestones.

**Caveats.** Preprint posting is free; the co-located AJE editing, translation and figure-formatting services are paid and heavily advertised — you never have to buy them. In Review only works with participating publishers, mostly Springer Nature titles.

### [Review Commons](https://www.reviewcommons.org/)

`Free, email` · beginner 3/5 · journal-independent peer review

Free journal-independent refereeing platform launched by ASAPbio and EMBO with support from bioRxiv, medRxiv and HHMI: one submission produces a full set of referee reports, the reviews and your response are posted publicly with the preprint, and you may then take that package to any of roughly 25 affiliate journals (including eLife, EMBO Journal, PLOS Biology, PLOS Genetics, Genome Biology and Genes & Development) instead of starting review from scratch.

**Access.** Submit the manuscript through the platform linked from reviewcommons.org (reviewcommons.msubmit.net); review is organised by Review Commons editors, then reports and author replies are posted alongside the bioRxiv/medRxiv preprint. Transferring to an affiliate journal afterwards is optional and done from the platform.

**Caveats.** No charge to authors at any stage, but scope is the life sciences and not every submission is sent out for review. Reviews transfer, decisions do not — each affiliate journal still makes its own call and may ask for more. It saves a duplicated review round rather than time on the first one, so budget a normal review cycle before you can submit anywhere.

*Also listed under: biology.*

### [Rogue Scholar](https://rogue-scholar.org/)

`Free (registration), email` · beginner 4/5 · DOIs and archiving for scholarly blogs

Archive that gives science blogs DOIs (prefix 10.59350), full-text search, long-term archiving and metadata deposit, turning blog posts into citable, preserved scholarly records. Useful for methods notes, negative results and commentary that no journal will take.

**Access.** Register your blog's RSS/Atom feed at rogue-scholar.org; posts are then imported, assigned DOIs and archived automatically. Free API, no key: curl 'https://api.rogue-scholar.org/blogs' and /posts for the full corpus.

**Caveats.** Your blog needs a working full-text feed and a licence statement; the service is run by a small non-profit operation, so treat it as promising infrastructure rather than something with institutional guarantees. A blog-post DOI carries no peer review and will not count as a publication in most formal evaluations.

### [SciELO](https://www.scielo.org/)

`Free, email` · beginner 4/5 · Latin American / Iberian OA journal network

Regional open access publishing network with national collections for Argentina, Bolivia, Brazil, Chile, Colombia, Costa Rica, Cuba, Ecuador, Mexico, Paraguay, Peru, Portugal, South Africa, Spain and Uruguay, plus SciELO Preprints, SciELO Data and SciELO Books. Most member journals are publicly funded and charge authors nothing.

**Access.** Search across collections at scielo.org; submit to an individual member journal through its own site. SciELO Preprints (preprints.scielo.org) accepts free multilingual preprint deposits with DOIs; SciELO Data hosts research datasets.

**Caveats.** Fee policies are set per journal, not centrally — the great majority levy nothing, but confirm on the journal's page. Much of the content is in Portuguese and Spanish, and multilingual publishing is encouraged. Indexing in Scopus/WoS varies by title, which matters if you are assessed on those databases.

### [SciPost](https://scipost.org/)

`Free, email` · beginner 3/5 · diamond OA journals with open refereeing (physics and beyond)

Scientist-run publishing house with genuinely no author charges — DOAJ records all six SciPost journals (SciPost Physics, SciPost Physics Core, SciPost Physics Lecture Notes, SciPost Physics Codebases, SciPost Physics Proceedings and SciPost Physics Community Reports) as having no APC and no other charges. Referee reports and author replies are published alongside accepted papers.

**Access.** Web submission at scipost.org: deposit the manuscript on arXiv first, then submit the arXiv identifier to the chosen SciPost journal. Refereeing is open — invited reports and contributed comments appear publicly on the submission page during review.

**Caveats.** Costs are covered by sponsoring institutions and consortia, not authors, so nothing is billed to you at any stage. Coverage is strongest in physics; the chemistry, astronomy, biology and mathematics titles are much smaller. The site is behind a JavaScript proof-of-work challenge, so command-line fetching fails — use a browser. Acceptance standards in SciPost Physics are high; SciPost Physics Core is the lower-threshold sibling.

*Also listed under: physics.*

### [Software Heritage](https://www.softwareheritage.org/)

`Free` · beginner 3/5 · source code archive and identifiers

Universal archive that harvests and preserves publicly available source code with full development history, and issues SWHIDs — intrinsic, cryptographically computed identifiers that pin an exact file, directory, commit or snapshot without depending on any hosting service staying alive.

**Access.** Use 'Save Code Now' at archive.softwareheritage.org/save/ to trigger immediate archiving of a public Git/Mercurial/SVN repository URL, then copy the SWHID (e.g. swh:1:rev:...) from the archived object and cite it in your paper. REST API documented under archive.softwareheritage.org/api/.

**Caveats.** Archives only publicly accessible repositories; nothing private, and no way to remove code once archived except through a documented takedown process. The REST API does answer plain HTTP clients — https://archive.softwareheritage.org/api/1/origin/search/numpy/?limit=1 returned HTTP 200 on 2026-08-28 — but the browsable web pages and Save Code Now sit behind a JavaScript challenge, so drive those from a browser. SWHIDs identify code, not a publication — pair them with a Zenodo DOI when you need a citable, described release.

*Also listed under: cs-ml, compute, workflow-tools.*

### [SSRN](https://www.ssrn.com/)

`Free (registration), email` · beginner 4/5 · preprint/working-paper repository (social sciences, law, economics)

Large working-paper repository, strongest in law, economics, finance, management and political science, where the SSRN version is often the de facto circulating draft. Posting and reading are free; submissions are moderated for scope and basic scholarly form.

**Access.** Web submission via an SSRN author account at ssrn.com; papers are organised into subject-matter eJournals that email new abstracts to subscribers, which is the main discovery mechanism.

**Caveats.** Owned by Elsevier, which makes some researchers prefer a scholar-run alternative; it is genuinely free to post and read, but it is not an open-infrastructure project and its metadata is not as openly reusable as arXiv's or OSF's. Not all papers receive DOIs. Bot protection blocks scripted access.

### [TechRxiv](https://www.techrxiv.org/)

`Free (registration), email` · beginner 4/5 · preprint server (electrical engineering and computer science)

IEEE-operated preprint server for electrical engineering, computer science and related technology fields. Posting is free and produces a citable DOI; content is screened rather than peer-reviewed.

**Access.** Web submission at techrxiv.org — create an account and upload; IEEE membership is not required to post. DOIs are registered with Crossref, so metadata is retrievable through the Crossref API.

**Caveats.** The site is behind Cloudflare and does not render without JavaScript, so scripted or command-line access fails — use a browser. Check that it is still posting before you choose it: TechRxiv's Crossref DOI prefix 10.36227 registered 1,534 records in the first quarter of 2026 and zero since 2026-03-31 (Crossref API, checked 2026-08-28), and none of its content appears in DataCite, so new postings may have paused. Confirm current submission terms on the site itself; IEEE has changed platform and policy more than once since launch.

### [Wayback Machine Save Page Now](https://web.archive.org/save)

`Free` · beginner 5/5 · web citation preservation

Internet Archive service that captures a live URL on demand and returns a permanent dated snapshot (web.archive.org/web/<timestamp>/<url>), which is how you make a cited web page, dataset landing page or policy document citable after it changes or disappears. A free availability API reports whether a URL is already archived and when.

**Access.** Paste the URL into the form at web.archive.org/save. Check existing captures with no key: curl 'https://archive.org/wayback/available?url=example.com'. A free archive.org account unlocks outlink capture, screenshots, emailed results and the SPN2 API (S3-style keys from archive.org/account/s3.php).

**Caveats.** Anonymous saves are rate-limited — a plain command-line request to /save returned HTTP 429 on 2026-08-28, so use the web form or sign in for scripted work. Pages behind logins, paywalls or crawler blocks cannot be captured, and site owners can have captures excluded later, so a snapshot is durable but not legally guaranteed. Cite the snapshot URL together with the access date.

## Funding

### [NeurIPS financial assistance](https://neurips.cc/Conferences/2026/FinancialAssistance)

`Free tier, application` · beginner 2/5 · conference registration and travel support

Application-based programme covering registration and, in some cases, travel and accommodation for attendees who could not otherwise afford to come to NeurIPS. It is the model example of a mechanism most large CS and ML conferences now run under some name.

**Access.** Web application on the conference site, opening on a published deadline each cycle (typically shortly after paper decisions); a separate volunteer programme also exchanges on-site work for a waived registration fee.

**Caveats.** Competitive, deadline-bound and re-decided every year, so treat the exact terms on this page as authoritative rather than anything written elsewhere. Assistance does not remove the visa problem, which is the harder barrier for many unaffiliated and Global South researchers. Check the equivalent pages for ICML, ACL, ICLR, CVPR and your own field's flagship conference — most have one, often under 'Diversity and Inclusion' or 'Registration'.

### [PLOS Publication Fee Assistance and Research4Life waivers](https://plos.org/publish/fees/)

`Free tier, application` · beginner 3/5 · APC waivers

PLOS publishes standard fees (PLOS ONE research articles $1,852–$2,477 depending on article type; most other titles $2,596–$3,165, listed 2026-08-28) alongside two relief routes: authors based at institutions in Research4Life Group A countries publish free in any PLOS journal and Group B authors publish free in PLOS Biology, PLOS Medicine and PLOS Sustainability and Transformation and pay a reduced $940 elsewhere — in both cases only where the research had no external funding; and the Publication Fee Assistance programme covers all or part of the fee for authors who demonstrate financial need.

**Access.** Apply at the point of manuscript submission — tick the Research4Life box, or complete the PFA application form; PFA decisions usually arrive within 10 business days and are kept away from editors and reviewers so they cannot affect the editorial decision.

**Caveats.** The honest catch for this catalogue's audience: Research4Life eligibility is defined by the institution you are based at, so a genuinely unaffiliated researcher in an eligible country cannot use it and must go through PFA instead. PFA requires demonstrating that you exhausted institutional, library and grant funding first, and is decided case by case — it is not guaranteed. Fees change; read the live page.

*Also listed under: biology, literature-access.*

### [Research4Life](https://www.research4life.org/)

`Free tier, application` · beginner 2/5 · content access and fee relief for lower-income countries

Public-private partnership giving institutions in eligible low- and middle-income countries free or very low-cost access to paywalled journals, books and databases through five programmes (Hinari, AGORA, OARE, ARDI, GOALI). Its country groupings are also the basis for APC waivers at many publishers, including PLOS.

**Access.** Institutional registration: a library, university, hospital, research institute, government office or qualifying NGO applies through research4life.org; individuals log in with their registered institution's credentials. Check country eligibility with the tool on the site before applying.

**Caveats.** Institution-gated by design — there is no route for an unaffiliated individual, which is the single most important caveat here. Group A countries get free access; Group B pay a low annual fee. Publisher participation varies by programme and country, and some large publishers withhold specific titles. Where it applies, though, it is by far the largest legal literature-access programme in existence.

## Learning

### [The Turing Way](https://book.the-turing-way.org/)

`Free` · beginner 5/5 · open handbook for reproducible research

Openly written, CC BY handbook covering reproducible research, project design, collaboration, communication and ethics — including practical chapters on licensing, version control, preregistration and open publishing. Written and reviewed by a large international volunteer community.

**Access.** Read online at the-turing-way.netlify.app; the whole book is on GitHub, so you can clone it, cite chapters, reuse figures under CC BY, or open a pull request to fix something.

**Caveats.** Broad rather than deep — it orients you and points onward rather than replacing a specialist text. Chapters vary in maturity because they are community-written, and some carry visible 'work in progress' notices. Its examples lean UK/EU and computational.

*Also listed under: social, literature-access, learning, workflow-tools.*

### [Think. Check. Submit.](https://thinkchecksubmit.org/)

`Free` · beginner 5/5 · predatory publisher avoidance

Cross-sector checklist for deciding whether a journal, book publisher or conference is trustworthy before you submit, maintained by a coalition of publishing and library organisations. Separate checklists exist for journals and for books/chapters, in many languages.

**Access.** Web interface: work through the checklist at thinkchecksubmit.org/journals-check/ or /books-and-chapters/. Pair it with two hard checks — is the journal in DOAJ, and does the publisher appear in Crossref with real deposited metadata.

**Caveats.** A checklist, not a blocklist: it will not name specific bad actors, so it takes a few minutes of judgement rather than one lookup. Predatory venues increasingly fake the surface signals it asks about (fabricated editorial boards, fake impact metrics, cloned journal sites), so verify at least one editor independently before trusting a title you have never heard of.

## Community

### [Academia Stack Exchange](https://academia.stackexchange.com/)

`Free (registration), email` · beginner 5/5 · Q&A on publishing, authorship and academic practice

Large moderated Q&A site where working academics answer practical questions about submission, authorship disputes, peer review, predatory venues, and — a recurring and well-answered topic — publishing without an institutional affiliation.

**Access.** Web interface at academia.stackexchange.com; reading needs no account, asking needs a free one. Search the 'independent-researcher' and 'affiliation' tags before posting; the common cases are already answered in depth.

**Caveats.** Answers reflect the norms of the answerer's field and country and are frequently contradictory across disciplines — read several and note the field. Questions seeking opinion, career prediction or venue recommendations are routinely closed as off-topic. It is not a substitute for your own field's mailing lists or a senior colleague.

### [Knowledge Commons (formerly Humanities Commons)](https://hcommons.org/)

`Free (registration), email` · beginner 4/5 · scholarly network and repository

Non-profit, open-source academic network offering free member profiles, discussion groups, hosted WordPress sites, and a deposit repository (KC Works) that mints DOIs for papers, syllabi, datasets and conference talks. Membership is open to anyone, not just people with a university post.

**Access.** Web interface at hcommons.org: register for a free account, join subject groups, and deposit work through the Works repository to get a DOI and a permanent record. Profiles are public and can serve as a lightweight academic homepage.

**Caveats.** Rebranded from Humanities Commons; older links and guides using that name refer to the same service. Strongest in the humanities, especially literature, history and digital humanities — activity in the sciences is thin. Deposits are not peer-reviewed. Funded by grants and member society support, so its long-run funding is less certain than a national infrastructure's.

*Also listed under: humanities.*

### [PKP Community Forum](https://forum.pkp.sfu.ca/)

`Free (registration), email` · beginner 3/5 · Q&A for people running journals

The support forum for Open Journal Systems, OPS and OMP, where journal managers, editors and developers answer concrete questions about running a small scholarly journal — plugin configuration, DOI deposit, upgrades, indexing applications.

**Access.** Web forum at forum.pkp.sfu.ca; free account to post, readable without one. Search first — most setup problems have been answered before. PKP staff and long-time community members answer regularly.

**Caveats.** Focused on the software and the operational side of publishing, not on editorial or scholarly questions. Responses come from volunteers and PKP staff, so response time varies; paid support contracts exist for organisations that need guarantees.

### [PREreview](https://prereview.org/)

`Free (registration), email` · beginner 5/5 · open preprint review community

Non-profit platform where anyone can write, request or collaboratively produce structured public reviews of preprints (and now datasets), explicitly aimed at researchers outside the usual invited-reviewer networks. Reviews are open, credited and citable.

**Access.** Web interface at prereview.org: log in with ORCID, find a preprint by DOI, and write a review with a guided template. Also offers PREreview Clubs (group review), Live Reviews (scheduled collaborative sessions), free peer-review training, and periodic review-a-thons.

**Caveats.** Login is via ORCID. A PREreview is not a journal decision and carries no formal weight in most hiring or tenure processes, though it is a legitimate, visible way to build a reviewing record when no editor has ever invited you. Coverage is heaviest in the life sciences.

### [PubPeer](https://pubpeer.com/)

`Free (registration), email` · beginner 4/5 · post-publication peer review

Free 'online journal club' operated by the non-profit PubPeer Foundation where any publication carrying a DOI, PubMed ID or arXiv ID can be discussed in public. It is the main venue where image duplication, statistical impossibilities and data-integrity problems surface, frequently ahead of a journal correction or retraction, and authors are alerted when their paper is commented on.

**Access.** Web interface at pubpeer.com — paste a DOI, PMID or arXiv ID to find or open a thread. Browser extensions for Firefox, Chrome and Safari flag commented papers inside PubMed results and on journal sites; a Zotero plugin highlights commented references in your own library. Commenting needs an account; if you have no indexed publication the FAQ says to email them and they will usually create one manually, and anonymous commenting via an access code is supported.

**Caveats.** There is no public API yet — the FAQ says one is coming and asks you to request a key. Comments are moderated and the site has been on the receiving end of legal action from commented-on authors, so keep claims factual and to publicly verifiable evidence; the FAQ recommends Tor for the strongest anonymity. A PubPeer thread carries no formal status: to get a paper corrected you still have to write to the journal.

*Also listed under: literature-access.*
