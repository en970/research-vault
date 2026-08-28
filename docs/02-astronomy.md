# Astronomy & space science

Part of [research-vault](../README.md). 66 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (32) · [Software](#software) (11) · [Literature](#literature) (2) · [Compute](#compute) (3) · [Publishing](#publishing) (5) · [Funding](#funding) (4) · [Learning](#learning) (6) · [Community](#community) (3)

## Data

### [AAVSO (American Association of Variable Star Observers)](https://www.aavso.org)

`Free` · beginner 4/5 · variable-star photometry + amateur-professional route

The AAVSO International Database holds over a century of variable-star photometry contributed by amateurs and professionals; the companion VSX index catalogues over 2 million known variable stars.

**Access.** Light Curve Generator and data download on aavso.org; VSX search at vsx.aavso.org (also mirrored in VizieR); submit your own observations via WebObs after obtaining a free observer code.

**Caveats.** Membership is paid but is NOT required to access data, submit observations, or propose new variables to VSX; free registration is required for submissions.

### [ALeRCE alert broker](https://alerce.science)

`Free` · beginner 4/5 · transient alert broker

Astronomical alert broker ingesting the ZTF stream and Rubin/LSST alerts (one of the official Rubin brokers), with machine-learning classifications, light curves and cross-matches for millions of transients and variables.

**Access.** Web explorer at alerce.online; Python client `pip install alerce` then `from alerce.core import Alerce`; public HTTP API.

**Caveats.** Alternatives with similar free access include Fink (fink-broker.org), Lasair and ANTARES; all serve the world-public Rubin alert stream, so no data rights are needed for alerts. This is the single most important free route into Rubin-era time-domain science for unaffiliated researchers.

### [ALMA Science Archive](https://almascience.org)

`Free` · beginner 2/5 · millimeter/submillimeter interferometry

All ALMA observations become public after a one-year proprietary period; the archive serves raw visibilities and, increasingly, imaged data products for thousands of projects.

**Access.** Query interface at almascience.org/aq (no login to search or download public data); `astroquery.alma` for scripted download.

**Caveats.** Reprocessing raw visibilities requires CASA (casadocs.readthedocs.io - free, developed by NRAO/ESO/NAOJ/JIV-ERIC, current release 6.7.6, installable as a pip wheel or as Linux/macOS tarballs) plus substantial disk and CPU. On a laptop, start from archival imaged products (continuum and line cubes) or the ARI-L and ALMINER value-added products.

### [ASAS-SN Sky Patrol](https://asas-sn.osu.edu)

`Free` · beginner 4/5 · all-sky photometry

All-Sky Automated Survey for Supernovae: 20 robotic telescopes at four sites (Hawaii, Chile, South Africa, Texas) image the entire visible sky every night to roughly 18th magnitude, and Sky Patrol returns V- and g-band light curves for any position with more than a decade of archival photometry.

**Access.** Web query at asas-sn.osu.edu for a handful of targets; Sky Patrol V2.0 at asas-sn.ifa.hawaii.edu/skypatrol/ with a Python client (pyasassn) for bulk work; separate variable-star, photometry and binary-star databases on the same site.

**Caveats.** Shallow by design (small telephoto lenses, ~18 mag) - ideal for bright variables, supernovae and long baselines rather than faint sources. The web form is meant for fewer than about 100 targets; use the Sky Patrol client for larger jobs.

### [Breakthrough Listen Open Data Archive](https://breakthroughinitiatives.org/opendatasearch)

`Free` · beginner 2/5 · radio SETI / technosignatures

Multi-petabyte public archive of radio (and some optical) SETI observations from the Green Bank Telescope, Parkes and the Automated Planet Finder, the largest open SETI dataset in existence.

**Access.** Search and direct download at breakthroughinitiatives.org/opendatasearch (also seti.berkeley.edu/opendata); read files with `pip install blimpy`; Doppler-drift searches with `turbo_seti`.

**Caveats.** Individual filterbank/HDF5 files are often several GB and formats require specialized tools; start with the tutorial datasets rather than raw voltages.

### [CHIME/FRB Catalogs](https://www.chime-frb.ca/catalog)

`Free` · beginner 3/5 · fast radio bursts

CHIME/FRB Catalog 2 contains 4,539 fast radio bursts from 3,641 unique sources detected between July 2018 and September 2023, an 8.5-fold increase over Catalog 1 (536 FRBs, 2021).

**Access.** Browse and download via the catalog site; machine-readable data and utilities via the open-data portal chime-frb-open-data.github.io and `pip install cfod`.

**Caveats.** Raw voltage and intensity data are not fully public; the catalogs contain burst properties and selected waterfall data.

### [DESI Data Archive](https://data.desi.lbl.gov)

`Free` · beginner 2/5 · spectroscopic survey

Public data from the Dark Energy Spectroscopic Instrument; DR1 (March 2025) contains spectra and redshifts for ~18.7 million galaxies, quasars and stars.

**Access.** Direct HTTPS download at data.desi.lbl.gov; individual spectra retrievable without bulk download via the SPARCL service (`pip install sparclclient`) at NOIRLab.

**Caveats.** Full-release files are very large; SPARCL or Astro Data Lab queries are the practical route on a laptop.

### [DESI Legacy Imaging Surveys](https://www.legacysurvey.org)

`Free` · beginner 5/5 · imaging survey + cutout service

Deep grz imaging and source catalogues from DECam, BASS and MzLS built for DESI targeting; the sky viewer serves image cutouts of any position on demand.

**Access.** Cutout API, e.g. https://www.legacysurvey.org/viewer/cutout.fits?ra=180.0&dec=30.0&layer=ls-dr10&pixscale=0.262 (also cutout.jpg); interactive viewer at legacysurvey.org/viewer; catalogues queryable via NOIRLab Astro Data Lab TAP.

**Caveats.** Cutout service is rate-limited for bulk use; for large jobs download bricks directly or query Data Lab.

### [e-CALLISTO](https://www.e-callisto.org)

`Free` · beginner 3/5 · solar radio spectrograms

Worldwide network of low-cost CALLISTO radio spectrometers monitoring solar radio bursts around the clock; daily FITS spectrograms from all stations are collected centrally and archived publicly.

**Access.** Browse and download gzipped FITS files at e-callisto.org/Data/data.html; daily quicklook plots and automatic burst lists on the same site.

**Caveats.** Data quality varies by station (radio-frequency interference). The network also welcomes new hosts - the spectrometer hardware is intentionally low-cost, making this one of the few practical routes for an individual or small institution to operate a real research instrument.

### [ESA Gaia Archive](https://gea.esac.esa.int/archive/)

`Free` · beginner 4/5 · astrometry catalogue

Gaia DR3 (June 2022) gives positions, parallaxes, proper motions and photometry for ~1.8 billion sources; DR4, based on 66 months of data, is scheduled for 2 December 2026, and DR5 is not expected before the end of 2030.

**Access.** ADQL queries in the web archive, or `pip install astroquery` then `from astroquery.gaia import Gaia; Gaia.launch_job('SELECT ...')`; bulk files via direct download. Subsets are also served by CDS, AIP and other partner data centres.

**Caveats.** Anonymous queries have row and job limits; a free account lifts them and keeps query history. The Focused Product Release (October 2023) sits between DR3 and DR4. Expect archive interface changes and much larger volumes at DR4.

### [ESO Science Archive](https://archive.eso.org)

`Free` · beginner 3/5 · ground-based observatory archive

Raw and pipeline-processed data from the VLT/VLTI, VISTA, VST, La Silla telescopes and APEX; observations become public after the proprietary period (typically one year), and processed science-ready collections are served alongside raw frames.

**Access.** Science portal at archive.eso.org/scienceportal; programmatic access via `astroquery.eso` and TAP; direct download of processed data products.

**Caveats.** Some services (large raw-data requests, calSelector) work best with a free ESO User Portal account. ESO observing-time proposals may be submitted by PIs of any nationality or affiliation, which makes archival plus proposal work a realistic pairing.

### [Euclid Q1 Data Release](https://www.cosmos.esa.int/web/euclid/q1-data)

`Free` · beginner 3/5 · cosmology survey imaging + spectroscopy

Euclid Quick Release 1 (19 March 2025): ~30 TB of VIS/NISP imaging, slitless spectra and catalogues over ~63 deg2 of the Euclid Deep Fields North, Fornax and South plus LDN1641.

**Access.** ESA Euclid Science Archive (linked from the Q1 data page); full mirror at IRSA with TAP/ADQL catalogue queries and AWS cloud copies; tutorial notebooks at caltech-ipac.github.io/irsa-tutorials.

**Caveats.** Q1 is single-visit depth over deep fields only; substantially larger cosmology-scale releases follow as the survey progresses.

### [Fermi Science Support Center](https://fermi.gsfc.nasa.gov/ssc/)

`Free` · beginner 2/5 · gamma-ray astronomy

All Fermi-LAT photon data have been public immediately since August 2009, with continuous all-sky coverage; GBM burst data and the 4FGL source catalogs are also served.

**Access.** LAT data server web query at fermi.gsfc.nasa.gov/ssc/; analysis with fermitools (conda install from the fermi channel) and `pip install fermipy`.

**Caveats.** No registration for data, but LAT likelihood analysis has a steep learning curve and needs several GB of spacecraft and diffuse-emission files.

### [GWOSC (Gravitational Wave Open Science Center)](https://gwosc.org)

`Free` · beginner 4/5 · gravitational-wave strain data

Public LIGO-Virgo-KAGRA strain data and event catalogues, all under CC BY 4.0; the cumulative GWTC event list stands at 391 events with the GWTC-5.0 release, and bulk strain data from the O4b segment of the fourth observing run are now public.

**Access.** Event portal and bulk downloads at gwosc.org; `pip install gwpy` then `TimeSeries.fetch_open_data('H1', t0, t1)`; the `gwosc` and `pycbc` packages for catalog queries and analysis.

**Caveats.** Strain data are released after a proprietary period, so the most recent observing-run segments lag public availability, and the catalogue is only updated periodically. The annual Open Data Workshop (April 2026 was the most recent) is a free crash course with recorded lectures and challenge problems.

### [HEASARC](https://heasarc.gsfc.nasa.gov)

`Free` · beginner 2/5 · high-energy astrophysics archive

NASA's archive for X-ray and gamma-ray astronomy: Chandra, XMM-Newton, Swift, NuSTAR, NICER, IXPE, Fermi and dozens of historical missions, plus the LAMBDA cosmic microwave background holdings.

**Access.** Xamin/Browse query tools at heasarc.gsfc.nasa.gov; `astroquery.heasarc`; analysis with the free HEASoft suite (XSPEC and friends); Chandra-specific tools via the CXC (cxc.cfa.harvard.edu, CIAO software).

**Caveats.** Data are free with no gates, but high-energy analysis (response files, effective areas) carries real overhead; Swift and NICER are the gentlest entry points. For CMB and cosmology, LAMBDA (lambda.gsfc.nasa.gov) serves WMAP, Planck, ACT DR6, SPT-3G and CLASS products with an online CAMB application and Python analysis examples.

### [Helioviewer](https://helioviewer.org)

`Free` · beginner 5/5 · solar imagery

Browse, animate and export solar imagery from SDO, SOHO, STEREO and other missions, spanning decades of observations, in a zoomable web interface backed by a public API.

**Access.** Web app at helioviewer.org; REST API at api.helioviewer.org; Python wrapper `pip install hvpy`.

**Caveats.** Serves browse-quality JPEG2000 images; for science-grade SDO FITS use the JSOC export system (jsoc.stanford.edu) or SunPy's Fido search, both free. For in-situ heliophysics and space-weather data (ACE, Wind, Parker Solar Probe, THEMIS, Cluster, MAVEN and dozens more) use NASA SPDF's CDAWeb (cdaweb.gsfc.nasa.gov), which offers web subsetting, direct file download and a REST API.

### [IceCube public data releases](https://icecube.wisc.edu/science/data-releases/)

`Free` · beginner 2/5 · neutrino astronomy

Public neutrino datasets including IceTracks-DR2 (21 May 2026): 14 years of track-like neutrino events from 2008 to 2022 with improved calibration and point-source analysis tools, extending the previous release by four years.

**Access.** Direct download from the data-releases page (files hosted on Harvard Dataverse); CSV/HDF5 formats readable with pandas, with documented instrument response functions.

**Caveats.** These are curated event lists and responses, not raw detector data; questions go to analysis@icecube.wisc.edu.

### [IRSA (NASA/IPAC Infrared Science Archive)](https://irsa.ipac.caltech.edu)

`Free` · beginner 4/5 · infrared and multi-mission archive

NASA's archive for infrared and submillimetre astronomy: WISE/NEOWISE, 2MASS, Spitzer, IRAS, AKARI, Herschel, Planck, COSMOS, DENIS and the public ZTF, PTF, SPHEREx and Euclid holdings, served as images, catalogues and spectra.

**Access.** Web tools (IRSAviewer, Finder Chart, catalogue search) at irsa.ipac.caltech.edu; VO services including a TAP endpoint at https://irsa.ipac.caltech.edu/TAP; `pip install astroquery` then `from astroquery.ipac.irsa import Irsa; Irsa.query_region(...)`; several collections are also mirrored on AWS S3 for in-cloud analysis.

**Caveats.** No login for public data. The biggest catalogues (AllWISE, ZTF light curves) should be queried through TAP with spatial or magnitude constraints rather than downloaded whole; IRSA is also the home of the SPHEREx and Euclid entries listed separately here.

### [JPL Solar System Dynamics (Horizons & SBDB)](https://ssd.jpl.nasa.gov)

`Free` · beginner 5/5 · ephemerides

Horizons computes high-precision ephemerides for essentially every known solar-system body plus spacecraft; the Small-Body Database serves orbital and physical parameters with close-approach data.

**Access.** Web app at ssd.jpl.nasa.gov/horizons/; REST APIs at ssd-api.jpl.nasa.gov (no key needed); scripted access via `astroquery.jplhorizons` and `astroquery.jplsbdb`.

### [MAST (Mikulski Archive for Space Telescopes)](https://archive.stsci.edu)

`Free` · beginner 4/5 · space-telescope archive

STScI archive holding JWST, HST, TESS, Kepler/K2, GALEX and Pan-STARRS data; all observations become public after any proprietary period (typically 12 months for JWST/HST GO programs) and public holdings are mirrored to AWS.

**Access.** Web portal at mast.stsci.edu, or `pip install astroquery` then `from astroquery.mast import Observations`; cloud reads via `Observations.enable_cloud_dataset()` against s3://stpubdata (anonymous, no AWS account needed).

**Caveats.** A free MyST account is only needed to download proprietary-period data you are authorized for; everything public is anonymous-access.

### [Minor Planet Center](https://www.minorplanetcenter.net)

`Free` · beginner 3/5 · asteroid and comet astrometry

The IAU's official clearinghouse for astrometric observations and orbits of over 1.4 million minor planets and comets; publishes orbit files (MPCORB), observation databases and the NEO Confirmation Page.

**Access.** Web services and database queries at minorplanetcenter.net; bulk MPCORB downloads; astrometry submissions accepted from anyone observing from a site with an MPC observatory code.

**Caveats.** Submitting observations requires an observatory code (free, but demonstrated astrometric accuracy is required) - a long-standing amateur-professional pathway, and now also the public route to Rubin solar-system discoveries.

### [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu)

`Free` · beginner 5/5 · exoplanet catalogue

Vetted database of confirmed exoplanets and their measured parameters with linked literature references; the front page listed 6,354 confirmed planets on 20 August 2026, alongside candidate tables, transit ephemerides and time-series products.

**Access.** Interactive tables in the browser; TAP/API queries at exoplanetarchive.ipac.caltech.edu/TAP; `pip install astroquery` then `from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive`.

**Caveats.** The companion ExoFOP service (exofop.ipac.caltech.edu) coordinates follow-up of TESS and K2 candidates; browsing is open and contributing observations needs only a free account - a genuine route for amateurs with modest telescopes.

### [NASA Planetary Data System (PDS)](https://pds.nasa.gov)

`Free` · beginner 3/5 · planetary mission archive

Permanent archive of data from NASA planetary missions (Mars orbiters and rovers, Cassini, New Horizons, Juno, OSIRIS-REx and more), organized in discipline nodes with peer-reviewed data standards.

**Access.** Search at pds.nasa.gov; direct HTTP download from discipline-node servers; image-focused browsing via the Cartography and Imaging Sciences node (PDS Imaging Atlas).

**Caveats.** Navigation across nodes takes practice; the SPICE toolkit (NAIF, naif.jpl.nasa.gov; Python wrapper `pip install spiceypy`) is the free standard for the geometry files that accompany most datasets.

### [NED (NASA/IPAC Extragalactic Database)](https://ned.ipac.caltech.edu)

`Free` · beginner 4/5 · extragalactic database

Cross-matched multiwavelength positions, redshifts, photometry, images and literature for hundreds of millions of extragalactic objects, fused from major sky surveys and journal tables.

**Access.** Web interface at ned.ipac.caltech.edu; `from astroquery.ipac.ned import Ned`; TAP and object-lookup APIs.

**Caveats.** Complements SIMBAD: NED is deeper for galaxies and redshift bookkeeping; SIMBAD is stronger for Galactic objects.

### [Rubin Observatory / LSST data](https://rubinobservatory.org/for-scientists/data-products/data-access)

`Free, application` · beginner 2/5 · optical survey + alert stream

Data Preview 1 (released 30 June 2025) covers seven ~1 deg2 fields observed with the LSST Commissioning Camera in late 2024, processed with Science Pipelines v29; in survey operations alerts are transmitted to brokers within 60 seconds of every image.

**Access.** Rubin Science Platform (data.lsst.cloud) notebooks, portal and TAP for data-rights holders - all US- and Chile-based scientists and students plus named international contributors; alerts are world-public through brokers (ALeRCE, Fink, Lasair, ANTARES and others) with no data rights needed; solar-system detections flow to the Minor Planet Center.

**Caveats.** Pixel and catalogue releases stay inside the data-rights community for a proprietary period before becoming world-public, so an unaffiliated researcher cannot get an RSP account today. Real time-domain science is still possible now through the public alert stream, broker portals and the MPC.

### [SDOML (SDO Machine Learning Dataset)](https://sdoml.github.io)

`Free` · beginner 2/5 · ML-ready solar dataset

Curated, calibration-corrected SDO dataset for machine learning: AIA images 2010-2020 in 10 wavebands at 512x512 and 6-minute cadence, HMI vector magnetograms at 12-minute cadence, and EVE irradiance 2010-2014, all in cloud-friendly Zarr format.

**Access.** Read directly from AWS S3 with zarr/fsspec (bucket listed at registry.opendata.aws/sdoml-fdl); loaders and examples at sdoml.github.io and github.com/SDOML.

**Caveats.** Downscaled from the full 4096x4096 resolution by design; for full-resolution science data go to JSOC instead.

### [SDSS SkyServer](https://skyserver.sdss.org)

`Free` · beginner 5/5 · optical survey database

SQL interface to all Sloan Digital Sky Survey releases; DR20 (announced 30 July 2026) is the third SDSS-V release and adds the first optical BOSS spectra taken from Las Campanas Observatory for the Milky Way Mapper and Black Hole Mapper programs, plus Local Volume Mapper tiles and value-added catalogues.

**Access.** Free-form SQL in the browser at skyserver.sdss.org; longer jobs via CasJobs (free account); `astroquery.sdss` for scripted access; flat files from data.sdss.org.

**Caveats.** CasJobs and SciServer compute require a free email registration; SkyServer quick queries have row and time limits.

### [SIMBAD](https://simbad.cds.unistra.fr)

`Free` · beginner 5/5 · object database

CDS reference database resolving names, cross-identifications, basic measurements and complete literature links for over 10 million astronomical objects outside the solar system.

**Access.** Web queries at simbad.cds.unistra.fr; `from astroquery.simbad import Simbad`; TAP service for bulk cross-identification.

**Caveats.** Part of the wider free CDS ecosystem: the Aladin interactive sky atlas (aladin.cds.unistra.fr, desktop and Lite web versions) and the CDS X-Match service for crossmatching billion-row catalogues. ESA's ESASky (sky.esa.int, with astroquery.esasky and the pyESASky Jupyter widget) plays the same role for space-mission footprints across Hubble, JWST, XMM-Newton, Herschel and planetary missions.

### [SPHEREx Archive at IRSA](https://irsa.ipac.caltech.edu/Missions/spherex.html)

`Free` · beginner 3/5 · infrared all-sky spectral survey

NASA's SPHEREx (launched March 2025) is performing the first all-sky 0.75-5 micron spectral survey in 102 bands; IRSA published the first quick-release products in July 2025 and the reprocessed Quick Release 2 in October 2025 (with an April 2026 header/PSF correction), plus specialised sets such as the SPLICES ice-source target list and comet 3I/ATLAS observations.

**Access.** IRSA search tools, TAP/ADQL queries and the SPHEREx Source Discovery and Mosaic tools; cloud access via the public AWS bucket (registry.opendata.aws/spherex-qr); documentation at caltech-ipac.github.io/spherex-archive-documentation.

**Caveats.** QR2 supersedes QR1; higher-level products (full-sky spectral maps, catalogues) roll out over the remaining mission.

### [Transient Name Server (TNS)](https://www.wis-tns.org)

`Free, email` · beginner 3/5 · transient discovery registry

The IAU's official registry for reporting and naming astronomical transients; essentially all supernova discoveries and classifications flow through it, and the database is searchable by anyone.

**Access.** Public web search without login; reporting discoveries or classifications requires a free registered account (individual or group); rate-limited REST API with an API key for bots.

**Caveats.** A working route for amateurs who discover transients: register, report with the required astrometry and photometry, and the object receives an official designation. For multimessenger and high-energy transients the equivalent rapid channel is NASA's General Coordinates Network (gcn.nasa.gov), where notices and circulars are free to receive with a self-service account.

### [VizieR](https://vizier.cds.unistra.fr)

`Free` · beginner 4/5 · catalogue library

CDS library of more than 20,000 published astronomical catalogues and tables, from small journal tables to full surveys, all queryable through uniform Virtual Observatory interfaces.

**Access.** Web queries at vizier.cds.unistra.fr; `pip install astroquery` then `from astroquery.vizier import Vizier`; TAP endpoint for ADQL at tapvizier.cds.unistra.fr.

**Caveats.** Default query row limits are low (50); set `Vizier.ROW_LIMIT = -1` in astroquery to retrieve full tables.

### [ZTF (Zwicky Transient Facility) public data](https://irsa.ipac.caltech.edu/Missions/ztf.html)

`Free` · beginner 3/5 · time-domain survey

Northern-sky time-domain survey; bimonthly public data releases of images and light curves are served at IRSA, and the real-time alert stream is redistributed publicly.

**Access.** IRSA web tools and light-curve API; `astroquery.ipac.irsa` for scripted queries; alerts via community brokers (ALeRCE, Fink, Lasair, ANTARES) or the bulk alert archive at ztf.uw.edu.

**Caveats.** Partnership-time data are proprietary; the public surveys are fully open. Light-curve queries scale poorly for millions of objects - use the bulk release files for statistics work.

## Software

### [Astrometry.net](https://astrometry.net)

`Free, email` · beginner 4/5 · astrometric plate solving

Blind astrometric calibration: hand it an image with no reliable pointing information and it returns a WCS solution plus a list of known objects in the field. This is the standard bridge from a small-telescope or amateur image to science-usable astrometry.

**Access.** Upload at the free web service nova.astrometry.net, or drive it through the documented REST API with a free API key; or install locally from source, apt, Homebrew or Docker and run `solve-field image.fits` after fetching index files matched to your field size.

**Caveats.** Web submissions are public by default and the service queues at busy times; a local install removes both the rate limit and the publicity, at the cost of downloading index files (hundreds of MB for wide fields, several GB for narrow ones). Images uploaded to the Flickr astrometry group are solved automatically.

### [Astropy](https://www.astropy.org)

`Free` · beginner 5/5 · core Python library

The core Python package for astronomy: coordinates, WCS, FITS and table I/O, units, time systems and cosmology; the foundation of essentially the whole Python astronomy ecosystem.

**Access.** `pip install astropy` (or conda); documentation at docs.astropy.org.

**Caveats.** BSD-licensed and community-developed. Affiliated and adjacent packages cover most tasks: photutils, specutils, regions and ccdproc for reduction and measurement; emcee (MIT-licensed affine-invariant MCMC, emcee.readthedocs.io) and dynesty for inference; yt (yt-project.org, BSD) for volumetric simulation analysis.

### [astroquery](https://astroquery.readthedocs.io)

`Free` · beginner 4/5 · archive query library

One Python package with uniform interfaces to dozens of archives and services - MAST, Gaia, SIMBAD, VizieR, IRSA, NED, ESO, ALMA, JPL Horizons, HEASARC and more - so a laptop can script against most of the world's astronomy data.

**Access.** `pip install astroquery`; e.g. `from astroquery.simbad import Simbad; Simbad.query_object('M31')`.

**Caveats.** Individual services keep their own rate limits and occasional required credentials; module namespaces changed in recent versions (e.g. `astroquery.ipac.ned`), so match examples to your installed version.

### [Lightkurve](https://docs.lightkurve.org)

`Free` · beginner 5/5 · time-series photometry

Python package for Kepler, K2 and TESS photometry: one-line search and download from MAST, detrending, periodograms and transit searches, with well-documented tutorials.

**Access.** `pip install lightkurve`; e.g. `import lightkurve as lk; lk.search_lightcurve('Pi Mensae', mission='TESS').download().plot()`.

**Caveats.** Runs comfortably on a laptop for single targets; for bulk work use the TIKE cloud platform, where the same data sit next to the compute.

### [MESA (Modules for Experiments in Stellar Astrophysics)](https://docs.mesastar.org)

`Free` · beginner 2/5 · stellar evolution code

Open-source 1D stellar structure and evolution code with peer-reviewed physics modules, covering a wide range of masses and evolutionary stages; output is bit-for-bit identical across supported compilers and operating systems.

**Access.** Download the release (about a 2 GB zip) plus the MESA SDK from docs.mesastar.org, set MESA_DIR/MESASDK_ROOT/OMP_NUM_THREADS and run `./install`; macOS or Linux, 64-bit CPU, 8 GB RAM and 20 GB free disk are the stated minimums.

**Caveats.** The strongest example in this catalogue of research that needs no institutional access at all - just a laptop. The cost is time: compilation is slow, and writing inlists for a new problem has a genuine learning curve. Windows requires WSL. Help comes from the mesa-users mailing list and the MESA GitHub.

### [REBOUND](https://rebound.readthedocs.io)

`Free` · beginner 4/5 · N-body dynamics

Open-source N-body integrator (IAS15, WHFast and other symplectic schemes) used across planetary dynamics and planetesimal studies; runs real research problems on a laptop.

**Access.** `pip install rebound`; add `reboundx` for extra forces (general relativity, radiation pressure, migration).

### [SAOImageDS9](https://sites.google.com/cfa.harvard.edu/saoimageds9)

`Free` · beginner 5/5 · FITS image viewer

The field's standard astronomical image viewer: FITS images, cubes and mosaics with WCS, scaling, colour maps, region files, catalogue overlays and frame blinking; current stable release 8.7, funded by the Chandra X-ray Center.

**Access.** Download the prebuilt binary for Linux, macOS or Windows from the DS9 site and run it - no build step; it exchanges images and tables with TOPCAT, Aladin and Python sessions over a SAMP hub.

**Caveats.** Licensed in part under GPL v3. It is the fastest way to check whether a FITS file you just downloaded actually contains what you think it does.

### [Skyfield](https://rhodesmill.org/skyfield/)

`Free` · beginner 5/5 · ephemeris computation

Pure-Python astronomy engine computing positions of planets, comets, asteroids and Earth satellites directly from JPL ephemerides and MPC/Celestrak data, with results consistent with JPL Horizons.

**Access.** `pip install skyfield`; e.g. `load('de421.bsp')` then observe planets from any topocentric location.

**Caveats.** Downloads ephemeris files on first use (tens of MB); ideal for observation planning, satellite passes and occultation work with no web-service dependency.

### [Stellarium](https://stellarium.org)

`Free` · beginner 5/5 · planetarium software

Open-source desktop planetarium rendering a realistic sky with large star catalogues, telescope control and observation planning; also available as Stellarium Web in the browser.

**Access.** Direct download (Windows/macOS/Linux, GPL) from stellarium.org; browser version at stellarium-web.org.

**Caveats.** The mobile apps are paid; the desktop and web versions are fully free.

### [SunPy](https://sunpy.org)

`Free` · beginner 4/5 · solar physics library

Core Python library for solar data analysis: the Fido interface searches and downloads from VSO, JSOC and other archives, with Map and TimeSeries classes for images and light curves.

**Access.** `pip install sunpy`; e.g. `from sunpy.net import Fido, attrs as a; Fido.search(a.Time(...), a.Instrument.aia)`.

**Caveats.** JSOC bulk exports ask for a (free) registered email address.

### [TOPCAT](https://www.star.bristol.ac.uk/mbt/topcat/)

`Free` · beginner 4/5 · table/catalogue tool

Desktop Java tool for interactive work on large tables: million-row crossmatching, sky and 3D plotting, algebraic column definitions and built-in Virtual Observatory access (TAP, cone search) to services like VizieR and Gaia; actively maintained (v4.10-8, 21 August 2026).

**Access.** Download topcat-full.jar and run `java -jar topcat-full.jar` (Java 8 or later); `brew install --cask topcat` on macOS; reads FITS, VOTable, CSV, Parquet and more; the command-line sibling STILTS scripts the same operations.

**Caveats.** Handles tables of millions of rows on modest hardware and works offline; the standard answer to 'how do I crossmatch two catalogues without writing code'.

## Literature

### [arXiv astro-ph](https://arxiv.org/archive/astro-ph)

`Free` · beginner 5/5 · preprint server

The astrophysics preprint server, running since 1992 across six astro-ph subcategories; near-universal practice in the field means a freely readable preprint exists for the large majority of current astronomy papers.

**Access.** Read free at arxiv.org; daily listings, RSS and full-text search; submission is free with an arXiv account.

**Caveats.** First-time submitters without an institutional email may need an endorsement from an established arXiv author - a real but usually surmountable hurdle for independent researchers.

### [SciX / NASA ADS](https://scixplorer.org)

`Free` · beginner 5/5 · bibliographic database

The field's free bibliographic database: the complete refereed astrophysics literature plus preprints, conference material and links to data and software, with full citation and reference graphs. SciX is the NASA-run successor interface extending the same corpus to heliophysics, planetary and Earth science; the classic ADS interface at ui.adsabs.harvard.edu continues to run.

**Access.** Search free at scixplorer.org or ui.adsabs.harvard.edu with no account; a free account adds private libraries, saved searches and alerts; a free API token enables scripted queries (`pip install ads`, or `astroquery.nasa_ads`).

**Caveats.** Indexes and links full text but does not itself unlock paywalled journal PDFs - in astronomy the arXiv link usually does. Interface details are in flux while the SciX transition proceeds, so check which UI and API endpoint your token targets.

## Compute

### [NOIRLab Astro Data Lab](https://datalab.noirlab.edu)

`Free` · beginner 4/5 · cloud science platform

NSF NOIRLab's open science platform: tens of terabytes of survey catalogues (DESI Legacy Surveys, NOIRLab Source Catalog, unWISE, Gaia and more) plus petabytes of images and spectra, with co-located Jupyter notebooks and TAP query services.

**Access.** Anonymous TAP/ADQL queries at datalab.noirlab.edu/tap (usable from TOPCAT or `pip install astro-datalab`); a free account unlocks the notebook server, a personal database (MyDB) and virtual storage; example notebooks at github.com/astro-datalab/notebooks-latest.

**Caveats.** Also hosts the SPARCL spectra service used for DESI and SDSS spectra. Anonymous queries have shorter time limits than authenticated ones.

### [SciServer](https://www.sciserver.org)

`Free (registration), email` · beginner 4/5 · cloud science platform

Johns Hopkins platform offering free Jupyter notebooks and persistent storage co-located with multi-terabyte datasets including the full SDSS catalogue databases (CasJobs), so survey-scale SQL plus Python analysis needs no local hardware.

**Access.** Free account at sciserver.org, then Compute (notebooks) and CasJobs (SQL with a personal MyDB database).

**Caveats.** Shared free resources with quotas; long-running jobs are queued. The standard companion to SDSS SkyServer for anything bigger than a browser query.

### [TIKE (Timeseries Integrated Knowledge Engine)](https://timeseries.science.stsci.edu)

`Free (registration), email` · beginner 4/5 · cloud science platform

STScI's free JupyterHub running in the same AWS region as the MAST cloud archive, so TESS, Kepler/K2, JWST, Hubble, GALEX and Pan-STARRS data can be analysed with no downloads; preloaded with lightkurve, astroquery and a full astronomy stack.

**Access.** Log in at timeseries.science.stsci.edu with a free MyST account; no AWS account or payment details needed; tutorials in the TIKEBook (spacetelescope/project-tikebook on GitHub).

**Caveats.** Compute is roughly equivalent to a modern laptop with four CPU cores, so it is for interactive analysis rather than large batch production. User storage is backed up by STScI about every two weeks, but keep your own copies of anything important.

## Publishing

### [Astronomy & Astrophysics (A&A)](https://www.aanda.org)

`Free, email` · beginner 2/5 · open-access journal (Subscribe-to-Open)

Major astronomy journal, fully open access since 2022 under the Subscribe-to-Open model; EDP Sciences has confirmed A&A remains open access in 2026 with no article processing charges, articles published CC BY 4.0.

**Access.** Standard manuscript submission at aanda.org; no APC invoice under S2O.

**Caveats.** S2O is renewed annually and depends on library subscriptions, so the no-APC status should be re-checked for each volume year. Page limits and language-editing policies apply.

### [JOSS (Journal of Open Source Software)](https://joss.theoj.org)

`Free, email` · beginner 3/5 · software papers

Free, developer-friendly peer-reviewed journal for research software; astronomy packages routinely publish here to make their code citable, with the review conducted openly on GitHub.

**Access.** Submit a repository plus a short paper.md via joss.theoj.org; review happens in a public GitHub issue; no charges at any stage.

**Caveats.** The software must be open source and represent substantial scholarly effort; small scripts are rejected as out of scope. Two neighbouring routes: the Astrophysics Source Code Library (ascl.net) registers astronomy codes so they are citable and indexed in ADS without writing a paper, and Zenodo (zenodo.org, run by CERN with OpenAIRE) mints a DOI for any code release or dataset and hooks directly into GitHub.

### [Research Notes of the AAS (RNAAS)](https://journals.aas.org/research-notes/)

`Free, email` · beginner 4/5 · brief-report venue

Venue for brief communications of at most 1,500 words with a single figure or table: fully open access with no article publication charge (confirmed on the AAS 2026 charges page), each note gets a DOI and ADS indexing, and notes appear within days of acceptance.

**Access.** Submit via the AAS journals submission system (AAS membership not required); LaTeX and Word templates provided.

**Caveats.** Moderated but not peer reviewed and not copy-edited - suitable for negative results, follow-up observations, and code or data announcements. In practice one of the most accessible first publication routes for individuals and advanced amateurs. The full AAS journals (ApJ, AJ, ApJL) charge four-figure fees per paper.

### [The Astronomer's Telegram](https://astronomerstelegram.org)

`Free, credentialing` · beginner 3/5 · rapid-communication venue

Short, citable, ADS-indexed reports of time-critical astronomical observations, in continuous use for decades with over 18,000 telegrams posted and a circulation list of roughly 8,500 subscribers.

**Access.** Read and search everything free with no account; posting requires credentialing as an author through the site's Credential page, after which telegrams are published immediately.

**Caveats.** Credentialing is a light editorial check rather than peer review, but it is a barrier for a complete newcomer; a first telegram usually comes through a collaborator. Telegrams are citable but carry far less weight than a refereed paper.

### [The Open Journal of Astrophysics](https://astro.theoj.org)

`Free, email` · beginner 3/5 · diamond OA journal

Peer-reviewed arXiv-overlay journal covering astrophysics and cosmology: submission, refereeing and publication are all free of charge, with the accepted version staying on arXiv and the journal supplying peer review, a DOI and indexing.

**Access.** Post your paper to arXiv, then submit the arXiv identifier through astro.theoj.org for peer review.

**Caveats.** No APC and no reader paywall, so it is one of the few realistic venues for a researcher with no publication budget. It is younger and smaller than ApJ/MNRAS/A&A, which matters if you are judged on venue prestige.

## Funding

### [AAS Chretien International Research Grants](https://aas.org/grants-and-prizes/chretien-international-research-grants)

`Free, application` · beginner 2/5 · international collaboration grants

Up to $20,000 available each year from the American Astronomical Society to support international collaborative projects in observational astronomy, emphasising long-term visits between countries.

**Access.** Application through the AAS grants page during the annual cycle.

**Caveats.** Open to astronomers worldwide but requires a PhD or equivalent; graduate students are not eligible.

### [IAU Office of Astronomy for Development grants](https://astro4dev.org/cfp/)

`Free, application` · beginner 3/5 · project grants

Annual open call funding astronomy-for-development projects worldwide; the 2026 call has EUR 60,000 available, typically spread across 10-15 projects with individual grants of EUR 1,000-15,000 (average around EUR 5,000).

**Access.** Two-stage online application (short concept, then full proposal) via astro4dev.org/cfp, open to applicants anywhere in the world; proposal-writing and translation help is offered on request.

**Caveats.** Funds development, education and community-impact projects that use astronomy, not pure research programmes. In the 2026 round Stage 1 closed on 31 May 2026, Stage 2 proposals are due 15 September 2026 and results come in mid-November, with funded projects running from early 2027; watch for the next annual call.

### [Las Cumbres Observatory Global Sky Partners](https://lco.global/education/partners/)

`Free, application` · beginner 2/5 · free telescope time

LCO allocates over 1,000 hours per year on its global robotic telescope network to organisations running their own education and public-engagement astronomy projects; around 30 partners are currently active across Europe, Asia, Africa, the Americas and Oceania.

**Access.** Apply to become a partner via lco.global/education/partners/becoming-global-sky-partner/; approved partners receive an observing allocation on the LCO network and run their own project and participants.

**Caveats.** This funds telescope access, not money, and is aimed at projects with participants rather than solo PI research; LCO's science time is allocated separately through competitive time-allocation committees. For instant, no-application access to a real robotic telescope, MicroObservatory / Observing With NASA (mo-www.cfa.harvard.edu/OWN/) lets anyone queue images free, though at education-grade depth.

### [Planetary Society Shoemaker NEO Grants](https://www.planetary.org/sci-tech/neo-grants)

`Free, application` · beginner 3/5 · observer grants

Grants for advanced amateur and under-funded professional astronomers anywhere in the world to find, track and characterise near-Earth objects; the programme has awarded $585,000 to 52 astronomers in 23 countries on six continents since 1997.

**Access.** Apply during announced rounds via the programme page, with a proposal describing your observing programme and the equipment upgrade you need; the current Request for Proposals is downloadable there.

**Caveats.** One of very few funding lines explicitly open to unaffiliated observers, but it funds equipment for NEO astrometry submitted to the Minor Planet Center, not salary or general research. The Planetary Society's separate STEP Grants fund larger open-call projects in planetary exploration, planetary defence and the search for life.

## Learning

### [Astrobites](https://astrobites.org)

`Free` · beginner 5/5 · paper summaries

Daily plain-language summaries of new astro-ph papers written by graduate students since 2010, plus guides on applying to graduate school, statistics, careers and observing; widely used to keep up with the literature.

**Access.** Web and RSS with no account; searchable archive by topic.

### [Data Carpentry: Foundations of Astronomical Data Science](https://datacarpentry.github.io/astronomy-python/)

`Free` · beginner 4/5 · data-science curriculum

Official Carpentries curriculum teaching ADQL/SQL database queries, Astropy and astroquery workflows and large-catalogue practices through a real science case: recovering the GD-1 stellar stream from Gaia and Pan-STARRS data.

**Access.** Self-paced lesson free on the web; all data and notebooks downloadable; also taught at free community workshops.

**Caveats.** Assumes basic Python and shell skills at Software Carpentry level.

### [Dynamics and Astrophysics of Galaxies (galaxiesbook.org)](https://galaxiesbook.org)

`Free` · beginner 2/5 · graduate textbook (galaxies)

Jo Bovy's graduate textbook on galactic dynamics and astrophysics, published in print by Princeton with the complete interactive web version free, including runnable in-browser Python examples and animations.

**Access.** Read free at galaxiesbook.org; code examples execute in the browser.

**Caveats.** Exercises and the index are reserved for the paid print/ebook edition; the full instructional text is free.

### [Essential Radio Astronomy](https://science.nrao.edu/opportunities/courses/era)

`Free` · beginner 3/5 · graduate textbook (radio)

Condon & Ransom's graduate radio astronomy textbook (Princeton, 2016), whose full course version is freely readable online by agreement with the publisher; the canonical text NRAO itself teaches from.

**Access.** Read free at the NRAO course site (science.nrao.edu/opportunities/courses/era); the print edition is sold by Princeton University Press.

### [Learn Astropy](https://learn.astropy.org)

`Free` · beginner 5/5 · tutorials

The Astropy Project's curated tutorials and guides - executable Jupyter notebooks covering FITS handling, coordinates, photometry, spectroscopy and archive queries - maintained by the package developers themselves.

**Access.** Browse and download notebooks at learn.astropy.org; run them locally or on any free notebook service.

### [OpenStax Astronomy 2e](https://openstax.org/details/books/astronomy-2e)

`Free` · beginner 5/5 · introductory textbook

Full peer-reviewed introductory astronomy textbook (Fraknoi, Morrison & Wolff), free to read online or download as PDF under a CC BY licence; the standard free text for a first course.

**Access.** Read in the browser or download the PDF at openstax.org; no account needed.

**Caveats.** Introductory level - a bridge into the field, not a graduate reference.

## Community

### [Astronomy Stack Exchange](https://astronomy.stackexchange.com)

`Free` · beginner 5/5 · Q&A forum

Question-and-answer site for astronomy with a substantial archive of answered questions, from observational practice to astrophysics calculations, answered by a mix of professionals and knowledgeable amateurs.

**Access.** Read without an account; free registration to ask or answer.

**Caveats.** Skews towards introductory and amateur questions; research-level physics sometimes fares better on Physics Stack Exchange, and software questions on the OpenAstronomy forum.

### [OpenAstronomy Community Forum](https://community.openastronomy.org)

`Free` · beginner 4/5 · software help forum

Discourse forum where developers and users of Astropy, SunPy, lightkurve and related open-source astronomy packages answer usage and development questions; maintainers reply directly.

**Access.** Read without an account; free registration to post.

### [Zooniverse](https://www.zooniverse.org)

`Free` · beginner 5/5 · citizen-science platform

The largest citizen-science platform, born from Galaxy Zoo; hosts active astronomy projects (galaxy morphology, planet hunting, variable-star vetting) whose classifications feed published research, with talk boards connecting volunteers and science teams.

**Access.** Classify in the browser at zooniverse.org; the free Project Builder lets researchers launch their own crowdsourcing project.

**Caveats.** A free account is needed to save contribution history and to build projects; several projects list volunteer contributors on the resulting papers, which is a real route to co-authorship without an affiliation.
