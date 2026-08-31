# Economics & finance

Part of [research-vault](../README.md). 82 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (40) · [Software](#software) (14) · [Literature](#literature) (8) · [Compute](#compute) (1) · [Publishing](#publishing) (4) · [Funding](#funding) (5) · [Learning](#learning) (7) · [Community](#community) (3)

## Data

### [AQR Data Sets](https://www.aqr.com/Insights/Datasets)

`Free` · beginner 3/5 · asset pricing factor returns

Public return files behind AQR's published papers: Betting Against Beta, Quality Minus Junk (factors plus 6- and 10-portfolio sorts), The Devil in HML's Details, Value and Momentum Everywhere, and the AQR momentum indices, in daily and monthly versions, with US series starting in the 1950s and international samples from 1986; the momentum index file was current through 31 July 2026 on 2026-08-28.

**Access.** Direct Excel download per dataset from the datasets page, no account. Each file's first sheet documents construction and sample; pair with the Kenneth French library for the standard factors these are meant to be measured against.

**Caveats.** Use is governed by AQR's terms of use and expects citation of the underlying paper; these are outputs, not inputs, so you cannot re-sort or extend them without the commercial security-level data (CRSP/Compustat/XpressFeed) they were built from. Update cadence differs by file — some refresh monthly, others were frozen at the paper's sample end, so check the last date in the sheet before assuming currency. Factor definitions differ in detail from French's (that is the point of the 'Devil in HML's Details' file), so do not treat AQR HML and French HML as the same series.

### [Atlas of Economic Complexity (Harvard Growth Lab)](https://atlas.hks.harvard.edu/)

`Free` · beginner 4/5 · bilateral product-level trade and complexity metrics

Reconciled bilateral trade data covering over 6,000 products and 250 countries and territories, built from UN Comtrade by mirroring exporter and importer reports with reliability weights and harmonising product codes across classification vintages. Available as HS 6-digit series (HS 1992 from 1995, HS 2012 from 2012, HS 2022 from 2022) and a long-run SITC Rev. 2 series from 1962 to the present, plus services trade from 1980 and the economic complexity index, rankings and country profiles built on top.

**Access.** Bulk CSV downloads at https://atlas.hks.harvard.edu/data-downloads/ with column filters to find the dataset you need, or query the GraphQL API documented on the Growth Lab's GitHub; the visual Explore tool and country profiles work in the browser with no account.

**Caveats.** About 95% of the data is refreshed once a year, typically April-June, and revisions rewrite history (most 2024 trade data only appears in 2026), so archive the file you used for replication. Figures in the visualisations can differ slightly from the bulk downloads because the two are refreshed on different schedules. Country profiles and rankings exclude countries with fewer than 1 million people, under $1bn average annual trade, or unreliable reporting - absence from the rankings is not absence of trade. Each downloaded file carries its own citation requirement.

### [BEA Data API (Bureau of Economic Analysis)](https://apps.bea.gov/API/)

`Free (registration), api-key` · beginner 3/5 · US national, regional and international accounts

Programmatic access to the US Bureau of Economic Analysis statistics: NIPA and underlying NIPA tables (GDP and its components), GDP by industry and underlying GDP by industry, fixed assets, regional income, employment and GDP for states, counties and metro areas, international transactions and trade in services, and direct investment/multinational enterprise data.

**Access.** Register at https://apps.bea.gov/API/signup/ with name, organisation and a non-disposable email address, click the activation link, and use the returned UserID as the key: https://apps.bea.gov/api/data?UserID=KEY&method=GetData&datasetname=NIPA&TableName=T10101&Frequency=Q&Year=2024&ResultFormat=JSON. Metadata methods (GetDataSetList, GetParameterList, GetParameterValues) let you discover table names before pulling data.

**Caveats.** Throttled per key at 100 requests per minute, 100 MB of data per minute and 30 errors per minute; exceeding any of these returns HTTP 429 with a RETRY-AFTER header and a temporary block, so write single-threaded clients that back off. Disposable email addresses are rejected at signup. The API serves currently published estimates, not vintages of past releases - for real-time/vintage work use the Philadelphia Fed's Real-Time Data Set instead.

### [BIS Statistics](https://data.bis.org/)

`Free` · beginner 3/5 · international banking & financial statistics

The canonical source for cross-border banking (locational and consolidated banking statistics), OTC derivatives, debt securities, effective exchange rates, residential and commercial property prices, credit-to-GDP gaps, debt service ratios and a long central bank policy rate series. The public SDMX API served 29 BIS dataflows when queried on 2026-08-28 (28 WS_* data flows plus the BIS_REL_CAL release calendar).

**Access.** No key. SDMX v1 REST: https://stats.bis.org/api/v1/data/BIS,WS_CBPOL,1.0/... ; discover flows at https://stats.bis.org/api/v1/dataflow/BIS. Full-dataset CSV bulk files from data.bis.org. Also mirrored in DBnomics under provider BIS.

**Caveats.** BIS data is free to use with attribution but not to redistribute commercially. Banking statistics are reported by BIS-member central banks only, so 'the world' means roughly the reporting set; counterparty-country detail is confidential in places and comes back suppressed rather than zero.

### [BLS Public Data API](https://www.bls.gov/developers/)

`Free (registration), api-key` · beginner 4/5 · US labour statistics

Programmatic access to CPS and CES employment and unemployment, CPI and PPI, JOLTS, employment cost index, occupational employment and wages, and productivity series. Verified live and key-free on 2026-08-28 (v1 request for LNS14000000 returned July 2026 unemployment at 4.1%).

**Access.** v1 needs no key: POST or GET https://api.bls.gov/publicAPI/v1/timeseries/data/LNS14000000. v2 uses a free registered key and raises the per-day, per-query series and per-query year limits. Python: `pip install bls-datasets` or plain `requests`. R: `install.packages('blsAPI')`.

**Caveats.** Daily query quotas apply to both versions and are stricter for unregistered v1 — the registered key is free and worth getting on day one. BLS actively blocks automated access to its documentation and website pages, so read the FAQ in a browser. Series IDs are structured codes, not names; build them from the BLS series-ID format tables.

### [CEPII databases (BACI, Gravity, TRADHIST)](https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele.asp)

`Free (registration), email` · beginner 3/5 · trade & gravity datasets

BACI reconciles UN Comtrade into a consistent bilateral trade panel covering more than 5,000 products and 200 countries (last updated January 2026). The Gravity database ships trade, GDP, population, distance, contiguity, language, colonial ties and trade agreements for all country pairs 1948-2020; TRADHIST extends bilateral trade and gravity back to 1827.

**Access.** Direct download of CSV/Stata/parquet files from cepii.fr after a free account. In R, read the files directly (`haven::read_dta()`, `arrow::read_parquet()`); the `cepiigravity` package is not on CRAN — the CEPII package that is on CRAN is `cepiigeodist` (GeoDist distances and country characteristics only).

**Caveats.** Academic and non-commercial use with citation; BACI is derived from Comtrade so UN terms flow through. Full BACI is a multi-gigabyte panel — filter by year on read rather than loading the whole thing on a laptop. TRADHIST has not been updated since November 2016. For economic complexity measures rather than raw flows, Harvard Growth Lab's Atlas (atlas.hks.harvard.edu/data-downloads) publishes free cleaned trade covering 6,000+ products and 250 countries, with SITC from 1962 and HS from 1995.

### [Damodaran Online data](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html)

`Free` · beginner 4/5 · valuation & cost-of-capital reference data

Aswath Damodaran's annually rebuilt reference datasets for corporate finance: industry-average betas, costs of capital and debt, equity risk premiums and country risk premiums, trading multiples (PE, EV/EBITDA, price-to-book), operating margins, effective tax rates and reinvestment rates, split into US, Europe, Japan, emerging-market, China, India and global aggregates. The current vintage was updated on 9 January 2026, with the next major update stated for early January 2027.

**Access.** Direct download of Excel/CSV files per dataset from the data page, no account; archived prior-year vintages are kept on the same site so you can pull a consistent annual series.

**Caveats.** Industry aggregates only — company-level files were withdrawn because the underlying vendor licence no longer permits redistribution. Updated once a year, so figures are stale for most of the calendar and are wrong as of-date inputs for a specific valuation date. Industry groupings are Damodaran's own, not SIC/NAICS/GICS, so merging to any other dataset needs a hand-built crosswalk. These are teaching and benchmarking inputs, not audited data, and the estimation choices (e.g. how the implied ERP is computed) are documented in his papers and worth reading before citing.

### [DBnomics](https://db.nomics.world/)

`Free` · beginner 4/5 · macro data aggregator

Aggregates and normalises economic series from 93 providers (verified via the API on 2026-08-28) — including IMF, OECD, Eurostat, BIS, BLS, BEA, ECB, national central banks and statistical offices — into one search index and one query grammar. Run by CEPREMAP.

**Access.** No key. REST: https://api.db.nomics.world/v22/series/IMF/WEO/USA.NGDPD?observations=1. Python: `pip install dbnomics` then `dbnomics.fetch_series('IMF','WEO','USA.NGDPD')`. R: `install.packages('rdbnomics')`.

**Caveats.** A convenience layer, not the system of record: series are mirrored on a provider-dependent schedule, so for anything time-critical (a policy rate this morning) go to the source. Dataset codes are versioned (e.g. WEO:2025-04) and old vintages get frozen, which is useful but means hard-coded codes eventually 301-redirect.

### [ECB Data Portal](https://data.ecb.europa.eu/)

`Free` · beginner 4/5 · euro area monetary & financial data

Euro area monetary policy, banking, balance sheet, securities, payments and exchange rate statistics. The public SDMX API exposed 104 ECB dataflows when queried on 2026-08-28 and returns CSV or SDMX-ML with no key.

**Access.** No key. REST: https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?lastNObservations=10&format=csvdata. Python: `pip install sdmx1` or `ecbdata`. R: via `rsdmx` or DBnomics. CSV download buttons throughout the web UI.

**Caveats.** This replaced the old Statistical Data Warehouse (sdw.ecb.europa.eu); SDW URLs and the sdw-wsrest.ecb.europa.eu API host in older scripts have been superseded by data-api.ecb.europa.eu. Series keys are long dot-separated strings — build them in the web UI first, then copy into code.

### [Economic Policy Uncertainty indices](https://www.policyuncertainty.com/)

`Free` · beginner 5/5 · text-based uncertainty indices

