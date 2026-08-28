# Earth, climate & environmental science

Part of [research-vault](../README.md). 58 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (22) · [Software](#software) (10) · [Literature](#literature) (3) · [Compute](#compute) (5) · [Publishing](#publishing) (5) · [Funding](#funding) (4) · [Learning](#learning) (5) · [Community](#community) (4)

## Data

### [Argo float profiles](https://argo.ucsd.edu/)

`Free` · beginner 3/5 · in-situ ocean profiles

Global array of profiling floats measuring temperature and salinity through the upper ~2000 m, with biogeochemical variables on BGC floats. Profiles are free from the Global Data Assembly Centres as netCDF and updated daily.

**Access.** `pip install argopy`; `from argopy import DataFetcher; ds = DataFetcher(mode='research').region([-75,-45,20,30,0,1000,'2024-01','2024-06']).to_xarray()`. Raw files via the Coriolis and US GDAC HTTPS/FTP mirrors, or through Ifremer's ERDDAP.

**Caveats.** Real-time profiles carry only automated quality control; delayed-mode data, available months later, is what climate work needs. Always respect QC flags (argopy's 'research' mode applies the strict filter for you). Whole-array downloads are large, so fetch by region and time.

### [ASF Vertex and HyP3 (SAR)](https://search.asf.alaska.edu/)

`Free (registration), email` · beginner 3/5 · synthetic aperture radar

Alaska Satellite Facility DAAC search and download for Sentinel-1 and legacy SAR missions such as ALOS PALSAR, with the HyP3 service generating radiometrically terrain-corrected products and InSAR interferograms on demand in the cloud instead of on your machine.

**Access.** Search Vertex with an Earthdata Login; script with `pip install asf_search` (`asf_search.search(platform='SENTINEL-1', intersectsWith=wkt, ...)`) and submit processing jobs with `pip install hyp3_sdk`.

**Caveats.** HyP3 jobs are free but metered by a monthly per-user credit allowance, so large InSAR stacks need planning. Doing the same processing locally means ESA SNAP plus a lot of RAM and disk; raw Sentinel-1 SLCs are several GB per scene.

### [CMIP6 analysis-ready Zarr in the cloud (Pangeo/ESGF)](https://pangeo-data.github.io/pangeo-cmip6-cloud/)

`Free` · beginner 3/5 · cloud-optimised climate model output

A large subset of CMIP6 rewritten as cloud-optimised Zarr in the public buckets gs://cmip6 and s3://cmip6-pds, with one CSV/JSON catalogue listing every store. Anonymous read access works with no billing account.

**Access.** `pip install intake-esm gcsfs zarr xarray`; `col = intake.open_esm_datastore('https://storage.googleapis.com/cmip6/pangeo-cmip6.json')`, then `col.search(source_id='MPI-ESM1-2-LR', variable_id='tas', experiment_id='ssp585').to_dataset_dict()`. Anonymous access uses `token='anon'` (GCS) or `anon=True` (S3).

**Caveats.** It is a curated subset of ESGF, not the whole archive, and lags new model submissions. Reading over a home connection is fine for single variables and subsets but slow for large ensembles; the same catalogue exists on AWS if you compute there.

### [Copernicus Climate Data Store (ERA5)](https://cds.climate.copernicus.eu/)

`Free (registration), api-key` · beginner 3/5 · reanalysis and climate indicators

ERA5 global reanalysis (hourly, 0.25 degree, 1940 to near-present), ERA5-Land at about 9 km, seasonal forecasts, satellite climate records and CMIP6-derived climate indicators, all retrievable by API after free registration.

**Access.** `pip install 'cdsapi>=0.7.7'`; put `url: https://cds.climate.copernicus.eu/api` and `key: <personal access token>` in ~/.cdsapirc, then `cdsapi.Client().retrieve('reanalysis-era5-single-levels', {...}, 'out.nc')`.

**Caveats.** You must accept each dataset's licence in the web interface before the API will serve it. Requests are queued: large ERA5 pulls take hours to days, and the most recent ~5 days are preliminary ERA5T that is later revised. The newer `ecmwf-datastores-client` adds asynchronous job handling.

### [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/)

`Free (registration), email` · beginner 4/5 · Sentinel satellite archive

Full free archive of Sentinel-1/2/3/5P plus Copernicus DEM and mirrored Landsat, served through OData, STAC, S3 and Sentinel Hub APIs. Free accounts get 12 TB of transfer per rolling 30 days, 50,000 catalogue requests per month and 10,000 Sentinel Hub processing units per month.

**Access.** Register, then use the Browser at browser.dataspace.copernicus.eu, the STAC catalogue at https://catalogue.dataspace.copernicus.eu/stac, or S3 with boto3 against the eodata endpoint; `pip install sentinelhub` or `pip install openeo` for the processing APIs.

**Caveats.** Quotas throttle rather than block: bandwidth drops to 1 MB/s and one concurrent connection once exceeded, and catalogue queries are limited to about 12 requests/minute. Server-side processing (Sentinel Hub processing units, openEO credits) is the scarce resource, not the downloads.

### [Copernicus Marine Service](https://marine.copernicus.eu/)

`Free (registration), email` · beginner 3/5 · ocean reanalysis, forecasts and in-situ

EU ocean data service providing satellite and in-situ observations, global and regional physical and biogeochemical reanalyses, and daily forecasts, in netCDF or Zarr. Data are free and open after registration.

**Access.** `pip install copernicusmarine`; `copernicusmarine login`, then `copernicusmarine subset --dataset-id <id> --variable thetao --minimum-longitude ... --start-datetime ...`, or `copernicusmarine.open_dataset()` in Python for lazy xarray access.

**Caveats.** Server-side subsetting is essential: whole products are terabytes. Dataset IDs carry version suffixes and older versions are retired after a notice period, so pin the exact ID in scripts and expect to update them.

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

### [NOAA Climate Data Online and GHCN-Daily](https://www.ncei.noaa.gov/cdo-web/)

`Free (registration), api-key` · beginner 4/5 · weather station records

Station climate records including GHCN-Daily: over 100,000 stations in 180 countries and territories with daily maximum and minimum temperature, precipitation, snowfall and snow depth, some series reaching back to the 18th century, updated daily.

**Access.** Request a free token by email, then `GET https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=...&startdate=...` with header `token: <key>`; or skip the API entirely and pull per-station .csv.gz from https://www.ncei.noaa.gov/pub/data/ghcn/daily/.

**Caveats.** The API allows 5 requests/second, 10,000 requests/day and at most 1,000 records per response, so anything bulk should use the flat files. Roughly half of GHCN-Daily stations report precipitation only, and station density is very uneven outside North America and Europe.

### [NOAA CoastWatch ERDDAP](https://coastwatch.pfeg.noaa.gov/erddap/)

`Free` · beginner 4/5 · ocean and atmosphere data server

ERDDAP server exposing 3,098 oceanographic and atmospheric datasets (satellite sea surface temperature, ocean colour, winds, buoys, model output) as subsettable griddap and tabledap endpoints returning netCDF, CSV, JSON, MATLAB or ready-made PNG maps from a single URL.

**Access.** Construct a URL such as .../erddap/griddap/<datasetID>.nc?sst[(2024-01-01)][(20):(40)][(-30):(-10)], or use `pip install erddapy`, or point `xarray.open_dataset()` straight at a griddap URL.

**Caveats.** Dataset IDs are server-specific and there are dozens of other ERDDAP installations (IOOS, IFREMER, EMODnet) with different holdings. Very large requests are throttled or time out; subset by time and bounding box in the URL rather than downloading whole datasets.

### [OpenStreetMap bulk extracts (Geofabrik) and Overpass API](https://download.geofabrik.de/)

`Free` · beginner 4/5 · open vector basemap and infrastructure data

Geofabrik publishes daily-updated OpenStreetMap extracts per continent and country as .osm.pbf (GeoPackage for some regions) under ODbL 1.0; for targeted questions the Overpass API returns features filtered by bounding box and tag with no download at all.

**Access.** Download e.g. https://download.geofabrik.de/africa/kenya-latest.osm.pbf and convert with osmium, ogr2ogr or `pip install pyrosm`; or POST Overpass QL to https://overpass-api.de/api/interpreter (`pip install overpy` or OSMPythonTools).

**Caveats.** ODbL requires attribution and share-alike on derived databases. Public Overpass instances ask users to stay under roughly 10,000 queries and 1 GB per day and are shared infrastructure; sustained or commercial use means self-hosting. OSM completeness varies enormously by region and theme.

### [OpenTopography](https://opentopography.org/)

`Free tier, api-key` · beginner 5/5 · digital elevation models and lidar

Portal and API for global DEMs (SRTM GL1/GL3, NASADEM, ALOS World 3D, Copernicus DEM GLO-30/GLO-90, GEDI L3), USGS 3DEP rasters at 1 m, 10 m and 30 m, and hosted lidar point clouds with on-the-fly derivative generation.

**Access.** Get a free API key from My Account, then `GET https://portal.opentopography.org/API/globaldem?demtype=COP30&south=..&north=..&west=..&east=..&outputFormat=GTiff&API_Key=..`; there is also a point-elevation API and a catalogue search API.

**Caveats.** Free keys are capped at roughly 200-250 calls per 24 hours for academic users and 50 for non-academic ones, and per-request area limits are tight for high-resolution data (about 250 km2 for 1 m 3DEP). Keys must not be shared or embedded in public applications.

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

### [WorldClim 2.1](https://www.worldclim.org/data/worldclim21.html)

`Free` · beginner 5/5 · gridded climate surfaces

Global interpolated climate surfaces at 30 arc-second to 10 arc-minute resolution: monthly minimum, mean and maximum temperature, precipitation, solar radiation, wind speed and vapour pressure averaged over 1970-2000, plus 19 bioclimatic variables, elevation, and downscaled CMIP6 future scenarios.

**Access.** Direct zip download per variable and resolution (12 monthly GeoTIFFs each); in R, `geodata::worldclim_global(var='bio', res=10, path='.')` fetches and caches the same files.

**Caveats.** Interpolated from station data, so it is least reliable where stations are sparse: high mountains, polar regions, and parts of Africa and Amazonia. The 30 arc-second global layers are multi-GB. Licence terms are not stated on the download page; cite Fick and Hijmans (2017) and check terms before commercial reuse.

## Software

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

### [ObsPy](https://docs.obspy.org/)

`Free` · beginner 3/5 · seismological data processing

Python framework for seismology (version 1.5.0, March 2026): readers for miniSEED, SAC, SEG-Y and StationXML, FDSN and SeedLink clients, instrument response removal, filtering, triggering, and event and station metadata handling.

**Access.** `conda install -c conda-forge obspy`; `st = obspy.read('trace.mseed'); st.remove_response(inventory=inv, output='VEL'); st.filter('bandpass', freqmin=0.05, freqmax=1.0)`; downloads via `obspy.clients.fdsn.Client`.

**Caveats.** LGPL. Response deconvolution and unit handling are the classic beginner trap: read the tutorial on `remove_response` before trusting amplitudes. Large waveform sets should be streamed to disk rather than held in memory.

### [pystac-client with odc-stac / stackstac](https://pystac-client.readthedocs.io/)

`Free` · beginner 3/5 · STAC search and lazy raster loading

Client for STAC APIs (Copernicus Data Space, Planetary Computer, Earth Search) that turns a space/time/collection query into an item collection; odc-stac or stackstac then load the matching Cloud-Optimized GeoTIFFs directly into an xarray cube without downloading whole scenes.

**Access.** `pip install pystac-client odc-stac`; `cat = Client.open('https://planetarycomputer.microsoft.com/api/stac/v1'); items = cat.search(collections=['sentinel-2-l2a'], bbox=bbox, datetime='2024-06/2024-09', query={'eo:cloud_cover':{'lt':20}}).item_collection(); ds = odc.stac.load(items, bands=['red','nir'], resolution=10, bbox=bbox)`.

**Caveats.** Lazy loading only helps if you constrain bbox, bands and resolution; requesting a full tile stack will still exhaust a laptop. Some catalogues need signed asset URLs (`planetary_computer.sign`) or a bearer token, and signatures expire during long jobs.

### [QGIS](https://qgis.org/)

`Free` · beginner 5/5 · desktop GIS

Full desktop GIS (4.2 is the current release line) for vector and raster editing, cartography, georeferencing, digitising and spatial analysis, with a large plugin ecosystem and an embedded Python console. GPLv2+ on Windows, macOS and Linux.

**Access.** Install from qgis.org or conda-forge; script with the built-in Python console and PyQGIS; the Processing toolbox exposes GDAL, GRASS and SAGA algorithms and can be run headlessly with `qgis_process`.

**Caveats.** For teaching and production use the long-term release branch rather than the newest feature release. Plugin quality varies and some depend on external binaries. Large rasters are slow unless you build overviews first.

### [xarray (with rioxarray and Dask)](https://docs.xarray.dev/)

`Free` · beginner 4/5 · labelled N-dimensional arrays

The standard Python library for labelled multidimensional data: netCDF, Zarr, GRIB and HDF climate and satellite arrays with named dimensions and coordinate-based selection, plus Dask-backed out-of-core computation that lets a laptop process datasets larger than its memory.

**Access.** `pip install 'xarray[complete]' rioxarray`; `ds = xr.open_dataset('era5.nc'); ds.t2m.sel(time='2024-07').mean('time').plot()`; `xr.open_mfdataset(files, chunks={'time': 24})` for multi-file archives; rioxarray adds CRS-aware clipping and reprojection.

**Caveats.** Chunk sizes matter more than machine size: badly chunked Dask graphs are the usual reason a laptop dies on ERA5. GRIB support needs cfgrib/eccodes, an extra install that is easiest through conda-forge.

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

### [Google Colab](https://colab.research.google.com/)

`Free tier, email` · beginner 5/5 · free hosted notebooks

Browser-based Jupyter notebooks with a preinstalled scientific Python stack and optional GPU, requiring no local installation. The default environment for most Earth Engine, geemap and xarray tutorials and the usual fallback where students have weak laptops.

**Access.** Open a notebook from GitHub, Drive or a URL; `!pip install` extra geospatial packages per session; mount Google Drive for persistence between sessions.

**Caveats.** Free sessions are pre-emptible and time-limited, GPU availability is not guaranteed, and anything not written to Drive or cloud storage disappears when the VM recycles. RAM and disk are modest: fine for tutorials and subsets, not for multi-hundred-GB archives.

### [Google Earth Engine](https://earthengine.google.com/)

`Free tier, application` · beginner 4/5 · hosted planetary-scale raster analysis

Server-side analysis over a hosted multi-petabyte catalogue (Landsat, Sentinel, MODIS, ERA5, Hansen forest change, SoilGrids and hundreds more). Noncommercial projects get 150 EECU-hours per month on the free Community Tier, or 1,000 EECU-hours per month on the Contributor Tier aimed at graduate students, researchers and nonprofits.

**Access.** Register a Cloud project for noncommercial use, then work in the Code Editor at code.earthengine.google.com (JavaScript) or `pip install earthengine-api` with `ee.Authenticate(); ee.Initialize(project='my-project')`; geemap and leafmap bridge it into notebooks.

**Caveats.** Commercial use requires a paid plan, and projects registered before 15 April 2025 had to verify noncommercial eligibility to keep access. Quotas reset monthly and exhausting them drops the project into restricted mode rather than cutting it off. The Contributor Tier requires a billing account to be attached even though Earth Engine itself is not charged. Exports go to Google Drive or Cloud Storage and count against those quotas.

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
