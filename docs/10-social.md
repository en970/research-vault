# Social sciences

Part of [research-vault](../README.md). 87 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (37) · [Software](#software) (16) · [Literature](#literature) (12) · [Compute](#compute) (3) · [Publishing](#publishing) (5) · [Funding](#funding) (4) · [Learning](#learning) (7) · [Community](#community) (3)

## Data

### [ACLED (Armed Conflict Location & Event Data)](https://acleddata.com/data/)

`Free (registration), api-key` · beginner 3/5 · political violence and protest event data

Near-real-time, geocoded event data on political violence, protests and riots worldwide, updated weekly, with actor, event-type, location, date and fatality coding. Coverage is now global, including Europe and North America.

**Access.** Register a free myACLED account, then use the Data Export Tool, the downloadable data files, or the REST API (see https://apidocs.acleddata.com/) authenticated with your account credentials.

**Caveats.** Access terms are strict, but narrower than a blanket ban. A free myACLED account covers academic and non-commercial research, bound by the End User License Agreement, Content Usage Terms and Attribution Policy, which restrict redistribution and require specific citation. On AI (checked 28 August 2026): EULA section 7.1 prohibits using ACLED content to train, test, develop or improve ML/LLM/AI systems 'in any manner that' creates or contributes to a substitute for ACLED content or services, allows third parties to access or extract ACLED content through such systems, or exceeds your licence scope; the Content Usage Terms add that this restriction 'applies regardless of whether such use is commercial, academic, or experimental in nature'. Section 7.2 further requires attribution and technical controls preventing extraction through any tool that incorporates the content. So a research classifier trained on ACLED labels is not categorically forbidden, but it is conditioned and audit-able - read sections 7 and 10 (competitive use) before building a pipeline. ACLED reserves audit rights and can restrict or revoke access, and platforms such as CAST and the Conflict Exposure Calculator are gated separately.

### [Afrobarometer](https://www.afrobarometer.org/data/)

`Free` · beginner 5/5 · African public opinion survey

Pan-African survey network measuring attitudes to democracy, governance, the economy and public services, run in repeated rounds across roughly 40 African countries. Country files, multi-country merged round files, and geocoded subnational files are all published.

**Access.** Direct download of country and merged datasets plus codebooks from the Data pages; a free online data analysis tool gives crosstabs and country comparisons in the browser.

**Caveats.** Afrobarometer states its data are free to use; read the Data usage and access policy page, which also covers the geocoded subnational releases. Countries covered differ by round, so merged files are unbalanced panels. The online analysis tool is the fastest route if you have a weak connection or no statistical software.

### [American National Election Studies (ANES)](https://electionstudies.org/data-center/)

`Free (registration), email` · beginner 4/5 · US election survey series

Pre- and post-election surveys of US voters running since 1948, including the 2024 Time Series Study (mixed-mode: face-to-face, web, phone) and the Time Series Cumulative Data File spanning the whole series.

**Access.** Web interface: create a free account, agree to the terms, and download per-study files in Stata, SPSS, SAS or CSV with codebooks. Also analysable in the browser through SDA at Berkeley without downloading anything.

**Caveats.** Free for research and teaching, with a terms-of-use agreement at download. The cumulative file carries three sets of weights (combined, face-to-face, web) and using the wrong one is the most common beginner error - read the codebook appendix on weights first.

### [AmericasBarometer (LAPOP)](https://www.vanderbilt.edu/lapop/)

`Free` · beginner 4/5 · Latin American and Caribbean public opinion survey

Two decades of nationally representative surveys on democratic attitudes, corruption, crime victimisation, migration intentions and political participation across the Americas, covering dozens of countries and hundreds of thousands of interviews. Now published by Vanderbilt's Center for Global Democracy, which also hosts the CSES secretariat and the Seligson Archive.

**Access.** Web interface: download raw country and merged data files free from the Data Access page with no subscription, or use the browser-based Data Playground to run crosstabs and comparisons without coding. An official 'lapop' R package for design-effect-aware analysis and publication-ready graphics exists but was archived from CRAN on 22 August 2026 (undeliverable maintainer email) - install from the CRAN archive or the project's GitHub, or just use survey/srvyr.

**Caveats.** The Center states the AmericasBarometer data are 'free, unrestricted and publicly available'; it asks that you cite LAPOP and, for journal articles, link to the site and share your syntax rather than redistributing the files. A separate 'Subscriber Login' exists for partner-funded content, so a newly fielded round may reach subscribers first. Country coverage and item wording shift across rounds - check the questionnaire before pooling. Complex sample design: apply the strata, cluster and weight variables.

### [Arab Barometer](https://www.arabbarometer.org/survey-data/data-downloads/)

`Free (registration), email` · beginner 5/5 · MENA public opinion survey

Nationally representative surveys of public opinion across the Middle East and North Africa since 2006, now through Wave IX (September 2025 - May 2026, covering Egypt, Iraq, Jordan, Lebanon, Morocco, Palestine, Tunisia, Syria and Mauritania). Wave VIII (2023-2024) data are already released.

**Access.** Web interface: fill a short form with your name, email and intended use, then download SPSS/Stata datasets, questionnaires and technical reports per wave. An online analysis tool gives crosstabs in the browser.

**Caveats.** Publicly available at no charge; the form exists only so Arab Barometer can report usage. Country composition changes substantially between waves (Gulf states appear only intermittently), and some country-waves are released later than others.

### [Asian Barometer Survey (ABS)](https://www.asianbarometer.org/datar?page=d10)

`Free (registration), application` · beginner 3/5 · East and Southeast Asian public opinion survey

Cross-national survey of political values, democratic legitimacy, governance and citizen participation across East, Southeast and (in a separate series) South Asia, run in waves since 2001. All 15 country datasets from Wave 5 (fieldwork 2018-2021) became public in 2023, and Wave 6 files for Taiwan, South Korea, Mongolia, the Philippines, Indonesia, Cambodia, Vietnam, Thailand, Australia, Japan and Malaysia were released in March 2026; Waves 1-4 and the South Asian Barometer Waves 1-2 (India, Pakistan, Bangladesh, Sri Lanka, Nepal, released May 2017) are also available.

**Access.** Submit the online data application form on the ABS data page (name, affiliation, purpose, and the waves and country files you want) to the project office at National Taiwan University (asianbarometer@ntu.edu.tw); approved applicants download the merged and country files free of charge, with Waves 4-6 supplied in both SPSS and Stata formats alongside the English core questionnaire and sampling documentation.

**Caveats.** Only the merged dataset and the core-questionnaire variables are released; country-specific items collected by national teams are not covered by the data-sharing agreement and must be requested from that country team directly (except Taiwan, administered by ABS headquarters). The rules bind the named applicant: no copying, printing, selling or supplying the data to anyone else, no re-archiving at your institution, academic/education/policy use only, at most 30 non-background variables for classroom use, prescribed acknowledgement text per wave, and bibliographies of resulting publications sent to ABS within a month. Violations mean permanent loss of access and public notification.

### [Comparative Study of Electoral Systems (CSES)](https://cses.org/data-download/)

`Free (registration), email` · beginner 3/5 · cross-national election survey

Post-election survey modules run in dozens of countries, harmonised into integrated modules (Modules 1-6) plus a merged bridging dataset, linking individual vote choice to macro-level institutional and election-result variables in the same file.

**Access.** Web interface: register once, then download integrated module datasets in Stata, SPSS or ASCII with codebooks. Variable and election-study tables on the site let you check coverage before downloading.

**Caveats.** The secretariat is run jointly by the Center for Global Democracy and GESIS. The strongest feature - macro variables merged onto individual records - is also the trap: the district- and system-level variables have their own coding conventions and missingness, so read the module codebook rather than assuming a clean country-year merge.

### [Correlates of War Project](https://correlatesofwar.org/data-sets/)

`Free` · beginner 3/5 · international relations datasets

The standard historical datasets for quantitative IR: Militarized Interstate Disputes (v5.0, 1816-2014), National Material Capabilities (v7.0, source of the CINC index), State System Membership (v2024), formal alliances, direct contiguity, bilateral trade (1870-2014), territorial change, IGO membership and the Arms Technology data (1816-2023). Still actively maintained in 2026.

**Access.** Direct download of CSV/Stata files per dataset from the Data Sets page after accepting the terms; each dataset has its own page with codebook and citation. R users can use the peacesciencer package, which assembles COW-based country-year and dyad-year datasets in one call.

**Caveats.** Terms are restrictive for a public dataset: no commercial use, no redistribution to third parties without written permission from the COW director and data host, and per-dataset citation is mandatory. Datasets are hosted by different scholars at different universities and end in different years, so a merged dyad-year panel is limited by whichever component ends earliest.

### [European Social Survey (ESS)](https://www.europeansocialsurvey.org/data-portal)

`Free (registration), email` · beginner 4/5 · cross-national attitude survey

Biennial academically driven survey of attitudes, beliefs and behaviour across Europe since 2002, now through Round 11, with 30+ countries having participated and an ERIC governance structure. Includes the CRONOS web panel and the human values scale used in thousands of papers.

**Access.** Web interface at the ESS Data Portal (https://ess.sikt.no/): free registration, then download country files or cumulative/integrated files in SPSS, Stata or SAS. The online data builder lets you assemble multi-round, multi-country extracts. R users: the essurvey package on CRAN is version 1.0.8, last published 9 January 2022, and predates the move of the archive to Sikt, so its download functions can fail - prefer the portal directly and read the downloaded files with haven::read_sav().

**Caveats.** Registration is free and open (no institutional affiliation required) but is required before download. Note the methodology break: ESS switched from face-to-face to self-completion in recent rounds, which affects comparability - see 'ESS's Switch to Self-Completion' before pooling rounds. Design weights and post-stratification weights must be applied; unweighted country comparisons are wrong.

### [Eurostat](https://ec.europa.eu/eurostat/web/main/data/database)

`Free` · beginner 4/5 · official European statistics

The EU's statistical office publishes thousands of harmonised tables on population, migration, income and living conditions (EU-SILC aggregates), labour force, education, crime and regional (NUTS) statistics, plus GISCO boundary files for mapping.

**Access.** Web interface plus bulk download; free SDMX and JSON APIs with no key. R: the CRAN package eurostat (version 4.0.0) - get_eurostat('demo_pjan', time_format='num'). Python: the eurostat package. GISCO shapefiles/GeoJSON for NUTS regions download directly.

**Caveats.** Aggregate tables are fully open. Microdata are not: EU-SILC, LFS and similar research microdata require a formal application from a recognised research entity to Eurostat, which is a real institutional gate for unaffiliated researchers. Dataset codes are cryptic - use the 'Stats finder A-Z' or the eurostat package's search_eurostat() rather than browsing.

*Also listed under: econ-finance.*

### [GDELT Project](https://www.gdeltproject.org/)

`Free` · beginner 2/5 · global news event and tone data

Monitors broadcast, print and web news from nearly every country in over 100 languages, coding actors, locations, organisations, themes, emotions, counts, quotes and events. The Event and Global Knowledge Graph files update every 15 minutes and go back to 1979.

**Access.** Direct download of raw CSV/zip files from the file lists (a master file index gives every 15-minute update), or query the whole corpus in Google BigQuery as the public dataset gdelt-bq. Free browser tools (GDELT Summary, TV Explorer) sit on top.

**Caveats.** The data are free; the compute is where costs appear. Full-history BigQuery scans blow through the free 1 TB/month query allowance quickly - always filter by date partition and select only the columns you need. GDELT's automated event coding has well-documented false-positive and duplicate-reporting problems; treat counts as media attention, not ground truth.

### [General Social Survey (GSS)](https://gss.norc.org/)

`Free` · beginner 5/5 · US repeated cross-sectional survey

NORC's benchmark survey of US attitudes and behaviour, running since 1972; the 2024 cross-section is released with a multi-mode design. The cumulative file is the standard resource for US social trend analysis.

**Access.** Direct download of the full cross-sectional cumulative file in SPSS, Stata or SAS format from the 'Get the Data' page - no account needed. Browser-based analysis via the GSS Data Explorer (https://gssdataexplorer.norc.org/), and the same data are mirrored at ICPSR and the Roper Center.

**Caveats.** Read the 'What's New' document before analysing 2021 onward: the mode change (face-to-face to web/mixed-mode) breaks naive time-series comparisons, and weights differ across releases. The cumulative file is large (thousands of variables) - it will strain a low-RAM laptop in SPSS but is fine in R with haven plus data.table.

### [GESIS Data Archive (GESIS Search)](https://search.gesis.org/)

`Free (registration), email` · beginner 3/5 · national social science data archive

Germany's national social science archive, holding more than 7,400 archived studies and over 546,000 searchable variables (GESIS site, August 2026), including ALLBUS (cumulation 1980-2023), the ISSP, the Eurobarometer series and the German Longitudinal Election Study. GESIS also runs SSOAR, an open access full-text repository, and the da|ra DOI registration agency for social science data.

**Access.** Web interface at search.gesis.org: search across studies, variables and publications, then download SPSS/Stata files after logging in with a free GESIS account and accepting the usage terms. SSOAR (https://www.ssoar.info/) is open with no account; da|ra mints DOIs for deposited data.

**Caveats.** Most archived studies download free once you have an account, but each study carries its own access class: a minority (official microdata, sensitive or identifying data held by the Secure Data Center) require an application and sometimes on-site or remote-desktop use. The site sits behind a bot check, so scripted downloads and command-line fetches often fail - use a browser. Interface is bilingual, but some study documentation and questionnaires exist only in German.

### [Global Terrorism Database (GTD)](https://www.start.umd.edu/data-tools/GTD)

`Free (registration), email` · beginner 4/5 · terrorist attack event data

Incident-level record of terrorist attacks worldwide from 1970 through 2020, compiled by START at the University of Maryland: more than 200,000 cases, including over 88,000 bombings, 19,000 assassinations and 11,000 kidnappings, with at least 45 coded variables per case and more than 120 for recent incidents. Covers domestic as well as transnational attacks; 1993 is missing because the original data were lost.

**Access.** Browse and filter incidents in the online GTD interface, or fill in the download form at https://www.start.umd.edu/gtd-download (name, contact details, user category such as academic/individual research, journalism, NGO or commercial) and accept the end user licence to get the full dataset — roughly an 80 MB Excel file plus a geodatabase and the codebook.

**Caveats.** The EULA grants a revocable, non-transferable licence for non-commercial research and analysis only; it forbids publicly posting or redistributing the data, codebook or auxiliary materials without written permission from the University of Maryland (publishing your own analyses and visualisations is allowed), forbids selling or sublicensing, and forbids scraping the site outside its robots.txt. Commercial use requires a separate agreement. The series stops at 2020, so it is a historical resource rather than a current-events feed, and START states it is under no obligation to update it. Cite as 'START (2022). Global Terrorism Database, 1970-2020'.

### [Harvard Dataverse](https://dataverse.harvard.edu/)

`Free` · beginner 5/5 · general research data repository

Open repository holding about 116,600 datasets (116,589 on 28 August 2026 via https://dataverse.harvard.edu/api/info/metrics/datasets), including the replication archives for much of political science and sociology; many journals require deposit here. Each dataset gets a DOI and versioned files.

**Access.** Web interface, no account needed for most downloads. Native REST API (https://dataverse.harvard.edu/api/) and the R package dataverse: get_dataframe_by_name(). Deposit is free for anyone via a free account.

**Caveats.** Some depositors set files to 'restricted' requiring you to accept terms or request access from the author, so not every file in a public dataset is instantly downloadable. Individual files are capped (2.5 GB per file for direct upload); very large collections are usually zipped or split.

### [Health and Retirement Study (HRS)](https://hrs.isr.umich.edu/)

`Free (registration), email` · beginner 3/5 · ageing and retirement panel study

US longitudinal panel of approximately 20,000 people over 50, funded by the National Institute on Aging (U01AG009740) and the Social Security Administration, with biennial waves since 1992 covering health, cognition, work, income, wealth, family and end-of-life, plus biomarker, genetic and life-history modules. It is the model for the ageing panels in Europe (SHARE), England (ELSA), China (CHARLS), Mexico (MHAS) and elsewhere.

**Access.** Register free on the HRS site, accept the conditions of use, and download public survey data in SAS, SPSS or Stata - most users start from the cleaned RAND HRS Longitudinal File rather than raw wave files. Cross-country harmonised versions of HRS and its sister studies are distributed by the Gateway to Global Aging Data (https://g2aging.org/).

**Caveats.** Public files are free after registration; sensitive health, genetic, restricted-geography and administrative-linkage files require a separate application with IRB approval and a data use agreement, and genetic data go through dbGaP. The same NIH review notice as PSID appears on the site. The raw wave structure across 15+ waves is unforgiving - the RAND files exist precisely so you do not have to reconcile it yourself.

### [ICPSR](https://www.icpsr.umich.edu/)

`Free (registration), email` · beginner 4/5 · social science data archive

The largest curated archive of social and behavioural science microdata, run by the University of Michigan since 1962. Studies come with full codebooks, DDI metadata and disclosure review; the topical archives (criminal justice/NACJD, ageing/NACDA, substance abuse and mental health, child care, health and medical care) are open to anyone.

**Access.** Web interface: create a free ICPSR account, search studies, download SPSS/Stata/SAS/delimited bundles. Non-members can also use the openICPSR self-deposit repository (https://www.openicpsr.org). R users can automate downloads with the CRAN package icpsrdata: icpsr_download(file_id = 12345).

**Caveats.** The honest split: only some ICPSR data are free to everyone - chiefly the federally funded topical archives (NACJD, NACDA, SAMHDA, child care, health and medical care) plus anything deposited in openICPSR. The rest requires membership through your institution. ICPSR does sell one-off access to non-members, but no price list appears on its public pages (checked 28 August 2026; the membership FAQ pages render only via JavaScript and quote no figure), so treat any circulated dollar amount as unconfirmed and ask ICPSR support for a current quote before budgeting. Online analysis (SDA) is member-institution-only. Restricted-use versions require a separate application and a data protection plan regardless of membership. Check the 'Access' notice on each study page before planning a project around it.

### [IPUMS](https://www.ipums.org/)

`Free (registration), email` · beginner 3/5 · harmonised census and survey microdata

Harmonised, variable-consistent microdata across time and countries. IPUMS International alone covers 104 countries, 656 censuses and surveys, and over 1 billion person records; sibling projects cover US census/ACS (IPUMS USA), CPS, DHS, time use, health surveys, and US historical GIS boundaries (NHGIS).

**Access.** Web extract system: register free, pick samples and variables, and IPUMS builds a custom rectangular file (fixed-width or CSV plus Stata/SPSS/R/SAS setup). Programmatic access via the IPUMS API with the R package ipumsr (define_extract_micro(), submit_extract()) or the Python package ipumspy.

**Caveats.** Free of charge, but registration is per-project (IPUMS International asks for a short statement of research purpose and takes a day or two to approve). Redistribution of extracts is prohibited - you share the extract definition, not the file. Large extracts can take hours to build and run to many GB; on a laptop, subset variables aggressively before downloading.

### [Latinobarómetro](https://www.latinobarometro.org/)

`Free (registration), email` · beginner 4/5 · Latin American public opinion survey

Annual public opinion study across 18 Latin American countries, roughly 20,000 interviews per wave covering more than 600 million inhabitants, tracking attitudes to democracy, the economy and society since 1995.

**Access.** Web interface: 'Documentation and Data' section gives wave-level data files, questionnaires and technical datasheets, plus a time-series file for comparative analysis. An online query platform covers all waves without downloading.

**Caveats.** Run by a Chilean non-profit corporation dependent on year-by-year funding, so some years have no fieldwork - check the wave list rather than assuming an unbroken annual series. Site and much documentation are Spanish-first; question wording changes between waves are documented only in the Spanish technical sheets.

### [LIS Cross-National Data Center (Luxembourg Income Study)](https://www.lisdatacenter.org/data-access/)

`Free (registration), application` · beginner 2/5 · harmonised income and wealth microdata

Harmonised household income (LIS), wealth (LWS) and consumption (LCS) microdata from national surveys across 50+ countries and five decades - the standard source for cross-national inequality and poverty comparison. Also publishes free Key Figures (Gini, poverty rates) and the DART tool.

**Access.** Remote execution, not download: register free for LISSY, then submit Stata, SAS, SPSS or R job scripts through the web interface or by email and receive the output back. Key Figures, Compare.It and DART give aggregate indicators through the browser with no registration.

**Caveats.** You never see or hold the microdata - LISSY runs your code on their server and returns results, and it blocks output that could disclose individual records (no raw listings, minimum cell sizes). That is a hard constraint on exploratory work: budget several iterations. Registration requires a research purpose. If you only need headline inequality series, the free Key Figures avoid LISSY entirely.

### [Manifesto Project (MARPOR)](https://manifesto-project.wzb.eu/datasets)

`Free (registration), api-key` · beginner 3/5 · party manifesto content analysis

Hand-coded quasi-sentence content analysis of party election manifestos. Version 2025a covers 877 elections, 1,412 parties and 5,285 manifestos, giving standard left-right (RILE) and policy-domain positions, plus a full-text corpus and extensions (immigration positions, government declarations, uncertainty estimates).

**Access.** Register free on the site to get an API key, then either download the main dataset (Stata/CSV/SPSS) from the web interface, or use the CRAN package manifestoR (version 1.6.3): mp_setapikey(); mp_maindataset(). A Python client (manifestata) and the manifestoberta classifier model are also published.

**Caveats.** Registration and an API key are required even for the plain dataset download. Updated at least annually. The category scheme changed between v4 and v5 and the coding of some older manifestos has been revised, so always record the dataset version - RILE scores are not identical across versions.

### [OECD Data Explorer and SDMX API](https://data-explorer.oecd.org/)

`Free` · beginner 3/5 · official cross-national statistics

OECD's statistical database for 38 member countries plus partners: employment and labour force, education outcomes (including PISA indicators), income distribution and poverty, social protection expenditure, health, migration, gender and public governance, in harmonised country-year series delivered through an SDMX API.

**Access.** Web interface at data-explorer.oecd.org (each table's developer button gives the exact query URL). Direct REST with no key, verified 28 August 2026: https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_ALFS@DF_ALFS_EMP,1.1/all?startPeriod=2023&format=csvfilewithlabels ; browse available dataflows at https://sdmx.oecd.org/public/rest/dataflow/OECD.SDD.TPS. R: the rsdmx package, or read the CSV URL directly.

**Caveats.** No key and no rate limit worth worrying about, but the dataflow identifiers are long, agency-scoped and version-pinned, so a URL that worked last year can 404 after a dataflow is revised. The legacy OECD.Stat service has been superseded by the Data Explorer, and the CRAN 'OECD' package (last published December 2021) targets the old service - treat it as stale. Statistical tables are open; OECD iLibrary books and some databases remain subscription products.

*Also listed under: econ-finance.*

### [Our World in Data](https://ourworldindata.org/data)

`Free` · beginner 5/5 · curated global indicators and charts

A charity-run (Global Change Data Lab, UK Reg. Charity No. 1186433) catalogue of cleaned, country-standardised long-run indicators on poverty, health, education, democracy, violence, energy and inequality, with thousands of interactive Grapher charts each carrying a downloadable, sourced CSV.

**Access.** Every chart has a 'Download' tab giving the underlying CSV plus source metadata. Programmatic access via the Chart API and the ETL catalog: Python pip install owid-catalog then owid.catalog.find()/load(); an R client (owidapi) covers the Chart API. Country names are standardised across all datasets, so joins across topics work.

**Caveats.** Charts, articles and OWID's own data are CC BY, but third-party data passed through OWID keep their original licences - check the chart's source note before redistributing. This is a re-publisher, not a primary source: cite the underlying producer as well. The Grapher software is under a custom licence, not fully open source.

### [Panel Study of Income Dynamics (PSID)](https://psidonline.isr.umich.edu/)

`Free (registration), email` · beginner 3/5 · US household panel study

The longest-running longitudinal household survey in the world: began in 1968 with over 18,000 individuals in 5,000 US families and has followed them and their descendants continuously, covering employment, income, wealth, expenditure, health, marriage, childbearing, child development, philanthropy and education. Over 7,600 peer-reviewed publications are based on it.

**Access.** Web interface: create a free account, then use the online Data Center to build a custom cross-year extract (pick variables, get SAS/SPSS/Stata setup files) or download packaged main and supplemental files (Child Development Supplement, Transition into Adulthood, Immigrant samples). Public files are free after accepting the conditions of use.

**Caveats.** Free, but the conditions of use require citation and prohibit re-identification, and restricted files (geocodes, administrative and Medicare/Medicaid linkages) need a separate contract with institutional review. The site carries an NIH-requested notice added 31 March 2025 stating the repository 'is under review for potential modification in compliance with Administration directives' - a real continuity risk worth mirroring anything you depend on. Variable names change every wave; use the Data Center's cross-year index rather than matching by hand.

*Also listed under: econ-finance.*

### [Pew Research Center datasets](https://www.pewresearch.org/datasets/)

`Free (registration), email` · beginner 5/5 · US and global survey microdata

Case-level microdata from Pew's own surveys released for secondary analysis after an embargo, including American Trends Panel waves, the annual National Public Opinion Reference Survey (NPORS), the Global Attitudes multi-country surveys (the Spring 2025 release covers 25 countries), and religion datasets such as Global Restrictions on Religion 2007-2022.

**Access.** Web interface: create a free account, then download SPSS files with questionnaires, topline results and methodology statements. Datasets are listed by collection date, with separate listings for the American Trends Panel and religion collections.

**Caveats.** High-quality probability samples with full methodology documentation, released free - unusually generous for a private research organisation. The embargo means the newest headline surveys are not yet downloadable. Panel waves are individually small; pooling ATP waves requires the panel weights and an understanding of panel attrition.

### [Quality of Government (QoG) Institute datasets](https://www.gu.se/en/quality-government/qog-data)

`Free` · beginner 5/5 · compiled country-year indicators

University of Gothenburg compilations that merge hundreds of governance, institutional and socio-economic indicators from many sources into ready-made country-year files (Basic, Standard, OECD, Environmental Indicators, EU Regional), plus original data: the QoG Expert Survey (100+ countries) and the European Quality of Government Index (subnational, three survey rounds).

**Access.** Direct download of Stata, SPSS, CSV and R files per dataset with codebooks - no account needed. A Data Finder and variable search tool let you locate an indicator across all datasets before downloading; QoG publishes Stata and R usage guidance.

**Caveats.** The fastest way to get a comparative country-year panel without merging ten sources by hand, and the codebook credits every original source. The flip side: it is a compilation, so coverage gaps and measurement quirks are inherited from the upstream sources - cite and check the original series for anything load-bearing.

### [SHARE (Survey of Health, Ageing and Retirement in Europe)](https://share-eric.eu/data/)

`Free (registration), credentialing` · beginner 2/5 · European ageing panel study

Multidisciplinary panel of the population aged 50+ across 27 European countries plus Israel, covering health, cognition, employment, pensions, finances, family and social networks, with linked SHARELIFE retrospective histories.

**Access.** Register at the SHARE Research Data Centre, sign and return the User Statement, and on approval (usually a few business days) download release files in Stata, SPSS or R format from the data portal.

**Caveats.** Free worldwide but not unconditional: access is for 'scientific use' and the User Statement asks you to state a scientific affiliation (researchers and students qualify; a fully unaffiliated applicant may need to explain their status). Record-linkage data have extra conditions. The panel structure across waves and countries is genuinely complex - use the official generated variables (gv_*) rather than rebuilding them.

### [The DHS Program](https://dhsprogram.com/data/)

`Free (registration), application` · beginner 3/5 · health and demographic household surveys

Nationally representative household surveys on health, fertility, nutrition, gender and mortality across roughly 90 low- and middle-income countries since 1984, with individual, household, children's and biomarker recode files plus geospatial cluster data.

**Access.** Register a free account, submit a short description of your research project, and request the specific country datasets you need; on approval (usually a few working days) download Stata, SPSS, SAS or flat files with recode manuals. Also a public API (https://api.dhsprogram.com/) for indicators, STATcompiler for pre-computed tables, and harmonised versions via IPUMS-DHS.

**Caveats.** The project description is a real (if light) review step, and access is granted per project - you must request additional countries separately. Data may not be redistributed or passed to colleagues; each person registers individually. GPS displacement means cluster coordinates are randomly offset (up to 2 km urban, 5-10 km rural), which matters for any spatial analysis.

### [UCDP (Uppsala Conflict Data Program)](https://ucdp.uu.se/downloads/)

`Free` · beginner 4/5 · armed conflict data

The reference dataset for organised violence: the UCDP/PRIO Armed Conflict Dataset covers 1946-2025 and the Georeferenced Event Dataset (GED) gives individual, geolocated, date-stamped violent events from 1989 onward. Current release is version 26.1.

**Access.** Direct download of every current dataset with codebooks and version histories, licensed CC BY 4.0. A REST API (https://ucdpapi.pcr.uu.se/) returns the same data as JSON for programmatic or bulk access; R users can wrap it directly or use community packages.

**Caveats.** Genuinely open under CC BY 4.0 - the most permissive of the major conflict datasets, and the right default if you need to redistribute derived data. The Candidate Events dataset is provisional monthly data that has not passed final annual coding; do not mix it with GED in a single series without saying so.

### [UK Data Service](https://ukdataservice.ac.uk/)

`Free (registration), email` · beginner 3/5 · national data archive

The UK's ESRC-funded archive of economic, population and social data: the major UK longitudinal studies (Understanding Society, Labour Force Survey, British Social Attitudes), census aggregate data, international macro series and a substantial qualitative collection.

**Access.** Web interface at the data catalogue. Non-UK and non-academic users apply for a username via an online form, then select 'UK Data Archive' as their organisation at login; after that you can download or request most End User Licence datasets.

**Caveats.** Registration is genuinely open worldwide - this is one of the few national archives that does not gate on institutional affiliation. But the tiers matter: End User Licence data are downloadable, Special Licence data require a signed agreement and often a named institution, and Secure Lab (detailed/identifiable) data effectively require UK-based accredited researcher status and a physical or approved safe setting. Commercial use triggers extra steps.

### [UNESCO Institute for Statistics (UIS) Data Browser and API](https://databrowser.uis.unesco.org/)

`Free` · beginner 4/5 · global education, culture and R&D statistics

The UN's official cross-national statistics on education (including the SDG 4 indicator set), science, technology and innovation, culture, and related demographic and socio-economic context. The public API listed 5,063 indicator definitions when checked on 31 August 2026 - 4,986 education, 35 demographic/socio-economic, 30 culture and 12 science-technology-innovation - with the February 2026 release as the current data vintage.

**Access.** Filter by indicator, country and year in the browser and export CSV or Excel, or call the free JSON API with no key: https://api.uis.unesco.org/api/public/data/indicators?indicator=CR.1&geoUnit=BRA&start=2015&end=2016 returns the completion rate for Brazil; /api/public/definitions/indicators lists every indicator with its time range and record count, and /api/public/versions/default reports the current data version.

**Caveats.** Coverage is very uneven: most indicators are national-level only, and country-years are simply absent where governments did not report or UIS could not validate the return. UIS revises and re-releases whole themes at once, so a figure can change between releases - record the version string from /api/public/versions/default for reproducibility. Some UIS series are modelled or imputed; check the indicator metadata before treating a value as an administrative count.

### [UNHCR Refugee Data Finder](https://www.unhcr.org/refugee-statistics/)

`Free` · beginner 4/5 · forced displacement and statelessness statistics

UNHCR's official population statistics on refugees, asylum-seekers, internally displaced people, stateless people and others in need of international protection, from UNHCR's annual statistical activities starting in 1951, supplemented with UNRWA registered Palestine refugees and IDMC conflict-displacement figures. Tables cover year-end population stocks by origin and asylum country, asylum applications and decisions, demographics, durable solutions, and annual flows back to 1962.

**Access.** Filter and export CSV in the web app; query the JSON API with no key, e.g. https://api.unhcr.org/population/v1/population/?yearFrom=2023&yearTo=2023&coo=SYR; or use the CRAN package refugees (install.packages("refugees")), which ships eight ready-made tables (population, flows, asylum_applications, asylum_decisions, demographics, solutions, idmc, unrwa) as tidy data frames.

**Caveats.** The refugees package is released under CC BY 4.0 and UNHCR asks for attribution to the Refugee Data Finder. Figures are reported by governments and UNHCR operations, are revised in later releases, and cells appear as "-" where a country did not report or the breakdown is unavailable, so pin the release year you used. IDMC and UNRWA series come from those agencies and follow their own definitions - do not add them to UNHCR counts without checking for overlap.

### [US Census Bureau data and API](https://www.census.gov/data/developers/data-sets.html)

`Free, api-key` · beginner 4/5 · official US statistics and microdata

The primary source for US demographic, social and economic statistics: American Community Survey 1- and 5-year estimates down to block group, the Decennial Census, CPS supplements, population estimates and business series, published both as tables on data.census.gov and through a machine-readable API covering hundreds of datasets.

**Access.** Web interface at https://data.census.gov for tables and maps. API example: https://api.census.gov/data/2023/acs/acs5?get=NAME,B01003_001E&for=state:*&key=YOUR_KEY - a free key from https://api.census.gov/data/key_signup.html is now required (checked 28 August 2026: keyless calls return a 'Missing Key' page). R: install.packages('tidycensus') (1.8.1) then get_acs(geography='county', variables='B19013_001', year=2023). Python: the census and censusdata packages.

**Caveats.** The key is free and arrives by email, but older tutorials that call the API without one now fail. ACS estimates come with margins of error that must be carried into any comparison - small-area 5-year estimates are often too noisy for the differences people want to claim. Table and variable IDs (B19013_001E) are cryptic; use tidycensus's load_variables() or the API discovery tool. For person-level microdata, IPUMS USA is far easier than raw PUMS files.

### [V-Dem (Varieties of Democracy)](https://v-dem.net/data/the-v-dem-dataset/)

`Free` · beginner 4/5 · democracy and governance indicators

The most detailed democracy measurement project available: version 16 (published March 2026) carries 531 indicators and 251 indices plus 62 indicators from other sources, in country-year, country-date and coder-level files, with expert-coded uncertainty estimates.

**Access.** Direct download of ZIPs (Stata, CSV, R, SPSS) including codebook, 'What's New' and cautionary notes - no account needed. For R, install the vdemdata package from GitHub (remotes::install_github('vdeminstitute/vdemdata')), which bundles the current dataset and helper functions.

**Caveats.** Published under CC BY-SA 4.0 (share-alike: derived datasets you redistribute inherit the licence, which matters if you are merging V-Dem into a package or an app). vdemdata is on GitHub, not CRAN. The coder-level files are large and only meaningful if you understand the measurement model; most users want the Country-Year Core file. Indicator codes change between major versions, so pin the version number in your replication code.

### [World Bank Open Data](https://data.worldbank.org/)

`Free` · beginner 5/5 · cross-national development indicators

The World Development Indicators database alone exposes 1,498 indicators across 295 countries and aggregates, with long annual series on population, education, employment, poverty, governance and infrastructure; the wider catalogue adds microdata surveys and subnational data.

**Access.** Free REST API with no key (https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json), bulk CSV downloads per indicator, and mature clients: R package WDI (version 2.8.0) - WDI(indicator='NY.GDP.PCAP.KD', country='all') - or Python's wbgapi / world_bank_data. The Microdata Library (https://microdata.worldbank.org/) holds survey microdata under per-survey licences.

**Caveats.** No key, no rate limit worth worrying about, and CC BY 4.0 on most indicators. Caveats are about the data, not access: many series are modelled or interpolated by the World Bank rather than reported by countries, and coverage for low-income countries is patchy in exactly the years people most want. Microdata Library surveys have their own access levels, some requiring an application.

*Also listed under: econ-finance.*

### [World Inequality Database (WID.world)](https://wid.world/data/)

`Free` · beginner 3/5 · income and wealth distribution series

The World Inequality Lab's database of income and wealth distribution built from combined survey, tax and national accounts sources (distributional national accounts), maintained by a network of over a hundred researchers covering more than seventy countries, with percentile-level shares and long historical series for the best-documented countries.

**Access.** Web interface: select indicators, countries and years and download the series, or use the 'Download full dataset' bulk export in the Data section. R: install.packages('wid') (0.0.3, July 2026) then download_wid(indicators='sptinc', areas='US', perc='p99p100'). Stata: ssc install wid, then wid, indicators(shweal) areas(FR) clear. Variable naming is documented in the Codes Dictionary.

**Caveats.** Free with no account. WID series are estimates that reconcile surveys with tax and national accounts data, so they are systematically higher at the top than survey-only measures and are not interchangeable with World Bank/PIP or SWIID Ginis - do not mix them in one series. Coverage and underlying source quality vary enormously by country and period; read the country method papers before drawing cross-country conclusions, and note that the six-letter WID codes are essential for using the packages.

*Also listed under: econ-finance.*

### [World Values Survey](https://www.worldvaluessurvey.org/)

`Free (registration), email` · beginner 4/5 · global values survey

The widest-coverage cross-national survey of human values, run in seven completed waves since 1981 (Wave 7: 2017-2022) with Wave 8 in the field. The WVS/EVS joint and trend files combine World Values Survey and European Values Study into a 1981-2022 time series.

**Access.** Web interface: pick a wave under Data and Documentation > Data Download, complete a short form, and download SPSS, Stata, SAS or R files plus questionnaires and codebooks. Also an online analysis tool for crosstabs without downloading.

**Caveats.** Free but you must agree to the conditions of use and cite the specific dataset version; redistribution of the files is not permitted. Country coverage varies sharply by wave, so 'global' trends usually rest on an unbalanced panel of countries - check which countries are present in each wave before interpreting movement over time.

## Software

### [Gephi](https://gephi.org/)

`Free` · beginner 4/5 · network visualisation and analysis

Open-source (GPL-3.0) desktop platform for exploring and visualising networks: force-directed layouts (ForceAtlas2, Yifan Hu), modularity-based community detection, centrality measures, filtering and dynamic (time-sliced) networks. Actively maintained as of August 2026.

**Access.** Free download for Windows, macOS and Linux; imports GEXF, GraphML, CSV edge lists and adjacency matrices. Exports publication-ready SVG/PDF. For scripted analysis pair it with igraph (R/Python) or NetworkX, and use Gephi for the visual layout stage.

**Caveats.** Java-based and memory-limited by default: graphs beyond roughly a hundred thousand edges need you to raise the JVM heap in the config file, and it will still struggle where igraph would not. Treat it as the visualisation and exploration tool, not the place where your reported statistics are computed.

### [igraph](https://igraph.org/)

`Free` · beginner 3/5 · network analysis library

The workhorse network analysis library, with the same algorithms exposed in R (2.3.3, June 2026), Python (1.0.0), Mathematica and C (1.0.1): degree, betweenness and eigenvector centralities, community detection (Louvain, Leiden, walktrap, infomap), k-cores, motifs, assortativity, shortest paths, random graph models and layouts, scaling to graphs with millions of edges.

**Access.** R: install.packages('igraph') then g <- graph_from_data_frame(edges, directed=FALSE); cluster_leiden(g); betweenness(g). Python: pip install igraph then import igraph as ig; g = ig.Graph.TupleList(edges); g.community_leiden(). C library and Mathematica bindings from igraph.org.

**Caveats.** GPL-licensed and free. The R and Python APIs are similar but not identical, so code does not port line for line, and the C core's 1.0 release (September 2025) renamed functions relative to the 0.10 series - pin versions in replication code. igraph computes; Gephi visualises. For inferential network models (ERGM, latent space, stochastic actor-oriented models) you still need statnet/ergm, latentnet or RSiena.

### [jamovi](https://www.jamovi.org/)

`Free` · beginner 5/5 · point-and-click statistics

Free, open-source statistical spreadsheet built on R, with over 5 million downloads and 70+ community modules. Shows the equivalent R syntax for every analysis you click, and saves data, analyses and results into a single reproducible file.

**Access.** Download the desktop application for Windows, macOS or Linux (always free), or use jamovi Cloud's free Guest plan in the browser with no install. Modules (medmod, GAMLj, jsq for Bayesian, MAJOR for meta-analysis) install from within the app.

**Caveats.** The best free path off SPSS for people who do not want to write code, and the syntax preview makes it a genuine bridge into R. Cloud has paid tiers for longer sessions and more memory; the desktop version has no such limits and is the one to use for real work. Some advanced modelling still needs R or specialised software.

### [JASP](https://jasp-stats.org/)

`Free` · beginner 5/5 · Bayesian and frequentist statistics GUI

Open-source statistics package from the University of Amsterdam offering standard analyses in both classical and Bayesian form side by side, with APA-formatted output you can paste straight into a manuscript and OSF integration for sharing analysis files.

**Access.** Free download for Windows, macOS and Linux; also runs from a browser. Analyses update dynamically as you change options; results copy out as APA tables and figures. A free online data library of teaching datasets and video library accompany it.

**Caveats.** The strongest free route into Bayesian hypothesis testing (Bayes factors) without learning Stan - the default priors are the Amsterdam group's, which is a substantive choice you should report. Less extensible than jamovi for custom models; for anything beyond the built-in menu you will drop to R.

### [KoboToolbox](https://www.kobotoolbox.org/)

`Free tier, email` · beginner 4/5 · mobile and offline data collection

Open-source XLSForm-based platform for field data collection: offline-capable Android app and web forms, skip logic and validation, GPS and multimedia capture, unlimited enumerators and collaborators, multilingual forms and dynamic data linking. Built for low-connectivity fieldwork.

**Access.** Web interface: sign up on a Kobo server, build forms in the browser or by uploading an XLSForm, deploy, and collect with KoboCollect (Android) or web forms. Data export to CSV, XLS, SPSS and via a REST API; R users can pull data with the robotoolbox package.

**Caveats.** Read the eligibility line carefully. The Community plan is free only for nonprofits, government agencies, UN organisations and educational institutions; it gives 5,000 submissions per month and 1 GB file storage. Private companies and 'personal use not associated with an organisation' fall into the Other category, where Community costs about US$99/month and the cheapest paid plan (Starter, 1,000 submissions/month) is US$25/month. An unaffiliated independent researcher may not qualify for the free tier - or can self-host the open-source stack instead.

### [lavaan](https://lavaan.ugent.be/)

`Free` · beginner 3/5 · structural equation modelling

Open-source R package (version 0.7-2) for latent variable analysis: confirmatory factor analysis, structural equation models, growth curve models, multi-group and measurement invariance testing, with robust and categorical-outcome estimators. The free replacement for Mplus, LISREL and AMOS.

**Access.** install.packages('lavaan') then write the model in lavaan syntax and fit: model <- 'f1 =~ x1 + x2 + x3'; fit <- cfa(model, data=d); summary(fit, fit.measures=TRUE, standardized=TRUE). Companion packages: semTools for invariance testing, semPlot / tidySEM for diagrams.

**Caveats.** Feature parity with commercial SEM software for the vast majority of published models; a few Mplus features (some mixture models, certain multilevel SEM specifications) are still missing or less mature. The lavaan website hosts a complete free tutorial that is the standard teaching resource.

### [LimeSurvey Community Edition](https://community.limesurvey.org/)

`Free` · beginner 2/5 · self-hosted survey platform

Open-source survey application supporting complex branching and conditional logic, quotas, randomisation, multilingual questionnaires (50+ interface languages), panel/token management and anonymous responses. Actively developed on GitHub.

**Access.** Download the Community Edition and self-host on any PHP/MySQL server (shared hosting is enough for most academic surveys); Docker images exist. Exports to CSV, SPSS, Stata and R, and offers a RemoteControl JSON-RPC API for automated response retrieval.

**Caveats.** Free only if you self-host - LimeSurvey's own cloud service is a paid product, and the ComfortUpdate auto-updater is a paid add-on even for CE. Self-hosting means you own the security and GDPR responsibilities, including patching; that is often exactly what an ethics committee wants, but it is real work.

### [NetLogo](https://ccl.northwestern.edu/netlogo/)

`Free` · beginner 4/5 · agent-based modelling

Agent-based modelling environment from Northwestern's Center for Connected Learning (release 7.0.4, May 2026), shipping a large Models Library that includes Schelling segregation, opinion dynamics, cooperation, diffusion and epidemic models you can run and modify within minutes. BehaviorSpace runs parameter sweeps and exports results to CSV.

**Access.** Free download for Windows, macOS and Linux, or run and edit models in the browser with NetLogo Web (no install, useful on locked-down machines). Models Library is bundled; the free NetLogo User Manual and interactive dictionary document the language. For large experiments, drive it from R (nlrx) or Python (pyNetLogo) and analyse the sweep output in your usual tools.

**Caveats.** The fastest route from a verbal social mechanism (segregation, threshold models, norm cascades) to something runnable, and the standard teaching tool for agent-based modelling. The language is idiosyncratic and effectively single-threaded, so very large or computation-heavy models are better in Mesa (Python) or Agents.jl (Julia). Deposit finished models in the CoMSES/OpenABM library - JASSS and most reviewers now expect runnable code.

### [oTree](https://www.otree.org/)

`Free` · beginner 2/5 · online experiments and behavioural games

Python framework for multiplayer strategy games, controlled behavioural experiments, surveys and quizzes - public goods games, auctions, trust games, prisoner's dilemma - running in any browser with no participant install. Actively developed (last release mid-2026).

**Access.** pip install otree then otree startproject and otree devserver to run locally. Deploy to a free-tier PaaS or a small VPS; connect participants via oTree 'Rooms' with per-participant links. Recruit through Prolific or MTurk with built-in integrations. Documentation and a three-part tutorial at https://otree.readthedocs.io/.

**Caveats.** Free and open source under an MIT-style licence, with a licence clause requiring you to cite Chen, Schonger and Wickens (2016) in publications reporting oTree experiments. The framework is free; participant payments and any managed hosting (oTree Hub) are not. You need working Python to build anything non-trivial, and self-hosting a session for dozens of simultaneous participants needs a real server, not a laptop.

### [QGIS](https://qgis.org/)

`Free` · beginner 3/5 · spatial analysis and mapping

Full-featured open-source desktop GIS: reads and writes shapefiles, GeoJSON, GeoPackage and rasters, joins survey data to administrative boundaries, runs spatial joins, buffers, kernel density and geostatistics, and produces publication-quality print layouts.

**Access.** Free download for Windows, macOS and Linux (long-term release recommended). Add data from IPUMS NHGIS/IHGIS, Eurostat GISCO, GADM or Natural Earth; the built-in Python console and Processing toolbox script repeatable workflows. R users can do much of the same with sf and tmap.

**Caveats.** A complete free replacement for ArcGIS Pro for the tasks social scientists actually need. It is memory-hungry on large rasters, and the plugin ecosystem varies in quality - stick to plugins with recent updates. Coordinate reference systems are the usual source of silent errors; set the project CRS deliberately.

### [QualCoder](https://github.com/ccbogel/QualCoder)

`Free` · beginner 3/5 · qualitative data analysis (CAQDAS)

Cross-platform open-source (LGPL-3.0) qualitative analysis application for text, images, audio and video: hierarchical codebooks, coded-segment retrieval, memos, attribute-based filtering, coder comparison with kappa, code co-occurrence matrices and REFI-QDA import/export. Actively developed (commits in August 2026).

**Access.** Install from the GitHub Releases page (Windows .exe or installer, plus packaged builds) or run from source: clone the repository, create a virtual environment, and pip install -r requirements.txt (Python 3.13 or newer and PyQt6 >= 6.5), then launch with python -m qualcoder. There is no 'qualcoder' project on PyPI - pip install qualcoder returns 404 (checked 28 August 2026). Projects are local SQLite-backed folders; coded segments, matrices and reports export to CSV/HTML, and REFI-QDA import/export moves projects to and from other CAQDAS tools.

**Caveats.** The most capable genuinely free alternative to NVivo, ATLAS.ti and MAXQDA, and it supports REFI-QDA so you can move a project between tools. It is a small volunteer project: the interface is plainer than the commercial packages, there is no team-collaboration server, and PyQt6 installation can be fiddly on macOS. For lightweight tagging with a hosted option, Taguette (https://www.taguette.org/) is simpler but does far less.

### [quanteda](https://quanteda.io/)

`Free` · beginner 3/5 · quantitative text analysis

R framework (version 4.5.0) for text-as-data: corpus management, tokenisation, document-feature matrices, dictionaries, keyness, collocations, scaling models (wordfish, wordscores) and topic models, built for the corpus sizes political scientists and sociologists actually work with.

**Access.** install.packages('quanteda') then corpus(txt) |> tokens() |> dfm(). Free tutorials in six languages at https://tutorials.quanteda.io/, plus companion packages quanteda.textstats, quanteda.textmodels, quanteda.textplots and readtext for importing PDFs, Word files and JSON.

**Caveats.** Created by Kenneth Benoit and Kohei Watanabe and funded by an ERC grant; maintained by the Quanteda Initiative CIC. Deliberately not a full NLP pipeline - for dependency parsing, NER or transformer embeddings you pair it with spacyr (a spaCy bridge) or udpipe. Non-space-delimited languages need a tokeniser plugin.

### [R survey and srvyr packages](https://cran.r-project.org/package=survey)

`Free` · beginner 3/5 · complex survey analysis

Thomas Lumley's survey package (version 4.5) is the reference implementation for analysing stratified, clustered, weighted survey samples in R: design-based means, totals, quantiles, regression, replicate weights and domain estimation. srvyr (1.3.1) wraps it in dplyr syntax.

**Access.** install.packages(c('survey','srvyr')) then define the design once: svydesign(ids=~psu, strata=~stratum, weights=~wt, data=d, nest=TRUE) and use svymean(), svyglm(), svyby() on it. srvyr: as_survey_design(d, ids=psu, strata=stratum, weights=wt) %>% group_by(x) %>% summarise(m = survey_mean(y)).

**Caveats.** Free and GPL-licensed, and it is the correct tool for essentially every dataset in this section (GSS, ESS, DHS, IPUMS all have complex designs). The learning cost is real: getting standard errors right means reading the survey's own weighting documentation, not just copying a svydesign call. Replicate-weight designs use svrepdesign(), not svydesign().

### [Stan (with brms)](https://mc-stan.org/)

`Free` · beginner 2/5 · Bayesian modelling

Probabilistic programming language and inference engine (Hamiltonian Monte Carlo/NUTS, plus variational inference and optimisation) used for multilevel and hierarchical models, item response theory, measurement models, latent variable models and any custom Bayesian model. Interfaces for R, Python, Julia and the shell, with a large free documentation set and case study library.

**Access.** R: install.packages('rstan') (2.32.7) or cmdstanr; the fastest route for survey researchers is brms (2.23.0) - brm(y ~ x + (1 | country), data = d, family = gaussian()) writes, compiles and runs the Stan program for you and returns posterior draws. Python: pip install cmdstanpy. Free User's Guide, Reference Manual and case studies at mc-stan.org.

**Caveats.** BSD-licensed and free; the cost is compilation and time - you need a working C++ toolchain, and non-trivial models run for minutes to hours. brms hides the Stan code but not the modelling decisions: its default priors are choices you must report. If you only need Bayes factors for standard tests, JASP is far quicker; Stan is for models with no off-the-shelf equivalent. Pair with Statistical Rethinking (already in this catalogue) for the conceptual grounding.

### [Whisper (openai-whisper / faster-whisper)](https://github.com/openai/whisper)

`Free` · beginner 3/5 · offline interview transcription

Open-weights automatic speech recognition models plus a reference Python implementation (MIT licence, release 20250625) that transcribe and translate roughly 100 languages entirely on your own machine. The faster-whisper reimplementation (1.2.1) runs the same weights several times faster on CPU or GPU.

**Access.** pip install openai-whisper then whisper interview01.m4a --model large-v3 --language tr --output_format srt (also txt, vtt, json). Or pip install faster-whisper for the CTranslate2 backend with the same model names. Model weights download once (about 1.5 GB for large-v3) and then everything runs offline.

**Caveats.** The reason this matters for qualitative social science: interview and focus-group audio never leaves your machine, which is usually what an ethics committee and a GDPR data protection plan require, and there is no per-minute fee - a 40-interview project costs nothing but electricity. Accuracy falls on overlapping speakers, strong accents and low-resource languages, and the model can hallucinate fluent sentences over silence, so verify transcripts against audio before coding them in NVivo or QualCoder. large-v3 wants a GPU or roughly 10 GB RAM; small/medium models run on a laptop with real quality loss.

### [Zotero](https://www.zotero.org/)

`Free` · beginner 5/5 · reference manager

Free, open-source reference manager: one-click capture of citations and PDFs from browsers and library catalogues, PDF reading and annotation, automatic bibliographies in Word, LibreOffice and Google Docs, over 10,000 citation styles, and shared group libraries for co-authored projects.

**Access.** Download the desktop app for Windows, macOS or Linux plus the browser connector; add references with the connector button, cite with the word-processor plugin. The software, local storage and metadata syncing are free; online file storage is 300 MB free, then US$20/year for 2 GB, US$60/year for 6 GB or US$120/year unlimited - or point Zotero at your own WebDAV server and pay nothing.

**Caveats.** Works fully offline with no account; a free account (email) is needed only for syncing across devices and for group libraries, and group files draw on the group owner's quota. The 300 MB free tier only bites if you sync PDFs, which most people do - WebDAV or a self-hosted alternative avoids the subscription. Run by the non-profit Corporation for Digital Scholarship (Digital Scholar) and funded by storage subscriptions, which is why the free tier is small rather than absent.

## Literature

### [APSA Preprints](https://preprints.apsanet.org/)

`Free (registration), email` · beginner 5/5 · discipline preprint server

The American Political Science Association's preprint server, hosted on Cambridge Open Engage, organised by APSA's own subfields - American politics, comparative politics, IR, methodology, political theory, public opinion, race and ethnicity, gender, public policy and others - with roughly 1,800 items posted.

**Access.** Web interface: free account, upload a manuscript or working paper, select a category, and it appears after screening with a DOI. Browsing and downloading require no account.

**Caveats.** Posting is free and open to non-members as well as APSA members. The site has carried a 'currently under development / beta' banner for a long time and volumes are far below SSRN's, so treat it as a discipline-signalling venue rather than your only distribution channel. Content is not peer reviewed prior to posting.

### [CORE](https://core.ac.uk/)

`Free` · beginner 4/5 · open access full-text aggregator

Aggregator of open access research harvested from thousands of institutional and subject repositories worldwide: 452 million papers indexed (site figure, August 2026) with search over the full text of the documents rather than just abstracts. Non-profit community infrastructure hosted by The Open University.

**Access.** Free web search at core.ac.uk with links to the harvested full text. Machine access through the CORE API v3 with a free registered API key (https://core.ac.uk/services/api), the FastSync service for incremental updates, and bulk dataset dumps for text and data mining.

**Caveats.** Complements Unpaywall rather than duplicating it: Unpaywall answers 'is there a legal free copy of this DOI', CORE lets you search inside the copies and download them in bulk for corpus work. Metadata is noisy - the same paper appears from several repositories, versions (preprint, accepted manuscript, published) are mixed, and DOIs are sometimes missing, so deduplicate before counting anything. Web search needs no account; the API needs a free key, and the full dumps are hundreds of gigabytes.

### [Directory of Open Access Books (DOAB)](https://www.doabooks.org/)

`Free` · beginner 5/5 · open access book index

Community-driven index of over 108,500 peer-reviewed open access scholarly books (August 2026) from vetted publishers, with substantial sociology, anthropology, political science, history and area studies coverage - the part of the literature where open access is thinnest. All DOAB services are free and its metadata is freely available.

**Access.** Web interface: search or browse by subject, publisher, language or collection; each record links straight to the full text on the publisher's or OAPEN's platform, normally a downloadable PDF or EPUB with no account. Bulk metadata is available for library catalogues; the PRISM service records how participating publishers peer review.

**Caveats.** For monograph-based fields this is the single most useful free index, because journal-focused tools (Unpaywall, OpenAlex, DOAJ) largely miss books. It only covers titles whose publishers have joined, so most commercial monographs - including the field-defining ones - are absent, and it is no substitute for library or interlibrary access. Licences vary by title (many are CC BY-NC-ND), so check before reusing figures or long excerpts.

### [Directory of Open Access Journals (DOAJ)](https://doaj.org/)

`Free` · beginner 5/5 · open access journal index

Community-curated index of 23,370 vetted open access journals (DOAJ search API, 28 August 2026) with article-level metadata for a large share of them, and filters for journals that charge no author fees at all - the practical way to find diamond open access outlets in your subfield.

**Access.** Web interface with an 'APC' filter to isolate no-fee journals; free search API (https://doaj.org/api/search/journals/{query}) and full metadata dumps under CC0 for journals, CC BY-SA for article metadata.

**Caveats.** DOAJ inclusion is an editorial-quality screen, not a peer-review guarantee, and it is not a completeness guarantee either - some legitimate journals have never applied. The 'no APC' filter reflects what the journal reported; confirm on the journal's own site before submitting, since fee policies change.

### [JSTOR free reading](https://www.jstor.org/register)

`Free (registration), email` · beginner 5/5 · journal archive personal access

A free personal JSTOR account gives read-online access to articles from participating publishers across JSTOR's archival journal collections, which are unusually deep in sociology, anthropology, history and political science back-runs.

**Access.** Register a free account at jstor.org/register, then read qualifying articles in the browser. JSTOR's Open & Free collections (open access books, journals and Reveal Digital primary sources) are additionally readable and downloadable by anyone with no account at all.

**Caveats.** Checked 28 August 2026 against JSTOR's own support pages ('How to Register & Get Free Access to Content' and 'How to Use Your Free Reads with a Personal Account'): both state 100 free article reads per rolling 30 days, and no reduction to 10 reads from 1 September 2026 is announced on support.jstor.org or about.jstor.org. Free reads are read-online only, not PDF downloads, and participating publishers decide which articles qualify; the counter and reset date are visible under 'Free Article Views' in your account. The separate JPASS product is a paid personal subscription. JSTOR has changed this allowance before, so re-check the support page before planning a reading schedule around it.

### [OpenAlex](https://openalex.org/)

`Free` · beginner 4/5 · open bibliographic database

Fully open index of scholarly works, authors, institutions, sources, topics and citations - about 322 million works, of which roughly 197 million are journal articles - built by OurResearch as the successor to Microsoft Academic Graph. The whole database is CC0.

**Access.** Free REST API with no key: https://api.openalex.org/works?filter=concepts.id:C144024400,publication_year:2025 (add &mailto=you@example.com to enter the faster polite pool). Python client pip install pyalex; R client openalexR - oa_fetch(entity='works', title.search='social capital'). Full monthly database snapshots are downloadable from AWS S3.

**Caveats.** The only large citation database you can legally download in bulk and analyse - the practical replacement for Web of Science and Scopus for bibliometric work without a subscription. Coverage is broad but metadata quality is uneven: author disambiguation, institution matching and topic assignment all contain errors, so validate before publishing counts. A paid 'premium' tier exists for higher rate limits and faster snapshots; the free API is sufficient for most research.

### [RePEc (IDEAS and EconPapers)](https://ideas.repec.org/)

`Free` · beginner 4/5 · working paper index

Crowd-sourced bibliographic infrastructure for economics and quantitative social science: 5,482,493 searchable items on 28 August 2026, including 1,316,142 working papers (1,110,757 with free full text) in 5,914 series, 3,752,228 journal articles, 69,347 books and 6,032 software components. Free services include author profiles, the CitEc citation index and the NEP new-paper email alerts.

**Access.** Two free front ends over the same data: IDEAS (ideas.repec.org) and EconPapers (econpapers.repec.org). Search or browse by JEL code, subscribe to NEP subject reports for weekly new working papers, register a free author profile so your work is indexed and cited correctly, and deposit unpublished work in MPRA (Munich Personal RePEc Archive) if your publisher does not participate in RePEc.

**Caveats.** The largest free index of working papers relevant to social science, and often the way to read a paper years before journal publication - but it is a metadata layer, not a repository: links point at publishers' and institutions' servers, and some resolve to paywalls or dead pages. Coverage is economics-centred, so political science, sociology and anthropology appear only where the series or journal self-registers. An email address is needed only for author registration and NEP subscriptions.

### [Research4Life](https://www.research4life.org/)

`Free tier, application` · beginner 2/5 · institutional access for low- and middle-income countries

Five UN-agency-partnered programmes - Hinari (health), AGORA (agriculture), OARE (environment), ARDI (innovation and technology) and GOALI (legal and social science) - giving institutions in around 125 low- and middle-income countries online access to major publishers' peer-reviewed content.

**Access.** Institutional registration through the Research4Life website; once registered, staff and students log in at the portal (https://portal.research4life.org/) and read across all five programmes' collections.

**Caveats.** The single biggest legal lever for researchers at poorly resourced institutions - but it is institution-level, not individual: your university, government agency, hospital, research institute or local not-for-profit must register, and you must be affiliated with it. Group A countries (lowest GNI per capita) get free access; Group B countries pay a low annual fee. Unaffiliated independent researchers are not eligible.

### [SocArXiv](https://osf.io/preprints/socarxiv)

`Free (registration), email` · beginner 5/5 · preprint server

Open archive of social science papers hosted on OSF Preprints and run by an academic steering committee at the University of Maryland. Free to post and free to read; every preprint gets a DOI and is indexed by Google Scholar, OpenAlex and Dimensions.

**Access.** Web interface: create a free OSF account, upload a PDF, add metadata and a licence, and it is live after a light moderation check. Full-text search on the site; metadata and full text also reachable through the OSF API (https://api.osf.io/v2/preprints/) and via OpenAlex.

**Caveats.** For researchers with no journal access and no library budget, posting here is the cheapest way to make work citable and findable. Check your target journal's preprint policy first - most social science journals now permit it, but a few still do not. The Center for Open Science's 2026 restructuring explicitly preserves OSF Preprints and OSF Registries; it is the separate OSF Projects workspace that is being retired.

### [SSRN](https://www.ssrn.com/)

`Free (registration), email` · beginner 5/5 · working paper repository

Over 1.5 million full-text papers from more than 1.9 million authors across 69 disciplines, with over 300 million downloads recorded. In political science, law, economics and management it is often where a paper circulates for years before journal publication.

**Access.** Web interface: browse and download most papers with no account; free registration to post your own work to a subject network or to set up email alerts on topics and authors.

**Caveats.** Owned by Elsevier since 2016, which is worth knowing when deciding where to deposit: SSRN is a commercial platform, not community-governed infrastructure, and its terms and metadata openness are Elsevier's to change. Some papers are abstract-only where the author has not posted full text. For a non-commercial alternative in the same fields, SocArXiv and APSA Preprints cover much of the same ground.

### [The Wikipedia Library](https://wikipedialibrary.wmflabs.org/)

`Free (registration), credentialing` · beginner 3/5 · database access for unaffiliated researchers

Gives established Wikipedia editors free accounts to more than 100 of the world's top subscription-only databases, with content in 32 languages - including collections that cover social science journals, newspapers and reference works normally locked behind institutional subscriptions.

**Access.** Log in with your Wikipedia account at the library card platform. Access to the general collection is automatic once you meet the criteria; some publishers require a short individual application through the same interface.

**Caveats.** The eligibility bar is concrete and takes months to clear: 500+ edits, 6+ months of editing, 10+ edits in the last 30 days, and no active blocks. That makes it a plan you start now for research you will do later, not a same-day solution. Access is granted for improving Wikipedia; using it is legitimate for your own reading, but the accounts exist for encyclopaedic work and publishers do audit usage patterns.

### [Unpaywall](https://unpaywall.org/)

`Free` · beginner 5/5 · legal open access finder

Harvests legal open access copies of paywalled articles from institutional repositories, preprint servers and publisher sites, and points you at them. Built by the same non-profit (OurResearch) that runs OpenAlex; the data underlie the OA status fields in many library systems.

**Access.** Browser extension for Chrome and Firefox: a green tab appears on an article page when a free legal copy exists. Free REST API for programmatic use: https://api.unpaywall.org/v2/{doi}?email=you@example.com - the email parameter is mandatory and must be real.

**Caveats.** Entirely legal - it indexes copies the authors or publishers made available, unlike shadow libraries. It cannot help where no OA copy exists, which is still the case for much of the older social science monograph and journal literature. Heavy API use should stay within the documented daily call limit; bulk users should take the data snapshot instead of hammering the endpoint.

## Compute

### [Google Colab](https://colab.research.google.com/)

`Free tier, email` · beginner 5/5 · hosted notebooks with free GPU

Hosted Jupyter notebooks with no setup and free access to CPU, GPU and TPU runtimes. Google's own FAQ states Colab is free of charge and that resources are 'not guaranteed and not unlimited', with usage limits that fluctuate and priority given to users actively working in a notebook.

**Access.** Web interface with a Google account: open or upload a notebook, choose Runtime > Change runtime type for a GPU or TPU, and !pip install whatever you need. Notebooks save to Google Drive, open directly from GitHub URLs, and can mount Drive for data files. Paid Pro/Pay-As-You-Go tiers buy longer sessions and better accelerators.

**Caveats.** For social scientists the honest use case is a bounded compute job - fine-tuning a text classifier, running Whisper over interview audio, a big simulation sweep - not a permanent workspace: runtimes are ephemeral and files vanish when they recycle, idle sessions are disconnected, and free GPU allocation is best-effort and can be refused at peak times. R support is second-class; Posit Cloud is the better free R environment. Do not upload confidential or identifiable interview data to a consumer Google account without checking your ethics approval and data protection plan.

### [Kaggle Notebooks](https://www.kaggle.com/code)

`Free tier, email` · beginner 4/5 · hosted notebooks with weekly GPU quota

Free hosted Python and R notebooks with attached datasets, GPU and TPU accelerators, persistent notebook versions and a large public dataset library. Unlike Colab, accelerator time comes as an explicit weekly quota shown in the session panel, which makes budgeting a job possible.

**Access.** Web interface at kaggle.com/code with a free account: create a notebook, attach a public dataset or upload your own (private by default), enable GPU/TPU in the settings pane, and commit the notebook for a clean reproducible run with saved outputs. Datasets can also be scripted with pip install kaggle plus an API token from your account page.

**Caveats.** Accelerator use is capped per week (Kaggle's long-published figures have been 30 GPU-hours and 20 TPU-hours, but the authoritative number is the one in your session sidebar and Kaggle has changed it before - check there rather than trusting any tutorial). Phone verification is required before GPUs are enabled, which is a real barrier for some users. Sessions have a maximum runtime, so long jobs must checkpoint to /kaggle/working. Notebooks are public unless set private - check before committing work on unpublished data.

### [Posit Cloud](https://posit.cloud/)

`Free tier, email` · beginner 5/5 · browser-based R and Python environment

RStudio and Jupyter notebooks running in the browser with nothing to install, which matters if your only machine is a low-spec laptop, a Chromebook or a shared lab computer. Projects are shareable by link, making it usable for teaching and for collaborative replication.

**Access.** Web interface: sign up free, create a project, and you get a full RStudio session with package installation. The Cloud Free plan includes 25 project hours per month, up to 25 projects and one shared space. A Cloud Student plan costs about US$5/month for more hours.

**Caveats.** 25 project hours a month is genuinely tight - it is enough to learn on, to run a seminar, or to reproduce someone's analysis, but not enough to be your main working environment for a dissertation. Free instances are memory-limited, so large IPUMS or GSS cumulative files will exhaust RAM. For anything sustained, install R locally (free) and use Posit Cloud for sharing and teaching.

## Publishing

### [AEA RCT Registry](https://www.socialscienceregistry.org/)

`Free (registration), email` · beginner 4/5 · trial preregistration

The American Economic Association's registry for randomised controlled trials in the social sciences, listing 12,677 studies with locations in 171 countries as of 28 August 2026. Each record documents the intervention, sample, randomisation, outcomes, timeline and (optionally) an uploaded pre-analysis plan, and receives a citable AEARCTR identifier.

**Access.** Web interface: browsing, advanced search and reading full trial records need no account; a free account is required to register a trial, and the registration form takes roughly twenty minutes. The whole registry is downloadable as a bulk data file from the Data page for meta-research.

**Caveats.** Now expected by most development economics, political economy and field experiment journals. The point is registering before enrolment starts - the record shows registration and start dates, so late registration is visible. Pre-analysis plans can be embargoed until the trial concludes. It is a registry, not a repository: data and code still need Dataverse, OSF or Zenodo. For non-experimental, lab or qualitative work, OSF Registries is the usual venue; EGAP stopped accepting registrations on 15 October 2023 and now points here and to OSF.

*Also listed under: econ-finance.*

### [Demographic Research](https://www.demographic-research.org/)

`Free` · beginner 5/5 · diamond open access journal

Peer-reviewed platinum (diamond) open access journal of the population sciences, published by the Max Planck Institute for Demographic Research since 1999. No subscription charges and no author charges; publishes full articles, descriptive findings, research materials and replicable-article flags.

**Access.** Web interface: read and download every article free, no account. Submit through the site's author account; the journal runs a rolling, fast-turnaround publication model with articles appearing individually rather than in fixed issues.

**Caveats.** Genuinely free at both ends - no APC, funded by the Max Planck Society - which makes it one of the few high-visibility journals an unfunded researcher can publish in without a waiver request. Scope is demography and population studies; adjacent sociology or policy work needs a clear demographic core to fit.

### [Journal of Artificial Societies and Social Simulation (JASSS)](https://www.jasss.org/)

`Free` · beginner 4/5 · diamond open access journal

Peer-reviewed journal of agent-based modelling and computational social science, published continuously since 1998, free to read and free to publish in. The reference outlet for simulation-based social science, with a strong norm of publishing model code alongside articles.

**Access.** Web interface: all issues free to read online with no account. Submit through the journal's system; authors are expected to make model code available (many articles link to CoMSES/OpenABM or GitHub repositories).

**Caveats.** No author fees and no subscription, run by the community rather than a commercial publisher. Narrow scope: your paper needs a simulation or computational-model contribution, not merely quantitative analysis. Pair it with NetLogo or Mesa for the modelling side.

### [OSF Registries](https://osf.io/registries)

`Free (registration), email` · beginner 4/5 · preregistration

Free registry for study preregistrations and registered reports, with templates covering pre-analysis plans for experiments, secondary data analysis, qualitative research and replications. Registrations are time-stamped, get a DOI, and can be embargoed for up to four years before becoming public.

**Access.** Web interface: free OSF account, choose a registration template, complete it, and submit. Registrations are searchable and citable; the OSF API exposes registration metadata programmatically.

**Caveats.** Preregistration is increasingly expected by reviewers in experimental and quantitative social science, and this is the free standard venue. Important 2026 context: the Center for Open Science is retiring the separate OSF Projects workspace - from 16 November 2026 no new projects can be created and after 19 February 2027 all projects become read-only - but OSF Registries and OSF Preprints continue unchanged, with COS pointing users to Zenodo for data, materials and code.

### [Zenodo](https://zenodo.org/)

`Free, email` · beginner 5/5 · data, code and materials repository

General-purpose research repository hosted by CERN, funded through EU infrastructure programmes. Mints a DOI for any deposit - datasets, code, questionnaires, coding schemes, presentations - supports versioning with a concept DOI, and integrates with GitHub to archive a release automatically.

**Access.** Web interface with a free account (ORCID or email login); REST API for scripted deposits. Storage: 50 GB and up to 100 files per record by default, plus an additional 150 GB account allowance you can distribute across uploads; higher quotas on request.

**Caveats.** The Center for Open Science now recommends Zenodo as the destination for material leaving OSF Projects, which makes it the default home for social science replication packages. It is a generalist repository, so it does no curation - no disclosure review, no metadata cleanup, no format migration. If your data contain human subjects, you are solely responsible for the anonymisation before upload.

## Funding

### [APSA Centennial Center Research Grants](https://connect.apsanet.org/centennialcenter/research-grants/)

`Free, application` · beginner 3/5 · small research grants

The American Political Science Association's grant programme, awarding over US$100,000 a year in small research grants through spring and summer cycles, with the Small Research Grant Program explicitly aimed at political scientists not employed at PhD-granting departments and at those in non-tenure-track or contingent positions.

**Access.** Online application through the APSA Centennial Center portal; spring deadline is typically mid-March, with a second summer cycle. Individual awards are small (roughly up to US$2,500) and cover research expenses such as data purchase, transcription, fieldwork travel and RA time.

**Caveats.** One of the very few programmes designed around exactly the audience this catalogue serves - contingent faculty, community college faculty and graduate students, with stated priority for applicants with limited departmental resources. You must be an APSA member to apply, and membership costs money (though APSA has income-scaled rates). Political science only.

### [Spencer Foundation Small Research Grants on Education](https://www.spencer.org/grant_types/small-research-grant)

`Free, application` · beginner 3/5 · education research grants

Field-initiated grants of up to US$50,000 for education research projects lasting one to five years, open internationally and explicitly welcoming sociology, anthropology, economics, history, philosophy and psychology approaches and qualitative, mixed-methods, ethnographic and participatory designs. Two application cycles per year.

**Access.** Online application through the Spencer portal (https://spencer.smartsimple.us/), with the full Request for Proposals published there. Indirect costs are not permitted; eligible investigators may request supplemental funds for a course release.

**Caveats.** Two hard eligibility gates: PIs and Co-PIs must hold an earned doctorate (graduate students may be on the team but cannot be PI), and Spencer does not award grants to individuals - the PI must be administered by a non-profit or public institution with 501(c)(3) status or equivalent. Proposals must be in English with US-dollar budgets. Check the site for the current deadline; cycles close and reopen.

### [Wenner-Gren Foundation grants and fellowships](https://wennergren.org/grants-fellowships/)

`Free, application` · beginner 3/5 · anthropology research grants

The main international funder of anthropological research that funds individuals directly: Dissertation Fieldwork Grants and Post-PhD Research Grants of up to US$25,000 each, plus Wadsworth International Fellowships and the Wadsworth African Fellowship, the Fejos and Hunt postdoctoral fellowships, Engaged Research grants and conference/workshop grants.

**Access.** Online application through the Foundation's portal; the Dissertation Fieldwork and Post-PhD deadlines are 1 May and 1 November each year, the portal opens two months before each deadline, and decisions take about six months. Each programme page carries the eligibility rules, allowable costs and the application guide, and the Foundation runs free proposal-writing webinars.

**Caveats.** Unusually open eligibility, which is why it belongs in a catalogue aimed at under-resourced researchers: Post-PhD applicants may be 'qualified scholars of any nationality or institutional affiliation', and the page states that 'independent scholars and senior scholars are welcome to apply'. Grants are non-renewable, pay no institutional overhead and no grant administration fees. Anthropology only (socio-cultural, linguistic, biological and archaeology, or the local equivalents); Dissertation Fieldwork applicants must be enrolled in a doctoral programme.

### [Wikimedia Research Fund](https://meta.wikimedia.org/wiki/Grants:Programs/Wikimedia_Research_%26_Technology_Fund/Wikimedia_Research_Fund)

`Free, application` · beginner 3/5 · research grants for individuals

Wikimedia Foundation fund supporting research on or about Wikimedia projects, explicitly across the humanities, social sciences, computer science, education and law. Requests run from US$2,000 to US$50,000 (Type 1 and 3), with larger multi-year awards up to US$150,000 (maximum US$75,000 per year). Typically 4-10 grants per round.

**Access.** Open call announced annually on Meta-Wiki; proposals are submitted through the Wikimedia grants portal. Individuals, informal groups and organisations may all apply - no institutional administering body is required.

**Caveats.** Unusually accessible: it funds individuals directly, and the review criteria explicitly prioritise applicants who have limited access to research funding and who are from regions under-represented in the Wikimedia research community. The constraint is topical - your project must genuinely be about Wikimedia projects or their communities - and applicants should be established Wikimedia researchers or team up with one.

## Learning

### [Causal Inference: The Remix (Mixtape)](https://mixtape.scunning.com/)

`Free` · beginner 3/5 · causal inference textbook

Scott Cunningham's causal inference text, free online, covering DAGs, potential outcomes, unconfoundedness, regression discontinuity, instrumental variables, difference-in-differences (including the recent heterogeneity-robust estimators) and synthetic control, with worked code in both R and Stata.

**Access.** Read free at mixtape.scunning.com. Code and datasets for every chapter are downloadable; the Stata and R implementations run side by side so you can follow in whichever your department uses.

**Caveats.** The online second edition is explicitly a work in progress as of the 2026 academic year - the authors flag typos and bugs and ask readers to report them - so cross-check anything surprising against the printed edition or the primary papers. The panel-data chapters are the current strength; they cover the post-2020 difference-in-differences literature that older texts predate.

*Also listed under: econ-finance.*

### [Causal Inference: What If](https://miguelhernan.org/whatifbook)

`Free` · beginner 2/5 · causal inference textbook

Hernan and Robins's causal inference textbook, downloadable in full at no cost: part 1 covers causal inference without models (counterfactuals, exchangeability, DAGs, selection and measurement bias), part 2 covers models (IP weighting, standardisation, g-estimation, propensity scores, instrumental variables), part 3 covers complex longitudinal data with time-varying treatments.

**Access.** Free PDF of the current version from the author's page (updated in place, so re-download rather than relying on an old copy). Code and data reproducing every analysis are maintained by the authors' group in R, Stata, SAS and Python.

**Caveats.** The reason to have this alongside The Effect and the Mixtape is part 3: time-varying treatments, marginal structural models and g-methods are barely covered by the economics-style texts, and they are exactly what longitudinal social science data demand. Written from an epidemiology tradition, so the notation and examples are clinical and the ramp is steeper than The Effect. The authors revise the PDF without documenting changes - record the version date you cite.

*Also listed under: medicine.*

### [DIME Wiki (World Bank DIME Analytics)](https://dimewiki.worldbank.org/)

`Free` · beginner 4/5 · field research and impact evaluation handbook

Public-good wiki from the World Bank's DIME Analytics team covering the whole workflow of applied field research: experimental and quasi-experimental design, power calculations, research ethics and IRB, questionnaire design, primary data collection and field management, data cleaning, reproducible analysis, publication and data publishing.

**Access.** Read free on the web with no account; pages cross-link to templates, checklists and example code. The companion Development Research in Practice handbook is a free PDF, and the team's Stata packages (ietoolkit, iefieldkit) are on SSC and GitHub - ssc install ietoolkit.

**Caveats.** Written for World Bank impact evaluations, so examples are field experiments in low- and middle-income countries and the code is Stata-first - but the data management, reproducibility and field-team sections transfer to any survey project, and there is very little else this practical that is free. It is a wiki: some pages are thorough, some are stubs, and revision dates vary. The site sits behind a bot check, so scripted fetches may fail even though a browser works.

*Also listed under: econ-finance.*

### [MIT OpenCourseWare](https://ocw.mit.edu/)

`Free` · beginner 4/5 · university course materials

Complete materials from MIT courses - lecture notes, problem sets with solutions, exams and video lectures - including the political science (course 17), economics (14), anthropology (21A), urban studies and planning (11) and statistics offerings that social scientists need. No registration required.

**Access.** Web interface: browse by department or search. Most courses offer a full ZIP download for offline study, and 'OCW To Go' packages material for mobile devices. Materials are licensed CC BY-NC-SA, so you may reuse and adapt them for teaching.

**Caveats.** Genuinely free and unusually valuable where you have no local course to sit in on, and the offline packages matter on a bad connection. It is course material, not a course: no instructor, no cohort, no credential, and older courses are not updated - check the term listed before relying on software instructions or reading lists.

### [Statistical Rethinking (course materials)](https://github.com/rmcelreath/stat_rethinking_2026)

`Free` · beginner 2/5 · Bayesian statistics course

Richard McElreath's full graduate course on Bayesian data analysis and causal inference, re-taught and re-released annually (the 2026 edition was updated in March 2026). Slides, homework with solutions, R code and a complete video lecture series are all public.

**Access.** Clone or browse the GitHub repository for slides, homework and scripts; lecture videos stream free on YouTube. Code uses the rethinking R package (install from GitHub) and there are community ports to brms/tidyverse, Python/PyMC, Stan, Julia and NumPyro.

**Caveats.** Widely regarded as the best free route into Bayesian modelling and DAG-based causal reasoning for social scientists, and it teaches the reasoning rather than software recipes. The accompanying textbook is a paid CRC Press book - the course is usable without it, but the lectures are pitched assuming the reading. Installing rethinking pulls in Stan, which needs a working C++ toolchain.

### [The Effect: An Introduction to Research Design and Causality](https://theeffectbook.net/)

`Free` · beginner 4/5 · causal inference textbook

Nick Huntington-Klein's textbook on research design with observational data, free in full as a Bookdown web version alongside the paid Chapman & Hall print edition. Part 1 covers design, DAGs and identification; Part 2 covers regression, matching, fixed effects, event studies, difference-in-differences, IV and regression discontinuity.

**Access.** Read free at theeffectbook.net. Run the examples with the causaldata package - install.packages('causaldata') in R, ssc install causaldata in Stata, or pip install causaldata in Python. Free companion video series, homework assignments, intro coding materials for R/Stata/Python, and course slides.

**Caveats.** The most approachable free causal inference text for people who have not had a formal econometrics sequence, and the R/Stata/Python parity is unusual and genuinely useful in mixed-language departments. Deliberately light on proofs - if you need the asymptotics you will still want a standard econometrics text. Last built October 2025 and now updated only to stay consistent with the print edition.

### [The Turing Way](https://book.the-turing-way.org/)

`Free` · beginner 4/5 · reproducible research handbook

Community-written open handbook on reproducible, ethical and collaborative data science, organised as guides to reproducible research, project design, communication, collaboration and ethical research. Covers version control, environments, licensing, data management plans, research ethics and open collaboration practice.

**Access.** Read free online, or download chapters; source and contribution workflow on GitHub. Licensed CC BY 4.0, so you can reuse chapters directly in your own teaching or lab documentation. An open Slack workspace and newsletter support the community.

**Caveats.** Explicitly designed to be dipped into rather than read cover to cover - start from the concept you need now. Supported by the Alan Turing Institute but written by a global volunteer community, so depth varies by chapter and some sections are more mature than others. Domain-general rather than social-science-specific: the ethics and data management chapters need supplementing with your own field's human-subjects rules.

## Community

### [Cross Validated](https://stats.stackexchange.com/)

`Free` · beginner 4/5 · statistics Q&A

Stack Exchange site for statistics, machine learning, data analysis and data visualisation, with 219,623 questions, 219,902 answers and 437,864 registered users (Stack Exchange API, 28 August 2026). The de facto place where applied questions about survey weights, multilevel models, SEM identification and causal identification get answered by practising methodologists.

**Access.** Web interface: search and read with no account; free registration to ask, answer or vote. All content is CC BY-SA licensed. Questions about R or Python code go to Stack Overflow instead; conceptual and methodological questions belong here.

**Caveats.** About 68,000 questions are unanswered, so a badly framed question sinks without trace - include your design, your sample size, what you have tried, and a reproducible example. The site is strict about scope: 'which test should I use for my dissertation' with no detail gets closed. Answer quality is high but not peer reviewed; check the credentials and the citations in an answer before building on it.

### [EGAP (Evidence in Governance and Politics)](https://egap.org/)

`Free` · beginner 4/5 · research network and methods guides

Research network on governance, accountability and political behaviour whose site publishes free Methods Guides - ten-point primers on randomisation, power analysis, clustering, pre-analysis plans, spillovers, survey experiments and related design problems - plus Learning Days teaching materials and coursebook, policy briefs, and the Metaketa coordinated multi-site replication programmes.

**Access.** Web interface, everything free with no account: Methods Guides and policy briefs read in the browser, and the Learning Days coursebook and exercises (with R code) download directly. Metaketa project pages link to the pooled data and pre-analysis plans.

**Caveats.** The Methods Guides are the most usable short reference on designing field and survey experiments in political science, and the Learning Days materials were built explicitly for researchers outside well-resourced departments. Network membership is by nomination, but nothing you need is behind it. Note that EGAP's own design registry stopped accepting registrations on 15 October 2023 - register new studies at OSF Registries or the AEA RCT Registry instead.

### [The Carpentries](https://carpentries.org/)

`Free` · beginner 5/5 · coding and data skills lessons

Volunteer-run organisation teaching foundational coding and data skills to researchers: 5,500 instructors, 5,014 workshops delivered and 72 countries reached as of August 2026. Lessons cover the Unix shell, Git, R, Python, SQL, OpenRefine and data organisation in spreadsheets, including a Data Carpentry curriculum written for social scientists.

**Access.** All lesson material is openly licensed and free to work through alone on the lesson websites, with the example datasets included - the social science track ('R for Social Scientists', 'Data Analysis and Visualization in R for Social Scientists') is the closest fit for survey workflows. Workshops are listed on the public calendar; instructor training is run regularly with places prioritised for member organisations.

**Caveats.** Self-teaching from the lessons costs nothing and needs no account - that is the part that matters for an unaffiliated researcher. Attending an official two-day workshop usually costs money or requires a hosting institution, and certified instructor training favours members of Partner organisations. The material is deliberately foundational: it will get you from spreadsheet-only work to reproducible scripting, not to advanced modelling.
