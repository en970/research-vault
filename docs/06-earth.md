# Earth, climate & environmental science

Part of [research-vault](../README.md). 84 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (36) · [Software](#software) (17) · [Literature](#literature) (3) · [Compute](#compute) (6) · [Publishing](#publishing) (5) · [Funding](#funding) (5) · [Learning](#learning) (7) · [Community](#community) (5)

## Data

### [AmeriFlux (and the FLUXNET network)](https://ameriflux.lbl.gov/)

`Free (registration), email` · beginner 3/5 · eddy covariance flux towers

Eddy covariance network for the Americas: 843 registered sites of which 592 have downloadable flux data as of 28 August 2026, spanning the USA (682), Canada (93), Brazil (23), Mexico (16), Peru, Argentina, Chile, Costa Rica, Colombia, Panama and Puerto Rico. Products are half-hourly BASE files (CO2, water and energy fluxes plus meteorology) and ONEFlux gap-filled FLUXNET-format files.

**Access.** Free account, accept the data policy, then select sites in the Download Data tool and retrieve zipped CSV; every site product carries its own DOI. Global network products and the FLUXNET2015 release are at https://fluxnet.org/.

**Caveats.** Since August 2021 most sites are CC BY 4.0, but Legacy Policy sites still require contacting the PI and offering co-authorship before publication, and combining the two forces the stricter rule on the whole analysis. BASE files are not analysis-ready: u* filtering, gap-filling, storage correction and energy balance closure are yours to handle, which is why the ONEFlux products exist. Africa, Asia and Europe are covered by other regional networks (ICOS, AsiaFlux), not this one.

### [AppEEARS](https://appeears.earthdatacloud.nasa.gov/)

`Free (registration), email` · beginner 5/5 · point and area subsetting service

NASA LP DAAC service that extracts and reformats subsets of gridded products (MODIS, VIIRS, HLS, ECOSTRESS, EMIT, Landsat ARD, SMAP, SRTM, Daymet, Gridded Population of the World) for a list of coordinates or an uploaded polygon, returning CSV, GeoTIFF or netCDF with quality flags attached, instead of whole tiles.

**Access.** Sign in with an Earthdata Login, submit a point or area sample in the web interface, or script it against the REST API at https://appeears.earthdatacloud.nasa.gov/api/ (task submit, status poll, bundle download); the `appeears` R package on CRAN wraps the same endpoints.

**Caveats.** Requests are queued and large areas or long time series can take hours to days; area requests have size caps, so tile large regions. Only catalogued products are available, and completed bundles are removed from the server after a retention period, so download promptly. This is the single biggest time-saver for anyone who needs MODIS or VIIRS time series at field sites rather than whole granules.

### [Argo float profiles](https://argo.ucsd.edu/)

`Free` · beginner 3/5 · in-situ ocean profiles

Global array of profiling floats measuring temperature and salinity through the upper ~2000 m, with biogeochemical variables on BGC floats. Profiles are free from the Global Data Assembly Centres as netCDF and updated daily.

**Access.** `pip install argopy`; `from argopy import DataFetcher; ds = DataFetcher(mode='research').region([-75,-45,20,30,0,1000,'2024-01','2024-06']).to_xarray()`. Raw files via the Coriolis and US GDAC HTTPS/FTP mirrors, or through Ifremer's ERDDAP.

**Caveats.** Real-time profiles carry only automated quality control; delayed-mode data, available months later, is what climate work needs. Always respect QC flags (argopy's 'research' mode applies the strict filter for you). Whole-array downloads are large, so fetch by region and time.

### [ASF Vertex and HyP3 (SAR)](https://search.asf.alaska.edu/)

`Free (registration), email` · beginner 3/5 · synthetic aperture radar

Alaska Satellite Facility DAAC search and download for Sentinel-1 and legacy SAR missions such as ALOS PALSAR, with the HyP3 service generating radiometrically terrain-corrected products and InSAR interferograms on demand in the cloud instead of on your machine.

**Access.** Search Vertex with an Earthdata Login; script with `pip install asf_search` (`asf_search.search(platform='SENTINEL-1', intersectsWith=wkt, ...)`) and submit processing jobs with `pip install hyp3_sdk`.

**Caveats.** HyP3 Basic gives every user 8,000 credits per month at no cost, with more available on request as ASF's budget allows, so large InSAR or RTC stacks have to be planned against that allowance. Job types include RTC, OPERA RTC-S1, InSAR, burst InSAR, ARIA S1 GUNW and autoRIFT. Doing the same processing locally means ESA SNAP plus a lot of RAM and disk; raw Sentinel-1 SLCs are several GB per scene.

### [CHIRPS](https://www.chc.ucsb.edu/data/chirps)

`Free` · beginner 4/5 · satellite-gauge precipitation

Climate Hazards Center rainfall dataset blending infrared satellite estimates with station observations at 0.05 degree resolution across 50S-50N, from 1981 to near-present, in daily, pentad, dekad and monthly steps. Public domain and the standard baseline for drought and food-security monitoring in gauge-sparse regions.

**Access.** Direct download from https://data.chc.ucsb.edu/products/CHIRPS-2.0/ (netCDF, GeoTIFF, BIL) with no login; also in Earth Engine as `UCSB-CHG/CHIRPS/DAILY` and through the ClimateSERV API.

**Caveats.** A preliminary near-real-time product is published within days and is later replaced by the final version, so re-pull rather than assuming files are stable. Quality tracks station density: it is strongest over Africa, where the CHC has station agreements, and it is a gridded estimate, not a gauge measurement, so validating against local rain gauges before use is expected. CHIRTS is the companion temperature product.

### [CMIP6 analysis-ready Zarr in the cloud (Pangeo/ESGF)](https://pangeo-data.github.io/pangeo-cmip6-cloud/)

`Free` · beginner 3/5 · cloud-optimised climate model output

A large subset of CMIP6 rewritten as cloud-optimised Zarr in the public buckets gs://cmip6 and s3://cmip6-pds, with one CSV/JSON catalogue listing every store. Anonymous read access works with no billing account.

**Access.** `pip install intake-esm gcsfs zarr xarray`; `col = intake.open_esm_datastore('https://storage.googleapis.com/cmip6/pangeo-cmip6.json')`, then `col.search(source_id='MPI-ESM1-2-LR', variable_id='tas', experiment_id='ssp585').to_dataset_dict()`. Anonymous access uses `token='anon'` (GCS) or `anon=True` (S3).

**Caveats.** It is a curated subset of ESGF, not the whole archive, and lags new model submissions. Reading over a home connection is fine for single variables and subsets but slow for large ensembles; the same catalogue exists on AWS if you compute there.

### [Copernicus Atmosphere Data Store (CAMS)](https://ads.atmosphere.copernicus.eu/)

`Free (registration), api-key` · beginner 3/5 · atmospheric composition and air quality

ECMWF-run store for Copernicus Atmosphere Monitoring Service data: 16 datasets covering the EAC4 global composition reanalysis, the EGG4 greenhouse gas reanalysis, 5-day global forecasts of 50+ chemical species, European air quality reanalyses and forecasts, GFAS biomass burning emissions, solar radiation time series and global emission inventories.

**Access.** `pip install 'cdsapi>=0.7.7'`; put `url: https://ads.atmosphere.copernicus.eu/api` and your ADS personal access token in ~/.cdsapirc, then `cdsapi.Client().retrieve('cams-global-reanalysis-eac4', {...}, 'out.nc')`.

**Caveats.** A separate account and token from the Climate Data Store even though the client is the same, and each dataset licence must be accepted in the web interface first. Requests are queued like CDS. EAC4 is about 0.75 degrees and 3-hourly, so it is far too coarse for street- or city-scale air quality: use it for background and long-range transport, not exposure studies.

### [Copernicus Climate Data Store (ERA5)](https://cds.climate.copernicus.eu/)

`Free (registration), api-key` · beginner 3/5 · reanalysis and climate indicators

ERA5 global reanalysis (hourly, 0.25 degree, 1940 to near-present), ERA5-Land at about 9 km, seasonal forecasts, satellite climate records and CMIP6-derived climate indicators, all retrievable by API after free registration.

**Access.** `pip install 'cdsapi>=0.7.7'`; put `url: https://cds.climate.copernicus.eu/api` and `key: <personal access token>` in ~/.cdsapirc, then `cdsapi.Client().retrieve('reanalysis-era5-single-levels', {...}, 'out.nc')`.

**Caveats.** You must accept each dataset's licence in the web interface before the API will serve it. Requests are queued: large ERA5 pulls take hours to days, and the most recent ~5 days are preliminary ERA5T that is later revised. The newer `ecmwf-datastores-client` adds asynchronous job handling.

### [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/)

`Free (registration), email` · beginner 4/5 · Sentinel satellite archive

Full free archive of Sentinel-1/2/3/5P plus Copernicus DEM and mirrored Landsat, served through OData, STAC, S3 and Sentinel Hub APIs. Free accounts get 12 TB of transfer per rolling 30 days, 50,000 catalogue requests per month and 10,000 Sentinel Hub processing units per month.

**Access.** Register, then use the Browser at browser.dataspace.copernicus.eu, the STAC catalogue at https://catalogue.dataspace.copernicus.eu/stac, or S3 with boto3 against the eodata endpoint; `pip install sentinelhub` or `pip install openeo` for the processing APIs.

**Caveats.** Quotas throttle rather than block: once the 12 TB rolling-30-day transfer allowance is exceeded, bandwidth drops to 1 MB/s and concurrent connections to 1. The documented free-tier limits are 4 concurrent connections and 20 MB/s per connection on S3/OData/STAC with up to 2,000 catalogue requests per minute; Sentinel Hub adds a 300 processing-unit-per-minute ceiling on top of the 10,000 units per month; openEO free accounts are limited to 2 concurrent API requests. Access tokens expire after 10 minutes and are refreshable for 60. Server-side processing (Sentinel Hub processing units, openEO credits) is the scarce resource, not the downloads.

### [Copernicus Marine Service](https://marine.copernicus.eu/)

`Free (registration), email` · beginner 3/5 · ocean reanalysis, forecasts and in-situ

EU ocean data service providing satellite and in-situ observations, global and regional physical and biogeochemical reanalyses, and daily forecasts, in netCDF or Zarr. Data are free and open after registration.

**Access.** `pip install copernicusmarine`; `copernicusmarine login`, then `copernicusmarine subset --dataset-id <id> --variable thetao --minimum-longitude ... --start-datetime ...`, or `copernicusmarine.open_dataset()` in Python for lazy xarray access.

**Caveats.** Server-side subsetting is essential: whole products are terabytes. Dataset IDs carry version suffixes and older versions are retired after a notice period, so pin the exact ID in scripts and expect to update them.

### [EarthChem](https://www.earthchem.org/)

`Free` · beginner 3/5 · geochemistry data repository

NSF-funded geochemistry data facility at Lamont-Doherty Earth Observatory: the EarthChem Library (a DOI-issuing repository for submitted geochemical datasets), the EarthChem Portal for federated search across geochemical databases, PetDB 2.0 for igneous and metamorphic whole-rock and mineral chemistry, and LEPR/TraceDs for experimental petrology and trace element partitioning.

**Access.** Search the Portal or PetDB in the browser and export results as CSV or Excel; no account needed to download. Depositing a dataset requires a free account and returns a DOI plus a persistent landing page.

**Caveats.** Registration gates submission only, not download. Compilations pool analyses across decades, laboratories and methods, so units, detection limits, normalisation and reference materials must be checked before combining records; the metadata are there but they are your responsibility. Coverage is strongest for igneous rocks and for US-funded sampling campaigns.

### [EarthScope (IRIS) FDSN web services](https://service.iris.edu/fdsnws/)

`Free` · beginner 3/5 · seismic waveforms and station metadata

Open access to the global seismological archive: fdsnws-dataselect returns miniSEED, SAC or GeoCSV waveforms and fdsnws-station returns StationXML metadata, covering permanent global networks and thousands of temporary deployments.

**Access.** `pip install obspy`; `from obspy.clients.fdsn import Client; st = Client('IRIS').get_waveforms('IU','ANMO','00','BHZ', t1, t2)`. Plain HTTP works too: https://service.iris.edu/fdsnws/dataselect/1/query?net=IU&sta=ANMO&cha=BHZ&start=...

**Caveats.** Open networks need no credentials, but embargoed or restricted networks require federated authentication. The documentation explicitly says not to poll these services for continuous real-time data; use SeedLink for that. Chunk multi-year, multi-station requests or they time out.

### [EM-DAT](https://www.emdat.be/)

`Free (registration), email` · beginner 4/5 · disaster impact database

CRED's international disaster database: over 27,000 mass disasters worldwide from 1900 to present with deaths, people affected and economic damage, entered when a threshold is met (10 deaths, 100 affected, a declared state of emergency, or an international appeal).

**Access.** Register at https://public.emdat.be/, filter by country, hazard type and period in the web interface, and export the selection as XLSX for analysis.

**Caveats.** Open access for non-commercial use only; commercial licensing is separate. Records depend on reporting, so early decades and low-income regions are systematically under-recorded and economic losses are inconsistent. Read the methodology before publishing counts or trends.

### [ESA WorldCover](https://esa-worldcover.org/)

`Free` · beginner 4/5 · global land cover

Global land cover maps at 10 m for 2020 (v100) and 2021 (v200) with 11 classes, produced from Sentinel-1 and Sentinel-2 by a VITO-led consortium for ESA and distributed as 3x3 degree GeoTIFF tiles under CC BY 4.0.

**Access.** Browse at https://viewer.esa-worldcover.org/worldcover, download tiles from the Terrascope/AWS Open Data bucket `s3://esa-worldcover` (anonymous read), or use `ESA/WorldCover/v200` in Earth Engine.

**Caveats.** Two epochs only, so it is a snapshot rather than a change product, and v100 and v200 use different algorithms: differencing them produces spurious change. Reported global overall accuracy is around 75 percent, with the worst confusion between shrubland, grassland and sparse vegetation. For annual time series use the Copernicus Global Land Cover or Dynamic World layers instead.

### [ESGF MetaGrid (CMIP6)](https://aims2.llnl.gov/search)

`Free (registration), email` · beginner 2/5 · climate model output

Federated archive of CMIP6 and CMIP5 model output plus obs4MIPs and input4MIPs. MetaGrid is the current search interface (aims2.llnl.gov redirects to metagrid.esgf-west.org) and generates wget scripts for bulk retrieval.

**Access.** Search in MetaGrid, download the generated wget script and run it; or script retrieval with `pip install esgpull` or `pip install intake-esgf`.

**Caveats.** Federation reliability is uneven: data nodes go offline and the same file often has to be retried from another replica. Some projects still require an ESGF OpenID plus a group registration step. For analysis at scale the cloud Zarr copy below is far less painful.

### [GEBCO gridded bathymetry](https://www.gebco.net/data-products/gridded-bathymetry-data)

`Free` · beginner 5/5 · bathymetry / global terrain model

GEBCO_2026 global terrain model at 15 arc-second resolution, published 23 April 2026, in netCDF, GeoTIFF and Esri ASCII, with a companion version giving under-ice topography for Greenland and Antarctica.

**Access.** Direct download of the global grid, of eight 90x90 degree tiles, or of a user-defined area through the download application; OPeNDAP access via CEDA for remote subsetting.

**Caveats.** Public domain and free of charge, but you are expected to cite the grid DOI. The global file is several GB, so use the area-of-interest download on a laptop. Values blend real soundings with satellite-derived predicted depth: it is a model, not measured bathymetry.

### [Global Forest Watch Open Data Portal](https://data.globalforestwatch.org/)

`Free (registration), api-key` · beginner 3/5 · forest change and deforestation alerts

Download portal and API for the Hansen/UMD 30 m annual tree cover loss and gain layers (2001 onward), near-real-time deforestation alerts (GLAD-L, GLAD-S2, RADD), fire alerts, and vector layers for concessions, protected areas and land use.

**Access.** Download 10x10 degree GeoTIFF granules from the portal, query https://data-api.globalforestwatch.org/ with a free API key, or use the same layers in Earth Engine (UMD/hansen/global_forest_change_*).

**Caveats.** Tree cover loss is not deforestation: it includes harvest, fire and storm damage. Each annual release reprocesses the full time series, so mixing versions across years is invalid. Granules are hundreds of MB each and the API is rate-limited.

### [HydroSHEDS](https://www.hydrosheds.org/)

`Free` · beginner 4/5 · hydrography / watershed data

Global hydrographic layers derived from SRTM, and for version 2 in the Americas from TanDEM-X: watershed boundaries (HydroBASINS), river networks (HydroRIVERS), lakes (HydroLAKES), environmental attributes (HydroATLAS) and flow-direction and flow-accumulation grids, in standard GIS formats.

**Access.** Direct download of shapefiles and GeoTIFFs per product and region from the Downloads pages; open in QGIS or with `geopandas.read_file()` / `rioxarray.open_rasterio()`.

**Caveats.** Attribution is required and the licence restricts some redistribution, so read the licence before republishing derived layers. Version 1 inherits SRTM's weaknesses in flat terrain and does not cover above 60 degrees North; version 2 currently covers only the Americas.

### [NASA Earthdata (CMR + earthaccess)](https://www.earthdata.nasa.gov/)

`Free (registration), email` · beginner 4/5 · multi-mission satellite and model archive

Entry point to NASA's Earth science holdings (MODIS, VIIRS, ICESat-2, GPM, SMAP, GRACE-FO, MERRA-2 and more) through the Common Metadata Repository. CMR search needs no token, returns JSON/UMM/STAC/Atom, and pages up to 2,000 results per request.

**Access.** `pip install earthaccess`; then `earthaccess.login()`, `results = earthaccess.search_data(short_name='ATL06', bounding_box=(...), temporal=(...))`, `earthaccess.download(results, 'data/')`. Raw API: https://cmr.earthdata.nasa.gov/search/granules.json?short_name=...

**Caveats.** Search is open but an Earthdata Login is required to download. Direct S3 access to cloud-hosted DAAC data only works from AWS us-west-2; from a laptop you get HTTPS instead. A few collections (commercial smallsat imagery) are restricted to NASA-funded users.

### [NASA GISTEMP v4](https://data.giss.nasa.gov/gistemp/)

`Free` · beginner 5/5 · global surface temperature record

NASA GISS Surface Temperature Analysis: global, hemispheric and zonal monthly land-ocean temperature anomalies relative to the 1951-1980 mean, distributed as plain-text tables, netCDF on a 2x2 degree grid, Zarr directories, equal-area subbox files and the input station data. Updated around the 10th of each month.

**Access.** Direct download from the Data page (tables as .txt/.csv, gridded fields as .nc); open the gridded file with `xr.open_dataset('gistemp1200_GHCNv4_ERSSTv5.nc')`. No account.

**Caveats.** These are anomalies, not absolute temperatures, and land values are smeared with a 1200 km interpolation radius, which matters in sparsely observed regions and the Arctic. The latest month can shift when upstream GHCN and ERSST inputs are revised. Cross-check with HadCRUT5, NOAAGlobalTemp and Berkeley Earth before making claims about a single year's ranking.

### [NASA Worldview and GIBS](https://worldview.earthdata.nasa.gov/)

`Free` · beginner 5/5 · near-real-time satellite imagery browser

Interactive browser for over 1,200 full-resolution global imagery layers, many available within hours of acquisition, with geostationary imagery in 10-minute steps for the last 90 days. The underlying Global Imagery Browse Services (GIBS) serve the same tiles as WMTS/WMS to QGIS and web maps.

**Access.** Web interface at worldview.earthdata.nasa.gov, no account needed to browse, animate or grab a snapshot. For scripted or GIS use add the WMTS endpoint https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi as a layer in QGIS, or use `pip install owslib`.

**Caveats.** This is visualisation, not science data: layers are rendered RGB or scaled products with no calibration guarantees, so never take measurements from them. Downloading the underlying granules needs an Earthdata Login. It is the fastest way to check whether a scene was cloudy, to find a fire or flood date, and to pick candidate acquisitions before a real download.

### [Natural Earth](https://www.naturalearthdata.com/)

`Free` · beginner 5/5 · public-domain basemap vectors

Public-domain vector and raster basemap data at 1:10m, 1:50m and 1:110m scales in cultural (countries, states, populated places, roads, railways), physical (coastlines, rivers, lakes, glaciated areas, graticules) and raster (shaded relief, bathymetry, ocean bottom) themes, built and maintained by volunteer cartographers with NACIS support.

**Access.** Direct zip download of shapefiles or a single GeoPackage from the downloads page, no account; also fetched automatically by `cartopy.feature.NaturalEarthFeature` and by the `rnaturalearth` R package.

**Caveats.** Public domain with no attribution required, but it is a cartographic product, not an authoritative boundary source: disputed boundaries follow the project's editorial choices, and the generalised geometries are unsuitable for area measurement or spatial joins at local scale. Use national or OSM data for anything analytical; use this for the map behind it.

### [NOAA Climate Data Online and GHCN-Daily](https://www.ncei.noaa.gov/cdo-web/)

`Free (registration), api-key` · beginner 4/5 · weather station records

Station climate records including GHCN-Daily: over 100,000 stations in 180 countries and territories with daily maximum and minimum temperature, precipitation, snowfall and snow depth, some series reaching back to the 18th century, updated daily.

**Access.** Request a free token by email, then `GET https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=...&startdate=...` with header `token: <key>`; or skip the API entirely and pull per-station .csv.gz from https://www.ncei.noaa.gov/pub/data/ghcn/daily/.

**Caveats.** The API allows 5 requests/second, 10,000 requests/day and at most 1,000 records per response, so anything bulk should use the flat files. Roughly half of GHCN-Daily stations report precipitation only, and station density is very uneven outside North America and Europe.

### [NOAA CoastWatch ERDDAP](https://coastwatch.pfeg.noaa.gov/erddap/)

`Free` · beginner 4/5 · ocean and atmosphere data server

ERDDAP server exposing 3,055 oceanographic and atmospheric datasets (count verified 28 August 2026): satellite sea surface temperature, ocean colour, winds, buoys and model output, served as subsettable griddap and tabledap endpoints returning netCDF, CSV, JSON, MATLAB or ready-made PNG maps from a single URL.

**Access.** Construct a URL such as .../erddap/griddap/<datasetID>.nc?sst[(2024-01-01)][(20):(40)][(-30):(-10)], or use `pip install erddapy`, or point `xarray.open_dataset()` straight at a griddap URL.

**Caveats.** Dataset IDs are server-specific and there are dozens of other ERDDAP installations (IOOS, IFREMER, EMODnet) with different holdings. Very large requests are throttled or time out; subset by time and bounding box in the URL rather than downloading whole datasets.

### [NOAA Global Monitoring Laboratory greenhouse gas records](https://gml.noaa.gov/ccgg/trends/)

`Free` · beginner 5/5 · atmospheric greenhouse gas time series

In-situ and flask CO2, CH4, N2O and SF6 records from NOAA's global cooperative air sampling network, including the Mauna Loa CO2 series started by C. D. Keeling in March 1958 (NOAA's own parallel record from May 1974); the monthly Mauna Loa mean for July 2026 was 429.12 ppm. Trends, annual growth rates and full station series are published as plain-text and CSV.

**Access.** Direct download, no key: `pandas.read_csv('https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv', comment='#')`; the whole station and ObsPack tree is under https://gml.noaa.gov/aftp/data/ over HTTPS.

**Caveats.** The most recent months are preliminary and get revised. Mauna Loa observations moved to a site on Mauna Kea after the November 2022 eruption cut access, so the record has a documented discontinuity there. NOAA and Scripps maintain separate Mauna Loa series with small offsets: do not mix them in one trend. ObsPack products have their own citation and DOI requirements.

### [NSF NCAR GDEX (formerly the Research Data Archive)](https://gdex.ucar.edu/)

`Free (registration), email` · beginner 3/5 · curated meteorological and oceanographic archive

NSF NCAR's Geoscience Data Exchange, the successor to the Research Data Archive at rda.ucar.edu (which now issues a 301 redirect here): curated long-record collections including NCEP/NCAR and NCEP/DOE reanalyses, ERA5 mirrors, JRA reanalyses, ICOADS marine observations and global radiosonde and station archives, with server-side subsetting, web services and cloud-optimised Zarr copies.

**Access.** Browse and download with a free UCAR account; submit subsetting jobs in the web interface or script them with the GDEX API client, and run notebooks against the archive in the hosted JupyterLab.

**Caveats.** The rda.ucar.edu to gdex.ucar.edu migration breaks older scripts, bookmarks and dataset paths of the form /datasets/dsNNN.N, so check any inherited download code. Most collections require a login before download and a few carry access conditions imposed by the originating agency. Some very large datasets are staged on request rather than served instantly.

### [Open-Meteo](https://open-meteo.com/)

`Free tier` · beginner 5/5 · weather and climate API

Free JSON weather API needing no key for non-commercial use: 16-day forecasts at hourly and 15-minute steps, an historical archive built on ERA5 and ERA5-Land from 1940, CMIP6 climate projections, plus marine, air quality, flood, seasonal and solar radiation endpoints.

**Access.** Plain HTTPS, no registration: `https://archive-api.open-meteo.com/v1/archive?latitude=-1.29&longitude=36.82&start_date=1991-01-01&end_date=2020-12-31&daily=temperature_2m_mean`. Official clients via `pip install openmeteo-requests`.

**Caveats.** The free non-commercial tier is capped at 600 calls per minute, 5,000 per hour and 10,000 per day, and carries no uptime guarantee; commercial use needs a paid key on reserved instances. Data are CC BY 4.0 and attribution is required. It repackages ERA5 and operational model output, so cite the underlying source as well and go to the CDS when you need the native grid rather than a point.

### [OpenAQ](https://openaq.org/)

`Free (registration), api-key` · beginner 4/5 · air quality measurements

Aggregator that harmonises open air quality measurements (PM2.5, PM10, NO2, O3, SO2, CO, black carbon) from government reference monitors and low-cost sensor networks worldwide into one schema, served through a versioned REST API and a public S3 archive of the full history.

**Access.** Register free at https://explore.openaq.org/register for a key, then `GET https://api.openaq.org/v3/locations?coordinates=6.5,3.4&radius=25000` with an `X-API-Key` header; `pip install openaq` is the official Python client. Bulk history is in the open `openaq-data-archive` S3 bucket.

**Caveats.** An API key has been mandatory since v3 and rate limits are enforced per key. Coverage follows whoever publishes an open feed, so large parts of Africa, Central Asia and Latin America are thin or sensor-only. Values are passed through as reported: no cross-network calibration is applied to low-cost sensors, and units and averaging periods differ by source.

### [OpenStreetMap bulk extracts (Geofabrik) and Overpass API](https://download.geofabrik.de/)

`Free` · beginner 4/5 · open vector basemap and infrastructure data

Geofabrik publishes daily-updated OpenStreetMap extracts per continent and country as .osm.pbf (GeoPackage for some regions) under ODbL 1.0; for targeted questions the Overpass API returns features filtered by bounding box and tag with no download at all.

**Access.** Download e.g. https://download.geofabrik.de/africa/kenya-latest.osm.pbf and convert with osmium, ogr2ogr or `pip install pyrosm`; or POST Overpass QL to https://overpass-api.de/api/interpreter (`pip install overpy` or OSMPythonTools).

**Caveats.** ODbL requires attribution and share-alike on derived databases. Public Overpass instances ask users to stay under roughly 10,000 queries and 1 GB per day and are shared infrastructure; sustained or commercial use means self-hosting. OSM completeness varies enormously by region and theme.

### [OpenTopography](https://opentopography.org/)

`Free tier, api-key` · beginner 5/5 · digital elevation models and lidar

Portal and API for global DEMs (SRTM GL1/GL3, NASADEM, ALOS World 3D, Copernicus DEM GLO-30/GLO-90, GEDI L3), USGS 3DEP rasters at 1 m, 10 m and 30 m, and hosted lidar point clouds with on-the-fly derivative generation.

**Access.** Get a free API key from My Account, then `GET https://portal.opentopography.org/API/globaldem?demtype=COP30&south=..&north=..&west=..&east=..&outputFormat=GTiff&API_Key=..`; there is also a point-elevation API and a catalogue search API.

**Caveats.** Verified 28 August 2026: free keys allow 200 calls per 24 hours for academic users on the global DEM and USGS 3DEP raster APIs and 250 per 24 hours on the point-elevation API, against 50 per 24 hours for non-academic users. Per-request area caps are 250 km2 for 1 m 3DEP, 450,000 km2 for all 30 m global DEMs, 4,050,000 km2 at 90 m and much larger for the coarse SRTM15+/GEBCO and GEDI L3 layers. Keys must not be shared or embedded in public applications; higher limits require OpenTopography Plus or a custom enterprise key.

### [PANGAEA](https://www.pangaea.de/)

`Free` · beginner 4/5 · data repository / data publisher

CoreTrustSeal-certified data publisher for Earth and environmental science run by AWI and the University of Bremen, archiving georeferenced datasets across oceans, cryosphere, geology, palaeontology, ecology and land surface, each with a DOI. Deposit and download are free.

**Access.** Search the web interface and download tab-delimited text or netCDF per dataset; in Python `pip install pangaeapy` then `PanDataSet('10.1594/PANGAEA.XXXXXX').data` returns a pandas DataFrame.

**Caveats.** Most datasets are CC-BY, but a minority sit under moratorium or restricted terms, so check each record. Deposits pass through editorial curation, so publishing data there takes days to weeks rather than minutes.

### [SoilGrids 250m](https://soilgrids.org/)

`Free` · beginner 3/5 · global soil properties

ISRIC's machine-learning global soil maps (version 2.0) at 250 m for six standard depth intervals from 0-5 cm to 100-200 cm, covering organic carbon, pH, texture fractions, bulk density, cation exchange capacity and nitrogen, with uncertainty layers alongside each prediction.

**Access.** Web viewer, WCS and REST endpoints, or GDAL directly against the hosted VRTs, e.g. `gdal_translate -projwin ... /vsicurl/https://files.isric.org/soilgrids/latest/data/phh2o/phh2o_0-5cm_mean.vrt out.tif`; the layers are also mirrored in the Earth Engine catalogue.

**Caveats.** These are predictions, not measurements, and local accuracy can be poor where training profiles are sparse; carry the uncertainty layers through any analysis. Downloading global layers at 250 m is heavy, so subset with a bounding box via WCS or /vsicurl.

### [USGS EarthExplorer / Landsat Collection 2](https://earthexplorer.usgs.gov/)

`Free (registration), email` · beginner 3/5 · Landsat and historical imagery

The whole Landsat archive under the USGS no-cost open data policy: Level-1 for Landsat 1-9 back to 1972 and Level-2 surface reflectance and surface temperature for Landsat 4-9 from 1982, alongside ASTER, declassified reconnaissance imagery, SRTM and aerial photography.

**Access.** Web search and download at earthexplorer.usgs.gov with a free ERS account; scripted access via the M2M JSON API at https://m2m.cr.usgs.gov/ (300+ USGS/EROS datasets) or Cloud-Optimized GeoTIFFs in the usgs-landsat S3 bucket.

**Caveats.** The M2M API needs a separate access request on top of the ERS account and approval is not instant. The usgs-landsat S3 bucket is requester-pays, so pulling scenes from outside AWS costs money; use EarthExplorer or the Copernicus mirror instead.

### [USGS Earthquake Catalog and real-time feeds](https://earthquake.usgs.gov/fdsnws/event/1/)

`Free` · beginner 5/5 · earthquake catalogue

Global earthquake catalogue with an FDSN event API returning QuakeML, GeoJSON, CSV or KML, capped at 20,000 events per query, plus real-time GeoJSON summary feeds (past hour/day/week/month by magnitude) for monitoring applications.

**Access.** No key needed: `GET https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-01-01&minmagnitude=5`. Feeds at https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/; ObsPy's `Client('USGS').get_events()` wraps the same service.

**Caveats.** Queries returning more than 20,000 events fail with HTTP 400, so page by time window. ComCat merges contributing networks, so magnitudes, depths and event IDs can be revised after publication, and catalogue completeness varies strongly by region and epoch.

### [USGS Water Data for the Nation (NWIS) and dataRetrieval](https://waterdata.usgs.gov/)

`Free` · beginner 4/5 · streamflow and water quality observations

Discharge, gage height, water temperature, groundwater level, precipitation and discrete water quality records from more than one million USGS monitoring locations with over 135 years of record, including about 13,500 real-time sites. Everything is served in machine-readable form through REST web services.

**Access.** `pip install dataretrieval` (or `install.packages('dataRetrieval')` in R): `from dataretrieval import nwis; df, meta = nwis.get_dv(sites='01646500', parameterCd='00060', start='2020-01-01')`. Raw endpoints at https://waterservices.usgs.gov/nwis/dv/?format=json&sites=...&parameterCd=00060 and the newer https://api.waterdata.usgs.gov/.

**Caveats.** United States only. USGS is modernising these services and retiring legacy NWIS endpoints in favour of api.waterdata.usgs.gov, so pin the client version and expect URLs to change; some new endpoints ask for a free API key. Real-time values are provisional and revised after review, and rating curves change, so never mix provisional and approved records in a trend analysis.

### [WorldClim 2.1](https://www.worldclim.org/data/worldclim21.html)

`Free` · beginner 5/5 · gridded climate surfaces

Global interpolated climate surfaces at 30 arc-second to 10 arc-minute resolution: monthly minimum, mean and maximum temperature, precipitation, solar radiation, wind speed and vapour pressure averaged over 1970-2000, plus 19 bioclimatic variables, elevation, and downscaled CMIP6 future scenarios.

**Access.** Direct zip download per variable and resolution (12 monthly GeoTIFFs each); in R, `geodata::worldclim_global(var='bio', res=10, path='.')` fetches and caches the same files.

**Caveats.** Interpolated from station data, so it is least reliable where stations are sparse: high mountains, polar regions, and parts of Africa and Amazonia. The 30 arc-second global layers are multi-GB. Licence terms are not stated on the download page; cite Fick and Hijmans (2017) and check terms before commercial reuse.

## Software

### [Cartopy](https://cartopy.readthedocs.io/)

`Free` · beginner 4/5 · map projections for matplotlib

Matplotlib-based mapping library built on PROJ, NumPy and Shapely: 30-plus map projections exposed as axes classes, correct transformation of points, lines, polygons and images between projections including dateline and pole handling, plus built-in Natural Earth features and WMS/WMTS tile access.

**Access.** `conda install -c conda-forge cartopy`; `ax = plt.axes(projection=ccrs.Robinson()); ax.coastlines(); ax.contourf(lon, lat, data, transform=ccrs.PlateCarree())`.

**Caveats.** BSD-3-Clause. Documentation moved from scitools.org.uk/cartopy to cartopy.readthedocs.io, so older links only give a redirect notice. Omitting `transform=ccrs.PlateCarree()` on plotted data is by far the most common bug and produces a plausible-looking wrong map. Natural Earth shapefiles are downloaded on first use, so the first figure needs network access.

### [Climate Data Operators (CDO)](https://code.mpimet.mpg.de/projects/cdo)

`Free` · beginner 3/5 · netCDF/GRIB command-line processing

Several hundred chainable command-line operators for climate and forecast model output in netCDF and GRIB: regridding, temporal and zonal statistics, masking, arithmetic, EOFs and file merging, developed at the Max Planck Institute for Meteorology.

**Access.** `conda install -c conda-forge cdo`; one-liners such as `cdo -remapbil,r360x180 -yearmean in.nc out.nc` or `cdo sellonlatbox,-20,50,-35,40 in.nc africa.nc`; Python bindings via `pip install cdo`.

**Caveats.** GPL; Linux and macOS are first-class, Windows works through WSL or conda. Operator chaining is powerful but terse, and `cdo -h <operator>` is the documentation you will actually use. NCO (`ncks`, `ncra`, `ncatted`) overlaps and is worth installing alongside.

### [ESA SNAP](https://step.esa.int/main/toolboxes/snap/)

`Free` · beginner 2/5 · EO image processing (SAR and optical)

ESA's desktop toolbox for Sentinel and other EO missions (SNAP 14 line), bundling the Microwave toolbox for Sentinel-1 calibration, terrain correction, polarimetry and InSAR, plus optical, SMOS, Proba-V and PolSARpro tools, with a graph-based batch processor.

**Access.** Download the multi-platform installer from step.esa.int; batch processing with `gpt <graph.xml>` from the command line; `esa_snappy` exposes the Java API to Python.

**Caveats.** Java-based and memory-hungry: InSAR on a laptop means small stacks, plenty of disk and patience. The Python bridge is fiddly to configure, so most people script gpt graphs instead. Questions get answered on the ESA STEP forum.

### [FloPy and MODFLOW 6](https://flopy.readthedocs.io/)

`Free` · beginner 2/5 · groundwater flow modelling

USGS Python package (version 3.10.0) for building, running and post-processing MODFLOW groundwater models: full MODFLOW 6 support plus MODFLOW-2005/NWT/USG, MT3D, SEAWAT, MODPATH and PEST, with structured, vertex and unstructured grid generation, boundary-condition packages, and readers for head, budget and particle-track output.

**Access.** `pip install flopy`, then `python -m flopy.utils.get_modflow :flopy` to fetch the compiled executables; `sim = flopy.mf6.MFSimulation(sim_name='m', sim_ws='./model'); gwf = flopy.mf6.ModflowGwf(sim); ...; sim.write_simulation(); sim.run_simulation()`.

**Caveats.** US Government public domain, and MODFLOW itself is public domain, so the whole stack is free including for commercial work. FloPy writes and reads model files; it does not teach hydrogeology, and a badly posed model converges happily and returns nonsense. The USGS example notebooks and the MODFLOW 6 example problems are the practical route in.

### [GDAL/OGR](https://gdal.org/)

`Free` · beginner 3/5 · geospatial format translation library

The translation and warping library underneath nearly every geospatial tool, reading and writing the large majority of raster and vector formats, with virtual filesystems that let you read remote Cloud-Optimized GeoTIFFs without downloading them.

**Access.** `conda install -c conda-forge gdal` (or OSGeo4W on Windows); CLI: `gdalinfo`, `gdal_translate`, `gdalwarp`, `gdalbuildvrt`, `ogr2ogr`; remote access with the `/vsicurl/`, `/vsis3/` and `/vsizip/` path prefixes.

**Caveats.** `pip install gdal` frequently fails against mismatched system libraries; conda-forge is the reliable route. The CLI is usually the fastest way to fix projection, nodata or format problems that stall a Python workflow.

### [GeoPandas](https://geopandas.org/)

`Free` · beginner 5/5 · vector data analysis in Python

pandas DataFrames with a geometry column: reads shapefile, GeoPackage, GeoJSON, FlatGeobuf and PostGIS, and performs spatial joins, overlays, buffering, dissolves and reprojection through shapely, pyproj and GDAL/pyogrio.

**Access.** `pip install geopandas`; `gdf = gpd.read_file('basins.gpkg', bbox=(...)); gdf.to_crs(3035).dissolve('region').plot()`; `gdf.sjoin(points)` for spatial joins.

**Caveats.** Memory-hungry on very large layers; use bbox and column filters in `read_file`, the pyogrio engine, or DuckDB spatial for millions of features. Invalid geometries in source data are the most common cause of failed overlays, so run `make_valid` first.

### [GRASS](https://grass.osgeo.org/)

`Free` · beginner 2/5 · geospatial processing engine

Long-established raster, vector and imagery processing engine (8.5.0, released 8 May 2026), strong in hydrology (r.watershed, r.stream.*), terrain analysis, image classification and time series through its temporal framework. An OSGeo and NumFOCUS project with a Python API.

**Access.** Install from grass.osgeo.org or conda-forge; `import grass.script as gs` inside a session; or run GRASS modules from the QGIS Processing toolbox without touching the GRASS interface at all.

**Caveats.** The location/mapset data model is the main barrier and catches most newcomers; meeting GRASS first through QGIS Processing is the gentler path. Several modules assume the data are already in a projected CRS.

### [leafmap](https://leafmap.org/)

`Free` · beginner 5/5 · interactive mapping in notebooks

Python package for interactive mapping and geospatial analysis in Jupyter with minimal code, wrapping ipyleaflet, folium and MapLibre and adding helpers for COGs, STAC items, local vectors, Earth Engine layers and split-screen comparison.

**Access.** `pip install leafmap`; `import leafmap; m = leafmap.Map(center=[0,35], zoom=6); m.add_cog_layer(url); m.add_stac_layer(collection='sentinel-2-l2a', item=item_id)`.

**Caveats.** Depends on many optional backends; install extras only as needed to avoid a heavy environment. Interactive maps need a live kernel, so they degrade to static images in exported HTML unless you plan for that.

### [MetPy](https://unidata.github.io/MetPy/)

`Free` · beginner 4/5 · meteorological calculations and plotting

Unidata's Python package (1.7 line, Python 3.10+) for weather data: unit-aware thermodynamic and dynamic calculations (CAPE, CIN, dewpoint, lifted index, isentropic analysis, frontogenesis, Q-vectors), Skew-T/log-P diagrams, hodographs and station plots, and readers for GEMPAK, NEXRAD Level II/III radar and GINI satellite files.

**Access.** `conda install -c conda-forge metpy`; `from metpy.calc import dewpoint_from_relative_humidity; from metpy.units import units`, and the `.metpy` xarray accessor attaches units and CRS to a dataset (`ds.metpy.parse_cf()`).

**Caveats.** BSD-3-Clause. Everything is unit-aware through pint, which is the main source of beginner errors: bare NumPy arrays without units raise or silently mis-scale. The example gallery and the 'MetPy Mondays' video series are the fastest way in. It handles diagnostics and plotting, not forecasting or model running.

### [ObsPy](https://docs.obspy.org/)

`Free` · beginner 3/5 · seismological data processing

Python framework for seismology (version 1.5.1; documentation last built 28 August 2026): readers for miniSEED, SAC, SEG-Y and StationXML, FDSN and SeedLink clients, instrument response removal, filtering, triggering, and event and station metadata handling.

**Access.** `conda install -c conda-forge obspy`; `st = obspy.read('trace.mseed'); st.remove_response(inventory=inv, output='VEL'); st.filter('bandpass', freqmin=0.05, freqmax=1.0)`; downloads via `obspy.clients.fdsn.Client`.

**Caveats.** LGPL. Response deconvolution and unit handling are the classic beginner trap: read the tutorial on `remove_response` before trusting amplitudes. Large waveform sets should be streamed to disk rather than held in memory.

### [Panoply](https://www.giss.nasa.gov/tools/panoply/)

`Free` · beginner 5/5 · netCDF/HDF/GRIB desktop viewer

NASA GISS desktop viewer (version 5.10.1, released 2 August 2026) that plots georeferenced arrays straight out of netCDF, HDF and GRIB files: maps in dozens of projections, longitude-vertical and time sections, line plots, differences between two variables or two files, and export to PNG, PDF or animation.

**Access.** Download the Java application for macOS, Windows or Linux and open a file; requires Java 11 or later and no Python environment at all.

**Caveats.** A viewer, not an analysis tool: no scripting, no batch processing, and it will not repair a malformed file. Its value is diagnostic, showing what is actually inside an unfamiliar file (variable names, dimension order, units, missing-value conventions, whether latitudes run north-to-south) before you write code, and it works on locked-down machines where installing packages is not possible.

### [PyGMT](https://www.pygmt.org/)

`Free` · beginner 3/5 · publication-quality maps and geophysical plotting

Python interface (v0.19.0) to the Generic Mapping Tools C API for maps and figures in geophysics, oceanography and planetary science: projections, coastlines, gridding and filtering, cross-sections, focal mechanisms, velocity vectors and 3D perspective plots, taking pandas, xarray and geopandas objects directly.

**Access.** `conda install -c conda-forge pygmt`; `fig = pygmt.Figure(); fig.basemap(region=[30,45,-5,10], projection='M15c', frame=True); fig.coast(land='grey', shorelines=True); fig.show()`. The `gmt` command line is installed alongside for shell scripting.

**Caveats.** BSD-3-Clause (GMT itself is LGPL). `pip install pygmt` regularly fails because the GMT C library version must match; conda-forge is the reliable route. Remote datasets such as Earth relief and seafloor age grids are downloaded and cached on first use, so the first figure needs a network connection.

### [pystac-client with odc-stac / stackstac](https://pystac-client.readthedocs.io/)

`Free` · beginner 3/5 · STAC search and lazy raster loading

Client for STAC APIs (Copernicus Data Space, Planetary Computer, Earth Search) that turns a space/time/collection query into an item collection; odc-stac or stackstac then load the matching Cloud-Optimized GeoTIFFs directly into an xarray cube without downloading whole scenes.

**Access.** `pip install pystac-client odc-stac`; `cat = Client.open('https://planetarycomputer.microsoft.com/api/stac/v1'); items = cat.search(collections=['sentinel-2-l2a'], bbox=bbox, datetime='2024-06/2024-09', query={'eo:cloud_cover':{'lt':20}}).item_collection(); ds = odc.stac.load(items, bands=['red','nir'], resolution=10, bbox=bbox)`.

**Caveats.** Lazy loading only helps if you constrain bbox, bands and resolution; requesting a full tile stack will still exhaust a laptop. Some catalogues need signed asset URLs (`planetary_computer.sign`) or a bearer token, and signatures expire during long jobs.

### [QGIS](https://qgis.org/)

`Free` · beginner 5/5 · desktop GIS

Full desktop GIS (4.2 is the current release line) for vector and raster editing, cartography, georeferencing, digitising and spatial analysis, with a large plugin ecosystem and an embedded Python console. GPLv2+ on Windows, macOS and Linux.

**Access.** Install from qgis.org or conda-forge; script with the built-in Python console and PyQGIS; the Processing toolbox exposes GDAL, GRASS and SAGA algorithms and can be run headlessly with `qgis_process`.

**Caveats.** Verified 28 August 2026: the latest release is QGIS 4.2.1 'Belem do Para' (31 July 2026) and the long-term release is 3.44.13 'Solothurn'. Use the LTR branch for teaching and production. Plugin quality varies and some plugins depend on external binaries; several are not yet ported to the 4.x line. Large rasters are slow unless you build overviews first.

*Also listed under: social.*

### [WhiteboxTools](https://www.whiteboxgeo.com/)

`Free` · beginner 3/5 · terrain, hydrology and lidar processing

Rust-based geospatial analysis engine from the University of Guelph with a large open-source tool library for terrain analysis, depression breaching and flow routing, stream network extraction, LiDAR/LAS point cloud processing, image processing and math operations, callable as a standalone binary or from Python, R and QGIS.

**Access.** `pip install whitebox`; `import whitebox; wbt = whitebox.WhiteboxTools(); wbt.breach_depressions_least_cost('dem.tif','filled.tif', dist=100); wbt.d8_pointer('filled.tif','ptr.tif'); wbt.d8_flow_accumulation('ptr.tif','fac.tif', pntr=True)`. Also the WhiteboxTools for QGIS plugin and the `whitebox` R package.

**Caveats.** The core engine is MIT-licensed and complete on its own, but Whitebox Workflows for Python Professional and the general/agriculture/lidar toolset extensions are commercial add-ons, and a handful of advanced tools live only there. Tools that measure distance or area assume a projected CRS: running them on degrees gives wrong numbers without warning. Its hydrological conditioning (breaching rather than filling) is the reason most geomorphologists reach for it over GRASS or SAGA.

### [xarray (with rioxarray and Dask)](https://docs.xarray.dev/)

`Free` · beginner 4/5 · labelled N-dimensional arrays

The standard Python library for labelled multidimensional data: netCDF, Zarr, GRIB and HDF climate and satellite arrays with named dimensions and coordinate-based selection, plus Dask-backed out-of-core computation that lets a laptop process datasets larger than its memory.

**Access.** `pip install 'xarray[complete]' rioxarray`; `ds = xr.open_dataset('era5.nc'); ds.t2m.sel(time='2024-07').mean('time').plot()`; `xr.open_mfdataset(files, chunks={'time': 24})` for multi-file archives; rioxarray adds CRS-aware clipping and reprojection.

**Caveats.** Chunk sizes matter more than machine size: badly chunked Dask graphs are the usual reason a laptop dies on ERA5. GRIB support needs cfgrib/eccodes, an extra install that is easiest through conda-forge.

### [xclim](https://xclim.readthedocs.io/)

`Free` · beginner 3/5 · climate indicators and bias adjustment

Ouranos-developed xarray/Dask library for climate services: a large catalogue of CF-compliant climate indicators including the ETCCDI and ET-SCI index families (heat and cold spells, frost and growing-season days, growing degree days, precipitation percentiles and drought indices), plus a bias-adjustment and statistical downscaling module (SDBA) and climate ensemble statistics.

**Access.** `pip install xclim` or conda-forge; `import xclim; hot = xclim.atmos.tx_days_above(tasmax=ds.tasmax, thresh='30 degC', freq='YS')`. Operates lazily on Dask-backed xarray objects, so it scales to CMIP6 ensembles.

**Caveats.** Apache-2.0. Deliberately strict about CF metadata and units: inputs without a `units` attribute or with the wrong calendar raise or warn, which is the point but is the main early friction. Bias adjustment is easy to misuse and can manufacture trends; work through the SDBA notebooks before applying it to projections. ESMValTool and climate-indices cover overlapping ground with different trade-offs.

## Literature

### [EarthArXiv](https://eartharxiv.org/)

`Free, email` · beginner 5/5 · preprint server

Community-governed preprint server for the Earth, planetary and environmental sciences, running on the open-source Janeway platform with California Digital Library support. Posting and reading are free and each preprint receives a DOI.

**Access.** Register, then use 'Start New Submission' to upload a PDF and metadata; browse or search the site directly, and preprints are picked up by Google Scholar and other discovery services.

**Caveats.** Moderation checks scope and basic suitability, not scientific correctness, so read preprints accordingly. Check your target journal's preprint policy before posting; most Earth-science journals accept preprints but a few still do not.

### [ESS Open Archive](https://essopenarchive.org/)

`Free, email` · beginner 4/5 · preprint and poster archive

Preprint archive for the Earth and space sciences run by AGU with Wiley, hosting preprints and conference posters with DOIs. Posting and reading cost nothing.

**Access.** Create a free account and upload a manuscript or poster; content is openly readable and indexed without an account.

**Caveats.** Screening is light and does not imply peer review. Because it is publisher-affiliated, the submission workflow is oriented towards AGU journals; verify the current transfer options on the site rather than assuming, and confirm your target journal's preprint policy either way.

### [NASA ADS / SciX](https://ui.adsabs.harvard.edu/)

`Free (registration), api-key` · beginner 4/5 · bibliographic database and API

Free literature search engine with full-text indexing, citation and reference graphs and links to preprints; the NASA Science Explorer (SciX) expansion extends the same index from astronomy to Earth science, planetary science and heliophysics. A free token opens a scriptable API.

**Access.** Create a free account, generate a token in user settings, then `GET https://api.adsabs.harvard.edu/v1/search/query?q=title:permafrost&fl=bibcode,title,citation_count` with header `Authorization: Bearer <token>`; Python client `pip install ads`.

**Caveats.** API allowances are per-endpoint and reported in response headers (commonly a few thousand calls per day). Earth-science coverage is newer and thinner than astronomy's, so cross-check OpenAlex and Crossref for geoscience bibliometrics. Full text is indexed only where publishers permit it.

## Compute

### [Copernicus Data Space openEO](https://openeo.dataspace.copernicus.eu/)

`Free tier, email` · beginner 3/5 · server-side EO datacube processing

Process the Sentinel archive where it is stored: define a datacube (collection, bounding box, time range, bands), chain operations, and download only the result. Free accounts receive 10,000 openEO credits per month, and the ecosystem also offers a hosted JupyterLab.

**Access.** `pip install openeo`; `con = openeo.connect('openeo.dataspace.copernicus.eu').authenticate_oidc()`, then `con.load_collection('SENTINEL2_L2A', spatial_extent=..., temporal_extent=..., bands=['B04','B08']).reduce_dimension(...).execute_batch('ndvi.nc')`.

**Caveats.** Credits are consumed per job, so long time series over large areas exhaust the monthly allowance quickly; prototype on a small extent first. Free accounts are limited to two concurrent API requests and about 12 requests per minute.

### [CryoCloud](https://cryointhecloud.com/)

`Free (registration), application` · beginner 3/5 · community JupyterHub for Earth science

NASA-supported JupyterHub operated in partnership with 2i2c for cryosphere and wider Earth-science research, running in AWS us-west-2 next to NASA's cloud-hosted data, with shared environments and an open JupyterBook of recorded tutorials and hackweek material.

**Access.** Request an account through the site, then work in the browser at hub.cryointhecloud.com with the community image; the tutorials at book.cryointhecloud.com are readable by anyone.

**Caveats.** Accounts are granted to community members rather than opened to everyone, and capacity depends on grant funding, so treat it as a shared and potentially temporary resource. Its main advantage is co-location with NASA DAAC data in us-west-2, which makes direct S3 access fast.

### [Digital Earth Africa Sandbox](https://sandbox.digitalearth.africa/)

`Free (registration), email` · beginner 4/5 · free JupyterHub over an African data cube

Free browser-based JupyterLab with an Open Data Cube covering the whole African continent: analysis-ready Landsat, Sentinel-1 and Sentinel-2, plus continental products including Water Observations from Space, cropland extent, coastlines, land cover and water quality, alongside a large repository of worked notebooks.

**Access.** Sign up at sandbox.digitalearth.africa and work in the browser; `import datacube; dc = datacube.Datacube(); ds = dc.load(product='s2_l2a', x=(36.7,36.9), y=(-1.4,-1.2), time='2024-01/2024-03', measurements=['red','nir'])`. The same products are readable from outside via the STAC API and the public `deafrica-services` S3 bucket.

**Caveats.** Sign-up uses phone verification that does not work for numbers registered in China, Turkey, the United States, the United Kingdom, Zambia or Burundi; those users must contact support to be added manually. Sandbox sessions are shared and modest in CPU and RAM, and larger jobs need a separate use-case request. Coverage is Africa only, which is exactly why it matters for researchers there.

### [Google Colab](https://colab.research.google.com/)

`Free tier, email` · beginner 5/5 · free hosted notebooks

Browser-based Jupyter notebooks with a preinstalled scientific Python stack and optional GPU, requiring no local installation. The default environment for most Earth Engine, geemap and xarray tutorials and the usual fallback where students have weak laptops.

**Access.** Open a notebook from GitHub, Drive or a URL; `!pip install` extra geospatial packages per session; mount Google Drive for persistence between sessions.

**Caveats.** Free sessions are pre-emptible and time-limited, GPU availability is not guaranteed, and anything not written to Drive or cloud storage disappears when the VM recycles. RAM and disk are modest: fine for tutorials and subsets, not for multi-hundred-GB archives.

### [Google Earth Engine](https://earthengine.google.com/)

`Free tier, application` · beginner 4/5 · hosted planetary-scale raster analysis

Server-side analysis over a hosted multi-petabyte catalogue (Landsat, Sentinel, MODIS, ERA5, Hansen forest change, SoilGrids and hundreds more). Noncommercial projects get 150 EECU-hours per month on the free Community Tier, or 1,000 EECU-hours per month on the Contributor Tier aimed at graduate students, researchers and nonprofits.

**Access.** Register a Cloud project for noncommercial use, then work in the Code Editor at code.earthengine.google.com (JavaScript) or `pip install earthengine-api` with `ee.Authenticate(); ee.Initialize(project='my-project')`; geemap and leafmap bridge it into notebooks.

**Caveats.** Commercial use requires a paid plan, and projects registered before 15 April 2025 had to verify noncommercial eligibility to keep access. Verified 28 August 2026: Community Tier is 150 EECU-hours per month (540,000 EECU-seconds) with no extra requirements; Contributor Tier is 1,000 EECU-hours per month but needs an active billing account attached even though Earth Engine itself is not charged; an application-only Partner Tier gives 100,000 EECU-hours per month for demonstrated high-impact climate mitigation, adaptation or protection work. Quotas reset monthly and exhausting them drops the project into restricted mode rather than cutting it off. Exports go to Google Drive or Cloud Storage and count against those quotas.

### [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/)

`Free` · beginner 3/5 · public STAC catalogue on Azure

Public STAC API and Azure-hosted copies of Sentinel, Landsat, NAIP, MODIS, Copernicus DEM, ERA5 and many derived collections. The STAC API at /api/stac/v1 was responding and the catalogue open as of August 2026.

**Access.** `pip install pystac-client planetary-computer odc-stac`; open https://planetarycomputer.microsoft.com/api/stac/v1, search, then `planetary_computer.sign(item)` before loading assets with odc-stac or rioxarray. No account is needed for anonymous reads of public collections.

**Caveats.** Treat the hosted JupyterHub ('the Hub') as unreliable for planning: access has been request-gated and its status is not clearly documented, so assume you supply your own compute and use this as a data source. Anonymous access to the underlying storage accounts was disabled in October 2024, so go through the signing API, and re-sign inside long-running jobs because signatures expire.

## Publishing

### [Earth System Science Data (ESSD)](https://essd.copernicus.org/)

`Free tier, email` · beginner 3/5 · data journal

Peer-reviewed journal for data papers: articles describe original, openly archived datasets rather than interpreting them, and pass through public discussion in ESSDD before final publication. The standard route to a citable, reviewed record for a dataset in this field.

**Access.** Deposit the dataset first in a trustworthy repository with a DOI (PANGAEA, Zenodo, a NASA DAAC), then submit the describing paper through the Copernicus editorial system.

**Caveats.** Free to read, but publication costs about EUR 1,400 per paper; the Copernicus waiver and discount routes noted above apply. Interpretation of the data is explicitly out of scope for regular articles, and the dataset must be openly accessible before review begins.

### [EGUsphere and Copernicus interactive public peer review](https://egusphere.copernicus.org/)

`Free tier, email` · beginner 3/5 · preprints and open peer review

EGU's preprint and discussion platform: submissions to most EGU journals are posted as preprints and reviewed in the open, with referee reports, author replies and community comments permanently archived alongside the final paper.

**Access.** Submit through the journal's Copernicus editorial system, which posts the preprint and opens the public discussion; all preprints, discussions and final papers are free to read with no account.

**Caveats.** Reading and preprint posting are free, but publishing the final paper in most EGU journals carries an APC (about EUR 1,800 for Atmospheric Chemistry and Physics, Biogeosciences and HESS; EUR 1,980 for Climate of the Past; EUR 1,400 per paper for ESSD). Copernicus offers reductions for EGU members and for authors from economically disadvantaged and Research4Life countries, and a few journals (Aerosol Research, Geographica Helvetica, History of Geo- and Space Sciences) charge nothing at all. Request waivers before submission, not after acceptance.

### [Journal of Open Source Software (JOSS)](https://joss.theoj.org/)

`Free, email` · beginner 4/5 · software paper venue

Diamond open-access venue for research software: a short paper plus fully open review of the repository itself, conducted in public GitHub issues, with Crossref DOIs and Portico archiving. No fees to authors at any stage.

**Access.** Submit the repository URL and a `paper.md` through the JOSS site; reviewers work through a public checklist against the live repository.

**Caveats.** Scope is genuine research software with documentation, tests, an OSI-approved licence and evidence of use; thin API wrappers and single-function packages are desk-rejected. Review happens in public, which some authors find exposing, and typically takes weeks to months.

### [Seismica](https://seismica.library.mcgill.ca/)

`Free, email` · beginner 4/5 · diamond open-access journal (seismology)

Diamond open-access journal for seismology and earthquake science published by McGill University Library since 2022: free to read and free to publish, CC-BY 4.0, one volume a year with two regular issues plus special issues, currently in volume 5 (2026).

**Access.** Submit through the OJS site; there are no submission, page or processing fees at any stage, and review is handled by volunteer community editors.

**Caveats.** A young journal, so indexing and citation metrics are thinner than for legacy titles, which matters if you are assessed on impact factors. Volunteer editorial capacity means review timelines vary.

### [Volcanica](https://www.jvolcanica.org/)

`Free, email` · beginner 4/5 · diamond open-access journal (volcanology)

Diamond open-access journal covering all of volcanology (research articles, reviews, reports and methods papers), free to publish and free to read, indexed in DOAJ with the DOAJ Seal; volume 9 published in 2026.

**Access.** Submit through the journal website; no article processing charges and no subscription barrier for readers.

**Caveats.** As with other volunteer-run diamond journals, turnaround depends on editor availability. For structural geology and tectonics the equivalent venue is Tektonika (tektonika.online), also community-led diamond open access.

## Funding

### [AWS Open Data Sponsorship Program](https://aws.amazon.com/opendata/open-data-sponsorship-program/)

`Free, application` · beginner 2/5 · in-kind data hosting sponsorship

AWS covers the cost of storing and sharing publicly available, cloud-optimised datasets through the Registry of Open Data on AWS, which is how a small group can publish a multi-terabyte Earth-science dataset without paying for hosting.

**Access.** Apply at https://application.opendata.aws; applications are reviewed on a rolling basis, with decisions usually within about two weeks.

**Caveats.** The obligations are real: an open licence, non-proprietary cloud-optimised formats, documentation and a tutorial notebook, a dedicated AWS account, and no fees charged to users. It funds hosting only, not salaries, fieldwork or analysis.

### [Idea Wild](https://www.ideawild.org/)

`Free, application` · beginner 3/5 · equipment grants for conservation researchers

US non-profit that gives field equipment rather than cash to biodiversity conservation, research and education projects: camera traps, GPS units, binoculars, acoustic recorders, laptops, dive and field gear. Projects costing under about USD 1,500 are an explicitly stated priority, and applications are accepted year-round from all countries.

**Access.** Apply through the online application at https://ideawild.org/application, listing the specific items needed; no institutional affiliation or grant-writing apparatus required.

**Caveats.** Targeted at conservationists in the Global South and under-resourced countries; applicants from wealthy countries are generally not funded unless representing tribal or marginalised communities or working with country nationals. It funds equipment and sometimes fieldwork costs, never scholarships or conference travel, and a valid US contact address is required to receive shipments (not Alaska, Hawaii or Puerto Rico). At most two applications per 12 months, and past recipients must report before reapplying.

### [National Geographic Society grants](https://www.nationalgeographic.org/explore/grants-investments/)

`Free, application` · beginner 2/5 · project grants for individuals

Project funding across six focus areas including Ocean, Land, Wildlife and Planetary Health. The Society has moved away from standing Level I/II tiers to targeted Requests for Proposals, with budgets set by each call.

**Access.** Apply through the National Geographic Society Funding Portal against an open RFP; applicants must be 18 or older, the project leader writes the application, and projects must start at least six months after the deadline.

**Caveats.** One of the few substantial routes that does not require an institutional affiliation, and local knowledge and community ties are explicitly valued. You may lead only one funded project at a time and must close out reports from previous grants first. Deadlines are per-RFP, so the portal needs checking regularly.

### [Rufford Foundation Small Grants](https://www.rufford.org/)

`Free, application` · beginner 3/5 · small conservation and field research grants

Grants for nature-conservation projects in eligible, mostly lower- and middle-income countries, awarded in four escalating tiers (1st and 2nd Rufford Small Grant, Booster Grant, Completion Grant) ranging from GBP 7,000 to GBP 18,000. 6,841 projects funded across 152 countries to date.

**Access.** Apply year-round through https://apply.ruffordsmallgrants.org; there are no fixed deadlines, and unsuccessful applicants may reapply after 12 months.

**Caveats.** Aimed at people early in a conservation career: current master's and doctoral students and recent graduates are the core audience, undergraduates are not funded, and the target species or habitat must be threatened. Country eligibility is a specific published list, so check it before writing. Higher tiers open only after a previous Rufford grant is completed.

### [TWAS research grants](https://twas.org/opportunities/research-grants)

`Free, application` · beginner 2/5 · grants for researchers in developing countries

Grants for scientists based in science- and technology-lagging countries, several of which explicitly cover Earth sciences: the Seed Grant for New African Principal Investigators lists Earth sciences among its disciplines, and the MENA collaborative programme includes marine and climate research.

**Access.** Apply through the TWAS online portal when a call is open; each call publishes its eligible-country list and age limits (typically 40 for early-career schemes, up to 46 for some collaborative ones).

**Caveats.** Call schedules shift year to year: as listed in 2026 several programmes were closed and TWAS stated that no call would open in 2026 for the basic-sciences grants. Applicants must hold a position at an eligible institution, so this does not serve fully unaffiliated researchers.

## Learning

### [Data Carpentry Geospatial workshop](https://datacarpentry.github.io/geospatial-workshop/)

`Free` · beginner 5/5 · hands-on geospatial curriculum

Two-day open curriculum in three lessons: geospatial concepts and data structures, introduction to R for geospatial data, and raster and vector analysis with sf, terra, ggplot2 and dplyr. Lesson text is CC-BY 4.0 and the teaching datasets are on Figshare under CC-BY.

**Access.** Work through the episodes self-paced from the website, or attend or host a Carpentries workshop; all code, data and setup instructions are included.

**Caveats.** R-centric; the Python geospatial equivalents live in the Carpentries Incubator and are less mature. Self-study loses the live instructor and helper feedback that makes the format effective, so work through it with someone if you can.

### [Earth Data Science / ESIIL Learning Portal (Earth Lab, CU Boulder)](https://www.earthdatascience.org/)

`Free` · beginner 5/5 · environmental data science curriculum

Free open textbooks and course material from Earth Lab and ESIIL at the University of Colorado Boulder, including 'Introduction to Earth and Environmental Data Science', 'IGNITE Data Analytics for early-career researchers', and lesson series on Python, R, Google Earth Engine, cloud computing, remote sensing time series and reproducible workflows, all with runnable code and sample data.

**Access.** Read directly on the site; lessons link to their source repositories so notebooks can be cloned and run locally or in the cloud. No account needed.

**Caveats.** The portal was reorganised around ESIIL, so some older earthdatascience.org lesson URLs are stale or redirect: search from the front page rather than trusting bookmarks or search-engine hits. Licence terms are not stated uniformly across pages, so check the source repository before reusing material in your own teaching. Strongest on the workflow and tooling side, lighter on the underlying Earth science.

### [End-to-End Google Earth Engine (Spatial Thoughts)](https://courses.spatialthoughts.com/end-to-end-gee.html)

`Free` · beginner 4/5 · Earth Engine course

Six-module applied remote sensing course in Earth Engine by Ujaval Gandhi: image collections and filtering, cloud masking and spectral indices, reducers and time series, supervised classification with accuracy assessment, change detection, apps, and the Python API.

**Access.** Free self-paced material online: written modules, a public Earth Engine script repository containing all code, slide decks, and video lessons on YouTube and Vimeo.

**Caveats.** You need an Earth Engine account (noncommercial registration) to run the exercises, so the free-tier quota applies. Earth Engine's API moves faster than course text, so occasional snippets lag current syntax.

### [EO College](https://eo-college.org/)

`Free (registration), email` · beginner 4/5 · Earth observation courses

Free online Earth observation courses, including the long-running Advanced Training Course series on radar polarimetry and land remote sensing, plus tutorials on water quality, agriculture and the ESA BIOMASS mission.

**Access.** Create a free account and enrol; courses are self-paced with video lessons, quizzes and downloadable material.

**Caveats.** Depth varies considerably between courses; the SAR and polarimetry material is the standout and is hard to find free elsewhere. Several courses are tied to specific ESA missions and their processing tools.

### [Geocomputation with R](https://r.geocompx.org/)

`Free` · beginner 4/5 · open textbook, spatial analysis in R

Free online second edition (CRC Press, 2024) of the standard open textbook for spatial data in R: sf and terra data structures, attribute and spatial operations, geometry operations, raster-vector interaction, reprojection, I/O, cartography, bridges to GDAL/GRASS/QGIS, spatial statistical learning, and applied chapters on transport, geomarketing and ecology.

**Access.** Read at r.geocompx.org; source, all code and exercise solutions are on GitHub, and a Python companion volume is at py.geocompx.org.

**Caveats.** The prose is CC BY-NC-ND 4.0 (non-commercial, no derivatives) while the code is CC0, so you can reuse the code freely but cannot remix the text into your own course notes. Assumes working R knowledge; it is not an introduction to programming. The first edition is archived separately on bookdown.org and now uses superseded packages.

### [NASA ARSET](https://www.earthdata.nasa.gov/data/projects/arset)

`Free (registration), email` · beginner 5/5 · applied remote sensing training

NASA's Applied Remote Sensing Training programme: free live webinars and self-paced online courses on air quality and health, agriculture, disasters, water resources, climate resilience, ecological conservation and wildland fires, with 'Fundamentals of Remote Sensing' as the entry course. Materials from 2015 onward are archived.

**Access.** Register for any training at no cost from the ARSET pages; recordings, slides, exercise data and Q&A summaries stay online afterwards, so past courses can be taken asynchronously.

**Caveats.** Application-focused rather than theory-heavy, and many exercises are tied to specific NASA portals and tools. Live sessions run in US time zones, which the archived recordings work around.

### [Project Pythia](https://projectpythia.org/)

`Free` · beginner 5/5 · geoscience Python curriculum

Pangeo's education arm: the Foundations book teaches the core stack (Python, NumPy, Matplotlib, Cartopy, Pandas, Xarray, Dask) and domain Cookbooks give executable end-to-end workflows. Code is Apache-2.0 and text CC-BY-4.0, supported by NCAR, Unidata and UAlbany with NSF funding.

**Access.** Read at projectpythia.org; every page links to its source repository so notebooks can be cloned and run locally, or launched in a browser from the provided buttons.

**Caveats.** Assumes basic programming comfort and offers no assessment or certificate. Cookbook quality varies by contributor, so Foundations is the reliable spine and Cookbooks are best treated as worked examples to adapt.

## Community

### [Copernicus Data Space Ecosystem forum](https://forum.dataspace.copernicus.eu/)

`Free (registration), email` · beginner 4/5 · official support forum

Discourse forum where Copernicus Data Space staff and moderators answer questions on the Sentinel data offer, the hosted JupyterLab, openEO, the STAC, OData and S3 APIs, and on-demand processing. Active in August 2026.

**Access.** Read without an account; register free to post. Search the archive first, as quota, authentication and product-availability questions repeat frequently.

**Caveats.** Staff response times vary and some threads go unanswered for weeks. It is the right venue for data-access and quota problems, but SNAP processing issues belong on the ESA STEP forum instead.

### [ECMWF user forum](https://forum.ecmwf.int/)

`Free (registration), email` · beginner 4/5 · reanalysis and NWP support forum

ECMWF-run forum covering the Climate and Atmosphere Data Stores, ERA5, IFS and OpenIFS, ECMWF software and training. 'Datasets and usage' is the busiest category and is where most CDS API and ERA5 problems get resolved.

**Access.** Read openly; register free to post. Check the announcements category for Data Store outages and migrations before opening a new thread.

**Caveats.** Answers come from a mix of ECMWF staff and experienced users, so response quality varies by category. It is not a general Python help desk; keep questions specific to ECMWF data and services.

### [GIS Stack Exchange](https://gis.stackexchange.com/)

`Free, email` · beginner 4/5 · practitioner Q&A

Large Q&A archive for practical geospatial problems: GDAL errors, coordinate reference systems, QGIS and PyQGIS, Earth Engine scripting, geopandas and rasterio. The physical-science counterpart is Earth Science Stack Exchange.

**Access.** Search the archive first, since most problems are already answered; a free account is needed only to ask or answer. Post a minimal reproducible example with versions and the exact error text.

**Caveats.** Strict about scope and duplicates: opinion-based questions, 'which tool should I use' and code-free problem descriptions get closed quickly. Earth Science Stack Exchange is much smaller and slower to receive answers.

### [Pangeo Discourse](https://discourse.pangeo.io/)

`Free (registration), email` · beginner 4/5 · forum for scalable geoscience computing

Forum of the Pangeo community covering Zarr, netCDF and HDF, Dask and cloud workflows, data catalogues, machine learning on large arrays, plus job posts and a regular community showcase. Active with posts through August 2026.

**Access.** Readable without an account; register free to post. Questions are often answered by the maintainers of the libraries themselves.

**Caveats.** Best for data-engineering questions (chunking, cloud storage, scaling, formats) and weaker for domain science. A minimal reproducible example gets far better results than a prose description of your workflow.

### [Software Underground](https://softwareunderground.org/)

`Free, email` · beginner 4/5 · geoscience programming community

Not-for-profit, member-supported community of geoscientists and engineers doing subsurface, geophysics and geological computing: a free open chat on Mattermost, the annual Transform conference and hackathons, and an archive of tutorials, recorded talks and open-source project discussion.

**Access.** Join free from the website to get into the chat; Transform conference recordings and hackathon material are public on YouTube and GitHub with no membership needed.

**Caveats.** Centre of gravity is subsurface geoscience (seismic, wells, petrophysics, geomechanics, geothermal) rather than climate or satellite remote sensing, and much of it grew out of the energy industry. The community moved off Slack to Mattermost, so old Slack invite links circulating in blog posts are dead. Volume is lower than Stack Exchange but the answers come from people who wrote the tools.