Baker-Bloom-Davis newspaper-text EPU indices for more than 50 countries and regions plus a global index, categorical EPU (trade, monetary, fiscal, climate policy), US state-level EPU, and related measures including geopolitical risk and firm-level uncertainty. Mostly monthly, some daily.

**Access.** Direct CSV/Excel download per index, no account. Most files are a date column plus one index column — trivially readable with `pandas.read_excel()`.

**Caveats.** CC BY 4.0. The indices are counts of newspaper articles matching keyword triples, so they inherit their newspapers' editorial and language coverage; cross-country level comparisons are weaker than within-country time variation. Base periods and normalisations differ between indices — check each file's readme before pooling.

### [Eurostat](https://ec.europa.eu/eurostat/data/database)

`Free` · beginner 4/5 · European official statistics

Harmonised statistics for EU/EEA and candidate countries — national accounts, HICP, labour force survey aggregates, structural business statistics, regional (NUTS) data — with a JSON-stat API that needs no key (verified live 2026-08-28).

**Access.** No key. REST: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_gdp?format=JSON&geo=DE&na_item=B1GQ&unit=CP_MEUR. R: `install.packages('eurostat')` then `get_eurostat('nama_10_gdp')`. Python: `pip install eurostat`. Bulk TSV/gz download service for whole tables.

**Caveats.** Reuse is free with attribution under the Commission's reuse policy. Microdata (EU-SILC, LFS, HBS) is a separate track: it requires a formal research-entity application through Eurostat's microdata access unit, is not open, and typically takes months — the API covers aggregates only.

### [FDIC BankFind Suite API](https://api.fdic.gov/banks/docs)

`Free` · beginner 3/5 · US bank call reports & failures

Institution-level data on every FDIC-insured US bank: charter and structure, branch locations, quarterly financial (call report) aggregates, failures, and merger history. Verified live and key-free on 2026-08-28 (1,286 California institutions returned).

**Access.** No key. REST on the current host: https://api.fdic.gov/banks/institutions?filters=STNAME:California&fields=NAME,CITY,ASSET&limit=100 (verified live 2026-08-28, meta.total 1,286); also /banks/financials, /banks/locations, /banks/failures, /banks/history and /banks/summary. The old banks.data.fdic.gov/api/... paths 301-redirect here, which breaks clients that do not follow redirects or that POST. Plain `requests` plus `pandas.json_normalize` is enough; results nest under data[].data.

**Caveats.** US-insured depositories only — no credit unions (that is NCUA), no bank holding company consolidated data (that is the Chicago Fed / FFIEC). Field names are call-report mnemonics; the data dictionary on the docs page is not optional reading. Historical panels have structural breaks at merger events that you must handle with the /history endpoint.

### [FRED (Federal Reserve Economic Data) & ALFRED](https://fred.stlouisfed.org/)

`Free (registration), api-key` · beginner 5/5 · macroeconomic time series

St. Louis Fed aggregator of US and international macro series (national accounts, labour, prices, policy and market rates, money and banking, regional). ALFRED, its sibling, serves the vintage/real-time versions of each series as they were originally published, which is what you need for honest forecast evaluation.

**Access.** Free API key from fred.stlouisfed.org/docs/api/api_key.html; endpoint https://api.stlouisfed.org/fred/series/observations?series_id=GDPC1&api_key=...&file_type=json. Python: `pip install fredapi` then `Fred(api_key=...).get_series('UNRATE')`. R: `install.packages('fredr')`. Web UI allows CSV/Excel download with no key.

**Caveats.** The API key is instant and free but is required for programmatic access; the website itself is browsable without one. Some series are redistributed under third-party terms (e.g. Haver, S&P) and carry redistribution restrictions — check the series' notes field before republishing values. For US national and regional accounts at source resolution (input-output tables, GDP by state and county, price parities), the BEA's own free-key API at apps.bea.gov/API/signup goes deeper than the FRED mirror.

### [FRED-MD and FRED-QD](https://www.stlouisfed.org/research/economists/mccracken/fred-databases)

`Free` · beginner 3/5 · macro forecasting benchmark panels

McCracken and Ng's monthly and quarterly balanced panels of US macro series, released as a single CSV with a transformation-code header row, plus archived monthly vintages. This is the standard benchmark dataset for factor models, dynamic factor forecasting and big-data macro papers.

**Access.** Direct CSV download from the St. Louis Fed page (current.csv plus a monthly vintage archive). Python: read the CSV directly — the first data row holds the transformation codes, so parse it separately — or `pip install fredmd`. R: the `fbi` package is GitHub-only, `remotes::install_github('cykbennie/fbi')`; there is no CRAN release.

**Caveats.** Not a raw data source: series are pre-selected and the transformation codes prescribe differencing/logging, which is the point but also a constraint. The panel composition changes across vintages as underlying FRED series get discontinued, so a paper that says 'FRED-MD' without naming the vintage is not reproducible.

### [Global Trade Alert](https://www.globaltradealert.org/)

`Free (registration), email` · beginner 3/5 · trade and industrial policy interventions

Independent monitoring of government measures that affect foreign commerce, with more than 52,500 recorded unilateral commercial policy interventions since November 2008. Each entry is coded with implementing and affected jurisdictions, announcement and implementation dates, instrument (tariff, subsidy, export curb, public procurement, FDI measure and so on), affected sectors and products, and an evaluation of whether it discriminates against or liberalises for foreign commercial interests.

**Access.** Use the Data Center at https://www.globaltradealert.org/data-center - create a free account, set filters (jurisdiction, intervention type, sector, product, period) and export individual entries, summary statistics or affected-trade estimates as CSV or Excel; curated pre-built datasets cover themes such as sanctions, subsidies, semiconductors and critical minerals.

**Caveats.** Content is published under CC BY-NC 4.0: free for non-commercial use only, and commercial use (including consultancy deliverables) requires a paid GTA licence. API, Power BI and MCP integrations are handled separately from the free web downloads - the API page offers only a demo key and directs you to contact GTA. The database records measures GTA's monitoring has found and verified, so counts are a lower bound and entries are added or revised retroactively; do not treat a snapshot as a closed universe.

### [IMF Data](https://data.imf.org/)

`Free` · beginner 2/5 · international macro & financial statistics

IMF's rebuilt data portal serving IFS, BOP, GFS, DOTS, WEO, FSI and Monetary and Financial Statistics through an SDMX 3.0 REST API (verified live 2026-08-28), with dataflows carrying explicit vintage annotations (e.g. 'Vintage for 2026-M05').

**Access.** No key. Structure: https://api.imf.org/external/sdmx/3.0/structure/dataflow — then query data by dataflow id. Python: `pip install sdmx1` and point it at the IMF SDMX endpoint, or reach the same series through DBnomics. WEO aggregate tables also download as flat files from the WEO database pages.

**Caveats.** The portal was rebuilt around 2024-2025 and the legacy dataservices.imf.org JSON endpoint that most older tutorials and blog posts use is no longer serving — code written against it will fail silently or return empty. The SDMX 3.0 grammar is a real learning curve; DBnomics is the gentler route to the same numbers.

### [IPUMS CPS and IPUMS USA](https://www.ipums.org/)

`Free (registration), email` · beginner 3/5 · US harmonised microdata

Harmonised, consistently coded individual-level microdata: IPUMS CPS covers the monthly US Current Population Survey from 1962 to the present including its supplements (ASEC income, food security, volunteering, fertility, tobacco); IPUMS USA covers decennial census and ACS samples. Free of charge.

**Access.** Free account, then build a custom extract (choose samples, variables, formats) through the web interface — you receive a download link by email. Programmatic extracts via the IPUMS API: `pip install ipumspy` or R `install.packages('ipumsr')` with a free API key.

**Caveats.** Registration requires stating a research purpose and agreeing not to redistribute the microdata — you share your extract definition and code, not the data file. Large extracts take from minutes to hours to build and can be several GB. Harmonised variable names (e.g. EMPSTAT) differ from the original survey's names, which is the whole point but breaks copy-pasted CPS code.

*Also listed under: social.*

### [IPUMS International](https://international.ipums.org/international/)

`Free (registration), application` · beginner 2/5 · cross-national census microdata

Harmonised census and survey microdata from 104 countries — 656 censuses and surveys, over 1 billion person records — contributed by national statistical offices and distributed free of charge.

**Access.** Register and submit a short application describing your research project; approved users then build custom extracts through the same web interface as other IPUMS projects, or via the IPUMS API with `ipumsr` / `ipumspy`.

**Caveats.** The application is a genuine gate — it is reviewed, takes days, and unaffiliated applicants should write a specific, concrete project description rather than 'general research'. Some countries restrict their samples further and require separate permission. Redistribution is prohibited and the licence binds you personally, not your institution. For harmonised cross-national income and wealth microdata specifically, LIS (lisdatacenter.org) is free for non-commercial research but works only through LISSY remote code submission — you never see the data, which makes debugging slow.

### [Jordà-Schularick-Taylor Macrohistory Database](https://www.macrohistory.net/database/)

`Free` · beginner 4/5 · long-run macro-financial panel

Annual panel of 48 real and nominal variables for 18 advanced economies since 1870 — credit, money, house prices, equity/housing/bond/bill returns, government finances, bank capital and loan-to-deposit ratios, and dated financial crises. Release 6 is current.

**Access.** Direct download of a single Stata (.dta) or Excel file from macrohistory.net/database. One file, one row per country-year — usable on any laptop.

**Caveats.** CC BY-NC-SA 4.0: non-commercial use only and derivatives must carry the same licence, which rules out some consulting uses. Coverage is 18 rich countries by construction, so results do not travel to emerging markets. Wartime years and early series are spliced from heterogeneous historical sources.

### [Kenneth R. French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)

`Free` · beginner 4/5 · asset pricing factors & portfolios

The reference source for Fama-French 3- and 5-factor returns, momentum and reversal factors, size/value/profitability/investment sorted portfolios, 5-to-49 industry portfolios and breakpoints — US from 1926 and developed/emerging regions from the 1970s-1990s, at daily, weekly, monthly and annual frequency. Updated through June 2026 as of 2026-08-28.

**Access.** Direct download of zipped TXT/CSV, no account. Python: `pandas_datareader.data.DataReader('F-F_Research_Data_5_Factors_2x3','famafrench')`. R: `install.packages('frenchdata')` then `download_french_data('Fama/French 3 Factors')`.

