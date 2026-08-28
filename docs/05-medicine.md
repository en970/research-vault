# Medicine & health sciences

Part of [research-vault](../README.md). 72 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (24) · [Software](#software) (15) · [Literature](#literature) (10) · [Compute](#compute) (3) · [Publishing](#publishing) (6) · [Funding](#funding) (5) · [Learning](#learning) (6) · [Community](#community) (3)

## Data

### [All of Us Research Hub](https://www.researchallofus.org/)

`Free tier, application` · beginner 3/5 · US precision-medicine cohort

NIH cohort combining surveys, EHR, physical measurements, wearables and whole-genome sequencing. Three tiers: a Public Tier of aggregate counts open to everyone through the Data Browser, a Registered Tier of individual-level non-genomic data, and a Controlled Tier adding genomics and unshifted dates.

**Access.** Public Tier: browse variable-level counts at databrowser.researchallofus.org with no account. Registered and Controlled Tiers: apply on the Researcher Workbench, complete training and identity verification, then analyse in-browser with Jupyter, RStudio or SAS Studio.

**Caveats.** The honest gate: Registered and Controlled Tier access requires your institution to hold a Data Use and Registration Agreement with All of Us, so unaffiliated researchers generally cannot get in. Registration itself costs nothing and each Workbench user receives $300 in initial cloud credits, but compute and storage beyond that is billed to you. No data may be downloaded out of the Workbench — all analysis happens inside it.

### [CDC WONDER](https://wonder.cdc.gov/)

`Free` · beginner 4/5 · US vital statistics query system

Ad-hoc query system over US public health datasets: underlying and multiple cause of death, natality, infant deaths, cancer incidence, TB, STDs, population estimates and environmental exposure series, cross-tabulated by year, age, sex, race and geography down to county level.

**Access.** Web query wizard producing tables and TSV export; each database also has a POST XML API endpoint (e.g. `https://wonder.cdc.gov/controller/datarequest/D77` for Multiple Cause of Death). R: `install.packages('wonderapi')`.

**Caveats.** Sub-national cells with fewer than 10 deaths are suppressed and rates from small numbers are flagged unreliable, which limits rare-cause county work. The XML-request API is awkward; most people start in the web wizard. CDC has announced a modernisation of WONDER, so interfaces and URLs may shift during 2026.

### [ChEMBL](https://www.ebi.ac.uk/chembl/)

`Free` · beginner 3/5 · drug and bioactivity database

EMBL-EBI's manually curated database of bioactive drug-like molecules. Release ChEMBL_37 (1 May 2026) holds 2,921,148 distinct compounds, 24,527,044 activity measurements against 18,552 targets, curated from 101,100 publications, plus approved-drug and clinical-candidate annotations.

**Access.** Web interface plus a keyless REST API: `https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL25.json`, and `https://www.ebi.ac.uk/chembl/api/data/status.json` reports the current release and record counts. Python: `pip install chembl_webresource_client`. Full Oracle/MySQL/PostgreSQL dumps and an RDF distribution are on the EBI FTP.

**Caveats.** Licensed CC BY-SA 3.0, so derivative datasets and some models must be shared alike — this matters if a commercial partner is involved. Activities are extracted from heterogeneous published assays with differing units, assay formats and confidence scores; naively pooling IC50 values across assay types is the classic beginner error. It is medicinal-chemistry data, not clinical outcome data.

*Also listed under: chemistry.*

### [ClinicalTrials.gov](https://clinicaltrials.gov/)

`Free` · beginner 5/5 · clinical trial registry

US NLM registry holding 600,582 registered studies as of 28 August 2026, with protocol details, eligibility criteria, locations, and posted summary results for a subset. It is also the registry most journals accept for prospective trial registration.

**Access.** REST API v2, no key and no registration: `https://clinicaltrials.gov/api/v2/studies?query.cond=sepsis&pageSize=100&format=json`; `/api/v2/stats/size` returns registry totals. Bulk full-study JSON/XML downloads are offered from the Data API page. Python: `pip install pytrials`.

**Caveats.** Registering your own trial (rather than reading) needs a free PRS organisation account, which normally requires an institutional sponsor. Unaffiliated investigators are usually better served by another WHO primary registry that registers free of charge — PACTR (pactr.samrc.ac.za) for Africa, CTRI for India, ANZCTR for Australia/New Zealand. WHO ICTRP (trialsearch.who.int) federates all of them for searching. Posted results cover only a minority of completed studies.

### [Grand Challenge](https://grand-challenge.org/)

`Free (registration), email` · beginner 3/5 · medical imaging challenges and benchmarks

Platform hosting medical image analysis challenges together with their datasets, leaderboards and containerised algorithm submissions, filterable by modality (CT, MR, PET, histology, OCT, dermoscopy, ultrasound, X-ray) and anatomical region. Run by the Diagnostic Image Analysis Group, Radboud UMC.

**Access.** Web interface; register free to join a challenge, download its data and submit an algorithm as a Docker container. Archived challenge pages remain readable without an account. The Medical Segmentation Decathlon (medicaldecathlon.com) offers a similar ten-task segmentation benchmark by direct AWS download.

**Caveats.** Data access is decided per challenge: some are open downloads, some require a signed usage agreement, and some datasets are withdrawn once a challenge closes. Submission compute is capped per challenge. It is a benchmark venue, not a general repository — you cannot deposit arbitrary data there.

### [IHME Global Burden of Disease Results Tool](https://vizhub.healthdata.org/gbd-results/)

`Free (registration), email` · beginner 3/5 · burden of disease estimates

Query and download interface for GBD 2023, the current round: estimates for 204 countries and territories plus subnational locations, across 463 health outcomes and risk factors, 1990-2023, in deaths, DALYs, YLLs, YLDs, prevalence and incidence with uncertainty intervals.

**Access.** Web query builder — select measure, cause, location, year, age and sex, and receive a CSV by email link. Companion tools: GBD Compare for visual exploration, the GBD Sources Tool for input-data provenance, and the GHDx catalogue at ghdx.healthdata.org for the underlying datasets.

**Caveats.** Free only for non-commercial use, under the IHME Free-of-Charge Non-Commercial User Agreement; commercial use needs a separate licence. Large queries are queued and delivered asynchronously, sometimes hours later. Sequela-level YLD, prevalence and incidence results are not in the tool and must be requested by email. These are modelled estimates, not vital registration counts.

### [LOINC](https://loinc.org/)

`Free (registration), email` · beginner 3/5 · laboratory and clinical observation codes

Regenstrief Institute's universal code system for laboratory tests, measurements and clinical documents. Version 2.83 was released on 19 August 2026 as an 88.5 MB archive; releases come twice yearly, in February and August.

**Access.** Create a free LOINC account, then download the Loinc_2.83.zip table and accessory files, or use the RELMA mapping tool (Windows). A HL7 FHIR terminology service and a hierarchy browser are available online; search at loinc.org/search.

**Caveats.** Free worldwide including commercial use, but bound by the LOINC License — you may not fork the code system or redistribute modified versions as LOINC. Mapping local lab codes to LOINC is skilled, slow work that RELMA assists but does not automate. The site sits behind a Cloudflare bot filter (HTTP 403 to scripted requests), so downloads need a browser session; for automation, Regenstrief documents a download API at loinc.org/kb/api/download. Note the cadence change: releases are twice yearly now but Regenstrief has announced a move to monthly releases in 2027, so pin the version you map against.

### [MedMNIST / MedMNIST+](https://medmnist.com/)

`Free` · beginner 5/5 · medical imaging ML benchmark

Eighteen standardised biomedical image classification datasets (12 2D, 6 3D) totalling roughly 708,000 2D and 10,000 3D images with fixed train/validation/test splits, available at 28x28 up to 224x224 for 2D and 28^3 to 64^3 for 3D. Modalities include pathology, chest X-ray, dermatoscopy, OCT, ultrasound, CT and MRI.

**Access.** `pip install medmnist` (v3.0.2, Apache-2.0), then `from medmnist import PathMNIST; PathMNIST(split='train', download=True, size=224)` returns a PyTorch-compatible dataset. Raw .npz files also downloadable from Zenodo.

**Caveats.** Designed for laptops and free GPU tiers — the 28px versions train in minutes on CPU. Per-dataset licences are inherited from the source datasets (mostly CC BY or CC BY-NC), so check before commercial use. Downsampled images are for methods benchmarking, never for clinical claims.

### [MIMIC-IV](https://physionet.org/content/mimiciv/)

`Free (registration), credentialing` · beginner 2/5 · ICU and hospital EHR

De-identified EHR data from Beth Israel Deaconess Medical Center covering 364,627 unique patients, 546,028 hospitalizations and 94,458 ICU stays admitted 2008-2022. Current release is v3.1 (11 October 2024); dates are shifted into 2100-2200 and the hospital and ICU modules link on subject_id and hadm_id.

**Access.** Credentialed download from PhysioNet as gzipped CSVs, or query without downloading on Google BigQuery (`physionet-data.mimiciv_3_1_hosp`) once your Google account is linked to your approved PhysioNet profile. Official build scripts and concept SQL: github.com/MIT-LCP/mimic-code.

**Caveats.** Free of charge but genuinely gated: a PhysioNet account, a completed CITI 'Data or Specimens Only Research' training report (the report, not the certificate), a signed PhysioNet Credentialed Health Data License 1.5.0, and a reference/supervisor contact. Review is manual. Start with the open demo (next entry) while your application is pending. The licence forbids redistribution and any re-identification attempt.

### [MIMIC-IV Clinical Database Demo](https://physionet.org/content/mimic-iv-demo/)

`Free` · beginner 4/5 · ICU and hospital EHR (open subset)

Open-access v2.2 subset of MIMIC-IV using the identical table schema, published under the Open Data Commons ODbL. It is the only route into MIMIC-style ICU data that requires no account, no training and no data use agreement.

**Access.** Direct download: `wget -r -N -c -np https://physionet.org/files/mimic-iv-demo/2.2/`. Load the CSVs into DuckDB or SQLite and develop the same queries you will later run against full MIMIC-IV.

**Caveats.** A small patient sample, so it is for pipeline development and teaching only — never for estimating anything. It is a v2.2 snapshot while the full database is at v3.1, so a few columns differ.

### [NCI Genomic Data Commons (GDC)](https://portal.gdc.cancer.gov/)

`Free` · beginner 3/5 · cancer genomics and linked clinical data

Harmonised cancer genomics repository (TCGA, TARGET, CPTAC, MMRF and others): 93 projects, 50,571 cases and 1,337,360 files at Data Release 46.0 (10 August 2026). The open tier includes clinical and biospecimen tables, gene-expression and copy-number matrices, and mutation summaries.

**Access.** Web portal, plus a keyless REST API: `https://api.gdc.cancer.gov/files?filters=...&format=TSV`. Bulk transfer with the gdc-client CLI and a manifest; in R use Bioconductor's `TCGAbiolinks`.

**Caveats.** The open tier needs nothing at all. The controlled tier (raw BAM/FASTQ, germline variants) requires dbGaP authorisation via an eRA Commons account and an institutional Signing Official — effectively closed to unaffiliated researchers. The open tier is still sufficient for most secondary analyses.

### [NHANES](https://wwwn.cdc.gov/nchs/nhanes/Default.aspx)

`Free` · beginner 3/5 · national health examination survey

US National Health and Nutrition Examination Survey: linked interview, physical examination, dietary and laboratory files with complex survey weights. The latest fully released public cycle is August 2021 - August 2023; continuous cycles run back to 1999-2000 and the 2025-2026 cycle is in the field.

**Access.** Direct download of SAS XPT files per component from the questionnaires and datasets pages. R: `install.packages('nhanesA')` then `nhanes('DEMO_L')`, analysed with the `survey` package using WTMEC2YR/SDMVPSU/SDMVSTRA. Python: `pandas.read_sas(url)`.

**Caveats.** Public files are fully open, but restricted variables (fine geography, some linkages, mortality linkage detail) live in the NCHS Research Data Center and require an application and fees. Ignoring the survey design weights is by far the most common analytical error with these data.

### [Open Targets Platform](https://platform.opentargets.org/)

`Free` · beginner 3/5 · target-disease association evidence

EMBL-EBI, Wellcome Sanger and pharma-partner platform that integrates GWAS and rare-disease genetics, somatic mutations, expression, pathways, animal models, known drugs and text-mined literature into scored target-disease associations. Data release 26.06 is live, served by GraphQL API version 26.6.3 as of 28 August 2026.

**Access.** Web interface at platform.opentargets.org; keyless GraphQL at `https://api.platform.opentargets.org/api/v4/graphql` — e.g. `{target(ensemblId:"ENSG00000169083"){approvedSymbol biotype}}` returns AR / protein_coding. Whole releases download as Parquet from the EMBL-EBI FTP under /pub/databases/opentargets/platform/ and are mirrored for BigQuery.

**Caveats.** Association scores are an automated prioritisation heuristic, not evidence of causality, and they move between releases — pin the release version in any analysis you publish. The legacy REST API was retired in favour of GraphQL, so old tutorials and the `opentargets` pip client will not work. Licensing follows the constituent data sources; check per-source terms before redistributing.

### [openFDA](https://open.fda.gov/)

`Free` · beginner 4/5 · drug, device and food safety data

Elasticsearch-backed API over FDA public datasets: adverse event reports (FAERS), drug labelling, the NDC directory, recalls and enforcement, device adverse events (MAUDE), 510(k) and PMA clearances, and food enforcement. Responses carry a metadata block giving the data's last-update date.

**Access.** Keyless HTTPS GET, e.g. `https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:"metformin"&count=patient.reaction.reactionmeddrapt.exact`. Add `api_key=` for higher limits. Quarterly bulk JSON downloads are also published.

**Caveats.** Without a key: 240 requests per minute and 1,000 per day, per IP. With a free email-issued key: 240 per minute and 120,000 per day. FAERS is spontaneous-report data — no denominators, heavy reporting bias, and FDA states results are unvalidated; disproportionality signals are hypothesis-generating only.

### [OpenPrescribing](https://openprescribing.net/)

`Free` · beginner 4/5 · prescribing and pharmacoepidemiology

Search and analysis interface over the English Prescribing Dataset published monthly by the NHS Business Services Authority, covering every item dispensed in NHS primary care in England, aggregated by practice, PCN, Sub-ICB Location, ICB and region. Built by the Bennett Institute for Applied Data Science, University of Oxford.

**Access.** Web 'Analyse' tool for charts and maps; open REST API under `https://openprescribing.net/api/1.0/` (spending, spending_by_org, bnf_code, org_code endpoints, `format=json` or `csv`). Code is MIT-licensed at github.com/ebmdatalab/openprescribing.

**Caveats.** England only — Scotland, Wales and Northern Ireland publish separately. Source data are under the Open Government Licence; attribute OpenPrescribing and the NHS BSA. Denominators are practice list sizes, not exposed populations, so raw comparisons need standardisation. The site sits behind a bot filter, so scripted access can be challenged.

### [PhysioNet](https://physionet.org/)

`Free` · beginner 4/5 · clinical and physiological signal archive

MIT-run archive of 428 clinical and physiological datasets as of August 2026, split across four access tiers: 232 open, 45 restricted (data use agreement only), 139 credentialed, 12 contributor-review. Content ranges from single-subject ECG recordings to full ICU electronic health records.

**Access.** Web interface with per-project download pages; every project also exposes a plain wget/rsync mirror (e.g. `wget -r -N -c -np https://physionet.org/files/<project>/<version>/`). Python: `pip install wfdb` then `wfdb.rdrecord('100', pn_dir='mitdb')` streams open records without downloading.

**Caveats.** Only the 232 open projects need no account. Restricted projects need a free login plus a signed DUA; credentialed projects (including MIMIC and eICU) need identity verification and human-research training — see the CITI Program entry in this file. Credentialing review is manual and can take days to weeks.

*Also listed under: neuro-psych.*

### [RxNav and the RxNorm APIs](https://lhncbc.nlm.nih.gov/RxNav/APIs/index.html)

`Free` · beginner 4/5 · drug terminology and normalisation

NLM's public APIs over RxNorm (normalised clinical drug names with ingredient, brand and dose-form relationships), RxTerms, the Prescribable subset, and RxClass (ATC, MeSH pharmacologic action and other class systems). The standard tool for mapping free-text medication strings to codes.

**Access.** Keyless REST, e.g. `https://rxnav.nlm.nih.gov/REST/rxcui.json?name=metformin`, `.../REST/rxcui/6809/allrelated.json`, `.../REST/rxclass/classMembers.json?classId=C0004096&relaSource=MEDRT`. RxMix runs batch jobs; RxNav-in-a-Box runs the whole stack locally in Docker for unlimited querying.

**Caveats.** RxNorm itself is free of UMLS licence restrictions and may be redistributed, but RxNorm files that bundle restricted source vocabularies, and the full UMLS, require a UMLS licence. NLM asks for rate-limited use (about 20 requests per second per IP) — use RxNav-in-a-Box for heavy workloads. The NLM Drug Interaction API has been retired, so do not build on it.

### [SEER Cancer Data](https://seer.cancer.gov/data/)

`Free (registration), application` · beginner 2/5 · population-based cancer registry

NCI's population-based cancer incidence and survival data from US registries, with tumour characteristics, stage, treatment summary and follow-up, delivered through the SEER*Stat client. Two products: SEER Research Data (lighter) and SEER Research Plus (additional variables).

**Access.** Apply through the SEER Data Request System, then download the database and analyse it in the free SEER*Stat desktop application (Windows; runs under Wine). R: `install.packages('SEER2R')`, or read exported ASCII with the supplied dictionaries.

**Caveats.** Read the tiering carefully. SEER Research Plus and NCCR require authentication with an eRA Commons or HHS account that must then be linked to a Login.gov account, plus a non-free-mail institutional email address — closed in practice to unaffiliated researchers, and requests from gmail/icloud addresses are rejected. SEER's own instructions state that if you cannot obtain an eRA Commons account, are requesting data for personal use, or do not need the extra Research Plus variables, you can register for SEER Research Data instead — that is the route for independents, and its access policy was updated on 13 June 2025. Since 4 April 2025 NIH prohibits access to SEER Research Plus and NCCR data by users located in countries of concern.

### [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/)

`Free` · beginner 3/5 · medical imaging archive

NCI-funded DICOM archive; the public NBIA API lists 156 collections as of August 2026, spanning CT, MR, PET, mammography and digital histopathology, with linked clinical, genomic and expert-annotation files. Large single collections include NLST at 26,254 subjects.

**Access.** Browse and download via the Radiology or Histopathology search portals plus the NBIA Data Retriever desktop client for bulk .tcia manifests. Programmatic: REST at `https://services.cancerimagingarchive.net/nbia-api/services/v1/` (e.g. `getCollectionValues`, `getSeries?Collection=...`) with no key for public collections; `pip install tcia_utils` wraps it.

**Caveats.** Most collections are open under Creative Commons licences and need no login, but a minority are marked 'Limited' and require a signed request. Licences vary per collection — check the collection page before redistributing derivatives. Downloads are large: a single collection can run to hundreds of GB, so plan disk and bandwidth.

### [The DHS Program](https://dhsprogram.com/)

`Free (registration), application` · beginner 3/5 · LMIC household health surveys

USAID-funded Demographic and Health Surveys: nationally representative household surveys run in over 90 low- and middle-income countries since 1984, covering fertility, family planning, child and maternal mortality, nutrition, anthropometry, malaria, HIV biomarkers and health service use, with GPS cluster files.

**Access.** Register a project, state your research question, and receive dataset download rights in Stata, SPSS, SAS and flat formats. Aggregate indicators need no login through STATcompiler and the keyless DHS API (`https://api.dhsprogram.com/rest/dhs/data?countryIds=KE&indicatorIds=...`). R: `install.packages('rdhs')`.

**Caveats.** Microdata access is per-project and per-country: you must describe your study and request each country's files, and approval is manual, usually taking days. GPS files require a separate request. Redistribution of microdata is prohibited. Surveys use complex multi-stage designs, so weights and clustering are mandatory in analysis.

### [UMLS Metathesaurus](https://www.nlm.nih.gov/research/umls/index.html)

`Free (registration), api-key` · beginner 2/5 · biomedical terminology

NLM's integration of over 200 biomedical vocabularies — SNOMED CT, ICD-10-CM, LOINC, MeSH, RxNorm, CPT and others — into shared concept identifiers with synonymy and relationship tables. The current release is 2026AA, and precomputed subsets are offered that need no MetamorphoSys build.

**Access.** Obtain a free UMLS Terminology Services licence, then download the full release or a precomputed subset, or query the UTS REST API with your key: `https://uts-ws.nlm.nih.gov/rest/search/current?string=myocardial+infarction&apiKey=...`. Python: `pip install quickumls` for local concept extraction.

**Caveats.** The licence is free and open to individuals worldwide, but it is a real agreement with per-source restrictions — some constituent vocabularies (notably CPT) restrict redistribution and some restrict use outside certain countries. A UMLS licence also delivers SNOMED CT to users in SNOMED International member countries, which is a far simpler route than licensing SNOMED separately. Annual re-affirmation of the licence is required.

### [Vivli](https://vivli.org/)

`Free (registration), application` · beginner 2/5 · individual participant data from clinical trials

Global platform for sharing anonymised individual participant data from completed clinical trials, including industry-sponsored trials. Platform metrics dated 30 June 2026: 8,644 studies listed for sharing, 6.36 million participants, 142 countries, 59 data contributors, 2,048 data requests submitted and 991 approved.

**Access.** Search the study catalogue free at search.vivli.org without an account. To obtain data, register, submit a research proposal with a statistical analysis plan, sign the data use agreement, and analyse inside the Vivli secure research environment. Disease-specific portals exist for antimicrobial resistance (amr.vivli.org) and HIV.

**Caveats.** Genuinely gated: requests are reviewed by the data contributor or an independent review panel, review takes weeks to months, and rejection is common — 248 requests denied and 809 withdrawn against 991 approved as of June 2026. Data cannot be downloaded; all analysis happens inside the walled environment. Treat Vivli's own FAQ as the authority on any charges for the research environment rather than assuming there are none, and expect to name a statistician and an institutional affiliation.

### [WHO Global Health Observatory](https://www.who.int/data/gho)

`Free` · beginner 4/5 · global health indicators

WHO's official indicator repository, exposing 3,095 indicators as of August 2026 covering mortality, disease burden, health systems, immunisation, risk factors and the SDG health targets, mostly disaggregated by country and year.

**Access.** Keyless OData API: list indicators at `https://ghoapi.azureedge.net/api/Indicator`, then pull values with `https://ghoapi.azureedge.net/api/<IndicatorCode>`. R: `install.packages('rgho')`. CSV export from the web data pages.

**Caveats.** Indicator codes are opaque and inconsistently documented; expect to grep the Indicator list first. Many indicators are WHO model estimates rather than raw country reports, and country coverage is uneven — read the indicator metadata before comparing across countries.

### [WHO ICTRP Search Portal](https://trialsearch.who.int/)

`Free` · beginner 3/5 · clinical trial registry federation

WHO's federated search across the recognised primary trial registries — ClinicalTrials.gov plus ANZCTR, ChiCTR, CTRI, ISRCTN, IRCT, jRCT, PACTR, REBEC and others — so trials registered outside the United States appear in one query. Searching registries beyond ClinicalTrials.gov is expected by Cochrane MECIR and by PRISMA-S.

**Access.** Web search and Advanced Search at trialsearch.who.int, with result-set export; the registry network, the WHO Trial Registration Data Set and the Universal Trial Number application are documented at who.int/clinical-trials-registry-platform. Bulk access to the full ICTRP data set is arranged through those WHO pages rather than an open API.

**Caveats.** An ageing ASP.NET application with awkward paging and no modern REST API, so large harvests are painful; plan on the WHO data-set route instead of scraping. Records are supplied by member registries, so completeness, language and update frequency vary widely, and the same trial registered in two registries appears twice and must be deduplicated by hand. It indexes registrations, not results.

## Software

### [3D Slicer](https://www.slicer.org/)

`Free` · beginner 3/5 · medical image visualisation and segmentation

Cross-platform desktop application for medical image computing — DICOM import, multiplanar and 3D rendering, manual and semi-automatic segmentation, registration, quantification and surgical planning — extended by an extension manager carrying hundreds of community modules. Developed under NIH grants for nearly two decades.

**Access.** Direct download of prebuilt binaries for Windows, macOS and Linux from download.slicer.org. Scripting through the built-in Python console (`slicer.util.loadVolume(...)`); headless batch processing via `Slicer --no-main-window --python-script`. Source on GitHub under a BSD-style licence permitting commercial use.

**Caveats.** Free and open with no institutional gate, but it is a heavy application: expect 8 GB RAM as a floor and much more for large CT volumes, plus a real learning curve on the segmentation workflow. Explicitly not cleared for clinical diagnosis — research use only.

### [ASReview](https://asreview.ai/)

`Free` · beginner 3/5 · systematic review screening

Open-source active-learning tool for title and abstract screening in systematic reviews: you label records, a classifier reorders the remaining queue, and relevant records surface far earlier than in random order. Version 3.0.8, Apache-2.0, from Utrecht University.

**Access.** `pip install asreview` then `asreview lab` opens a local web app in your browser; import a RIS, CSV or BibTeX export from PubMed, Embase or Europe PMC, mark a few known-relevant and known-irrelevant records to prime the model, and screen. `asreview simulate` benchmarks stopping rules against an already-labelled dataset.

**Caveats.** Runs entirely on your own machine with no account and no upload of your data, which is a real advantage over cloud screening tools for sensitive or unpublished datasets. It reorders screening but does not decide when to stop, and stopping criteria remain a live methodological debate. Journals and Cochrane may require you to justify machine-assisted screening in your methods.

### [DHIS2](https://dhis2.org/)

`Free` · beginner 3/5 · health management information system

Free open-source (BSD 3-clause) web platform for routine health information: aggregate reporting, individual-level tracker programmes, dashboards, maps and metadata exchange. Coordinated by the HISP Centre at the University of Oslo and used by more than 80 low- and middle-income country governments as the national health data system, and in over 100 countries counting NGO programmes.

**Access.** Explore the live public demo at play.dhis2.org before installing anything. Self-host with the official Docker images; everything is reachable through the Web API (`/api/analytics`, `/api/dataValueSets`, `/api/trackedEntityInstances`). Documentation at docs.dhis2.org, free courses at academy.dhis2.org, and a very active forum at community.dhis2.org.

**Caveats.** The software is free; the data usually are not yours. In most countries a DHIS2 instance holds ministry-owned routine data, so a researcher needs a formal data request to the ministry rather than a login. Running an instance is a real systems job (PostgreSQL tuning, Java, scheduled analytics table generation). Routine service data carry well-known biases — incomplete facility reporting, unreliable denominators — and are not a substitute for survey data such as DHS.

### [Epi Info](https://www.cdc.gov/epiinfo/index.html)

`Free` · beginner 4/5 · field epidemiology (discontinued)

CDC's public-domain suite for outbreak investigation and field epidemiology — form design, data entry, epidemiological statistics, maps and graphs — long used where there is no statistician and no licence budget. CDC discontinued product development and technical assistance in September 2025; the desktop version still ran on Windows 11 as of that date.

**Access.** Download the last Windows desktop release from the CDC page; the full user guide is archived at archive.cdc.gov/www_cdc_gov/epiinfo/pdfs/userguide/EI7Full.pdf.

**Caveats.** Included because it remains in wide use and because its discontinuation is not yet widely known — plan a migration rather than a new dependency. No further bug fixes, security patches or support, and no guarantee it survives future Windows releases. For new work prefer R with the Epidemiologist R Handbook, or KoboToolbox/ODK for form-based field collection. OpenEpi (openepi.com) still works for quick 2x2 and sample-size calculations but has not been updated since 2013.

### [ITK-SNAP](https://www.itksnap.org/)

`Free` · beginner 4/5 · 3D image segmentation

Focused desktop tool for manual and semi-automatic segmentation of 3D medical images, with active-contour propagation and, since version 4.4.0 released in September 2025, integrated AI-based segmentation. It does one job well and is far lighter than a full imaging platform.

**Access.** Direct download of installers for Windows, macOS and Linux; the command-line companion Convert3D (`c3d`) handles format conversion and batch operations on NIfTI, NRRD and DICOM.

**Caveats.** Open source under the GPL and free for any use, but with a far narrower feature set than 3D Slicer — no registration pipelines, no extension ecosystem. The best first tool for a student who needs to produce reliable manual ground-truth masks on a laptop. Research use only.

### [jamovi](https://www.jamovi.org/)

`Free` · beginner 5/5 · point-and-click statistics

Free open-source statistics application built on R with a spreadsheet interface: descriptives, t-tests, ANOVA, linear and logistic regression, factor analysis, and add-on modules for survival analysis, meta-analysis (MAJOR) and medical diagnostic-accuracy work (ClinicoPath). Current release 2.7.34. Every analysis can display the underlying R syntax, so work started by clicking can be reproduced in code.

**Access.** Direct download for Windows, macOS, Linux (flatpak) and ChromeOS from jamovi.org/download.html; install add-ons from the in-app jamovi library. The `Rj` module runs arbitrary R inside a jamovi session against the open data set.

**Caveats.** The desktop application is free and open source (AGPL); the hosted jamovi Cloud option is priced separately, so check its current terms before relying on it. This is the realistic SPSS replacement for clinicians and students with no licence budget, but it is not a scripted pipeline: complex survey weights, multilevel models and reproducible reporting are still better done directly in R. Community-maintained modules vary in quality and update rate.

### [KoboToolbox](https://www.kobotoolbox.org/)

`Free tier, email` · beginner 4/5 · field data collection

Open-source XLSForm/ODK-based data collection platform designed for humanitarian and low-connectivity settings: offline Android collection, skip logic, GPS and media capture, multi-language forms, and browser-based tables, maps and exports. The free Community plan gives non-profit users 5,000 submissions per month and 1 GB of file storage; the entry free tier is 1,000 submissions per month, and paid Starter is $25 per month ($21 billed annually).

**Access.** Create an account on a hosted server (kf.kobotoolbox.org or the EU server), build a form in the browser or upload an XLSForm, collect via the KoboCollect Android app or a web form, and export to XLSX, CSV or SPSS. REST API under `/api/v2/` for programmatic export; R: `install.packages('robotoolbox')` (1.6.2) with an API token from account settings. Self-hosting with Docker is supported.

**Caveats.** The honest alternative to REDCap for someone with no institutional server, and named as such in the REDCap entry — but it is not equivalent: there is no 21 CFR Part 11 validated audit trail, so it is not the right tool for a regulated interventional trial. Data sit on a third-party server, so check your ethics approval and any data use agreement before collecting identifiable clinical data. Submission and storage caps are per account, and exceeding them blocks new submissions.

### [metafor and meta (R meta-analysis)](https://cran.r-project.org/package=metafor)

`Free` · beginner 3/5 · meta-analysis

The two standard R packages for meta-analysis in medicine: metafor 5.0-1 for the general random- and mixed-effects framework (rma.uni, rma.mv, meta-regression, network meta-analysis, publication-bias diagnostics) and meta 8.5-0 for the clinical-trial-shaped interface (metabin, metacont, forest and funnel plots). Both are GPL.

**Access.** `install.packages(c('metafor','meta','robvis'))`. Typical path: `m <- meta::metabin(e.e, n.e, e.c, n.c, data=d, sm='RR', method.tau='REML'); forest(m)`; drop to `metafor::rma()` for anything unusual. robvis 0.3.1 turns a RoB 2 or ROBINS-I assessment table into publication-ready traffic-light plots.

**Caveats.** Free, offline and reproducible — a genuine substitute for RevMan and for commercial meta-analysis packages, and the combination most Cochrane-adjacent methodologists actually use. The hard part is not the software but the model choice (fixed versus random effects, tau estimator, small-study corrections); pair it with chapter 10 of the Cochrane Handbook rather than reading the vignettes alone.

### [MONAI](https://github.com/Project-MONAI/MONAI)

`Free` · beginner 3/5 · deep learning for medical imaging

PyTorch-based framework for healthcare imaging AI: domain-specific transforms (intensity, spatial, DICOM- and NIfTI-aware), medical network architectures (UNet, UNETR, SwinUNETR), sliding-window inference, and losses and metrics such as Dice and Hausdorff distance. Version 1.6.0 was released on 11 June 2026 under Apache-2.0.

**Access.** `pip install monai[all]`, then e.g. `from monai.networks.nets import UNet` and `from monai.transforms import Compose, LoadImaged, ScaleIntensityd`. MONAI Label plugs interactive AI annotation into 3D Slicer, QuPath and OHIF; MONAI Bundles ship pretrained models.

**Caveats.** The project's own domain is broken: monai.io, www.monai.io and docs.monai.io all failed to resolve in DNS on 28 August 2026. Working entry points are the GitHub repository, the documentation at https://monai.readthedocs.io/en/stable/ (HTTP 200) and the project site now advertised by the repo, https://project-monai.github.io/. The code is actively maintained — v1.6.0 was tagged 11 June 2026 and the repo was last pushed 26 August 2026. Training 3D models needs a GPU with substantial VRAM — 2D slice models or MedMNIST are the realistic starting point on a free tier. For plain segmentation baselines, nnU-Net (github.com/MIC-DKFZ/nnUNet, Apache-2.0) remains the reference implementation.

### [OHDSI and the OMOP Common Data Model](https://www.ohdsi.org/)

`Free, email` · beginner 2/5 · observational health data standard and analytics stack

Open community standard for representing observational health data (the OMOP CDM) plus an open-source analytics stack: ATLAS v2.15.0 for cohort definition and characterisation, the HADES R packages (CohortMethod, SelfControlledCaseSeries, PatientLevelPrediction, FeatureExtraction) and the standardised Athena vocabularies.

**Access.** Run ATLAS and WebAPI locally with the Broadsea Docker distribution, or install the R side directly (`remotes::install_github('OHDSI/CohortMethod')`) against a CDM in PostgreSQL or DuckDB. Download vocabularies free at athena.ohdsi.org. The full textbook, The Book of OHDSI, is free at ohdsi.github.io/TheBookOfOhdsi/.

**Caveats.** The software and standards are free and Apache-licensed; what is not free is patient data — you supply your own CDM instance, or work with Eunomia, the small synthetic OMOP dataset (`remotes::install_github('OHDSI/Eunomia')`), which is the realistic entry point without a data partner. Athena downloads that include CPT4 require a UMLS licence key. Standing up ATLAS is a multi-day systems task.

### [Polyglot Search Translator (Systematic Review Accelerator)](https://polyglot.sr-accelerator.com/)

`Free` · beginner 5/5 · systematic review search translation

Free tool from Bond University's Institute for Evidence-Based Healthcare that translates a search string between database syntaxes — PubMed, Ovid MEDLINE, Embase, Cochrane CENTRAL, Web of Science, CINAHL, Scopus and others — preserving field tags, truncation and line references, with built-in RCT and systematic-review filters.

**Access.** Paste a PubMed or Ovid MEDLINE query into the box at polyglot.sr-accelerator.com and copy the translation per database; it runs in the browser with no account. Sibling Systematic Review Accelerator tools (Deduplicator, SearchRefinery, Word Frequency Analyser) have moved to the Evidence Research Accelerator at tera-tools.com.

**Caveats.** Bond states Polyglot stays at the old address while the rest of the Systematic Review Accelerator migrated to TERA, which does need an account; tera-tools.com served a 'Site down for maintenance' page on 28 August 2026, so do not make it a critical dependency yet. Translations are a strong first draft only: MeSH and Emtree headings are not semantically mapped and must be reworked by hand, and the search still needs PRESS-style peer review.

### [QuPath](https://qupath.github.io/)

`Free` · beginner 3/5 · digital pathology image analysis

Open-source desktop application for whole-slide and tissue image analysis: reads vendor slide formats through Bio-Formats and OpenSlide, does cell and nucleus detection, stain (H-DAB) deconvolution, tissue and object classification, TMA dearraying and positive-cell scoring. Version 0.7.0 was released on 2 March 2026 under the GPLv3.

**Access.** Direct download of installers for Windows, macOS and Linux from qupath.github.io. Batch work is scripted in the built-in Groovy editor and applied with 'Run for project'; a command-line `script` entry point runs the same scripts headlessly. StarDist and Cellpose extensions plug in deep-learning segmentation, and MONAI Label can drive interactive annotation.

**Caveats.** Fills the obvious hole in a CT/MRI-centric toolchain — 3D Slicer and ITK-SNAP do not handle whole-slide pathology at all. Slides are commonly 1-10 GB each, so disk, RAM and tile-cache settings are the real constraint. Scripting is Groovy rather than Python, which surprises people arriving from a Python stack. Research use only, not a diagnostic device.

### [Rayyan](https://www.rayyan.ai/)

`Freemium, email` · beginner 5/5 · collaborative review screening

Hosted collaborative screening platform for systematic reviews with blinded dual screening, conflict resolution, duplicate detection, labels and AI relevance predictions. The free tier allows 3 active reviews, 2 invited reviewers and 1 sample.

**Access.** Web app plus mobile apps; import RIS, EndNote or CSV exports, invite a co-screener, screen blinded and resolve conflicts. Stated user base of over 1 million researchers across 20,000+ institutions.

**Caveats.** The free tier covers a typical two-person student review, but PRISMA flow-diagram generation, automatic duplicate resolution, unlimited mobile use and more than 2 reviewers require the paid Essential plan or higher. Essential is $4.99 per seat per month billed annually, or $8.33 per month billed quarterly, and raises the free-reviewer allowance from 2 to 5. Your records are uploaded to a third-party service — check that this is acceptable for unpublished or sensitive datasets, and prefer ASReview if not.

### [REDCap](https://project-redcap.org/)

`Free tier, application` · beginner 3/5 · clinical data capture

Vanderbilt-developed web application for building study databases and surveys, with audit trails, branching logic, data dictionaries, e-consent and a 21 CFR Part 11 module. In use at 8,404 institutions across 166 countries, hosting 2.8 million projects and 4.5 million users.

**Access.** Not installable by an individual: REDCap is server software that your organisation's IT staff must license and install, after which you use it in a browser. Programmatic access to your own project is via its REST API — R: `install.packages('REDCapR')`; Python: `pip install PyCap`.

**Caveats.** The most honestly institutional entry in this file. The licence is free to non-profit organisations, but it is granted to the organisation rather than the person and requires a server, a database administrator and ongoing maintenance; cloud providers are explicitly barred from supporting your instance. An unaffiliated researcher cannot realistically obtain or run REDCap — practical free alternatives are KoboToolbox (free hosted tier, humanitarian and field data collection) or self-hosted LimeSurvey Community Edition.

### [TotalSegmentator](https://github.com/wasserth/TotalSegmentator)

`Free` · beginner 4/5 · pretrained anatomical segmentation

Command-line tool and pretrained models that segment 117 anatomical structures in CT — organs, bones, muscles and vessels — with additional MR and specialised task models. Version 2.18.0, Apache-2.0 licensed, built on nnU-Net.

**Access.** `pip install TotalSegmentator`, then `TotalSegmentator -i ct.nii.gz -o segmentations/`; add `--fast` for a lower-resolution CPU-friendly pass and `--roi_subset liver spleen` to limit output. Also available as a 3D Slicer extension and a Docker image.

**Caveats.** Model weights download automatically on first run and run to several GB. Full-resolution inference wants a GPU; `--fast` runs on CPU in minutes per scan. Trained mainly on adult CT, so performance degrades on paediatric scans, unusual protocols and heavy pathology — always inspect the masks. Research use only, not a diagnostic device.

## Literature

### [Cochrane Library](https://www.cochranelibrary.com/en/help/access)

`Free tier` · beginner 4/5 · systematic reviews and trial register

Home of the Cochrane Database of Systematic Reviews and CENTRAL, the largest curated register of controlled trial reports. Abstracts, plain language summaries and CENTRAL records are readable worldwide; full reviews are gated, but with unusually wide free provision.

**Access.** Search the web interface directly. Free full text arrives by one of three routes: national funded provision, where residents of the UK, Ireland, Denmark, Finland, Spain, Brazil, Ecuador, South Africa, Malaysia, Australia and several Canadian provinces get one-click access by IP; one-click free access by IP recognition in over 100 low- and middle-income countries and territories; or green open access, under which every Cochrane review becomes free 12 months after publication.

**Caveats.** Access is decided by IP address, so a VPN endpoint in the wrong country silently costs you access. Reviews published in the last 12 months outside a provision country are paywalled; gold open access costs authors $5,100 per review. CENTRAL search results are free everywhere and are the fastest way to assemble a trial list even without full text.

### [Europe PMC](https://europepmc.org/)

`Free` · beginner 4/5 · full-text repository and API

EMBL-EBI's biomedical literature service holding 48,779,933 records as of August 2026 — PubMed and PMC content plus preprints, patents, NHS and NICE guidelines, theses and agricultural literature — with full-text search, citation networks, grant linkage and text-mined annotations.

**Access.** Keyless REST API: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22sepsis%20bundle%22&format=json&pageSize=100`, with `cursorMark` paging for large harvests and `/fullTextXML` for open-access articles. R: `install.packages('europepmc')`. OAI-PMH and annotations APIs are also offered.

**Caveats.** The most practical free API for large literature harvests in medicine — no key, no daily cap, and cursor paging through the full result set. Full text is retrievable only for the open-access portion; the rest returns metadata and abstracts. Be polite with request rates.

### [medRxiv](https://www.medrxiv.org/)

`Free, email` · beginner 4/5 · preprint server

The health sciences preprint server run by Cold Spring Harbor Laboratory, BMJ and Yale. It has posted 87,955 unique preprints (109,166 versions) between its June 2019 launch and 27 August 2026, screened for plausibility and patient identifiability but not peer reviewed.

**Access.** Post free of charge through the submission portal (ORCID plus author confirmation; no fee at any stage). Read and harvest with the keyless API: `https://api.biorxiv.org/details/medrxiv/2026-08-01/2026-08-27` for date ranges, `/details/medrxiv/<DOI>` for one paper, and `/pubs/medrxiv/...` for subsequent journal publication links.

**Caveats.** The most realistic way for an unaffiliated researcher to put health research on the public record with a DOI at zero cost. Screening rejects case reports of identifiable patients and anything readable as clinical advice; trial reports should carry a registration number. Some clinical journals still treat preprinting cautiously, so check the target journal's policy first. The website blocks scripted fetches — use the API.

### [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/)

`Free` · beginner 5/5 · free full-text books and clinical reference

NLM's archive of free full-text biomedical books, reports and reference chapters, holding 1,330,418 records as of 27 August 2026. It includes StatPearls (116,932 chapters), GeneReviews, the NCBI Handbooks, AHRQ and WHO reports, and many out-of-print textbooks.

**Access.** Web reading at ncbi.nlm.nih.gov/books with no account; every chapter has a stable NBK identifier. Scriptable through the same E-utilities as PubMed with `db=books`, e.g. `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=books&term=sepsis[title]&retmode=json`.

**Caveats.** Free to read but not open licensed: publishers retain copyright on most titles, so unlike the PMC Open Access Subset you generally may not redistribute or text-mine them. Quality is uneven — StatPearls is templated point-of-care material, not a peer-reviewed review, and some deposited textbooks are a decade old with no update or retraction mechanism.

### [NICE guidance](https://www.nice.org.uk/guidance)

`Free` · beginner 4/5 · clinical guidelines and evidence reviews

The UK National Institute for Health and Care Excellence guidance library — clinical guidelines, technology appraisals, diagnostics and medtech assessments, quality standards — published free worldwide together with the underlying evidence reviews, GRADE profiles and economic models. Related free resources include Clinical Knowledge Summaries (cks.nice.org.uk) and the British National Formulary (bnf.nice.org.uk).

**Access.** Free web reading at nice.org.uk/guidance with no account; each guideline page links its full evidence review PDFs and committee papers, which are the part researchers actually want. A syndication API is offered for reusing NICE content inside other systems.

**Caveats.** Reading is free everywhere, but the content is not openly licensed: the NICE UK Open Content Licence covers reuse in UK settings only, and any international reuse needs a permission request to NICE — so do not treat guideline text or figures as reusable in your own publication. Some BNF content is restricted by UK access checks. Guidance is written for the English NHS, and its thresholds and cost-effectiveness assumptions do not transfer directly to other health systems.

### [OpenAlex](https://openalex.org/)

`Free` · beginner 4/5 · open bibliographic index and API

Fully open scholarly index from OurResearch (the Unpaywall team) holding 322,147,582 works as of 28 August 2026, with authors, institutions, funders, topics, citation links and open-access status. It replaced Microsoft Academic Graph and is the practical free stand-in for Scopus or Web of Science in bibliometrics and citation searching.

**Access.** Keyless REST API: `https://api.openalex.org/works?filter=title.search:sepsis,publication_year:2026&per-page=200&mailto=you@example.org`, with cursor paging for full result sets. Python: `pip install pyalex`. Complete monthly snapshots are on AWS S3 (s3://openalex) under CC0.

**Caveats.** No key and no account, but adding `mailto=` puts you in the faster 'polite pool' and is expected of anything more than casual use; large harvests should take the S3 snapshot rather than hammer the API. Coverage is broader but noisier than PubMed — no MeSH indexing, real author-disambiguation errors, and preprint-plus-journal versions that are not always merged — so it complements rather than replaces PubMed for clinical searching.

### [PubMed and the NCBI E-utilities](https://pubmed.ncbi.nlm.nih.gov/)

`Free` · beginner 5/5 · bibliographic database

NLM's index of biomedical literature holding 41,074,375 records as of 27 August 2026, with MeSH indexing, publication-type filters and structured abstracts. The E-utilities expose the same index as a scriptable API, which is what makes systematic searching reproducible.

**Access.** Web search at pubmed.ncbi.nlm.nih.gov; API at `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=...&retmode=json`, then `efetch.fcgi` for the records. Python: `pip install biopython` and use `Bio.Entrez`. R: `install.packages('easyPubMed')`. The annual MEDLINE baseline plus daily updates are downloadable by FTP.

**Caveats.** Without an API key you get 3 requests per second per IP; a free NCBI account key raises it to 10 per second. PubMed indexes citations, not full text — a large share of records link only to a paywalled publisher page. Use the Advanced Builder and save the exact query string; MeSH indexing lags publication by months for new records.

### [PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/)

`Free` · beginner 5/5 · full-text repository

NLM's free full-text archive of biomedical and life sciences journal articles, holding 12,559,759 records as of 27 August 2026. The Open Access Subset within it carries machine-readable licences permitting text mining and redistribution.

**Access.** Web reading and search; Open Access Subset bulk download by FTP or AWS S3 as JATS XML or .txt packages, listed at pmc.ncbi.nlm.nih.gov/tools/openftlist/. Programmatic: the OA Web Service (`https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC...`) and the E-utilities with `db=pmc`.

**Caveats.** Not everything in PMC is reusable: many articles deposited under funder public-access policies are free to read but are author-manuscript versions with all rights reserved, and only the Open Access Subset may be mined or redistributed. Some publisher deposits carry a 6-12 month embargo before appearing.

### [Research4Life (HINARI)](https://www.research4life.org/)

`Free tier, application` · beginner 3/5 · journal access for low-income countries

Partnership of WHO, FAO, UNEP, WIPO, ILO, Cornell, Yale and over 200 publishers giving eligible institutions in low- and middle-income countries access to paywalled journals, books and databases. HINARI is its health programme. Group A countries receive free access; Group B pays a low annual fee per institution.

**Access.** Institutional rather than individual: a local not-for-profit institution — university, teaching hospital, ministry, research institute or NGO — registers at research4life.org/access/register and receives credentials its staff and students then use. Group A includes most least-developed countries; current eligibility lists are published on the site.

**Caveats.** The most important literature route for researchers at poorly resourced institutions, and of no use to a genuinely unaffiliated one: there is no individual sign-up. Eligibility is revised annually against GNI, GNI per capita, LDC status, HDI and healthy life expectancy, and countries do graduate off the lists. Content varies by programme and by publisher opt-in — not every journal is available in every country.

### [Unpaywall](https://unpaywall.org/products/api)

`Free, email` · beginner 5/5 · legal open-access locator

Index of legally posted open-access copies of scholarly articles, harvested from publisher sites, PMC and institutional and preprint repositories, keyed by DOI. It is the legal alternative to shadow libraries and the engine behind many library link resolvers.

**Access.** Keyless API using your own email as the identifier: `https://api.unpaywall.org/v2/10.1136/bmj.n71?email=you@example.com` returns `is_oa`, `best_oa_location.url_for_pdf` and every located copy. Browser extensions for Chrome and Firefox add a green tab on paywalled pages. Full database snapshots are available for bulk use.

**Caveats.** You must pass a real address in the `email` parameter or the API returns HTTP 422. Roughly 100,000 calls per day is the stated soft limit; heavy users should take the data dump. It finds only copies that authors or publishers actually posted, so a large share of clinical literature returns is_oa=false — that is an accurate answer, not a failure.

## Compute

### [Google Colab](https://colab.research.google.com/)

`Free tier, email` · beginner 5/5 · hosted notebooks with GPU

Hosted Jupyter notebook service with free-of-charge access to CPU, GPU and TPU runtimes and no setup. In medical work it is the standard way to run MONAI, TotalSegmentator in `--fast` mode, MedMNIST training and pandas analysis of open clinical datasets without owning a GPU.

**Access.** Sign in with a Google account and open a notebook; `!pip install monai medmnist` at the top, mount Google Drive for persistence, and pick a GPU runtime under Runtime > Change runtime type.

**Caveats.** Google states explicitly that free resources are neither guaranteed nor unlimited and that usage limits fluctuate; idle sessions are reclaimed and long training runs will be interrupted, so checkpoint to Drive constantly. Do not upload credentialed clinical data (MIMIC, SEER, DHS microdata) to Colab without checking the data use agreement — most forbid transfer to third-party services.

### [Kaggle Notebooks](https://www.kaggle.com/code)

`Free tier, email` · beginner 5/5 · hosted notebooks with GPU quota

Free hosted notebook environment with NVIDIA Tesla P100 GPUs on a weekly quota that resets each week and is documented as 30 hours, or sometimes higher depending on demand and available resources, plus TPU access and persistent dataset storage.

**Access.** Free account, then create a notebook, toggle the accelerator in the settings panel, and attach public datasets. `pip install kaggle` gives a CLI for pushing notebook versions and downloading datasets without an interactive session.

**Caveats.** The quota is per week and shared across sessions, so forgotten interactive sessions and duplicate batch commits burn it quickly; interactive sessions idle out after 60 minutes. Better than Colab when you need a predictable weekly budget rather than best-effort allocation. The same caution applies: credentialed clinical data generally may not be uploaded.

### [NIH Cloud Lab](https://cloud.nih.gov/resources/cloudlab/)

`Free tier, application` · beginner 3/5 · cloud credits and training

NIH STRIDES programme giving eligible researchers up to 90 days of access to an AWS, Google Cloud or Azure account with $500 of credits, plus interactive tutorials and public biomedical datasets, inside an NIH-approved environment with no risk of overspending.

**Access.** Complete the Cloud Lab account request form on the NIH STRIDES site, choose a cloud provider, and receive login instructions within a few days of approval.

**Caveats.** Eligibility is the gate: NIH employees and contractors, NIH-affiliated researchers and students, and — relevant to this audience — researchers without an active NIH award who are currently seeking NIH funding may be eligible on enquiry. Genuinely unaffiliated researchers with no NIH connection are unlikely to qualify. Access ends at 90 days or $500, whichever comes first; it is a learning programme, not a production allocation.

## Publishing

### [African Journals OnLine (AJOL)](https://www.ajol.info/)

`Free tier` · beginner 4/5 · regional open-access publishing platform

The largest online collection of African-published peer-reviewed scholarly journals, with dedicated Health, Veterinary Science and Psychology/Psychiatry categories and browsing by roughly 30 African countries. Hosting, DOIs and discovery are provided to journals at no cost to them.

**Access.** Read abstracts and, for open-access titles, full text free at ajol.info; the platform is OJS-based with per-journal submission portals. To publish, submit directly to a hosted journal — APC policies vary and many charge nothing or only a nominal handling fee.

**Caveats.** A mixture of fully open access and subscription or request-a-copy titles; the article page states which. Journal quality varies widely across the platform, so check editorial board, described peer review process and indexing status. For African clinical and public health work this is often where the regionally relevant literature actually lives, and PubMed covers it poorly.

### [Directory of Open Access Journals (DOAJ)](https://doaj.org/)

`Free` · beginner 4/5 · no-APC journal finder

Curated index of 23,371 vetted open access journals and 13.5 million articles as of August 2026. Decisively for authors without grant money, 14,658 of those journals charge no article processing charge at all, and 2,658 indexed journals sit under the Medicine subject heading.

**Access.** Web search with facets for subject, language, licence and 'without APCs'. Keyless API: `https://doaj.org/api/search/journals/bibjson.apc.has_apc%3Afalse%20AND%20bibjson.subject.term%3A%22Medicine%22?pageSize=50` returns candidate diamond open-access venues as JSON.

**Caveats.** DOAJ inclusion is a basic integrity screen — real peer review, declared licensing, no deceptive practice — not a statement about impact or clinical rigour, so read a few published articles before submitting. APC fields are self-reported by publishers and can be stale; confirm on the journal's own site. Many no-APC medical journals are society- or ministry-published and slower than commercial venues.

### [Emerging Infectious Diseases (CDC)](https://wwwnc.cdc.gov/eid/)

`Free` · beginner 4/5 · diamond open-access journal

Peer-reviewed monthly journal published by the US CDC, fully open access online with no article processing charge to authors, covering emerging and re-emerging infections, outbreak investigations, surveillance, antimicrobial resistance and one-health topics. Indexed in PubMed/MEDLINE.

**Access.** Read all content free at wwwnc.cdc.gov/eid. Submit through the journal's manuscript system following the Author Instructions and the mandatory Author Checklist, both free downloads from the Author Resource Center; article types include full research articles, dispatches, research letters and photo quizzes.

**Caveats.** No fees at any stage, which makes it one of the few genuinely diamond-open-access, well-indexed venues in clinical infectious disease — but it is competitive and topically narrow. As US government work the articles are largely in the public domain. Its sibling CDC journal Preventing Chronic Disease works the same way for chronic disease and public health practice.

### [EQUATOR Network](https://www.equator-network.org/)

`Free` · beginner 5/5 · reporting guidelines

Searchable library of over 700 reporting guidelines for health research, including CONSORT and SPIRIT for trials, STROBE for observational studies, PRISMA and PRISMA-P for systematic reviews, STARD for diagnostic accuracy, TRIPOD+AI for prediction models, CARE for case reports, SQUIRE, CHEERS and ARRIVE.

**Access.** Web search by study type; each entry links the guideline paper, the checklist, and usually a fillable form and an explanation-and-elaboration document. Download the checklist before you start writing, not after.

**Caveats.** Most medical journals now require the relevant completed checklist at submission, so this is not optional advice. The site indexes guidelines rather than hosting all of them — a few link out to publisher pages that may be paywalled, though the checklists themselves are almost always free.

### [PROSPERO](https://www.crd.york.ac.uk/prospero/)

`Free, email` · beginner 4/5 · systematic review registration

International prospective register of systematic reviews, run by the Centre for Reviews and Dissemination at the University of York. Registration is free, produces a citable record with a registration number, and is expected or required by many journals and by PRISMA 2020 item 24a.

**Access.** Free web account, complete the structured registration form covering review question, eligibility criteria, search strategy outline, outcomes and planned analysis, and submit for editorial checking. Records are public and searchable, and amendments are versioned and visible.

**Caveats.** Scope is restricted to reviews with a health-related outcome; scoping reviews and reviews already past data extraction are normally rejected, so register before you screen. Editorial checking adds days to weeks. The Open Science Framework registries are the usual fallback for out-of-scope reviews.

### [SciELO](https://scielo.org/)

`Free` · beginner 4/5 · regional open-access publishing network

Latin American, Iberian and South African open-access journal network with national collections (Brazil, Argentina, Chile, Colombia, Cuba, Mexico, Peru, Spain, Portugal, South Africa and others), a dedicated Public Health collection, plus SciELO Preprints and SciELO Data.

**Access.** Read and search all collections free at scielo.org, including full text and PDFs. To publish, submit to an individual SciELO-indexed journal — the majority charge no APC because they are funded by universities, societies or research agencies. SciELO Preprints accepts health preprints in Portuguese, Spanish and English at no cost.

**Caveats.** Substantial content is in Portuguese and Spanish, which is an advantage for regional relevance and a barrier for English-only readers; many journals accept English submissions. PubMed indexing varies by journal, so check before submitting if PubMed visibility matters. APC policy is set per journal, not centrally.

## Funding

### [Elrha](https://www.elrha.org/funding/)

`Free, application` · beginner 2/5 · humanitarian health research and innovation

UK-based funder of research and innovation for humanitarian response, running the Research for Health in Humanitarian Crises (R2HC) programme and the Humanitarian Innovation Fund. Funds public health, clinical and health-systems research conducted in crisis-affected settings.

**Access.** Funding opportunities and guidance are listed at elrha.org/funding; calls specify eligible applicant types and typically require a partnership between a research team and an operational humanitarian organisation.

**Caveats.** Calls are periodic rather than rolling, and most require an academic-plus-operational consortium, so this is not a route for a lone researcher. Strong preference for teams that include researchers and organisations from crisis-affected countries. Elrha also publishes its funded research, gap analyses and toolkits openly, which is useful even if you never apply.

### [Grand Challenges (Gates Foundation)](https://grandchallenges.org/)

`Free, application` · beginner 3/5 · global health innovation grants

Family of open, recurring funding calls in global health and development run by the Gates Foundation with partner funders. The programme site reports 4,163 awarded grants across 124 countries as of August 2026, with new grant opportunities posted through the year — open calls in August 2026 included low-cost pathogen sequencing workflows, multiplex micronutrient/inflammation assays, and Keystone Symposia global health travel awards for scientists from low- and middle-income countries.

**Access.** Browse open calls at grandchallenges.org, read the specific challenge's eligibility rules and submission instructions, and submit through the online portal. Grand Challenges Explorations-style calls have historically used two-page applications with no preliminary data required.

**Caveats.** One of the few large global health funders whose calls are genuinely open to applicants anywhere and to non-traditional applicants, though most awards still require an organisation able to receive and administer funds. Eligibility, award size and whether individuals may apply vary per challenge — read the specific call, not the programme page. Calls close on fixed dates and are competitive.

### [NIH RePORTER](https://reporter.nih.gov/)

`Free` · beginner 4/5 · grant award database

Searchable database of NIH and other HHS-funded research projects with abstracts, funding amounts, principal investigators, institutions, study sections and linked publications and patents. The API returned 76,271 projects for fiscal year 2025.

**Access.** Web search at reporter.nih.gov; keyless JSON API by POST: `curl -X POST -H 'Content-Type: application/json' -d '{"criteria":{"fiscal_years":[2025]},"limit":500}' https://api.reporter.nih.gov/v2/projects/search`, with a matching `/v2/publications/search`. Annual ExPORTER bulk CSV files are also downloadable.

**Caveats.** US federal awards only — useless for mapping Wellcome, EU or LMIC funding. Its practical value to an outsider is reconnaissance: which study sections fund which topics, which principal investigators hold data you could ask for, and what funded aims actually look like. Reported amounts are fiscal-year obligations, not total project cost, and are routinely misquoted as such.

### [TDR, the WHO Special Programme for Research and Training in Tropical Diseases](https://tdr.who.int/grants)

`Free, application` · beginner 3/5 · LMIC research grants, fellowships and training

WHO-hosted programme funding research on diseases of poverty with an explicit mandate to build research capacity in low- and middle-income countries: impact research grants, a postgraduate training scheme, regional training centres, the Clinical Research Leadership fellowship, and SORT IT operational research training.

**Access.** Open calls are listed on the TDR grants pages and announced through the eTDR portal; applications are submitted online. SORT IT and the postgraduate scheme run through partner institutions in eligible regions.

**Caveats.** Eligibility for most schemes is deliberately restricted to researchers based in low- and middle-income countries — a rare case where poorly resourced applicants are favoured over well-resourced ones. Awards are modest by international standards and usually require an institutional host. Call frequency is irregular, so check the page periodically rather than expecting an annual cycle.

### [Wellcome](https://wellcome.org/research-funding)

`Free, application` · beginner 2/5 · health research grants and fellowships

Independent UK foundation funding health research worldwide across discovery research plus three priority areas — infectious disease, mental health, and climate and health — with schemes from early-career fellowships to large multi-year awards, including schemes explicitly open to researchers based in low- and middle-income countries.

**Access.** Search open schemes at wellcome.org/research-funding, check the eligibility and location rules for each, and apply through the Wellcome Funding portal.

**Caveats.** The hard gate: essentially every Wellcome scheme requires an eligible host organisation to administer the grant, so an unaffiliated individual cannot apply. Realistic for graduate students and for researchers at poorly resourced institutions, not for independents. Eligible-country lists and the scheme portfolio change between rounds — verify against the current scheme page rather than a remembered call.

## Learning

### [Causal Inference: What If](https://miguelhernan.org/whatifbook)

`Free` · beginner 2/5 · causal inference and epidemiological methods

Hernán and Robins's textbook on causal inference in three parts of increasing difficulty: causal inference without models, with models, and from complex longitudinal data (g-formula, inverse probability weighting, g-estimation, target trial emulation). Distributed free as a PDF with accompanying code and data.

**Access.** Download the book PDF, the code (R, Stata, SAS, Python) and the NHEFS example dataset from the author's page. Work the chapter exercises against NHEFS rather than reading passively.

**Caveats.** Free online only; the authors note a print version may follow, and the text is revised without full change documentation, so cite the version date. Demanding — parts II and III assume comfortable regression and some probability. It is the standard reference behind target trial emulation, now the expected framing for observational treatment-effect studies.

### [CITI Program: Data or Specimens Only Research](https://physionet.org/about/citi-course/)

`Free, email` · beginner 4/5 · human subjects research training

The human-research-protections course that unlocks credentialed access to PhysioNet datasets including MIMIC-IV and eICU. PhysioNet documents an explicit route for people with no CITI-subscribing institution, so the course can be completed at no cost.

**Access.** Create a CITI Program account, choose 'Add affiliation' and select 'Massachusetts Institute of Technology Affiliates' — an affiliation that exists specifically so non-MIT people can take this course for PhysioNet access. Answer questions 1, 2 and 3 to enrol in 'Data or Specimens Only Research', and answer Yes to Conflicts of Interest. Complete both modules, then under Records download the full training REPORT (not the certificate) and upload the report to PhysioNet.

**Caveats.** The non-obvious detail that saves money: registering on CITI as an 'independent learner' incurs a fee, whereas affiliating with MIT Affiliates does not. Use an institutional or work email address if you have one. The course takes a few hours; PhysioNet's credentialing review afterwards is separate and manual. This training satisfies PhysioNet — it is not a substitute for local IRB or ethics approval for your own study.

### [Cochrane Handbook for Systematic Reviews of Interventions](https://training.cochrane.org/handbook)

`Free` · beginner 3/5 · systematic review methodology

The reference methods text for intervention systematic reviews: question framing, searching, study selection, data collection, RoB 2 and ROBINS-I risk-of-bias assessment, meta-analysis (chapter 10), heterogeneity, subgroup analysis, reporting biases and GRADE. Readable free chapter by chapter online.

**Access.** Full current version at training.cochrane.org/handbook with no account. For a gentler start, Cochrane Evidence Essentials (training.cochrane.org/essentials) is a free introductory course on evidence-based medicine and clinical trials in English, Spanish, Russian and German.

**Caveats.** The online Handbook is free; the print edition and Cochrane Interactive Learning (the structured paid course) are not, and Cochrane's authoring platform RevMan Web is reserved for registered Cochrane review authors. The RoB 2 and GRADE tools referenced in the text are separately free but each has its own site and its own learning curve.

### [OpenWHO](https://openwho.org/)

`Free` · beginner 5/5 · public health and emergency response training

WHO's open learning platform for health emergencies, launched in 2017 and redesigned in 2025 into a resource hub of videos, slides and handouts on outbreak response, infection prevention and control, clinical management of emerging pathogens, risk communication and community engagement, in many languages and low-bandwidth formats.

**Access.** Browse learning materials by topic at openwho.org. Since the 2025 redesign the site is completely open with no registration required, and materials can be downloaded, adapted and translated.

**Caveats.** Important change: after the 2025 redesign OpenWHO no longer enrols learners in individual courses and no longer issues certificates — WHO removed registration deliberately, having found it acted as an access barrier. The site now runs as a Kaltura MediaSpace resource hub, and legacy course URLs of the form openwho.org/courses/<slug> return HTTP 404, so previously cited or bookmarked course links are dead and citations to them cannot be resolved. If you need a certificate for a job or a grant, this is no longer the route; the Global Health Network Training Centre entry in this file still issues certificates. Content is operational and emergency-focused rather than research-methods focused.

### [The Epidemiologist R Handbook](https://epirhandbook.com/)

`Free` · beginner 4/5 · applied epidemiology in R

Free online handbook by Applied Epi covering the applied epidemiology workflow in R across roughly 50 chapters: cleaning, dates, standardised rates, moving averages, outbreak detection, epidemic modelling, contact tracing, survey analysis, survival analysis, GIS, epicurves, transmission chains, reports and dashboards. Available in English, French, Spanish, Portuguese, Vietnamese, Japanese, Turkish and Russian.

**Access.** Read online at epirhandbook.com; a downloadable offline version and the example datasets are provided, so it works without reliable internet. Each chapter is copy-paste runnable against the bundled data.

**Caveats.** The book the field genuinely recommends for practising epidemiologists moving off Excel and Stata. It assumes you can install R and RStudio and does not teach statistics, so pair it with a methods text. Applied Epi sells paid courses and an R help desk, but the handbook itself has no gate.

### [The Global Health Network Training Centre](https://globalhealthtrainingcentre.tghn.org/)

`Free (registration), email` · beginner 4/5 · clinical and global health research training

Free online training in clinical research practice from The Global Health Network, a WHO Collaborating Centre based at Oxford: Good Clinical Practice, research ethics, informed consent, data management, protocol development, epidemic preparedness and site-level trial conduct, aimed at researchers in resource-limited settings.

**Access.** Register free, take short self-paced courses in the browser, and download certificates of completion. The wider Global Health Network hosts topic-specific member sites — pandemic sciences, AMR, migrant health and others — with process maps, templates and SOPs you can adapt.

**Caveats.** The most credible free GCP-style training that is not tied to a university subscription, and it does still issue certificates, which matters because commercial GCP courses are a real financial barrier for unaffiliated and LMIC researchers. Certificate recognition varies by sponsor and regulator, so confirm acceptance with your trial sponsor before relying on it.

## Community

### [3D Slicer Community (Discourse)](https://discourse.slicer.org/)

`Free, email` · beginner 4/5 · medical imaging software support

Support and development forum for 3D Slicer and its extensions, carrying over 13,000 support topics and nearly 4,000 development topics. Core developers answer routinely, often with working Python snippets.

**Access.** Free account to post; search the archive first, since most segmentation, DICOM import and scripting questions are already answered. Include your Slicer version, operating system and a minimal reproducer.

**Caveats.** The de facto help desk for open-source medical image computing generally, not just Slicer — MONAI Label, DICOM handling and segmentation workflow questions land here productively. Never post identifiable patient images; the forum is fully public and search-indexed.

### [Applied Epi Community](https://community.appliedepi.org/)

`Free, email` · beginner 4/5 · applied epidemiology Q&A

Free forum run by Applied Epi for practising epidemiologists, with categories for epi methods (surveys, sampling, surveillance, qualitative work, evaluation), R code for public health, other software (Excel, Python, DHIS2, ODK, KoboToolbox, QGIS, REDCap), mathematical modelling and genomic epidemiology.

**Access.** Free account to post; the R code category is the most active and is the natural companion to the Epidemiologist R Handbook.

**Caveats.** Smaller and slower than Stack Overflow or Cross Validated — expect hours to days for an answer rather than minutes — but replies come from people doing field epidemiology rather than statisticians answering in the abstract. Applied Epi sells a paid R Help Desk service; the forum itself is free.

### [OHDSI Forums](https://forums.ohdsi.org/)

`Free, email` · beginner 3/5 · observational health data methods forum

The working forum of the Observational Health Data Sciences and Informatics community, with active categories for implementers, developers, researchers, CDM builders and vocabulary users totalling over 7,000 topics, where the people who wrote the OMOP tools answer questions directly.

**Access.** Free Discourse account to post; read without one. Pair it with the weekly OHDSI community calls and the workgroup calendar listed on ohdsi.org, both open to anyone.

**Caveats.** Open to anyone including unaffiliated researchers, and unusually welcoming to newcomers — the 'Introduce Yourself' thread is a genuine entry point. Discussion presumes you already have or are building an OMOP CDM instance; general clinical epidemiology questions get thinner answers here than tooling and methods questions.
