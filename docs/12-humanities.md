# Linguistics & humanities

Part of [research-vault](../README.md). 60 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (23) · [Software](#software) (15) · [Literature](#literature) (4) · [Publishing](#publishing) (6) · [Funding](#funding) (4) · [Learning](#learning) (5) · [Community](#community) (3)

## Data

### [Chronicling America (Library of Congress)](https://www.loc.gov/collections/chronicling-america/)

`Free` · beginner 4/5 · historic newspapers

Digitised American newspaper pages from nearly every US state and territory, published through 1963, produced by the National Digital Newspaper Program, with page images, OCR text and a directory of US newspapers. New pages are added regularly.

**Access.** Web search across full text; the loc.gov JSON API — append `?fo=json` to any collection or search URL — returns structured results with pagination. Bulk OCR and METS/ALTO datasets are published under the collection's Datasets tab.

**Caveats.** Important change: the legacy chroniclingamerica.loc.gov site and its separate API now redirect to the loc.gov collection, so older code and tutorials written against the old endpoint need rewriting for the loc.gov JSON API. OCR is uncorrected and noisy on nineteenth-century type. The loc.gov site is behind Cloudflare and rate-limits aggressive scripts — use the published datasets for bulk work rather than hammering the API.

### [CLARIN](https://www.clarin.eu/)

`Free` · beginner 3/5 · European language-resource infrastructure

Federated infrastructure linking national language-technology centres across Europe. Key services: the Virtual Language Observatory (metadata search across centres), Federated Content Search (query many corpora at once), and the Language Resource Switchboard (upload a file, get a list of tools that can process it).

**Access.** Web interfaces, no account for discovery and for the Switchboard. Depositing and some restricted corpora use federated academic login (eduGAIN/Shibboleth).

**Caveats.** The honest caveat for this catalogue's audience: a meaningful share of CLARIN corpora — especially newspaper and commercial text — sits behind academic federated login, which an unaffiliated researcher cannot obtain. Discovery, the Switchboard and openly licensed deposits are fully usable without affiliation; the gated portion is not. CLARIN centres also host well-documented open datasets on their own repositories (LINDAT, CLARIN-D, etc.) that are downloadable without login.

### [DPLA (Digital Public Library of America)](https://dp.la/)

`Free (registration), api-key` · beginner 4/5 · US cultural heritage aggregator

Aggregates records from US libraries, archives and museums through a network of state and regional hubs; as of June 2026 the index was approaching 55 million items. The DPLA network has also contributed over 11.25 million files to Wikimedia Commons.

**Access.** Web search; free JSON-LD API at https://api.dp.la/v2 (items and collections resource types) after requesting an API key — append `&api_key=YOUR_KEY` to every request. Bulk metadata downloads are published for whole-index analysis.

**Caveats.** Time-sensitive: leadership of DPLA's cultural heritage aggregation programme is transferring to Cleveland Public Library, with the formal transfer completing during 2026 and funding from the Sloan, MacArthur, Mellon and Ford foundations. DPLA states that ingestion and services continue unchanged through the transition, but branding and infrastructure may shift. Like Europeana, DPLA holds metadata and links, not the objects. The site has had repeated outages from bot traffic in 2026 and now applies CAPTCHAs and rate limits, so script politely.

### [EEBO-TCP (Text Creation Partnership)](https://textcreationpartnership.org/tcp-texts/eebo-tcp-early-english-books-online/)

`Free` · beginner 3/5 · early modern English full text

Keyed, SGML/TEI-encoded transcriptions of early English printed books: Phase I is 25,368 texts (public since 1 January 2015) and Phase II adds 34,963 texts, all free to the public since 1 August 2020. Coverage runs from the first book printed in English in 1475 to 1700.

**Access.** TEI XML for all released texts from github.com/textcreationpartnership (one repo per text, plus the aggregate `Texts` repo); rendered reading interfaces at Michigan's quod.lib.umich.edu and via the Oxford Text Archive. Parse with lxml or `pip install tei-reader`.

**Caveats.** Texts are dedicated to the public domain, but the page images they were keyed from are ProQuest's Early English Books Online and remain subscription-only — you get accurate text without the facsimile unless your library subscribes. Transcription is diplomatic, retaining early modern spelling and unresolved characters marked as gaps; normalisation (e.g. with VARD or MorphAdorner) is usually a prerequisite for analysis. TCP production has effectively concluded, so the corpus will not grow much further.

### [ELAR (Endangered Languages Archive)](https://www.elararchive.org/)

`Free (registration), email` · beginner 3/5 · endangered-language archive

Digital repository of multimedia language documentation deposits — everyday conversation, procedural texts, kinship and ethnobotanical explanations, verbal art — searchable by language, country, continent, depositor and date.

**Access.** Browse the catalogue without an account; register free to request access to deposits. Some collections stream or download directly; others require a request to the depositor.

**Caveats.** Catalogue metadata is CC BY-NC-SA 4.0, but the data files themselves are governed by ELAR Access Conditions set by each depositor — a substantial fraction is restricted and access can take weeks or be refused. This is by design: depositors negotiate terms with speaker communities. Plan around it rather than treating the archive as bulk-downloadable.

### [Europeana](https://www.europeana.eu/)

`Free (registration), api-key` · beginner 4/5 · European cultural heritage aggregator

Aggregated metadata and media links for digitised objects — manuscripts, paintings, photographs, newspapers, sound and film — from thousands of European galleries, libraries, archives and museums, operated under the EU's common European data space for cultural heritage.

**Access.** Web search interface with no account. For programmatic use, create a free Europeana account and request an API key, then use the Search API, the Record API and the IIIF APIs (which let you pull page images into Mirador or a local viewer).

**Caveats.** Europeana aggregates metadata and thumbnails; the full-resolution object usually lives on the contributing institution's own site, with its own rights statement, ranging from public domain to fully restricted. Metadata quality varies sharply between providers, and rights statements are the field to check first. Records disappear when a provider withdraws a collection.

### [Gallica (Bibliothèque nationale de France)](https://gallica.bnf.fr/)

`Free` · beginner 4/5 · French digitised heritage

The BnF's digital library: books, manuscripts, maps, images, press and periodicals, sound recordings, scores and objects, with strong coverage of French-language print from the fifteenth century onward and of the French colonial press.

**Access.** Web interface in six languages; SRU search API (`gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=...`), IIIF Image and Presentation APIs for page images, and OAI-PMH for metadata. `pip install gallica-autobib` or plain requests both work.

**Caveats.** No account needed for public-domain material, which is most of it. Some items are consultable only on BnF premises for rights reasons. OCR quality on early modern typography and on the nineteenth-century press is variable, and the OCR text is not always exposed through the API for every document type.

### [Glottolog](https://glottolog.org/)

`Free` · beginner 4/5 · language catalogue and genealogical classification

Version 5.3 lists 7,674 spoken L1 languages classified into 246 families and 183 isolates, each with a stable Glottocode, plus a bibliography of 460,382 descriptive references (grammars, dictionaries, word lists).

**Access.** Web interface for browsing; full data as CLDF from github.com/glottolog/glottolog and Zenodo (DOI 10.5281/zenodo.18840935). Python: `pip install pyglottolog`. References export as BibTeX for Zotero.

**Caveats.** CC BY 4.0. Classification is the editors' best guess and changes between releases, so always cite the version you used. Glottolog deliberately does not give speaker numbers or vitality assessments the way Ethnologue does.

### [Grambank](https://grambank.clld.org/)

`Free` · beginner 4/5 · typological database

Global database of grammatical structure covering over 2,000 languages and 195 features, coded from grammars and grammar sketches. Actively maintained by the MPI for Evolutionary Anthropology as part of the Glottobank consortium.

**Access.** Web interface; CLDF release from github.com/grambank/grambank and Zenodo. Python: `pip install pygrambank`. Joins to Glottolog on Glottocode.

**Caveats.** CC BY 4.0. New versions are released continuously, so record the version in any analysis. Complements rather than replaces WALS — the feature sets overlap only partly.

### [HathiTrust Digital Library](https://www.hathitrust.org/)

`Free` · beginner 4/5 · digitised book corpus

Roughly 18 million digitised volumes contributed by member libraries, with full-text search across the whole corpus including in-copyright works.

**Access.** Web full-text search is open to anyone with no account — you can find which page of which edition contains a phrase, across all 18 million volumes. Public-domain volumes are readable page by page and downloadable as PDF.

**Caveats.** The gate is real and worth stating plainly: full-view reading and whole-book PDF download apply only to public-domain volumes, and even those sometimes require login from a member institution for the full PDF. In-copyright volumes give search-only results (page numbers and hit counts, no text). The HathiTrust Research Center offers derived non-consumptive datasets, but capsule compute and some datasets are tied to member institutions. Unaffiliated researchers should treat HathiTrust as a bibliographic and page-location discovery tool rather than a text source.

### [Internet Archive](https://archive.org/)

`Free (registration), email` · beginner 5/5 · general digital archive and lending library

Digitised books, periodicals, audio, film, software and the Wayback Machine's web captures. For humanities work the important parts are the public-domain full-text scans (with OCR text and DjVu/EPUB derivatives) and the Wayback Machine as a citable source for born-digital material.

**Access.** Web interface; full-text search across scanned books; direct download of public-domain items. Programmatic: `pip install internetarchive` then `ia download <identifier>`, or the Wayback CDX API for capture listings.

**Caveats.** Public-domain items download freely with no account. Controlled-digital-lending titles are different: they need a free account, loans are one hour (renewable if a copy is free) or fourteen days, and downloads of borrowed books are LCP-DRM-protected files readable only in Thorium or Cantook. Following the Hachette v. Internet Archive litigation, many in-copyright titles were withdrawn from lending, so a book you remember borrowing may no longer be available.

### [Mozilla Common Voice](https://commonvoice.mozilla.org/en/datasets)

`Free (registration), email` · beginner 4/5 · crowdsourced speech corpus

Release 26.0 (12 June 2026) of the scripted-speech corpus spans 294 locales with roughly 28,900 validated hours out of about 42,400 recorded hours. A separate spontaneous-speech corpus (release 4.0, June 2026) covers 78 locales.

**Access.** Web interface: pick a language, give an email address, download the tar.gz (MP3 clips plus TSV transcripts). Also on Hugging Face as `mozilla-foundation/common_voice_*`. Per-release statistics as JSON at github.com/common-voice/cv-dataset.

**Caveats.** CC0, which is unusually permissive for speech data. Distribution is extremely uneven — English and a few European languages dominate, while many locales have only a handful of validated hours. Large locales are multi-gigabyte downloads; take a delta release if you only need the increment. Demographic metadata (age, sex, accent) is self-reported and often missing.

### [Old Bailey Online](https://www.oldbaileyonline.org/)

`Free` · beginner 5/5 · historical court records

Fully searchable transcriptions of every surviving edition of the Old Bailey Proceedings, 1674–1913 — over 197,000 trials — plus the Ordinary of Newgate's Accounts 1676–1772 and biographical detail on about 2,500 people executed at Tyburn. Version 9.0 (2023) rebuilt the site and search.

**Access.** Web search by keyword, name, and crime/verdict/punishment; statistical search for aggregate counts; a documented API; and bulk TEI-XML downloads of the whole corpus from the Downloads page.

**Caveats.** Free for non-commercial use — commercial reuse requires permission. The transcriptions are of the published Proceedings, which were themselves edited and abridged, so they are not a verbatim record of what was said in court; the site's 'Value as a Historical Source' pages document this carefully and should be read before quantitative work. The site sits behind a bot filter that blocks plain scripted requests.

### [OPUS](https://opus.nlpl.eu/)

`Free` · beginner 3/5 · parallel corpora

Aggregates 1,214 parallel corpora covering 1,038 languages and roughly 102.9 billion sentence pairs; the largest collections are OpenSubtitles (27.2B), NLLB (22.7B) and CCMatrix (17.2B).

**Access.** Web query interface; REST API at opus.nlpl.eu/opusapi/; command line via `pip install opustools` then `opus_read -d OpenSubtitles -s en -t tr -wm moses`. Downloads are per language pair, so you can take a 10 MB slice rather than the whole corpus.

**Caveats.** Licences vary per corpus and OPUS does not normalise them — OpenSubtitles in particular has murky provenance and is unsuitable for some redistribution. Web-mined corpora (CCMatrix, NLLB) are automatically aligned and noisy; use OpusFilter before treating them as gold data.

### [Pangloss Collection (CNRS)](https://pangloss.cnrs.fr/)

`Free` · beginner 4/5 · endangered-language recordings

Open archive of audio and video documents in rare and little-described languages, collected by professional linguists, with time-aligned transcriptions and translations. Interface in French and English.

**Access.** Browse or search on the web; recordings and their XML/ELAN annotation files download directly with no account. OAI-PMH endpoint for metadata harvesting.

**Caveats.** Genuinely open-access — one of the few endangered-language archives where you can download annotated recordings without a request workflow. Coverage is driven by which CNRS-affiliated fieldworkers deposited, so it is deep in a few families (Sino-Tibetan, Austronesian, Niger-Congo) and absent elsewhere.

### [PARADISEC](https://www.paradisec.org.au/)

`Free (registration), email` · beginner 3/5 · endangered-language archive

Pacific and Regional Archive for Digital Sources in Endangered Cultures holds 20,500 hours of audio and 4,000 hours of video — over 320 TB — representing 1,460 languages, mainly but not only from the Pacific region.

**Access.** Search the catalogue at catalog.paradisec.org.au; open items stream and download directly; restricted items have a documented request route.

**Caveats.** Access conditions are set per collection by the depositor and speaker community; some material is closed or requires community permission. Much of the collection is digitised analogue field recordings, so audio quality varies widely and transcription coverage is patchy.

### [Perseus Digital Library and the Scaife Viewer](https://www.perseus.tufts.edu/hopper/)

`Free` · beginner 4/5 · classical texts with linguistic annotation

Greek and Latin texts with word-by-word morphological analysis, dictionary lookup (LSJ, Lewis & Short), translations and commentaries. The Scaife Viewer (scaife.perseus.org) is the newer reading environment built with the Open Greek and Latin project, and is the first phase toward Perseus 5/6.

**Access.** Web reading interface with click-through morphology; source texts as TEI XML from github.com/PerseusDL/canonical-greekLit and canonical-latinLit, addressable by CTS URN. Combine with CLTK for programmatic analysis.

**Caveats.** Texts and lexica are CC BY-SA. The Perseus 4 'Hopper' interface is dated and periodically slow; the Scaife Viewer is more modern but covers a different (in places larger, in places smaller) text set. Editions are often nineteenth-century public-domain ones rather than current critical texts — fine for language work, sometimes inadequate for textual criticism.

### [PHOIBLE](https://phoible.org/)

`Free` · beginner 4/5 · phonological inventories

PHOIBLE 2.0 (2019) aggregates 3,020 phoneme inventories for 2,186 distinct languages, using 3,183 segment types with full phonetic feature vectors.

**Access.** Web interface; CLDF and long-format CSV from github.com/phoible/dev. R users can read the aggregated CSV directly from the repo URL; Python via pandas.

**Caveats.** CC BY-SA 3.0. Inventories come from several source doculects and often disagree for the same language — PHOIBLE keeps them all rather than reconciling, so you must decide how to aggregate. No release since 2.0.

### [Project Gutenberg](https://www.gutenberg.org/)

`Free` · beginner 5/5 · public-domain ebook corpus

79,277 free ebooks, proofread and marked up, mostly pre-1929 literature in English with substantial French, German, Finnish, Dutch, Portuguese and other collections. The default clean-text corpus for stylometry and literary text mining.

**Access.** Direct download in plain text, EPUB, HTML and Kindle formats, no registration. For corpus work use the mirrors or `pip install gutenbergpy` / the Gutendex JSON API rather than crawling the site; a curated metadata-plus-text distribution is available as Standardized Project Gutenberg Corpus.

**Caveats.** The site's robot access policy forbids bulk crawling of the main server — use an official mirror or the bulk archive instead, or you will be blocked. Texts carry a Project Gutenberg licence header and footer that must be stripped before analysis. US public domain is the selection criterion, so availability differs from what is public domain in the EU. Access from Germany has been restricted following litigation over a small set of titles.

### [TalkBank / CHILDES](https://talkbank.org/)

`Free (registration), email` · beginner 3/5 · conversation and child-language corpora

Fourteen linked repositories (CHILDES for child language, plus PhonBank, AphasiaBank, DementiaBank, BilingBank, CABank and others) holding transcripts in the CHAT format, contributed by hundreds of researchers working in over 42 languages, much of it aligned to audio and video.

**Access.** Register for a free TalkBank account, then browse or bulk-download corpora by language group. Analysis with the free CLAN program; SQL-style querying via TalkBankDB; `pip install pylangacq` reads CHAT files in Python; Batchalign handles ASR and UD conversion.

**Caveats.** As of August 2026 the CHILDES site carries a notice that the repository 'is under review for potential modification in compliance with Administration directives' — worth checking before you plan work that depends on continued availability. Clinical banks (aphasia, dementia, psychosis) require an additional permission request beyond the basic account. All use must cite at least one corpus reference and acknowledge NICHD grant HD082736.

### [Trove (National Library of Australia)](https://trove.nla.gov.au/)

`Free (registration), api-key` · beginner 4/5 · Australian newspapers and heritage aggregator

Aggregates Australian newspapers and gazettes, magazines, images, maps, archives, music and websites from partner institutions. The digitised newspaper corpus is unusually good because volunteers have hand-corrected large amounts of the OCR.

**Access.** Web search with no account. Free API key after registering an account; documented at the Trove API technical guide, with bulk download options for some collections. The `trove-newspaper-harvester` Python package (Tim Sherratt) is the usual way to pull a search result set to disk.

**Caveats.** API terms restrict some commercial reuse and require attribution; the key is free but is issued per project. Copyright status varies by item and many post-1954 newspapers are not digitised. The site uses an anti-bot proof-of-work challenge, so use the API rather than scraping HTML.

### [Universal Dependencies](https://universaldependencies.org/)

`Free` · beginner 4/5 · syntactically annotated treebanks

Cross-linguistically consistent morphosyntactic annotation: release 2.18 (15 May 2026) covers over 200 treebanks in over 150 languages, built by 600+ contributors. Data is CoNLL-U plain text, so a laptop handles it comfortably.

**Access.** Direct download of the whole release from the UD site or LINDAT (hdl.handle.net/11234/1-6149); per-treebank git repos at github.com/UniversalDependencies. Read in Python with `pip install conllu` or `pip install pyconll`.

**Caveats.** Licences differ per treebank: mostly CC BY-SA 4.0, but some are CC BY-NC-SA or GPL. Check the individual treebank before redistributing derived data or training a commercial model. A handful of treebanks distribute only annotation and require you to obtain the underlying text separately.

### [WALS Online (World Atlas of Language Structures)](https://wals.info/)

`Free` · beginner 5/5 · typological database

192 typological features coded for 2,660 languages, giving 76,475 datapoints, each linked to the source grammar. Current release is v2020.4.

**Access.** Web interface with maps per feature; full dataset as CLDF from github.com/cldf-datasets/wals (languages.csv, parameters.csv, values.csv) or Zenodo DOI 10.5281/zenodo.13950591. Load directly into pandas or R.

**Caveats.** CC BY 4.0. WALS is explicitly a finished project — the site says it will no longer be updated, and the underlying 2013 edition has known coding errors. Coverage is uneven: most languages are coded for only a fraction of the 192 features, which matters for statistical work. For an actively maintained alternative, see Grambank.

## Software

### [AntConc](https://www.laurenceanthony.net/software/antconc/)

`Free` · beginner 5/5 · corpus concordancer

Freeware desktop corpus analysis toolkit (current release 4.4.2): concordance lines, KWIC sorting, collocates, n-grams, keyword lists against a reference corpus, and word frequency. Runs from a single executable with no installation.

**Access.** Direct download for Windows (installer or portable), macOS (Apple Silicon) and Linux (Flatpak) from Laurence Anthony's site. Point it at a folder of plain-text files and it works immediately.

**Caveats.** Freeware rather than open source. Everything is held in memory, so multi-gigabyte corpora need a server-class concordancer instead. The 3.x series is still downloadable and behaves differently from 4.x — tutorials written for one version often do not match the other.

### [CLTK (Classical Language Toolkit)](https://docs.cltk.org/)

`Free` · beginner 3/5 · historical-language NLP

Python NLP for pre-modern languages — Latin, Ancient Greek, Old English, Old Norse, Sanskrit, Akkadian and others — with tokenisation, lemmatisation, morphosyntactic analysis, prosody/scansion, stopword lists and named pipelines per language.

**Access.** `pip install cltk`; `from cltk import NLP; nlp = NLP(language='lat'); doc = nlp.analyze(text)`. Corpora are fetched on demand from CLTK's own data repositories.

**Caveats.** MIT-licensed. Language support is very uneven — Latin and Ancient Greek are well served, other languages sometimes offer little beyond tokenisation. The API has changed substantially between major versions, so older tutorials frequently do not run. Some processes now optionally call external LLM backends; the core pipeline does not require them.

### [ELAN](https://archive.mpi.nl/tla/elan)

`Free` · beginner 3/5 · multimodal annotation

Annotation tool from the Max Planck Institute for Psycholinguistics for adding an unlimited number of time-aligned tiers of text — transcription, gloss, translation, gesture coding, comment — to audio and video recordings. The standard tool in language documentation and gesture research.

**Access.** Direct download for macOS, Windows and Linux from The Language Archive. Files are open .eaf XML; read them in Python with `pip install pympi-ling` or in R with the `phonfieldwork` package.

**Caveats.** Open source (GPL). Java-based and memory-hungry on long video files — on a modest laptop, work with compressed proxy video. Interoperates with FLEx and with CLAN/CHAT, though round-tripping loses some tier structure.

### [eScriptorium and Kraken](https://escriptorium.readthedocs.io/)

`Free` · beginner 2/5 · handwritten text recognition (HTR)

Fully open-source HTR stack: Kraken is the recognition engine (layout analysis, line segmentation, transcription) built for historical and non-Latin scripts, and eScriptorium is the web front end for uploading images, correcting segmentation and transcription, and training your own models.

**Access.** Kraken: `pip install kraken`, then `kraken -i page.png out.txt segment ocr -m model.mlmodel`. eScriptorium: self-host with Docker Compose from gitlab.com/scripta/escriptorium. Pretrained models are shared on Zenodo and the HTR-United / Kraken model repositories.

**Caveats.** Genuinely free with no credit metering and no vendor — the reason to prefer it over Transkribus if you can run it. The cost is setup: eScriptorium needs Docker and a few gigabytes of RAM, and model training benefits greatly from a GPU (a free Colab or Kaggle GPU session is a workable substitute). Some public eScriptorium instances offer accounts, but availability varies.

### [FieldWorks Language Explorer (FLEx)](https://software.sil.org/fieldworks/)

`Free` · beginner 2/5 · lexicography and interlinear text

SIL's desktop suite for building a dictionary and a corpus of interlinearised texts in parallel: lexical entries, morphological parsing, glossing, and publication-ready dictionary and grammar output.

**Access.** Direct download for Windows and Linux from SIL; no account. Data exports as LIFT XML (interchangeable with other lexicography tools) and as FlexText.

**Caveats.** Free and open source, but the learning curve is steep and the data model is opinionated — plan on working through SIL's training materials. macOS support is via a virtual machine rather than a native build, which is a real obstacle for Mac-only fieldworkers.

### [Omeka (Classic and Omeka S)](https://omeka.org/)

`Free` · beginner 3/5 · digital collections and exhibits

Open-source web publishing platform for cultural heritage collections: describe items with Dublin Core or any RDF vocabulary, build browsable collections and narrative exhibits, and expose the result over a REST API and OAI-PMH. Omeka S is the multi-site, linked-data-oriented version; Omeka Classic is the simpler single-site one.

**Access.** Download and self-host on any PHP/MySQL server (`omeka.org/s/download/`), or use omeka.net's hosted service. Modules add IIIF viewers, CSV import, geolocation and Zotero import.

**Caveats.** GPL and free to run, but self-hosting means you pay for and administer a server — realistically a few dollars a month plus sysadmin time. The hosted omeka.net has a limited free tier with a small storage cap; larger plans are paid. Omeka S and Omeka Classic have different module ecosystems and are not interchangeable.

### [Praat](https://www.fon.hum.uva.nl/praat/)

`Free` · beginner 3/5 · phonetic analysis

The standard free program for acoustic phonetics: spectrograms, formant, pitch and intensity tracking, segmentation into TextGrids, articulatory synthesis and a scripting language for batch analysis. Runs on macOS, Windows, Linux, Raspberry Pi and Chromebook.

**Access.** Direct download of a single binary from the University of Amsterdam site; no installer dependencies. Batch work through Praat scripts, or drive it from Python with `pip install parselmouth` (praat-parselmouth).

**Caveats.** Open source (GPL) with source available. The interface is idiosyncratic and the scripting language is unlike anything else — budget time for the built-in Intro tutorial. Runs happily on a decade-old laptop.

### [Recogito Studio](https://recogitostudio.org/)

`Free` · beginner 2/5 · collaborative annotation

Open-source platform for collaborative, standards-based annotation of TEI XML texts, IIIF images and PDFs, producing W3C Web Annotations, with real-time multi-user editing and a plugin SDK for custom tools and export formats.

**Access.** Self-host with Docker/Docker Compose following the documentation; a hosted demo is available on request.

**Caveats.** This is the successor to the original Pelagios Recogito, whose free hosted service at recogito.pelagios.org was retired — old links and tutorials point at a service that no longer exists. Recogito Studio assumes you can run Docker and a reverse proxy, which is a real barrier if you have no server; a small VPS suffices.

### [Stanza](https://stanfordnlp.github.io/stanza/)

`Free` · beginner 4/5 · multilingual NLP pipeline

Stanford NLP Group's Python toolkit with neural pipelines trained mainly on Universal Dependencies treebanks: tokenisation, multi-word token expansion, POS and morphological features, lemmatisation, dependency and constituency parsing, NER, sentiment, language identification and coreference. Also ships biomedical/clinical models.

**Access.** `pip install stanza` then `stanza.download('tr')`; `nlp = stanza.Pipeline('tr')`. Published per-language accuracy tables let you check whether a language is usable before committing.

**Caveats.** Apache 2.0. Much wider language coverage than spaCy because it piggybacks on UD, but noticeably slower and heavier; a GPU helps for anything beyond a few thousand sentences. Model quality tracks the size of the underlying UD treebank, so small-treebank languages parse poorly.

### [stylo (R)](https://cran.r-project.org/package=stylo)

`Free` · beginner 4/5 · stylometry and authorship attribution

The reference R package for computational stylistics: Burrows's Delta and its variants, cluster analysis and bootstrap consensus trees, principal component analysis, rolling classification for collaborative texts, and the oppose/craig-zeta contrastive methods.

**Access.** `install.packages("stylo")`; running `stylo()` with a folder of plain-text files opens a GUI that produces a dendrogram with no code written. Scriptable for reproducible pipelines.

**Caveats.** GPL. The GUI makes it unusually approachable, which is also its risk — it will happily produce a confident-looking dendrogram from badly prepared or unbalanced data. Read the Computational Stylistics Group's tutorials on sample size and text preparation before trusting a result.

### [TEI Guidelines (Text Encoding Initiative)](https://tei-c.org/guidelines/)

`Free` · beginner 2/5 · text encoding standard

The community standard for encoding humanities texts in XML — manuscript description, critical apparatus, drama, dictionaries, correspondence, linguistic annotation — with a full schema, customisation mechanism (ODD) and worked examples. Nearly every scholarly digital edition uses it.

**Access.** Read the Guidelines free on the web; generate a project-specific schema with the Roma web tool or `pip install roma`-free alternatives; validate with any XML tool. Publish with TEI Publisher, CETEIcean or an XSLT of your own.

**Caveats.** CC BY. The Guidelines are enormous and written as a reference, not a tutorial — start from a subset such as TEI Lite or from an existing project's ODD rather than reading front to back. Encoding is labour, not software: the standard is free but the time is not.

### [Transkribus](https://www.transkribus.org/)

`Free tier, email` · beginner 4/5 · handwritten text recognition (HTR)

Hosted HTR platform with a document editor, a large library of public models for European handwriting and print, and custom model training. The free plan gives 50 credits per month (one credit ≈ one page of text recognition), one user seat and 20 GB of storage.

**Access.** Web application after creating a free account; upload images, run a public model, correct in the editor, export PageXML/ALTO/plain text. Custom model training is available on the free plan.

**Caveats.** 50 pages a month is enough to evaluate the tool or transcribe a short document, not to process an archive. Beyond it: Scholar at €8.25/month billed annually for 900 credits a year, Team at €37.42/month for 1,500 credits and 5 seats, or on-demand credits at €59.50 for 250. Your images are uploaded to Transkribus's servers — check that this is compatible with any archive's reproduction terms. For unmetered work on your own hardware, use eScriptorium/Kraken instead.

### [Tropy](https://tropy.org/)

`Free` · beginner 5/5 · archival photo organisation

Desktop application for organising and describing the thousands of photographs researchers take in archives: group images into items, add metadata using standard templates, tag, transcribe and annotate, and export to formats other tools can read.

**Access.** Direct download for macOS, Windows and Linux; free, open source, from the Corporation for Digital Scholarship (the Zotero developers). Data lives in a local SQLite database you own.

**Caveats.** Entirely local with no cloud service, which means no vendor lock-in but also no built-in sync or backup — arrange your own. It organises and describes images; it does not do OCR or handwriting recognition, so pair it with Transkribus or eScriptorium.

### [Voyant Tools](https://voyant-tools.org/)

`Free` · beginner 5/5 · browser-based text analysis

Web-based reading and visualisation environment for text corpora: word clouds, frequency and trend graphs, collocation networks, KWIC concordances and document comparison, all from a pasted URL, uploaded files or typed text. The usual first tool for a humanities researcher who does not code.

**Access.** Paste text or upload files at the web interface. To run offline or on large or sensitive corpora, download VoyantServer from github.com/voyanttools/VoyantServer and run it locally (Java).

**Caveats.** The hosted instance at voyant-tools.org is frequently down — it returned 502 for the whole of a check on 2026-08-28. For anything you depend on, run your own copy: VoyantServer is a self-contained download that runs locally with a bundled Java, and the source is on GitHub under GPL-3.

### [Zotero](https://www.zotero.org/)

`Free tier, email` · beginner 5/5 · reference manager

Open-source reference manager with browser connectors that capture citations and PDFs from library catalogues, archives and journal sites, a built-in PDF reader with annotation extraction, word-processor plugins for every major citation style, and shared group libraries.

**Access.** Download the desktop app plus the browser connector; free account for syncing. Local libraries are unlimited in size regardless of the storage plan; `pip install pyzotero` drives the web API.

**Caveats.** The app and all features are free; only cloud file storage is metered — 300 MB free, then $20/year for 2 GB up to $120/year unlimited. You can keep attachments local and sync only metadata, or point file storage at your own WebDAV server, and stay free indefinitely. Group libraries draw on the group owner's storage quota.

## Literature

### [ACL Anthology](https://aclanthology.org/)

`Free` · beginner 5/5 · open bibliographic archive (computational linguistics)

Complete open archive of papers from ACL, EMNLP, NAACL, COLING, LREC and associated venues: 131,027 papers by 133,924 authors across 3,495 volumes, all with free PDFs, BibTeX and stable URLs.

**Access.** Web browse by venue and year; every paper has a one-click BibTeX entry for Zotero. Bulk metadata as a single BibTeX/YAML export from github.com/acl-org/acl-anthology; `pip install acl-anthology-py` for programmatic access.

**Caveats.** Papers are typically CC BY 4.0 (older material varies). This is the model of what an open disciplinary archive looks like — no paywall, no embargo, machine-readable metadata. It covers computational linguistics and speech, not theoretical linguistics or the humanities more broadly.

*Also listed under: cs-ml.*

### [JSTOR free personal account and Open Content](https://about.jstor.org/whats-in-jstor/)

`Free (registration), email` · beginner 5/5 · journal archive access

A free personal (MyJSTOR) account lets anyone read up to 100 articles every 30 days online, alongside JSTOR's permanently free Open Content: Early Journal Content (pre-1923 US / pre-1870 elsewhere) and a growing set of open-access books and journals.

**Access.** Register with an email address, then read online in the browser; save items to a Workspace and export citations to Zotero. Open Content items download as PDF without any account.

**Caveats.** The 100-article allowance is read-online only — you cannot download PDFs of subscription articles, and the counter is per 30-day window. This is the single most useful legal route into paywalled humanities journal literature for an unaffiliated researcher, but it is a reading room, not a library you can build a corpus from. JSTOR also offers text-analysis support for its corpus; note that the Constellate platform that formerly provided this was sunset on 1 July 2025.

### [LingBuzz](https://lingbuzz.net/)

`Free` · beginner 5/5 · preprint archive (theoretical linguistics)

Archive and community space for linguistics papers, currently holding around 10,080 articles, weighted toward syntax, semantics and phonology. Where a large part of generative linguistics circulates before and independently of journal publication.

**Access.** Browse or search the web interface with no account; PDFs download directly. Free account to upload your own papers, published or not.

**Caveats.** Run by one person (Michal Starke) rather than an institution, with no long-term preservation guarantee and minimal metadata — no DOIs, inconsistent versioning. Not moderated for quality. For anything you need citable and archived, deposit in a repository with DOIs as well. Coverage is narrow: little on typology, sociolinguistics or documentation.

### [OpenEdition](https://www.openedition.org/)

`Freemium` · beginner 4/5 · European humanities publishing platform

French-led infrastructure comprising OpenEdition Journals (several thousand humanities and social science journals), OpenEdition Books (scholarly monographs), Hypothèses (research blogs) and Calenda (a calendar of humanities events). Strong Francophone, Hispanophone and Lusophone coverage that Anglophone indexes miss.

**Access.** Web reading with no account; OAI-PMH and a documented API for metadata. Most content is readable in HTML directly in the browser.

**Caveats.** The Freemium model is the thing to understand: HTML full text is generally free to read, while PDF and ePub versions of the same article or book are often reserved for subscribing institutions. For an unaffiliated reader that usually means reading in the browser rather than downloading. A substantial minority of titles are fully open in all formats.

## Publishing

### [Glossa: a journal of general linguistics](https://www.glossa-journal.org/)

`Free` · beginner 5/5 · diamond open-access journal

General linguistics journal published on the Open Library of Humanities platform, founded when the editorial board of Lingua resigned over open access. Articles are CC BY 4.0 with authors retaining copyright.

**Access.** Read and download every article free; submit through the journal's OJS-based system.

**Caveats.** Explicitly diamond: no obligatory fees for readers or authors. Authors with institutional or grant open-access funds are asked, on an honour system, for a £450 Voluntary Author Contribution — this is not required, and authors at OLH-supporting institutions are not asked at all. Unaffiliated and unfunded authors pay nothing.

### [Language Science Press](https://langsci-press.org/)

`Free` · beginner 5/5 · diamond open-access book publisher

Scholar-led open-access publisher of linguistics monographs and edited volumes, with 386 titles in its catalogue across 35 series (grammars, typology, syntax, phonology, historical linguistics, translation studies and more). Free for both authors and readers.

**Access.** Download every book as PDF, and many as HTML and ePub, with no account. To publish: choose a series, follow the submission checklist, and work in the LaTeX or Word templates provided; production is community-supported with volunteer proofreaders.

**Caveats.** Genuinely diamond — no book processing charges and no reader paywall, funded by a library consortium. Authors do more production work than at a commercial press (typesetting in the LaTeX template, recruiting proofreaders), which is the trade-off. Turnaround depends on series editor availability. Their grammar series is a realistic venue for a documentation dissertation.

### [Open Book Publishers](https://www.openbookpublishers.com/)

`Free` · beginner 5/5 · open-access monograph publisher

Award-winning scholar-led non-profit open-access academic press, founded 2008 in the UK, publishing peer-reviewed monographs, edited collections, textbooks and critical translations. All books are free in PDF and HTML (sometimes XML), with affordably priced print editions.

**Access.** Read or download every book free from the website with no account; also distributed through OAPEN and DOAB. Proposals are submitted through the 'Publish with us' pages.

**Caveats.** Does not charge authors to publish and authors retain full control of their work — a real diamond monograph route, unusual in the humanities. Some titles do attract a book processing charge where funding exists, so confirm terms for your specific proposal. ePub editions are usually sold rather than given away, unlike the PDF and HTML.

### [Open Library of Humanities](https://www.openlibhums.org/)

`Free` · beginner 5/5 · diamond open-access journal platform

Publishes 39 open-access humanities journals, funded collectively by more than 345 libraries worldwide rather than by author charges. Articles get DOIs, are widely indexed, and are digitally preserved.

**Access.** Read everything free; submit to any of the 39 journals through the platform. OLH also offers journal hosting and migration for editorial boards leaving commercial publishers.

**Caveats.** No APCs — the model is library consortium funding, which is why it works for unaffiliated authors. Journal scopes are specific (from Nineteenth-Century Matters to Digital Medievalist); check whether one fits before assuming OLH is an option. If you are an editorial board wanting to leave a commercial publisher, the migration service is the practical route.

### [punctum books](https://punctumbooks.com/)

`Free` · beginner 5/5 · open-access para-academic publisher

Independent non-profit open-access publisher (a California public benefit corporation) for scholarship that falls between or outside conventional disciplinary boundaries — theory, medieval and early modern studies, philosophy, experimental and hybrid scholarly writing.

**Access.** All titles free to download as PDF from the website and from the Open Monograph Press catalogue; print copies for sale. Proposals through the submissions pages.

**Caveats.** Supported by a library membership programme and donations rather than author fees, though contributions are welcomed where funding exists. Deliberately unconventional editorial scope — an asset for work that mainstream presses find unclassifiable, a poor fit for a conventional monograph. Small operation, so production timelines are variable.

### [Semantics and Pragmatics](https://semprag.org/)

`Free` · beginner 5/5 · open-access journal (LSA)

Fully open-access peer-reviewed journal of natural-language semantics and pragmatics, published by the Linguistic Society of America and, since 2013, one of only two full LSA journals alongside Language.

**Access.** Read and download all articles free; submit through the journal site. LaTeX class file provided.

**Caveats.** No article processing charges and no submission charges of any kind. Society-backed, so it carries the prestige that new diamond journals often lack. Scope is narrow — semantics and pragmatics, plus material of relevance to philosophers of language.

## Funding

### [ELDP (Endangered Languages Documentation Programme)](https://www.eldp.net/)

`Free, application` · beginner 2/5 · language documentation grants

The main international funder dedicated to endangered-language documentation, offering Rapid grants (small, fast-turnaround), Documentation grants (full projects) and Legacy material grants (digitising and cataloguing existing collections), plus grantee training and an online training series.

**Access.** Apply through the ELDP application system during an open call; the Apply pages give current eligibility, deadlines and budget ceilings for each grant type.

**Caveats.** Grants are competitive and applications are substantial documents; the Rapid grant is the realistic entry point. Deposit of the resulting materials in an accessible archive is a condition. Check the current call for eligibility — requirements around institutional affiliation and career stage differ between the grant types and have changed between rounds.

### [Endangered Language Fund](https://www.endangeredlanguagefund.org/)

`Free, application` · beginner 3/5 · small language documentation and revitalisation grants

US non-profit, now in its thirtieth year, running the Language Legacies small-grant programme for documentation and revitalisation, the Native Voices Endowment for Lewis and Clark trail languages, the ELF-UNESCO traineeship and a Sharing Language Diversity fellowship.

**Access.** Apply online during the annual Language Legacies cycle; applications are short compared with major funders, which makes this a realistic first grant.

**Caveats.** Awards are small — typically low thousands of dollars — and suit a discrete piece of fieldwork, equipment, or a community workshop rather than a salaried project. Explicitly open to community members and language activists, not only academics. Programme availability varies year to year; check the current funding opportunities page.

### [Foundation for Endangered Languages](https://www.ogmios.org/)

`Free, application` · beginner 3/5 · small grants and community network

Registered charity supporting documentation, protection and promotion of endangered languages through small grants, a newsletter (Ogmios), a bibliography, and an annual conference — the 2026 meeting is in Paris, 3–5 November, on endangered languages and innovative technologies.

**Access.** Grant applications through the Grants pages during the annual call; membership (modest fee, with reduced rates) brings the newsletter and conference access.

**Caveats.** Grants are very small — suitable for a specific piece of community language work, recording equipment or a publication subsidy, not for supporting a person. Volunteer-run, so response times are slow. The annual conference is one of the more accessible venues for community language workers to present alongside academics.

### [Wenner-Gren Foundation Post-PhD Research Grant](https://wennergren.org/program/post-phd-research-grant/)

`Free, application` · beginner 2/5 · anthropology and linguistic anthropology grants

Research grants of up to $25,000 for scholars holding a doctorate in anthropology (including linguistic anthropology) or a related field with an anthropology appointment. Grants are non-renewable and may cover research spread over multiple phases.

**Access.** Apply through the Wenner-Gren online system during an open cycle; a resubmission with a response statement is permitted once.

**Caveats.** The eligibility line matters for this catalogue: 'qualified scholars of any nationality or institutional affiliation' — independent and senior scholars are explicitly welcome. A doctorate is required. Awards include no institutional overhead, which suits unaffiliated applicants. Competitive; expect a long lead time.

## Learning

### [DARIAH-Campus](https://campus.dariah.eu/)

`Free` · beginner 4/5 · digital humanities training platform

Discovery framework and hosting platform for digital humanities learning resources from DARIAH, the pan-European infrastructure for arts and humanities scholars using computational methods: hosted training resources, recordings of past DARIAH events, and curated 'pathfinder' collections of external material.

**Access.** Browse or search free with no account; resources include video, slides and written tutorials. Linked to the DH Course Registry for finding formal training.

**Caveats.** DARIAH-Campus is deliberately not exhaustive — it collects what DARIAH and its partners produce, so coverage is patchy across methods and skewed toward European projects and infrastructures. Quality is generally high but resources are not versioned or maintained the way Programming Historian lessons are.

### [Essentials of Linguistics (2nd edition)](https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/)

`Free` · beginner 5/5 · open introductory textbook

Openly licensed introductory linguistics textbook by Catherine Anderson, Bronwyn Bjorkman, Derek Denis, Julianne Doner, Margaret Grant, Nathan Sanders and Ai Taniguchi, covering phonetics, phonology, morphology, syntax, semantics, sociolinguistics and language acquisition, with embedded videos and exercises.

**Access.** Read free in the browser; download as EPUB, digital PDF, print PDF or Pressbooks XML for adaptation. No account.

**Caveats.** Open licence means you can remix it for your own teaching. Written for a North American undergraduate audience with English-centred examples, so supplement it for typological breadth. The videos are hosted externally and occasionally break.

### [Introduction to Cultural Analytics & Python](https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html)

`Free` · beginner 5/5 · open textbook (text analysis)

Melanie Walsh's free online textbook and course, built as a Jupyter Book: command line basics, Python from variables to functions, then applied chapters on text analysis, web scraping, APIs, topic modelling and network analysis using cultural datasets.

**Access.** Read free on the web; every page is a runnable notebook you can download or open in Binder/Colab, so you can execute the examples without installing anything locally.

**Caveats.** Assumes no prior programming, which makes it the right entry point for humanists before Programming Historian's more specialised lessons. Some examples use datasets that require download; a few third-party APIs used in the web-scraping chapters have changed their terms since the book was written.

### [Speech and Language Processing (Jurafsky & Martin, 3rd edition draft)](https://web.stanford.edu/~jurafsky/slp3/)

`Free` · beginner 3/5 · open textbook (computational linguistics)

The standard textbook for computational linguistics and NLP, released free as a continuously revised draft; the 19 August 2026 release adds a new introductory chapter, merges the transformers/pretraining/decoding material into one chapter, and begins an interpretability chapter.

**Access.** Download the whole book or individual chapters as PDF, free, no account. Slides for teaching are posted alongside.

**Caveats.** It is a draft: chapter numbering and content shift between releases, so cite the release date and expect links from other people's syllabi to point at renumbered chapters. Coverage has shifted heavily toward large language models in recent releases, with less space for classical symbolic and statistical methods than earlier editions.

### [The Programming Historian](https://programminghistorian.org/)

`Free` · beginner 5/5 · peer-reviewed methods tutorials

123 peer-reviewed English-language tutorials (plus separate Spanish, French and Portuguese editions) organised by research phase — acquire, transform, analyse, present, sustain — covering Python, APIs and web scraping, text analysis, mapping, network analysis, machine learning and digital publishing.

**Access.** Read free on the web; every lesson lists its software prerequisites and data, and most run on a laptop with a plain Python or R install. CC BY, so lessons can be adapted for teaching.

**Caveats.** The model open pedagogical resource in the field: openly peer reviewed, versioned, and maintained with a formal process for retiring lessons that no longer run. Some older lessons still depend on library versions that have moved on — check the lesson's revision date and reported dependencies before following it step by step.

## Community

### [Knowledge Commons (formerly Humanities Commons)](https://hcommons.org/)

`Free (registration), email` · beginner 5/5 · scholarly network and open repository

Non-profit, academy-owned network for humanities and adjacent fields: member profiles, topic and society groups (MLA, HASTAC, ARLIS/NA, AUPresses and others), hosted WordPress sites, and KC Works — an open repository that assigns DOIs to deposited papers, syllabi, datasets and grey literature.

**Access.** Free account with an email address, no institutional affiliation required. Deposit into KC Works through the web form; each deposit gets a DOI and is openly licensed at your choice.

**Caveats.** One of the few humanities scholarly networks explicitly open to unaffiliated researchers — this is its main value for this audience. The repository was formerly called CORE and the network formerly Humanities Commons, so older references use different names. Group activity is uneven: some are lively, many are dormant.

### [Linguistics Stack Exchange](https://linguistics.stackexchange.com/)

`Free (registration), email` · beginner 4/5 · Q&A site

Question-and-answer site for professional linguists, students and enthusiasts, covering phonetics and phonology, morphology, syntax, semantics, historical linguistics, sociolinguistics and computational linguistics, with voting and an explicit on-topic policy.

**Access.** Read with no account; register free with an email address to ask or answer. All content is CC BY-SA, so answers are quotable and archivable.

**Caveats.** Strict scope rules: 'what does this word mean', translation requests, conlang design and homework dumps get closed quickly. Read the on-topic page before asking. Traffic is moderate compared with the larger Stack Exchange sites, so obscure questions can sit unanswered for weeks. For language-specific usage questions, the separate Linguistics-adjacent sites (English Language & Usage, Latin) are often the better venue.

### [The LINGUIST List](https://linguistlist.org/)

`Free` · beginner 5/5 · disciplinary mailing list and noticeboard

The field's central noticeboard since 1990: calls for papers, conference announcements, job postings, dissertation abstracts, book notices and reviews, summaries of discussion threads, and directories of linguists, programmes and software.

**Access.** Browse the web archive free with no account; subscribe by email to the daily digest or to topic-specific feeds. Posting an announcement is free.

**Caveats.** This is where the discipline's practical information actually circulates — an unaffiliated researcher who reads nothing else will still see the conferences, calls and jobs. Volume is high; use the topic filters rather than the full digest. Job listings skew heavily toward institutions in North America and Europe.