**Caveats.** Returns are in percent, not decimals, and the raw text files stack several tables (monthly, then annual, then value-weighted vs equal-weighted) in one file with blank-line separators — parsing naively silently concatenates them. Portfolios are built from CRSP/Compustat, so you get the outputs for free but cannot reconstruct or extend them without those paid databases.

### [Maddison Project Database 2023](https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2023)

`Free` · beginner 4/5 · long-run historical GDP

Per-capita GDP and population estimates for 169 countries running up to 2022, with the longest series reaching back centuries. The standard source for long-run growth and Great Divergence work.

**Access.** Direct download of Excel and Stata files via the Groningen Dataverse. Load with `haven::read_dta()` in R or `pandas.read_stata()` in Python.

**Caveats.** CC BY 4.0, but the maintainers ask that you cite the original country studies when plotting data or analysing subsets of fewer than twelve countries. Pre-1900 figures are reconstructions with wide and largely unquantified uncertainty — treat them as ordinal evidence, not measurement.

### [O*NET Resource Center](https://www.onetcenter.org/database.html)

`Free` · beginner 3/5 · occupational task & skill data

US Department of Labor's occupational database: for the 1,016 occupations of the O*NET-SOC taxonomy it scores abilities, skills, knowledge, work activities, work context, tasks and technology use. Database release 31.0 is current (page last updated 25 August 2026), with 208 occupations re-surveyed in that release. It is the raw input behind most routine-task-intensity, offshorability and AI-exposure measures in the labour literature.

**Access.** Direct download of the full database with no account, in Excel, CSV, JSON, MySQL/Oracle/SQL Server dumps and RDF serialisations (JSON-LD, N-Triples, RDF/XML, Turtle); an optional registration form is only requested from people building products on top of it. Web Services API at services.onetcenter.org needs a free registered account (verified reachable 2026-08-28). In Python just read the tab-delimited or CSV files with pandas.

**Caveats.** Public domain, but you must credit O*NET and not imply endorsement. Ratings come from incumbent-worker and analyst surveys with modest per-occupation samples, and are updated on a rolling basis, so 'change over time' in O*NET partly reflects re-survey timing rather than real occupational change. SOC crosswalks between O*NET versions are non-trivial and are the usual source of silent merge errors.

### [OECD Data Explorer](https://data-explorer.oecd.org/)

`Free` · beginner 3/5 · OECD-country statistics

OECD's statistics portal covering national accounts, productivity, labour, taxation, health, education, trade and environment for OECD members plus partner economies. Its public SDMX endpoint exposed 1,546 dataflows when queried on 2026-08-28 (including flows mirrored from Eurostat and other agencies).

**Access.** No key. SDMX REST: https://sdmx.oecd.org/public/rest/data/{agency},{dataflow},{version}/{key}?format=csvfilewithlabels. Discover flows at https://sdmx.oecd.org/public/rest/dataflow/all/all/latest (1,546 dataflows on 2026-08-28). Python: `pip install sdmx1` or `pandasdmx`. R: use `rsdmx` against the sdmx.oecd.org endpoint — the CRAN `OECD` package is version 0.2.5 from 2021-12-01 and predates the migration off stats.oecd.org, so install the maintained development version from github.com/expersso/OECD if you want that interface. CSV/Excel export from the web UI.

**Caveats.** The old stats.oecd.org / OECD.Stat interface and its SDMX-JSON URLs were retired in favour of this one, so pre-2024 example code and dataset codes generally no longer resolve. Large unfiltered queries time out; filter by reference area and time period in the URL key rather than downloading everything.

### [Open Source Asset Pricing (Chen-Zimmermann)](https://www.openassetpricing.com/)

`Free` · beginner 3/5 · cross-sectional return predictors

Replicated returns for 212 published cross-sectional stock return predictors, with 209 firm-level characteristics and both long-short portfolio returns and the underlying signals, most series running through December 2024. Each predictor links back to its originating paper in a documented Signal Browser.

**Access.** Direct download of CSVs (portfolio returns are small; the full firm-level characteristics zip is ~1.6 GB). Python: `pip install openassetpricing` then `OpenAP().dl('signed_predictors_dl_wide')`. An R package and self-contained download scripts are also provided.

**Caveats.** The single best free answer to 'I want to do cross-sectional asset pricing but have no WRDS account'. Option-implied-volatility predictors currently stop at December 2022. The firm-level file is too big for a naive in-memory read on a modest laptop — pull the portfolio-level returns first and only go to firm level when you need it. Replications are the authors' best effort, not the original authors' code; discrepancies with published t-statistics are documented and worth reading.

### [Opportunity Insights data](https://opportunityinsights.org/data/)

`Free` · beginner 4/5 · intergenerational mobility & place effects

Publicly released outputs of the Chetty-team administrative-data projects: the Opportunity Atlas (neighbourhood-level adult outcomes by childhood tract), the Social Capital Atlas (social connectedness for every US ZIP code, high school and college), college mobility report cards, migration patterns, and the Economic Tracker's real-time spending and employment series.

**Access.** Direct CSV and Stata downloads from opportunityinsights.org/data and the Economic Tracker GitHub repository; no registration. Interactive maps at opportunityatlas.org and socialcapital.org.

**Caveats.** These are aggregated, noise-infused published statistics — the underlying IRS and Facebook microdata are not available to anyone outside the project, so you can use these as covariates or outcomes but cannot reproduce or extend the estimates. Cells are suppressed or noisy at small counts; the readme's noise-infusion notes matter for inference.

### [Panel Study of Income Dynamics (PSID)](https://psidonline.isr.umich.edu/)

`Free (registration), email` · beginner 2/5 · US household panel microdata

The longest-running household panel in the world: begun in 1968 with roughly 4,800 US families and following them and their descendants annually to 1997 and biennially since, with income, employment, wealth, housing, expenditure, education and health, plus supplements on child development, transition to adulthood and immigrant samples.

**Access.** Free account, then build extracts in the online Data Center (variable search across waves, custom cross-year files) or download whole-wave data with the supplied Stata/SAS/SPSS setup files. R: `install.packages('psidR')` assembles cross-wave panels from the downloaded files.

**Caveats.** The genealogical design is the hard part: family and individual identifiers change across waves and building a clean person-year panel by hand takes days, which is what psidR or a published crosswalk saves you. Restricted geocode files (state, county, tract) require a separate contract and are not part of the public release. The site sits behind a bot challenge and could not be machine-verified on 2026-08-28 — it is browser-usable but not scriptable; the CRAN psidR page was reachable and current.

### [Penn World Table 11.0](https://www.rug.nl/ggdc/productivity/pwt/)

`Free` · beginner 4/5 · cross-country national accounts

PPP-adjusted output, input, capital stock, employment, hours and productivity for 185 countries covering 1950-2023. Version 11.0 was published on 7 October 2025 by the Groningen Growth and Development Centre.

**Access.** Direct download of the full table as Excel or Stata from the PWT page; also an online data-browsing tool. R: `install.packages('pwt10')` covers earlier releases — for 11.0 read the .dta/.xlsx directly with `haven::read_dta()` or `pandas.read_stata()`.

**Caveats.** Free with citation of the Feenstra-Inklaar-Timmer paper. Levels across PWT versions are not comparable — a growth rate computed by splicing PWT 10.x onto 11.0 is an artefact. Real GDP comes in expenditure-side (rgdpe), output-side (rgdpo) and chained (rgdpna) flavours that answer different questions; picking the wrong one is the classic beginner error.

### [Philadelphia Fed Real-Time Data Research Center](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research)

`Free` · beginner 3/5 · macro data vintages and forecast surveys

Home of the Real-Time Data Set for Macroeconomists - vintages (monthly snapshots) of the major US macroeconomic time series as they were actually published, updated at the end of each month and now including 24 gross domestic income variables - together with the Survey of Professional Forecasters (begun in 1968, the oldest quarterly survey of US macroeconomic forecasts, run by the Philadelphia Fed since 1990), the Livingston Survey (started 1946 by columnist Joseph Livingston, the oldest continuous survey of economists' expectations), Greenbook/Tealbook projections, the Aruoba-Diebold-Scotti business conditions index, the Aruoba term structure of inflation expectations, and state coincident indexes.

**Access.** Direct download from each product page - 'Complete vintage history' Excel/CSV files for the real-time data set, and mean/median plus individual-forecaster microdata files, documentation and error statistics for the SPF and Livingston surveys. No account, no key.

**Caveats.** Vintages reproduce what was published at the time, so definitions, base years and seasonal factors change across vintages and columns are not a consistent time series - read the general notes and the Croushore-Stark documentation before splicing vintages. SPF microdata identify forecasters only by number, and the panel composition changes over time, which matters for panel estimation.

### [Robert Shiller online data](https://shillerdata.com/)

`Free` · beginner 5/5 · long-run US market & housing series

Shiller's monthly US stock market file (ie_data.xls): S&P composite price, dividends, earnings, CPI and long-term interest rates from January 1871 to the present with the cyclically adjusted price-earnings ratio (CAPE) and a total-return variant added in 2018; plus the long-run US home price index running back to 1890 and updated monthly.

**Access.** Direct .xls download from shillerdata.com, no account, no key.

**Caveats.** Nineteenth-century values are reconstructions spliced from Cowles and other historical sources, and several early series are interpolations of lower-frequency data — good for long-run illustration, weak for month-by-month inference. Trailing earnings are reported with a lag, so recent CAPE readings get revised. The files are legacy Excel with title rows and trailing footnotes: read with an explicit skiprows and trim the tail rather than assuming a clean rectangle.

### [SEC EDGAR APIs (submissions, XBRL companyfacts, full-text search)](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)

`Free` · beginner 4/5 · corporate filings & financial statements

Every filing by every SEC registrant since 1993-1994, with structured XBRL financial statement data exposed per company and per concept. Completely free with no key and no paywall — verified live 2026-08-28 (Apple's AccountsPayableCurrent history returned from FY2009 forward).

**Access.** No key; you must send a descriptive User-Agent with a contact email or you get 403. Endpoints: https://data.sec.gov/submissions/CIK0000320193.json (filing history), https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json (all tagged facts), https://data.sec.gov/api/xbrl/frames/us-gaap/Revenues/USD/CY2024Q1I.json (cross-section), and https://efts.sec.gov/LATEST/search-index?q=... for full-text search. Python: `pip install sec-edgar-downloader` or `edgartools`.

**Caveats.** Rate-limited to roughly 10 requests/second under the SEC's fair-access policy; a User-Agent header identifying you is mandatory. XBRL tagging is inconsistent across filers and eras — the same economic quantity appears under different us-gaap tags, so cross-company panels need reconciliation work. This is the free substitute for Compustat fundamentals, and the honest caveat is that Compustat's value is precisely the normalisation you now have to do yourself. CRSP, Compustat and WRDS have no free tier at all: stop looking for one.

### [The DHS Program (Demographic and Health Surveys)](https://dhsprogram.com/)

`Free (registration), application` · beginner 3/5 · developing-country household health & demographic microdata

Nationally representative household surveys in over 90 countries from more than 300 surveys (site figures, 2026-08-28) with fertility histories, child and maternal health, anthropometrics, mortality, nutrition, HIV biomarkers in some waves, and an asset-based wealth index; most surveys ship GPS coordinates for sampling clusters as a separate geographic dataset.

**Access.** Free account, then a per-project dataset request describing the research; approved users download Stata, SPSS, SAS and flat files plus questionnaires and recode manuals. Model datasets download with no registration for practice. Indicator API at api.dhsprogram.com needs no key; R: `install.packages('rdhs')` handles login and extraction. Harmonised cross-survey versions via IPUMS DHS.

**Caveats.** The dataset request is per project and per country and is reviewed (usually a day or two, not weeks), and redistribution of the microdata is prohibited — you share code and derived results. GPS cluster coordinates are deliberately displaced (up to 2 km urban, 5 km rural, with a 1% subsample up to 10 km), which caps the resolution of any spatial merge and should be modelled, not ignored. Surveys are repeated cross-sections, not panels; retrospective birth and sibling histories carry recall error that grows with distance from the interview.

*Also listed under: medicine, social.*

### [Tiingo](https://www.tiingo.com/)

`Free tier, api-key` · beginner 4/5 · market price & fundamentals API

Commercial market data API with a genuine free tier: 50 requests per hour, 1,000 per day, 500 unique symbols per month, 1 GB monthly bandwidth, and 30+ years of end-of-day history (limits published on tiingo.com/about/pricing, checked 2026-08-28).

**Access.** Free account gives an API token. REST: https://api.tiingo.com/tiingo/daily/AAPL/prices?startDate=2020-01-01&token=... Python: `pip install tiingo` then `TiingoClient().get_dataframe('AAPL')`; also supported by `pandas-datareader`.

**Caveats.** The paid Power tier ($30/month) is what unlocks broad-universe work — 500 unique symbols a month is a real constraint for cross-sectional research, though ample for a handful of series. News history beyond 3 months and the crypto/IEX firehose are paid. Worth preferring over Alpha Vantage, whose free tier is now only 25 requests per day. OpenBB (`pip install openbb`) wraps many providers behind one API, but with only free keys it resolves back to these same free sources, so it adds convenience rather than coverage.

### [UN Comtrade](https://comtradeplus.un.org/)

`Free tier, email` · beginner 3/5 · bilateral merchandise trade

Official bilateral trade flows by reporter, partner, HS/SITC commodity code, direction and year or month, back to 1962 for SITC. The free public API tier allows 500 calls per day at up to 100,000 records per call, throttled to 1 call per second (limits published on uncomtrade.org, checked 2026-08-28).

**Access.** Free preview endpoint needs no key: https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=842&period=2022&partnerCode=0&cmdCode=TOTAL&flowCode=X (verified working). Free registered subscription key raises quotas. Python: `pip install comtradeapicall`. R: `install.packages('comtradr')`.

**Caveats.** Bulk file downloads, async 'data delivery', and the higher 2.5M-record calls are premium-only and paid. For a full multi-year, all-country gravity panel the free tier is painful — use CEPII BACI instead, which is Comtrade already cleaned and reconciled. Mirror-statistics asymmetries (A's exports to B ≠ B's imports from A) are real and large; do not treat either side as truth.

### [US Census Bureau Data API](https://www.census.gov/data/developers/data-sets.html)

`Free (registration), api-key` · beginner 3/5 · US survey & business statistics API

Programmatic access to the Census Bureau's public datasets: American Community Survey 1-year and 5-year tables, decennial census, Current Population Survey extracts, County Business Patterns, Business Dynamics Statistics, LEHD/LODES origin-destination employment, Small Area Income and Poverty Estimates and the economic censuses. The machine-readable catalogue at https://api.census.gov/data.json listed 1,798 dataset endpoints when queried on 2026-08-28.

**Access.** Free API key from api.census.gov/data/key_signup.html — a key is now mandatory (a keyless request to https://api.census.gov/data/2023/acs/acs5?get=NAME,B01001_001E&for=state:06 returned a 'Missing Key' page on 2026-08-28). REST: append &key=YOURKEY to that URL. R: `install.packages('tidycensus')` then `get_acs(geography='county', variables='B19013_001', year=2023)`. Python: `pip install census` or `pip install censusdis`.

**Caveats.** Variables are table codes (B19013_001E), not labels — read each dataset's variables.json before querying. Geography hierarchies are strict and dataset-specific: ACS 1-year exists only for areas above 65,000 population, so sub-county work means the 5-year file. Margins of error (…M variables) ship alongside every ACS estimate and belong in your inference, not the bin. The firm-level microdata behind CBP, BDS and LEHD is confidential and reachable only through a Federal Statistical Research Data Center application, which is a US-institution route.

*Also listed under: social.*

### [World Bank Enterprise Surveys](https://www.enterprisesurveys.org/)

`Free (registration), email` · beginner 3/5 · firm-level survey microdata

Nationally representative face-to-face surveys of registered private firms in over 160 economies (the site states coverage moving toward 180), covering access to and cost of finance, corruption and informal payments, electricity and infrastructure, competition, workforce, innovation and firm performance, with repeated waves and some country panels.

**Access.** Aggregated indicators and country profiles browse free on enterprisesurveys.org; firm-level microdata after free registration and a stated research purpose on the data portal at login.enterprisesurveys.org, which serves Stata and CSV files with questionnaires and sampling documentation.

**Caveats.** Formal registered firms above a size cutoff only — informal firms are a separate, much smaller survey programme, so any 'firms in country X' statement from this data excludes most of the actual business population in low-income countries. Sampling frames are often outdated business registries; use the supplied weights and read the country's implementation note. Questionnaires and stratification change between waves, so cross-wave comparability is limited to the harmonised core questions, and the panel subsets are documented separately from the cross-sections.

### [World Bank Microdata Library](https://microdata.worldbank.org/)

`Free (registration), email` · beginner 3/5 · household survey microdata

Catalogue of 7,098 survey and census datasets (count shown on the site, 2026-08-28), including LSMS, Living Standards, labour force and enterprise surveys, with questionnaires, codebooks and DDI metadata alongside the microdata.

**Access.** Web interface at microdata.worldbank.org; metadata via the NADA API (/index.php/api/catalog/search). 'Public use' datasets download after a free account and a stated research purpose; 'licensed' datasets need a short application describing the project.

**Caveats.** Access tiers vary per dataset and are set by the data owner, not the World Bank: open, public-use (register), licensed (apply, days to weeks), and data-enclave-only. Redistribution of licensed microdata is prohibited — you publish derived estimates and code, not the raw file.

### [World Bank Open Data / World Development Indicators](https://data.worldbank.org/)

`Free` · beginner 5/5 · cross-country development indicators

Cross-country panel of development, macro and social indicators (WDI plus ~60 other databases including International Debt Statistics and Worldwide Governance Indicators), for roughly 200 economies with coverage generally from 1960.

**Access.** No key. REST: https://api.worldbank.org/v2/country/tur/indicator/NY.GDP.MKTP.CD?format=json. Python: `pip install wbgapi` then `wb.data.DataFrame('NY.GDP.MKTP.CD', time=range(2000,2024))`. R: `install.packages('WDI')` then `WDI(indicator='NY.GDP.MKTP.CD')`. Bulk CSV/Excel per indicator from the web UI.

**Caveats.** Most of it is CC BY 4.0, but a minority of series are relicensed from third parties with tighter terms. Coverage is thin and irregular for low-income countries and for pre-1990 years; many 'country' values are World Bank estimates rather than reported national figures, which matters if you are estimating on a panel with gaps.

### [World Bank Poverty and Inequality Platform (PIP)](https://pip.worldbank.org/)

`Free` · beginner 3/5 · global poverty & distribution statistics

The World Bank's official source for global poverty and distributional statistics computed from harmonised household surveys: headcount, poverty gap, squared gap, Watts index, mean and median welfare, Gini, and full decile shares for any user-specified poverty line. The /versions endpoint returned release 20260324 in both 2017-PPP and 2021-PPP vintages on 2026-08-28.

**Access.** No key. REST: https://api.worldbank.org/pip/v1/pip?country=IDN&year=2019&povline=3.0&format=json returned Indonesia 2019 (SUSENAS, consumption): headcount 0.1085, Gini 0.3536 and all ten decile shares, verified live. Other endpoints: /versions, /countries, /aggregate. R: `install.packages('pipr')` then `get_stats(country='IDN', povline=3.0)`. Web interface with country profiles and a poverty calculator at pip.worldbank.org.

**Caveats.** Poverty lines are tied to a PPP vintage: the 2021-PPP international line is $3.00/day and its counts are not comparable with the older $2.15 (2017-PPP) line — mixing vintages across a time series is the standard error. Welfare is consumption in some countries and income in others (flagged per row) and the two are not comparable in levels. Years without a survey are interpolated or extrapolated when fill_gaps=true; several countries have decade-long survey gaps behind apparently continuous series. India and a few other large countries carry documented comparability breaks.

### [World Inequality Database (WID.world)](https://wid.world/)

`Free` · beginner 3/5 · income & wealth distribution

Distributional national accounts — top income and wealth shares, full percentile distributions, and pre/post-tax series — built by combining tax records, surveys and national accounts rather than surveys alone, which is what lets it capture the top tail. Maintained by the World Inequality Lab.

**Access.** Free bulk CSV download of the whole database plus per-country tables from the web UI, no account. R: `install.packages('wid')` (CRAN 0.0.3, 2026-07-28) then `download_wid(indicators='shweal', areas='US')`. Stata: `ssc install get-wid`. There is no maintained Python client — pull the bulk CSV and read it with pandas.

**Caveats.** Coverage and method quality vary sharply by country and era: some series are solid tax-based estimates, others are regional imputations flagged in the metadata. Read the variable-code grammar (indicator + percentile + age + population) before querying; it is the main source of confusion. The imputation choices for top wealth are actively debated in the literature.

### [World Integrated Trade Solution (WITS)](https://wits.worldbank.org/)

`Free (registration), email` · beginner 2/5 · tariffs & trade policy data

World Bank platform that joins UN Comtrade merchandise trade with UNCTAD TRAINS and WTO IDB/CTS tariff schedules — MFN and preferential applied rates at HS 6-digit and tariff-line level — plus non-tariff measures and derived indicators. Tariffs are the piece that Comtrade and CEPII BACI do not carry; the TRAINS metadata endpoint listed 481 country entities on 2026-08-28.

**Access.** Web interface (register free for custom queries and bulk downloads). Public REST/SDMX API needs no key: https://wits.worldbank.org/API/V1/SDMX/V21/rest/data/DF_WITS_Tariff_TRAINS/.840.000.010121.reported/?startPeriod=2020&endPeriod=2020 returned SDMX-ML tariff data, and https://wits.worldbank.org/API/V1/wits/datasource/trn/country/ALL returns the code lists (both verified live).

**Caveats.** The API rejects over-broad queries by design — you cannot ask for all reporters and all partners at once — and the older /datasource/TRN/reporter/... path style returned 403 for scripted clients on 2026-08-28, so build against the SDMX rest/data path. Tariff coverage is uneven: many developing countries report to TRAINS irregularly and missing years are genuinely missing, not zero. Applied rates ignore rules of origin and utilisation, so 'preferential rate available' is not 'preferential rate used'.

## Software

### [arch](https://bashtage.github.io/arch/)

`Free` · beginner 4/5 · volatility & financial econometrics

Python library for ARCH/GARCH/EGARCH/HARCH volatility models with a range of error distributions, plus unit root tests, cointegration tests, bootstrap inference, multiple comparison procedures (SPA, reality check, model confidence set) and long-run covariance estimators. Version 8.0.0 on PyPI as of 2026-08-28.

**Access.** `pip install arch`, then `arch_model(returns, vol='GARCH', p=1, q=1, dist='t').fit()`.

**Caveats.** Scale matters: pass returns in percent (multiply by 100), or the optimiser struggles and warns. The model confidence set and SPA test implementations are the free equivalent of tooling that is otherwise scattered across authors' personal MATLAB code.

### [did (Callaway & Sant'Anna)](https://bcallaway11.github.io/did/)

`Free` · beginner 3/5 · staggered difference-in-differences

R implementation of the Callaway-Sant'Anna group-time average treatment effect estimator for staggered treatment adoption, with doubly robust and inverse-probability-weighted estimators, event-study aggregation, group and calendar-time aggregation, and simultaneous confidence bands.

**Access.** `install.packages('did')` then `att_gt(yname='y', tname='year', idname='id', gname='first_treat', xformla=~x, data=df)` followed by `aggte(..., type='dynamic')` for the event study. Python port: `pip install differences` or `csdid`.

**Caveats.** Necessary because two-way fixed effects with staggered adoption and heterogeneous effects is biased — a fact that invalidated a large slice of the pre-2020 applied literature, so referees now ask for this. You must supply a never-treated or not-yet-treated comparison group; with universal eventual treatment the estimator has nothing clean to compare against. Read the accompanying paper before interpreting the aggregations.

### [Dynare](https://www.dynare.org/)

`Free` · beginner 2/5 · DSGE & macro model solving

The standard free toolbox for solving, simulating and estimating DSGE and OLG models — perturbation and perfect-foresight solution, Bayesian estimation with MCMC, optimal policy, occasionally binding constraints. Version 7.1 released 28 May 2026, GPL v3+.

**Access.** Download from dynare.org; write a .mod file describing the model in near-paper notation and run `dynare model.mod`. Runs on MATLAB, GNU Octave and Julia — the Octave route means the whole stack costs nothing.

**Caveats.** Dynare itself is free but MATLAB is not; use GNU Octave (also free) if you have no MATLAB licence, accepting that some routines run slower and a few advanced features are MATLAB-first. Steep learning curve — but the official manual, the example .mod files that ship with it, and the active user forum carry most people through. The official forum at forum.dynare.org is where the core developers debug users' actual .mod files, and is effectively the only place to get an authoritative answer on why a model will not solve.

### [fixest (R)](https://lrberge.github.io/fixest/)

`Free` · beginner 4/5 · R high-dimensional fixed effects

Very fast estimation with arbitrarily many high-dimensional fixed effects for OLS, IV, Poisson/negative binomial (PPML for gravity models) and logit, with multi-way clustered standard errors, staggered difference-in-differences (sunab), event-study plots and multiple-estimation syntax built in.

**Access.** `install.packages('fixest')` then `feols(y ~ x | firm + year, cluster = ~firm, data = df)`; `fepois()` for PPML gravity; `etable()` produces publication-ready LaTeX tables directly.

**Caveats.** This is the package that made 'you need Stata's reghdfe' stop being true, and `etable()` removes the other common reason people stayed on Stata. Coefficients on absorbed fixed effects are not reported by design. The multi-estimation syntax (csw, sw, multiple dependent variables) is powerful and easy to misread in output tables.

### [gretl](https://gretl.sourceforge.net/)

`Free` · beginner 5/5 · free econometrics GUI

A complete cross-platform econometrics package with a point-and-click GUI and a scripting language: OLS, ML, GMM, LASSO/ridge/elastic net, ARIMA, GARCH, VAR/VECM, logit/probit/tobit, panel estimators and SVM. Version 2026b, released 30 April 2026, GPL v3, for Windows, macOS and Linux.

**Access.** Download the installer from gretl.sourceforge.net. Reads Stata .dta, EViews workfiles, Excel, CSV and SPSS .sav directly, so you can open a colleague's Stata dataset without owning Stata.

**Caveats.** The realistic answer for a student or department that cannot afford Stata or EViews and is not ready to write code: a menu-driven interface with textbook-matching output. Frontier methods (modern staggered DiD, causal ML, synthetic control variants) arrive here late or not at all — you will outgrow it for research, but it is excellent for teaching and for opening .dta files.

### [grf (generalized random forests)](https://grf-labs.github.io/grf/)

`Free` · beginner 3/5 · heterogeneous treatment effects

Athey-Tibshirani-Wager generalized random forests in R: causal forests for experimental and selection-on-observables data, instrumental and local linear forests, quantile and survival forests, with honest splitting, out-of-bag conditional average treatment effect estimates, doubly robust average effects, best linear projection and RATE/TOC evaluation. CRAN 2.6.1 (2026-03-04).

**Access.** `install.packages('grf')` then `cf <- causal_forest(X, Y, W)`, `average_treatment_effect(cf, target.sample='overlap')`, `test_calibration(cf)` and `best_linear_projection(cf, X)`. Python equivalents: EconML (`pip install econml`) and DoubleML.

**Caveats.** Honest heterogeneity estimation needs samples most economics datasets do not have — with a few thousand observations the CATE surface is mostly noise, and test_calibration() exists to tell you that. The forest does not fix identification: run it on confounded data and you get well-tuned bias. Propensity overlap must be checked before interpreting subgroup effects, and data-mined subgroups still need a pre-specified or split-sample confirmation to be publishable.

### [linearmodels](https://bashtage.github.io/linearmodels/)

`Free` · beginner 3/5 · Python panel & IV estimation

Panel data (fixed effects, random effects, between, first difference, Fama-MacBeth), instrumental variables (2SLS, LIML, GMM with weak-instrument diagnostics), system regression (SUR, 3SLS) and asset pricing (time-series and cross-section factor models, GMM). Version 7.0 on PyPI as of 2026-08-28, by the author of `arch`.

**Access.** `pip install linearmodels`. `PanelOLS.from_formula('y ~ x + EntityEffects + TimeEffects', data=panel).fit(cov_type='clustered', cluster_entity=True)` — requires a MultiIndex of (entity, time).

**Caveats.** The MultiIndex requirement trips up nearly everyone on first use; set it explicitly before estimating. High-dimensional fixed effects (firm × year × product) are slow here compared with fixest or pyfixest, which use the alternating-projections trick — switch libraries rather than waiting.

### [PyFixest](https://py-econometrics.github.io/pyfixest/)

`Free` · beginner 4/5 · Python high-dimensional fixed effects

A Python port of fixest's syntax and speed: high-dimensional fixed effects OLS, IV and Poisson, multi-way clustering, wild cluster bootstrap, randomisation inference, difference-in-differences estimators and fixest-style regression tables. Version 0.60.0 on PyPI as of 2026-08-28.

**Access.** `pip install pyfixest`, then `pf.feols('y ~ x | firm + year', data=df, vcov={'CRV1':'firm'})` and `pf.etable([m1, m2])`.

**Caveats.** Closes the last real gap that pushed Python-first applied economists back to R or Stata. Younger and less battle-tested than fixest itself; for a headline result, cross-check one specification against fixest or reghdfe. API is still evolving between minor versions — pin the version in your replication package. For causal machine learning on top of this stack, DoubleML (`pip install doubleml`, also on CRAN) implements double/debiased ML with cross-fitting in both languages; EconML is the main alternative for heterogeneous effects.

### [QuantLib](https://www.quantlib.org/)

`Free` · beginner 2/5 · quantitative finance library

The reference open-source quantitative finance library: date and calendar conventions, day counters, yield curve and volatility surface bootstrapping, fixed income, swaps, and equity/FX/interest-rate option pricing across analytic, tree, finite-difference and Monte Carlo engines. Release v1.43, July 2026; modified BSD licence.

**Access.** C++ core with bindings; easiest route is `pip install QuantLib` (SWIG bindings), then e.g. build a `ql.PiecewiseLogCubicDiscount` curve or price with `ql.AnalyticEuropeanEngine`. R, Java, C# bindings and Excel/LibreOffice addins also exist.

**Caveats.** Modelled on C++ object hierarchies, so the Python API is verbose and unpythonic and the documentation assumes you know the finance. The permissive BSD licence means it is usable in proprietary work. Budget real time for the first curve bootstrap; after that the calendar and day-count machinery alone justifies it.

### [rdrobust](https://rdpackages.github.io/rdrobust/)

`Free` · beginner 3/5 · regression discontinuity estimation

The Calonico-Cattaneo-Farrell-Titiunik implementation of local polynomial regression discontinuity estimation with data-driven MSE- and CER-optimal bandwidths and robust bias-corrected confidence intervals, for sharp, fuzzy and kink designs, with companion packages rddensity (manipulation testing), rdlocrand (randomisation inference near the cutoff) and rdmulti (multiple cutoffs and scores). CRAN 4.0.0 (2026-05-16); PyPI 2.0.0.

**Access.** R: `install.packages('rdrobust')` then `rdrobust(y, x, c = 0)` for the estimate and `rdplot(y, x, c = 0)` for the binned-scatter figure. Python: `pip install rdrobust`. Stata: `net install rdrobust, from(https://raw.githubusercontent.com/rdpackages/rdrobust/master/stata)`.

**Caveats.** Report the robust bias-corrected interval, not the conventional one — referees in economics now treat the conventional CI alone as a red flag. The estimate moves with the bandwidth, so show the sensitivity and say which bandwidth selector you used. Density (rddensity) and covariate-balance checks at the cutoff are separate steps this package does not run for you, and no software fixes a running variable that agents can manipulate.

### [Sequence-Space Jacobian (SSJ)](https://github.com/shade-econ/sequence-jacobian)

`Free` · beginner 2/5 · heterogeneous-agent macro modelling

Auclert, Bardoczy, Rognlie and Straub's Python toolkit implementing the sequence-space Jacobian method from their 2021 Econometrica paper: it solves steady states, computes Jacobians of model blocks and produces linearised and nonlinear perfect-foresight transitions for heterogeneous-agent models (HANK, Krusell-Smith, Aiyagari). Version 1.0.0 on PyPI.

**Access.** `pip install sequence-jacobian`; build a model as a DAG of `@simple` blocks and `het` household blocks, then `create_model([...])`, `.solve_steady_state()`, `.solve_jacobian()` and `.solve_impulse_linear()`. The repository ships runnable notebooks for the canonical HANK and Krusell-Smith examples; requires NumPy/SciPy/Numba only.

**Caveats.** This is the gap Dynare does not cover — Dynare is representative-agent-first, and heterogeneous-agent transition dynamics used to require in-house code. You still need to know how to discretise an income process and solve the household problem; the toolkit assembles blocks, it does not diagnose a badly specified one. Estimation support is likelihood-based on the linearised model; full nonlinear Bayesian estimation is out of scope. Development is academic and episodic, so pin the version in a replication package.

### [statsmodels](https://www.statsmodels.org/)

`Free` · beginner 4/5 · Python econometrics

The general-purpose statistical modelling library for Python: OLS/GLS/WLS with robust and clustered standard errors, GLM, discrete choice (logit, probit, multinomial, count), time series (ARIMA, SARIMAX, VAR, VECM, state space, local projections), unit root and cointegration tests, and quantile regression. Version 0.15.0 on PyPI as of 2026-08-28.

**Access.** `pip install statsmodels`. Formula API mirrors R: `smf.ols('y ~ x + C(industry)', data=df).fit(cov_type='cluster', cov_kwds={'groups': df.firm})`. BSD-3 licensed.

**Caveats.** Together with linearmodels and pyfixest this is the credible free replacement for Stata's core regression workflow. Panel and IV support is thinner here than in linearmodels — reach for the right library rather than forcing statsmodels. Some time-series APIs (tsa.arima vs tsa.arima_model) were reorganised across versions, so old tutorials import names that no longer exist.

### [Synth, synthdid and scpi (synthetic control)](https://cran.r-project.org/package=Synth)

`Free` · beginner 2/5 · synthetic control estimation

The three implementations that span current synthetic control practice: Synth, the original Abadie-Diamond-Hainmueller donor-weighting estimator (CRAN 1.1-10, 2026-04-29); synthdid, the Arkhangelsky et al. synthetic difference-in-differences estimator (R, GitHub); and scpi, the Cattaneo-Feng-Palomba-Titiunik package that adds prediction intervals, multiple treated units and staggered adoption (scpi-pkg 4.0.0 on PyPI, plus R and Stata).

**Access.** `install.packages('Synth')` then `dataprep(...)` followed by `synth(...)` and `path.plot()`; `remotes::install_github('synth-inference/synthdid')` then `synthdid_estimate(Y, N0, T0)`; `pip install scpi-pkg` or `install.packages('scpi')` for prediction intervals.

**Caveats.** Classic Synth produces no standard errors: inference is placebo/permutation-based and with a small donor pool the achievable p-values are coarse (1/(N+1)). synthdid is the more robust default when pre-treatment fit is imperfect; scpi is what to use when you need honest uncertainty or have several treated units. All of them need a long, clean pre-treatment window — short pre-periods overfit donor weights and produce a beautiful fit that means nothing. Check that the treated unit lies inside the donor pool's convex hull before believing the weights.

### [yfinance](https://github.com/ranaroussi/yfinance)

`Free` · beginner 5/5 · market price data client

Python library that pulls historical and recent OHLCV prices, dividends, splits, options chains and some fundamentals for equities, ETFs, indices, FX and crypto from Yahoo Finance. Version 1.7.0 on PyPI as of 2026-08-28.

**Access.** `pip install yfinance`, then `yf.download('AAPL MSFT', start='2015-01-01')` or `yf.Ticker('AAPL').history(period='max')`. Apache-2.0 licensed.

**Caveats.** Read this honestly: yfinance is an unofficial scraper of an undocumented endpoint, not a licensed feed. Yahoo's terms restrict this use, the endpoint changes without notice (the library has broken repeatedly and been fixed after), and aggressive querying gets your IP rate-limited. Prices are not survivorship-bias-free — delisted tickers vanish — and adjusted closes have known inconsistencies. Fine for teaching, prototyping and replication of illustrative examples; do not build a published empirical result on it without cross-checking against a citable source.

## Literature

### [AEA Data and Code Repository (openICPSR)](https://www.openicpsr.org/openicpsr/aea)

`Free (registration), email` · beginner 3/5 · replication archive

The mandatory deposit archive for data and code behind every article published in an American Economic Association journal since the AEA's 2019 data availability policy, curated by the AEA Data Editor. Thousands of complete, verified replication packages with README documentation.

**Access.** Free browsing and download from openicpsr.org/openicpsr/aea; a free account is needed to download most packages. Search by article, author or JEL code.

**Caveats.** The most undervalued teaching resource in economics: a verified pipeline from raw data to a published table, with the AEA Data Editor's reproducibility check already applied. The honest limit is that packages for papers built on proprietary data (CRSP, Compustat, restricted administrative files) contain the code but not the data, so you can read the method and not run it. Much of the code is Stata, which you may not own — read it as documentation and port to R or Python. The site is behind a bot challenge, so use a browser rather than scripted downloads.

### [arXiv econ and q-fin](https://arxiv.org/archive/econ)

`Free` · beginner 5/5 · preprint server

arXiv's economics archive, live since September 2017, has three subject classes — econ.EM (econometrics), econ.GN (general economics) and econ.TH (theory) — with 5,785 items in econ.EM alone as of 2026-08-28. The older q-fin archive covers quantitative finance across eight classes including q-fin.ST (statistical finance, 4,346 items), q-fin.PR (pricing) and q-fin.RM (risk management).

**Access.** Free reading and download with no account. Full-text listings at arxiv.org/list/econ/recent. Machine access via the free arXiv API (http://export.arxiv.org/api/query?search_query=cat:econ.EM), OAI-PMH, or the bulk-access options. Submission needs a free account plus endorsement.

**Caveats.** Posting to econ.* or q-fin.* requires endorsement from an existing arXiv author in that archive if you have no prior submissions — this is the one real barrier for unaffiliated researchers, and it is usually solved by emailing a co-author or a researcher who knows your work. Mainstream economics still posts working papers to RePEc/NBER/SSRN more than arXiv, so arXiv alone is not sufficient coverage of the field.

### [IZA Discussion Papers](https://www.iza.org/publications/dp)

`Free` · beginner 4/5 · labour economics working paper series

The largest labour economics preprint series, listing 18,864 discussion papers on 2026-08-28 across employment, wages, education, migration, family, health, personnel and behavioural economics, from IZA's network of fellows and affiliates.

**Access.** Every paper is a free PDF at the stable path https://docs.iza.org/dp{number}.pdf with no account (dp17000.pdf downloaded at 592 KB when checked on 2026-08-28). Browse and search at iza.org/publications/dp, subscribe free to subject-area alerts, or reach the same records through RePEc/IDEAS and EconStor.

**Caveats.** Not peer reviewed: papers are screened for scope, and inclusion signals network membership rather than quality. Posting is restricted to IZA fellows and affiliates and their coauthors, so for an unaffiliated researcher this is a reading source, not a submission venue — MPRA is the route for that. IZA World of Labor (short evidence syntheses) is a separate free product with a different editorial process.

### [Journal of Economic Perspectives](https://www.aeaweb.org/journals/jep)

`Free` · beginner 5/5 · free-to-read survey journal

The AEA's quarterly journal of accessible synthesis articles, written for economists outside the author's own subfield. All four issues a year are publicly accessible at no charge, compliments of the American Economic Association.

**Access.** Read and download PDFs directly at aeaweb.org/journals/jep — no subscription, no account. Full back archive is open.

**Caveats.** The fastest way into an unfamiliar literature: a JEP symposium gives you the state of a debate and its canonical references in twenty pages. Articles are commissioned by the editors, so it is a reading resource, not a submission venue. The AEA's other journals (AER, AEJ series) are subscription or member-access, not free.

### [NBER Working Papers](https://www.nber.org/papers)

`Free tier` · beginner 4/5 · working paper series

Over 1,200 new papers a year from the National Bureau of Economic Research, historically the single most-read US working paper series. Every user of the site gets three complimentary downloads a year, and residents of countries whose PPP-adjusted GDP per capita is below $35,000 (2024, IMF) get complimentary access to the whole series.

**Access.** Browse and download at nber.org/papers. Free weekly New This Week email digest after free registration. Recent papers are also usually on the authors' own pages, on RePEc, or in an institutional working paper series — checking there is the standard workaround.

**Caveats.** The stated policy (nber.org/subscribe/working-papers-subscriptions-and-access, 2026-08-28) is: all users get three complimentary downloads annually; full complimentary subscriptions go to NBER Corporate Associates, journalists, US federal/state/local government employees with a .gov address, and residents of countries where PPP-adjusted GDP per capita is under $35,000 (2024, IMF) — a threshold that covers most of the world outside the richest economies and makes this series effectively free for much of this catalogue's audience. Institutional subscribers get IP-based access. When you are outside all of those, the standard workaround is the author's page, RePEc/IDEAS, or the same paper in a university or central bank working paper series.

### [RePEc / IDEAS](https://ideas.repec.org/)

`Free` · beginner 4/5 · economics bibliographic database

The field's own decentralised bibliography: over 5,400,000 indexed items of economics research, of which over 4,800,000 are downloadable in full text (counts shown on IDEAS, 2026-08-28), covering working papers, journal articles, book chapters, books and software components.

**Access.** Web search at ideas.repec.org or econpapers.repec.org (a second front end over the same data). Free NEP (New Economics Papers) email alerts give you human-curated weekly new-paper lists by subject at nep.repec.org. Author pages and citation counts via CitEc; register as an author through the RePEc Author Service for free.

**Caveats.** Coverage of working papers is unmatched, but it indexes what archives contribute, so metadata quality is uneven and some journal records point to paywalled publisher pages rather than free full text. The 4.8M 'downloadable' figure includes links out to publishers you may not be able to read; filter on working papers when you need guaranteed access. When you need results you can definitely read today, search EconStor (econstor.eu, 317,846 open access documents as of 2026-08-28), a ZBW-run repository that feeds into RePEc and is open access by construction.

### [SSRN](https://www.ssrn.com/)

`Free (registration), email` · beginner 4/5 · preprint & working paper repository

Large social science preprint repository with deep economics, finance, accounting and law networks. Most economics and finance working papers posted here are free to download, and posting your own paper is free.

**Access.** Free account to download and to upload. Browse by network (Economics Research Network, Financial Economics Network) or search; papers download as PDFs. Abstract pages are indexed by search engines and by RePEc.

**Caveats.** Owned by Elsevier since 2016, and that shapes it: some series are restricted, an optional paid promotion tier exists, and download counts drive a leaderboard culture that is not a quality signal. Papers are not peer reviewed and not version-controlled the way arXiv is. Posting here does not conflict with most journals' preprint policies, but check the target journal's rules.

### [World Bank Open Knowledge Repository](https://openknowledge.worldbank.org/)

`Free` · beginner 4/5 · development research repository

The World Bank's open repository of its own research and reports: 41,509 items on 2026-08-28, of which 9,301 match the Policy Research Working Paper series, alongside World Development Reports, country diagnostics, impact evaluations, books and journal articles from the Bank's own titles.

**Access.** Free full-text PDF download, no account. Machine access via the DSpace REST API: https://openknowledge.worldbank.org/server/api/discover/search/objects?query=inflation&size=20 (verified live), plus OAI-PMH harvesting for bulk metadata.

**Caveats.** Most items are CC BY 3.0/4.0 IGO — unusually permissive for a large publisher — but co-published books and some third-party content carry tighter terms shown per record, so check before reusing figures. Policy Research Working Papers pass internal review, not peer review, and reflect Bank research priorities. The web front end is a JavaScript app: script the REST API rather than scraping pages.

## Compute

### [Google Colab](https://colab.research.google.com/)

`Free tier, email` · beginner 5/5 · free notebook compute

Hosted Jupyter notebooks with a free tier: sessions run up to 12 hours depending on availability and usage, with GPU access available but, in Google's own words, 'heavily restricted' on the free plan. The QuantEcon lectures, DoubleML and most Python econometrics tutorials open directly in it.

**Access.** Sign in with a Google account and open a notebook; `pip install` works inside a cell. Mount Google Drive for persistent files. GitHub notebooks open via colab.research.google.com/github/{user}/{repo}.

**Caveats.** Sessions are ephemeral: the filesystem is wiped when the runtime disconnects, so write results to Drive or download them. Idle notebooks are disconnected. Premium GPUs, high-memory machines, longer runtimes and background execution require paid compute units. Free-tier GPU availability is not guaranteed on any given day, which matters if you are following the QuantEcon JAX lectures on a deadline. For an R-first workflow, Posit Cloud (posit.cloud) runs RStudio in the browser on a free plan with capped monthly project hours and limited RAM — verify the current limits on their plans page, which has been revised more than once.

## Publishing

### [AEA RCT Registry](https://www.socialscienceregistry.org/)

`Free, email` · beginner 4/5 · trial pre-registration

The American Economic Association's registry for randomised controlled trials in economics, holding 12,677 registered studies across 171 countries as of 2026-08-28. Registration of a trial and search of the registry are both free.

**Access.** Free account, then register a trial through the web form (title, location, intervention, outcomes, power calculations, optional pre-analysis plan attachment). Search and browse need no account; registry metadata is downloadable in bulk as CSV.

**Caveats.** Pre-registration before data collection is now expected by most economics journals for experimental work, so this is a practical publication prerequisite, not an optional virtue. The bulk CSV of registrations is itself a research dataset (for studying publication bias and specification search). Registering does not gate you from changing the analysis — but deviations must be declared.

### [MPRA (Munich Personal RePEc Archive)](https://mpra.ub.uni-muenchen.de/)

`Free, email` · beginner 4/5 · self-deposit preprint archive

A RePEc service hosted by the University Library of LMU Munich, holding 61,599 records as of 2026-08-28, explicitly built for economists who are not affiliated with an institution that runs its own working paper series.

**Access.** Free account, upload a PDF with metadata, an editor approves it, and the paper then propagates into RePEc, IDEAS and EconPapers with a stable URL and a working-paper identity. Accepts papers in any language.

**Caveats.** The single most useful publishing route in this catalogue for an unaffiliated researcher: it is the standard way to get a working paper a citable identity and RePEc-indexed visibility without a departmental series behind you. Editorial screening is for scope and basic academic form, not peer review, so an MPRA paper carries no quality signal by itself. Depositing keeps your copyright in the preprint version, which most journals then still accept.

### [Social Science Data Editors template README](https://social-science-data-editors.github.io/template_README/)

`Free` · beginner 4/5 · reproducibility standard

The standard replication-package README template endorsed by the data editors of the major economics journals, specifying what a package must document: data sources and their access conditions (registration, cost, application), software and package versions, hardware and expected runtime, and a script sequence that runs end to end without manual intervention.

**Access.** Free download in HTML, Markdown, PDF, Word and LaTeX from the site and its GitHub repository. CC BY-NC licensed. Copy the template into your project on day one, not the day before submission.

**Caveats.** Following this before you submit removes the most common cause of desk-stage reproducibility delays at AEA, Econometric Society and other journals. It also happens to be the clearest available checklist for organising your own project. The 'data availability' section is where researchers without institutional access should be explicit about which inputs a replicator cannot obtain. If your journal wants a permanent archive and you have no institutional repository, Zenodo (zenodo.org, CERN-run, free, DOI per deposit, up to 100 files and 50 GB per record) is the standard destination, and it can auto-archive a GitHub release.

### [Theoretical Economics and Quantitative Economics](https://econometricsociety.org/publications/theoretical-economics)

`Free` · beginner 3/5 · open access journals

Two Econometric Society journals that are fully open access with no article processing charge — Theoretical Economics (theory, first issue March 2006, now volume 21) and Quantitative Economics (quantitative and applied). The society's own page states of TE: 'Theoretical Economics is open access, so all content is freely available.'

**Access.** Read and download every article free at the Econometric Society site, no account. To submit you must be an Econometric Society member and pay a submission fee; papers transferred after an Econometrica rejection have the submission fee waived. A public working paper version (personal site or arXiv) is required at submission.

**Caveats.** Be precise about what is free: reading costs nothing and there is no APC on acceptance, but submitting costs a society membership plus a submission fee, which is a real barrier for an unfunded researcher. Econometric Society membership is priced on a sliding scale by country income and career stage — check the rates before assuming it is out of reach. These are top-tier venues with correspondingly low acceptance rates.

## Funding

### [African Economic Research Consortium (AERC)](https://aercafrica.org/)

`Free, application` · beginner 3/5 · African economics research support

Pan-African consortium supporting economic research and graduate training in sub-Saharan Africa through thematic and collaborative research grants, biannual research workshops where funded work is presented and revised, and collaborative Master's and PhD programmes in economics.

**Access.** Apply to thematic research calls and training programmes announced on aercafrica.org; the biannual research workshop cycle structures the grant-and-revision process.

**Caveats.** Eligibility is centred on researchers based at African institutions. The workshop model — present, get discussant feedback, revise, resubmit — is as valuable as the money for someone without a strong local seminar culture. Calls and their terms are announced on the site; I could not read the live grants page on 2026-08-28, so verify current amounts and deadlines there.

### [International Growth Centre (IGC)](https://www.theigc.org/)

`Free, application` · beginner 3/5 · development economics research grants

LSE- and Oxford-based centre funding policy-relevant research on growth in low-income countries, running general calls for proposals alongside targeted country-programme calls, PhD fellowships and early-career researcher workshops.

**Access.** Apply through the calls listed at theigc.org/funding; most calls open with an expression of interest, then a full proposal. Country programme teams are named on the site and are approachable directly.

**Caveats.** Calls open and close on a rolling schedule — the general call was closed when checked on 2026-08-28, with country- and theme-specific calls live — so subscribe to their alerts rather than checking once. IGC actively funds researchers based in the countries studied, which makes it one of the more realistic routes for economists at institutions in low- and middle-income countries. Research must be policy-relevant and tied to an IGC partner country.

### [J-PAL research initiatives](https://www.povertyactionlab.org/initiatives)

`Free, application` · beginner 2/5 · randomised evaluation funding

J-PAL's thematic initiatives (King Climate Action Initiative, jobs, health, education, digital agriculture and others) run competitive requests for proposals funding pilots, full randomised evaluations and scale-ups, mostly in low- and middle-income countries. On 2026-08-28 two calls were open: K-CAI with proposals due 21 October 2026 and the UM6P-J-PAL applied agriculture lab (UJALA) due 30 October 2026; the other initiatives showed no active cycle.

**Access.** Apply through the specific initiative's RFP page linked from povertyactionlab.org/initiatives; calls typically run in two stages (short proposal, then full proposal and budget) and require a named principal investigator plus an implementing partner and, usually, IRB clearance.

**Caveats.** Eligibility is the real gate: most initiatives require at least one J-PAL affiliated professor (the network states more than 1,100 researchers) or an invited researcher on the team, so an unaffiliated applicant normally needs a co-PI inside the network. Some initiatives run smaller separate windows for PhD students or for researchers based in the study country — read each RFP's eligibility section rather than assuming. Most calls are closed at any moment, so treat this page as the calendar and check it monthly.

### [Partnership for Economic Policy (PEP)](https://www.pep-net.org/)

`Free, application` · beginner 3/5 · Global South research grants and training

A Southern-led organisation that funds and trains locally based research teams in developing countries, combining research grants with certified online courses in development economics methods, mentoring by senior researchers, and policy-engagement support.

**Access.** Apply to calls listed under pep-net.org/grants; applications are from teams based in developing countries. Grants normally bundle funding with methodological training and assigned mentors rather than money alone.

**Caveats.** Explicitly designed for researchers who are in the country being studied rather than visiting it — one of the few funders whose eligibility rules favour, rather than disadvantage, economists at under-resourced institutions in the Global South. Calls are periodic; check the grants page for what is currently open. The mentoring and training component means a longer commitment than a pure grant.

### [Washington Center for Equitable Growth grants](https://equitablegrowth.org/funding-opportunities/)

`Free, application` · beginner 3/5 · inequality & growth research grants

Funds academic research on how inequality affects economic growth and stability. Early Career Grants are $15,000 over one year for PhD students and postdocs and $30,000 over one to two years for pre-tenure faculty; the AEA Summer Economics Fellows Program carries a $30,000 prorated stipend for an 8-12 week placement.

**Access.** Respond to the annual Request for Proposals announced at equitablegrowth.org/funding-opportunities; email grants@equitablegrowth.org to be notified when the next RFP opens.

**Caveats.** Hard eligibility limit: applicants must be at US universities or institutions, and faculty applicants must be within 8 years of the PhD and untenured. The 2025 RFP was closed when checked on 2026-08-28, and RFPs run on an annual cycle, so the practical move is to join the alert list now. Not a route for researchers outside the US.

## Learning

### [Causal Inference: The Mixtape](https://mixtape.scunning.com/)

`Free` · beginner 4/5 · causal inference textbook

Scott Cunningham's book on causal inference for applied economists, free to read online in full, covering potential outcomes, directed acyclic graphs, matching and subclassification, regression discontinuity, instrumental variables, panel data, difference-in-differences and synthetic control, with code in R, Stata and Python.

**Access.** Read free at mixtape.scunning.com; no account. Datasets used in the examples are downloadable from the book's site. A paid Yale University Press print edition exists.

**Caveats.** More narrative and historical than The Effect — it explains where each method came from and why the profession adopted it, which helps when you need to justify a design to a referee. Cunningham's paid 'Mixtape Sessions' workshops are a separate commercial offering; the book itself is free.

### [Coding for Economists](https://aeturrell.github.io/coding-for-economists/)

`Free` · beginner 4/5 · Python research workflow book

Arthur Turrell's free online book covering the whole Python research workflow for economists: environments and version control, pandas data cleaning and reshaping, visualisation, regression and generalised regression, causal inference, time series, text analysis, geospatial work, and reproducible Quarto write-ups. MIT-licensed, chapters are downloadable notebooks.

**Access.** Read free in the browser at aeturrell.github.io/coding-for-economists; no account. Each chapter can be downloaded and run as a Jupyter notebook locally or in Colab.

**Caveats.** Assumes Python is the decision already made; it will not help you choose between R, Stata and Python. The econometrics chapters are a practical tour, not a theory course — pair with The Effect or a graduate metrics text for identification and proofs. Library APIs move faster than the book, so occasional cells drift out of date between revisions.

### [CORE Econ](https://www.core-econ.org/)

`Free` · beginner 5/5 · open economics textbooks

Free open-access economics textbooks used in undergraduate courses worldwide: The Economy 2.0 (Microeconomics and Macroeconomics), Understanding our Economy, Doing Economics (empirical projects with real data), Experiencing Economics (classroom experiments) and CORE Insights, with translations into Spanish, French, Italian, German, Portuguese, Finnish and others.

**Access.** Read free in the browser at books.core-econ.org; no payment. Free optional registration unlocks additional instructor and learner materials. Doing Economics ships datasets and R/Excel walkthroughs.

**Caveats.** Teaches economics starting from inequality, institutions and empirical evidence rather than the standard supply-and-demand-first sequence, which is a deliberate pedagogical stance rather than a neutral one. Some complementary materials are CC BY-NC-ND, meaning you may not redistribute modified versions. Doing Economics is the standout for someone teaching themselves applied work. For video-first learning, Marginal Revolution University (mru.org) offers 750+ free lessons with an openly free-market editorial slant, and MIT OpenCourseWare (ocw.mit.edu) publishes full graduate problem sets and solutions — but check course dates, since applied econometrics material from before roughly 2020 predates the staggered-DiD literature.

### [NBER Methods Lectures](https://www.nber.org/conferences/methods-lectures)

`Free` · beginner 3/5 · econometric methods video lectures

Free video and slide archive of the methods lectures delivered at the NBER Summer Institute, in which the authors of new econometric methods teach them directly to applied researchers; the 2026 lecture was Melissa Dell and Ashesh Rambachan on estimation and inference with AI-generated data, and the archive runs back over a decade of Summer Institutes.

**Access.** Watch free on nber.org with no account; each lecture page links slides and, for many lectures, code. The same video section carries other free NBER lecture series.

**Caveats.** Lecture-level, not a course: these start where a graduate textbook stops and assume you already know the standard estimators. Coverage is what NBER chose to teach in a given summer, not a curriculum, and older lectures reflect the state of the art at the time — pre-2020 panel and DiD material predates the staggered-adoption corrections. The listing page is a JavaScript app, so browse it rather than scripting it.

### [QuantEcon](https://quantecon.org/lectures/)

`Free` · beginner 4/5 · computational economics lectures

The field's standard free computational economics curriculum, in Python and Julia: Python Programming for Economics and Finance, A First Course in Quantitative Economics, Intermediate and Advanced Quantitative Economics, Quantitative Economics with JAX (GPU), Continuous Time Markov Chains, and Introduction to Economic Modeling and Data Science.

**Access.** Read free in the browser; every lecture has an 'open in Colab' button and downloadable notebooks, so you need no local install. Supporting library: `pip install quantecon` (0.11.4 as of 2026-08-28) for Markov chains, LQ control, optimisation and game-theory routines.

**Caveats.** Written by economists (Sargent, Stachurski and collaborators) for economists, so the examples are dynamic programming, search and matching, asset pricing and heterogeneous agents rather than generic data science. The JAX lectures assume a GPU — Colab's free tier is enough to follow them, with the usual free-tier GPU restrictions.

### [The Effect (Nick Huntington-Klein)](https://theeffectbook.net/)

`Free` · beginner 5/5 · causal inference textbook

A full introductory book on research design and causality with observational data, free in its online Bookdown version. Part 1 builds causal diagrams and design intuition; Part 2 covers regression, matching, fixed effects, difference-in-differences, instrumental variables and regression discontinuity, with worked code in R, Stata and Python side by side.

**Access.** Read free at theeffectbook.net; no account. Accompanying video lectures, homework assignments and coding tutorials for beginners in all three languages are also free. A paid Chapman & Hall print edition exists.

**Caveats.** The three-language code is the reason to pick this over alternatives if you are migrating off Stata or arriving from a Python background. Deliberately light on technical detail — pair it with Angrist-Pischke or a graduate metrics text when you need proofs rather than intuition. If your course text is Stock and Watson and you are migrating off Stata, econometrics-with-r.org reworks that entire syllabus in free, runnable R.

*Also listed under: social.*

### [World Bank DIME Wiki](https://dimewiki.worldbank.org/)

`Free` · beginner 4/5 · impact evaluation practice guide

A public wiki maintained by the World Bank's Development Impact Evaluation department documenting the operational side of empirical work: randomisation and sampling design, power calculations, survey instrument design, field data collection and quality checks, data management, coding standards and reproducible workflows.

**Access.** Read free in a browser at dimewiki.worldbank.org, no account. Pairs with the free DIME Analytics book 'Development Research in Practice' and with J-PAL's research resources at povertyactionlab.org/research-resources.

**Caveats.** Covers what textbooks skip — how to actually run a survey, structure a project folder, and hand a dataset to a colleague. Much of the code guidance is Stata-first, reflecting the department's practice. The site sits behind a bot challenge, so it is browser-readable but not scriptable.

## Community

### [Economics Stack Exchange](https://economics.stackexchange.com/)

`Free` · beginner 3/5 · Q&A site

Question-and-answer site for economics, with 16,251 questions, 19,935 answers and 45,256 registered users as of 2026-08-28 (figures from the Stack Exchange API). Covers micro and macro theory, econometric identification and interpretation, and where to find particular data.

**Access.** Read with no account; a free account lets you ask, answer and vote. Post a self-contained question with the model or specification written out — vague questions get closed.

**Caveats.** About 3,366 questions are unanswered, so response is not guaranteed and the site is much quieter than Cross Validated or Stack Overflow. Theory and 'what does this estimator identify' questions do best; homework-style and opinion questions get closed fast. For pure statistics questions, Cross Validated is a larger and faster room.

### [Quantitative Finance Stack Exchange](https://quant.stackexchange.com/)

`Free` · beginner 3/5 · Q&A site

Q&A site for quantitative finance practice and research, with 23,622 questions, 27,808 answers and 69,801 users as of 2026-08-28 (Stack Exchange API). Strong on derivatives pricing, volatility modelling, risk measures, portfolio construction and market microstructure.

**Access.** Read freely; free account to participate. Include the model, the assumptions and what you tried — pricing questions with a concrete payoff and measure get good answers.

**Caveats.** Skews practitioner rather than academic, which is a feature when you need implementation detail (day counts, calibration, data cleaning) and a limitation for asset pricing theory. 'Which data source should I use' and 'is my backtest good' questions are frequently closed as opinion-based.

### [Statalist](https://www.statalist.org/)

`Free, email` · beginner 3/5 · econometrics forum

Forum running since 1994 where applied economists and statisticians discuss estimation problems, maintained by StataCorp and moderated by users. Free to read and, after free registration, to post.

**Access.** Browse without an account; register free to post, using your real name as the forum asks. Post your exact command, the exact output and a data example (`dataex`) — the culture rewards reproducible questions and is blunt about ill-formed ones.

**Caveats.** Nominally Stata-specific, but a large share of threads are about econometric method rather than syntax — clustering choices, panel estimator selection, DiD specification — and those answers transfer to R or Python. Several well-known methodologists answer here regularly. The obvious caveat: the code examples assume Stata, which is paid software.
