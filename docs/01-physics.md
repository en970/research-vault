# Physics

Part of [research-vault](../README.md). 87 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (20) · [Software](#software) (28) · [Literature](#literature) (6) · [Compute](#compute) (7) · [Publishing](#publishing) (5) · [Funding](#funding) (6) · [Learning](#learning) (11) · [Community](#community) (4)

## Data

### [ATLAS Open Data](https://opendata.atlas.cern)

`Free` · beginner 5/5 · particle-physics data (education and research)

ATLAS's dedicated open-data site with two tracks: laptop-sized education datasets with Jupyter tutorials, and the 2024 research release of ~65 TB of 13 TeV proton-proton collision data from 2015-2016 (over 7 billion events, plus ~2 billion simulated events) under CC0.

**Access.** Web interface at opendata.atlas.cern; education notebooks run in the browser; research-grade PHYSLITE files are served through the CERN Open Data Portal and readable with `pip install uproot`. The collaboration's own `pip install atlasopenmagic` package resolves dataset names to streaming URLs and bundles cross-section metadata, which is the least painful way to start.

**Caveats.** The education datasets are simplified and not suitable for publishable measurements; the 2024 research release is, and has documentation aimed at people outside the collaboration.

### [BIPM Key Comparison Database (KCDB)](https://www.bipm.org/kcdb/)

`Free` · beginner 2/5 · metrology comparison data

The official record of world metrology under the CIPM Mutual Recognition Arrangement: 26,000+ calibration and measurement capabilities, ~1,278 key comparisons and ~777 supplementary comparisons from 260 participating institutes across nine measurement areas.

**Access.** Free web search (quick and advanced) over CMCs and comparison reports; comparison final reports downloadable as PDF.

**Caveats.** Reference material for anyone doing precision measurement — tells you the state of the art and its uncertainty for a given quantity — but it is a registry, not a bulk dataset.

### [CERN Open Data Portal](https://opendata.cern.ch)

`Free` · beginner 3/5 · particle-physics data

Public archive of collision data, simulations, software environments and documentation from CERN experiments — the portal's own front page lists ALICE, ATLAS, CMS, DELPHI, JADE, LHCb, OPERA, PHENIX and TOTEM, and advertises more than five petabytes of open particle-physics data. 82,385 records as of 28 August 2026. Every dataset gets a DOI and an open licence (mostly CC0).

**Access.** Web interface with direct downloads; bulk retrieval via `pip install cernopendata-client`; analysis environments ship as Docker images and CVMFS repositories so old software still runs.

**Caveats.** Research-grade datasets run to hundreds of GB or TB. On a laptop, work with derived formats (CMS NanoAOD, ATLAS PHYSLITE) and stream files with uproot/XRootD rather than downloading everything.

### [CODATA Fundamental Physical Constants (NIST)](https://physics.nist.gov/cuu/Constants/)

`Free` · beginner 5/5 · fundamental constants

The internationally recommended values of the fundamental physical constants with uncertainties and correlations. The CODATA 2022 adjustment is the current set as of 2026.

**Access.** Searchable web interface and downloadable ASCII table; also available programmatically as `scipy.constants` in the SciPy library.

**Caveats.** A new CODATA adjustment lands every four years — check which set your software version ships before high-precision work.

### [Crystallography Open Database (COD)](https://www.crystallography.net/cod/)

`Free` · beginner 4/5 · experimental crystal structures

Open-access collection of experimentally determined crystal structures of organic, inorganic, metal-organic compounds and minerals (biopolymers excluded): 534,681 entries as of 25 August 2026, all dedicated to the public domain under CC0.

**Access.** Web search, including structure-formula drawing, at crystallography.net/cod; the whole database downloads as CIF files over rsync/HTTP from the mirrors listed in the COD wiki; also exposed through OPTIMADE and readable directly by pymatgen or ASE.

**Caveats.** The free counterpart to the subscription ICSD and CSD. Curation is community-driven, so duplicates and low-quality refinements exist — check the source publication before using a structure as a DFT starting point. An account is only needed to deposit.

### [FAIR-MAST](https://mastapp.site)

`Free` · beginner 2/5 · fusion / tokamak experimental data

UKAEA's open archive of diagnostic data from the MAST spherical tokamak (campaigns M05-M09), served as cloud-optimised Zarr and Parquet from a public S3 store with a REST/GraphQL metadata API — one of the very few openly available real tokamak diagnostic datasets, widely used for fusion ML work.

**Access.** REST and GraphQL API at mastapp.site; bulk data from the public S3 endpoint (s3.echo.stfc.ac.uk); code and docs at github.com/ukaea/fair-mast.

**Caveats.** Raw diagnostic signals with minimal hand-holding; expect to invest time understanding tokamak diagnostics. Related releases appear on the UKAEA Open Data portal (opendata.ukaea.uk).

### [Gravitational Wave Open Science Center (GWOSC)](https://gwosc.org)

`Free` · beginner 4/5 · gravitational-wave strain data

LIGO/Virgo/KAGRA's public archive of calibrated detector strain data and event catalogues: full releases for observing runs O1, O2, O3a, O3b, O4a (24 May 2023 - 16 Jan 2024) and O4b (10 Apr 2024 - 28 Jan 2025) at 4 kHz and 16 kHz sampling, plus the cumulative Gravitational-Wave Transient Catalog listing 391 events across GWTC-1 through GWTC-5.0 (checked 28 August 2026). All data released under CC BY 4.0.

**Access.** Web interface and event portal at gwosc.org; `pip install gwosc` for the query client and `pip install gwpy` to read strain (`TimeSeries.fetch_open_data('H1', t0, t1)`); bulk transfers via the OSDF, which GWOSC names as the preferred route for large downloads.

**Caveats.** Short segments around individual events are laptop-sized; a whole observing run is hundreds of TB. Detection and parameter estimation (PyCBC, Bilby) are compute-hungry. The IGWN conda distribution is the least painful way to install the whole stack. Auxiliary/trend channels are released only for O3a and O3b.

*Also listed under: astronomy.*

### [HEPData](https://www.hepdata.net)

`Free` · beginner 4/5 · published particle-physics results

Repository of the numerical data behind published particle-physics results — cross-section tables, exclusion limits, correlation matrices — built on the Durham database accumulated over four decades and actively fed by ATLAS, CMS, LHCb and others. Hosted on CERN infrastructure, run from Durham/IPPP.

**Access.** Web interface; every table downloads as CSV, YAML, JSON, or ROOT; records are query-able via a REST/JSON API; submissions are prepared with `pip install hepdata-lib`.

**Caveats.** Coverage depends on collaborations depositing their tables; recent LHC results are well covered, older or smaller experiments patchier.

### [HITRAN](https://hitran.org)

`Free (registration), email` · beginner 3/5 · molecular spectroscopic line lists

The standard database of molecular spectroscopic parameters — line positions, intensities, pressure-broadening and temperature-dependence coefficients, absorption cross sections — used for radiative transfer and absorption modelling in atmospheric physics, astrophysics and laser spectroscopy. The HITRAN2024 edition was released in January 2026; the site reports 43,000+ registered users and 600+ GB of downloads per month.

**Access.** Free account required, then build and download line lists through the web interface, or use the Python API HAPI (`pip install hitran-api`), which fetches data over the web service and computes absorption coefficients, cross sections and transmittance locally.

**Caveats.** Registration is free but mandatory even for downloads. Cite the HITRAN2024 paper and record which edition you used — line parameters change between editions and shift computed spectra. Hot-environment line lists live in the separate HITEMP database, and the licence discourages redistribution, so link rather than mirror.

### [IAEA Nuclear Data Services](https://nds.iaea.org)

`Free` · beginner 4/5 · nuclear reaction and structure data

International clearing-house for nuclear data: the EXFOR experimental reaction database (over 21,000 experiments, over 11 million data points), mirrors of major evaluated libraries, and the LiveChart of Nuclides for browsing ENSDF structure and decay data graphically.

**Access.** Web interfaces; EXFOR web retrieval with plotting; LiveChart at nds.iaea.org/relnsd/vcharthtml/VChartHTML.html; most datasets downloadable in standard formats.

**Caveats.** Interfaces are dated but functional; the same EXFOR content is also mirrored by NNDC and the OECD NEA.

### [LXCat](https://www.lxcat.net)

`Free` · beginner 3/5 · plasma cross-section data

Community platform of contributed databases of electron- and ion-scattering cross sections and measured swarm/transport parameters for low-temperature plasma modelling, with an online Boltzmann-equation solver for computing electron energy distributions and rate coefficients.

**Access.** Web interface: browse, plot, and download cross-section sets as plain text; no account needed to download.

**Caveats.** Each contributed database has its own citation requirement — cite the specific database, not just LXCat. Contributor accounts are only needed to upload data.

### [Materials Project](https://materialsproject.org)

`Free, api-key` · beginner 3/5 · computed materials properties

DOE-funded database of DFT-computed structures, band structures, elastic, dielectric and thermodynamic properties covering over 150,000 inorganic compounds plus ~170,000 molecules; roughly 600,000 registered users as of 2025.

**Access.** Web app after free registration; API key from your dashboard, then `pip install mp-api` and use MPRester; bulk data also on public AWS S3 buckets with no account.

**Caveats.** All data is computed (GGA/GGA+U and r2SCAN DFT), not experimental — band gaps in particular carry systematic errors. Registration is free but required for the web app and API.

### [National Nuclear Data Center (NNDC)](https://www.nndc.bnl.gov)

`Free` · beginner 4/5 · nuclear structure and reaction data

Brookhaven's nuclear data hub: ENSDF evaluated nuclear structure and decay data, the ENDF/B-VIII.1 evaluated reaction library (released 2024), the NuDat 3 interactive chart of nuclides, XUNDL, and the NSR bibliography.

**Access.** Web interfaces (NuDat 3 for browsing, ENDF retrieval forms); ENDF/B-VIII.1 available as direct download in ENDF-6 and GNDS formats.

**Caveats.** Processed application libraries (ACE files for MCNP etc.) are distributed separately via LANL/RSICC channels, some of which require registration.

### [NIST Atomic Spectra Database](https://www.nist.gov/pml/atomic-spectra-database)

`Free` · beginner 4/5 · atomic spectroscopy reference data

Critically evaluated wavelengths, energy levels, transition probabilities and ionization energies for atoms and atomic ions — the standard reference for spectral-line identification in physics, plasma diagnostics and astrophysics.

**Access.** Web query forms at physics.nist.gov/asd with tab-delimited/CSV output for batch use.

**Caveats.** Cite the database version and retrieval date; there is no official bulk download of the entire database.

### [NIST Physical Reference Data](https://www.nist.gov/pml/productsservices/physical-reference-data)

`Free` · beginner 4/5 · radiation interaction and atomic reference data

NIST's hub of free reference databases used daily by experimentalists: XCOM photon cross sections and X-ray mass attenuation coefficients, ESTAR/ASTAR/PSTAR stopping-power and range tables for electrons, protons and alpha particles, X-ray and gamma-ray interaction data, molecular spectroscopy, isotopic compositions and atomic weights.

**Access.** Free web query forms per database under physics.nist.gov (e.g. physics.nist.gov/xcom, physics.nist.gov/Star); results come back as HTML/ASCII tables you can paste into analysis code.

**Caveats.** Web forms only — no bulk API or single download for the whole collection, so scripted use means scraping or caching your own tables. Record the database version and retrieval date when citing.

### [NOMAD](https://nomad-lab.eu)

`Free, email` · beginner 3/5 · computational materials data repository

FAIR repository for materials-science calculations run by the FAIRmat consortium: 19,425,275 uploaded entries covering 4,346,100 materials and 129.3 TB of files as of 28 August 2026, normalised into a common schema across DFT and other codes (VASP, Quantum ESPRESSO, FHI-aims, exciting and dozens more) and published under CC-BY-4.0.

**Access.** Web search and browser-hosted notebooks at nomad-lab.eu; REST API under `https://nomad-lab.eu/prod/v1/api/v1/entries/query`; `pip install nomad-lab` for the Python client and parsers; upload your own raw calculation outputs after free registration.

**Caveats.** Published data is searchable and downloadable without an account; uploading and private staging need one. Unlike Materials Project there is no single uniform workflow — entries are contributed raw outputs with varying functionals, cutoffs and convergence, so inspect the input files before trusting a number. An OASIS version can be self-hosted by a group.

*Also listed under: chemistry.*

### [OQMD — Open Quantum Materials Database](https://oqmd.org)

`Free` · beginner 3/5 · computed materials properties

Northwestern University database of DFT-calculated thermodynamic and structural properties containing about 1.4 million entries (1,407,395 as of August 2026), released under CC-BY 4.0.

**Access.** Web search at oqmd.org; RESTful and OPTIMADE APIs; full database downloadable as a MySQL dump; `qmpy` Python package for local queries.

**Caveats.** Like all high-throughput DFT sets, formation energies are reliable for ranking but individual values need convergence checks before publication-grade claims.

### [Particle Data Group (PDG)](https://pdg.lbl.gov)

`Free` · beginner 5/5 · evaluated particle properties

The Review of Particle Physics: evaluated masses, widths, branching ratios and limits for all known particles, plus ~100 review articles on topics from the Standard Model to statistics. The current edition is RPP 2026 (Takahashi et al., Int. J. Mod. Phys. A 41, 2630011 (2026)), free online; pdgLive gives interactive access to every measurement with references.

**Access.** pdgLive web interface at pdg.lbl.gov; machine-readable access via `pip install pdg` (docs at pdgapi.lbl.gov); summary tables and data files as direct downloads.

**Caveats.** The Python API is labelled beta by PDG — cross-check values against pdgLive before using them in a publication. The printed book/booklet costs money; all content is free online.

### [RefractiveIndex.INFO](https://refractiveindex.info)

`Free` · beginner 5/5 · optical constants

Refractive index and extinction coefficient data for optical materials — glasses, metals, semiconductors, crystals, organics — compiled from the published measurement literature since 2008. The database repository held 4,180 YAML datasets when checked on 31 August 2026.

**Access.** Web interface with plots, Sellmeier/tabulated data and basic calculations; the whole database downloads as a dated ZIP (rii-database-2026-05-24.zip) or from the refractiveindex.info-database repo on GitHub, and the About page links Python and Julia readers for the YAML files.

**Caveats.** Released under CC0, so reuse including commercial reuse is unrestricted. It is essentially a one-maintainer compilation (Mikhail Polyanskiy): every dataset cites its original paper, and you should check that reference and the stated wavelength range before trusting a curve — extrapolation outside the measured range is on you.

### [VAMDC Portal](https://portal.vamdc.eu)

`Free` · beginner 3/5 · atomic and molecular data federation

One query interface across the Virtual Atomic and Molecular Data Centre's federated nodes — energy levels, transition wavelengths and probabilities, cross sections, collisional and line-broadening data. The portal's front page states 39 databases are currently connected and serving data.

**Access.** Guided and advanced query forms in the browser, results exported as VAMDC-XSAMS XML; programmatic access via the VAMDC-TAP protocol and the pyVAMDC Python library (version 1.0 released June 2026), with a cross-node species lookup at species.vamdc.org.

**Caveats.** An account is optional and only buys saved queries. Individual nodes go down for maintenance, so the set of databases answering a given query varies between runs. Each node keeps its own citation policy — the portal's citation page tells you whom to credit, and you cite the underlying database, not the portal.

## Software

### [ASE — Atomic Simulation Environment](https://ase-lib.org)

`Free` · beginner 3/5 · atomistic simulation driver

Python framework for setting up, running, visualising and analysing atomistic simulations, driving external codes (Quantum ESPRESSO, GPAW, ABINIT, VASP, LAMMPS, CP2K, SIESTA and dozens more) through one Atoms/Calculator interface, with built-in structure optimisation, molecular dynamics, phonons and nudged elastic band. Version 3.29.0 (21 June 2026), LGPL-2.1-or-later.

**Access.** `pip install ase`; build an `Atoms` object, attach a calculator (`atoms.calc = EMT()` for a quick test, or a DFT calculator), then `BFGS(atoms).run(fmax=0.05)`; `ase gui traj.traj` inspects trajectories.

**Caveats.** ASE only orchestrates — you still need the underlying DFT/MD engine installed along with its pseudopotentials, and every calculator interface has its own quirks. Documentation moved from wiki.fysik.dtu.dk/ase to ase-lib.org; old links redirect.

*Also listed under: chemistry.*

### [Delphes](https://delphes.github.io/)

`Free` · beginner 2/5 · fast detector simulation

C++ framework for fast, parametrised simulation of a generic collider detector — tracking in a magnetic field, calorimeters, muon system, pile-up — reading LHE or HepMC events and writing reconstructed objects (isolated leptons, jets, missing transverse energy) in a ROOT tree. Ships detector cards for ATLAS, CMS and future-collider concepts.

**Access.** `git clone https://github.com/delphes/delphes` and `make` against a ROOT installation; run `./DelphesPythia8 cards/delphes_card_CMS.tcl ...`, then analyse the output tree with ROOT or uproot.

**Caveats.** Parametrised response, not full Geant4 — appropriate for phenomenology and sensitivity estimates, not for claims about detector-level effects. Together with MadGraph and Pythia it makes a complete collider-study chain that runs on a laptop.

### [Einstein Toolkit](https://www.einsteintoolkit.org)

`Free` · beginner 1/5 · numerical relativity

Community open-source platform for relativistic astrophysics and gravitational physics: 3+1 spacetime evolution, general-relativistic (magneto)hydrodynamics, horizon finding and gravitational-wave extraction, built on the Cactus framework with Carpet/CarpetX adaptive mesh refinement. Current release 'Hypatia', 10 July 2026.

**Access.** Download with the GetComponents script from einsteintoolkit.org/download.html (it assembles several hundred component repositories from git/svn), then build and run with the Simulation Factory; a new-user tutorial walks through a first single-black-hole evolution.

**Caveats.** Predominantly GPL components, but licences are per-thorn and worth checking before redistribution. Binary-merger production runs need a cluster allocation; the tutorial examples run on a workstation. Support is a weekly open Zoom call and a mailing list rather than a ticket system.

### [FORM](https://github.com/vermaseren/form)

`Free` · beginner 1/5 · symbolic algebra for very large expressions

Symbolic manipulation system designed for expressions far larger than memory — it streams terms to disk, so the practical limit is disk space, not RAM. The standard tool for multi-loop Feynman-diagram algebra, Dirac trace and colour computations and large perturbative series in QFT. Version 5.0.0.

**Access.** `git clone https://github.com/vermaseren/form` then `autoreconf -i && ./configure && make` (optional gmp/mpfr/zlib/flint dependencies); write a `.frm` program and run `form myjob.frm`. TFORM and ParFORM builds add threaded and MPI parallelism.

**Caveats.** Its own terse, non-interactive language — not a Mathematica replacement for exploratory work; it wins only when expressions reach millions of terms. Usually driven by diagram generators such as QGRAF. The nikhef.nl homepage puts a licence-acceptance gate in front of the documentation, so GitHub is the practical entry point.

### [Geant4](https://geant4.web.cern.ch)

`Free` · beginner 1/5 · particle-matter Monte Carlo simulation

The standard open-source C++ toolkit for simulating the passage of particles through matter, used across high-energy physics, medical physics, radiation protection and space instrumentation.

**Access.** Source and binary downloads from geant4.web.cern.ch; build with CMake; extensive examples included in the distribution.

**Caveats.** Serious learning investment (C++, physics lists, geometry description); many detector simulations run fine on a laptop. Free user forum and annual courses; documentation is thorough.

### [GWpy](https://gwpy.github.io)

`Free` · beginner 4/5 · gravitational-wave data analysis

Python package for reading, filtering and plotting time- and frequency-domain data from the LIGO, Virgo and KAGRA detectors: GWF/HDF5 I/O, spectrograms, Q-transforms, whitening and coherence. Version 4.0.2 released 14 August 2026, GPL-3.0-or-later.

**Access.** `pip install gwpy` or `conda install -c conda-forge gwpy`; `from gwpy.timeseries import TimeSeries; TimeSeries.fetch_open_data('L1', 1126259446, 1126259478)` pulls public strain straight from GWOSC and `.q_transform().plot()` reproduces the classic event spectrogram.

**Caveats.** GWpy reads and conditions data but does not do detection or parameter estimation — GWOSC points to PyCBC for matched filtering and Bilby for parameter estimation, both installable from the same conda channel or the IGWN distribution.

### [Kwant](https://kwant-project.org)

`Free` · beginner 3/5 · quantum transport simulation

Open-source Python package for tight-binding quantum transport: conductance, band structures, edge states and scattering problems in mesoscopic and topological systems.

**Access.** `conda install -c conda-forge kwant` (or pip on supported platforms); tutorial in the online documentation.

**Caveats.** Development pace is slow but the package is stable and still the community standard for this class of problem; the topocondmat.org course teaches it in context.

### [LAMMPS](https://www.lammps.org)

`Free` · beginner 2/5 · molecular dynamics

Sandia's open-source (GPL) classical molecular dynamics code for soft matter, solid-state and coarse-grained simulations, scaling from a single laptop core to the largest supercomputers.

**Access.** Prebuilt binaries, `conda install -c conda-forge lammps`, or source from lammps.org; driven by plain-text input scripts.

**Caveats.** Force-field choice is the hard part; the mailing list and the MatSci.org forum are active and answer beginner questions.

### [LHAPDF](https://gitlab.com/hepcedar/lhapdf)

`Free` · beginner 3/5 · parton distribution functions

The universal C++/Python interface for evaluating parton distribution functions; PDF sets from CT, MSHT, NNPDF and others are distributed as separate data files and read through one API. Version 6.5.6 released 20 February 2026, GPL-3.0.

**Access.** `conda install -c conda-forge lhapdf` or build the tarball from the GitLab releases; `lhapdf install CT18NLO` fetches a set, then `import lhapdf; p = lhapdf.mkPDF('CT18NLO', 0); p.xfxQ(21, 0.01, 100.0)`.

**Caveats.** Pythia, MadGraph and Herwig all link against it, so the PDF set and LHAPDF version propagate directly into published numbers — record both. Individual sets are tens to hundreds of MB; install only what you use. The hepforge website blocks automated fetches, so use the GitLab mirror.

### [MadGraph5_aMC@NLO](https://launchpad.net/mg5amcnlo)

`Free` · beginner 2/5 · matrix-element generator

Automated tool for computing tree-level and NLO cross sections and generating parton-level events for arbitrary Standard Model and BSM processes; the workhorse of LHC phenomenology. Current release 3.7.2 (5 January 2026), with 3.5.16 maintained as a long-term-stable branch.

**Access.** Download the tarball from launchpad.net/mg5amcnlo or `git clone https://github.com/mg5amcnlo/mg5amcnlo`; drive it from its own command shell; needs Python 3.7+ and gfortran for NLO.

**Caveats.** LO studies of simple processes run comfortably on a laptop; NLO with matching/merging gets computationally heavy. Pair with Pythia for showering.

### [Meep](https://meep.readthedocs.io)

`Free` · beginner 3/5 · computational electromagnetics (FDTD)

MIT's free finite-difference time-domain solver for Maxwell's equations — waveguides, photonic crystals, metasurfaces, resonators, LDOS, scattering and adjoint-based optimisation — scripted from Python. GPL-2.0 and actively developed (github.com/NanoComp/meep).

**Access.** `conda install -c conda-forge pymeep`; the docs carry a graded tutorial series from a straight waveguide upwards. Companion package MPB computes photonic band structures.

**Caveats.** 2D simulations run comfortably on a laptop; 3D structures grow quickly in memory and runtime (parallel builds exist via `pymeep=*=mpi_mpich_*`). Resolution convergence checks are essential — FDTD results are meaningless without them.

### [OpenMC](https://openmc.org)

`Free` · beginner 2/5 · Monte Carlo neutron and photon transport

Community-developed, MIT-licensed Monte Carlo transport code with a full Python API: k-eigenvalue and fixed-source calculations, constructive solid geometry or CAD models, depletion, a flexible tally system, and hybrid MPI/OpenMP parallelism. Developed openly at github.com/openmc-dev/openmc.

**Access.** `conda install -c conda-forge openmc` or build from source; build geometry, materials and tallies in Python (`import openmc`), then `openmc.run()`. Free HDF5 cross-section libraries derived from ENDF/B are downloadable from openmc.org/data-libraries.

**Caveats.** The realistic free route to neutron transport: MCNP and SERPENT are licence-restricted or export-controlled, and Geant4 is aimed at a different regime. Simple criticality benchmarks run in minutes on a laptop; full-core depletion does not.

### [openQCD](https://luscher.web.cern.ch/luscher/openQCD/)

`Free` · beginner 1/5 · lattice QCD

Martin Lüscher and Stefan Schaefer's GPL-licensed lattice QCD simulation package (HMC/SMD algorithms, O(a)-improved Wilson quarks, open/SF/periodic boundary conditions, master-field simulations), a reference code of the lattice community; openQCD-2.4.2 is the current release.

**Access.** Source tarball from the website; C code parallelised with MPI; full algorithmic documentation included in the distribution.

**Caveats.** Production lattices need HPC allocations, but small test lattices run on a workstation and the code doubles as a masterclass in simulation algorithms.

### [Overleaf](https://www.overleaf.com)

`Free tier, email` · beginner 5/5 · collaborative LaTeX editor

Browser-based LaTeX editor with a hosted TeX Live installation, journal and preprint templates (REVTeX, JHEP, Elsevier, arXiv-ready), and real-time co-editing. The free plan gives unlimited projects, one collaborator per project, basic compile timeout and 24 hours of document history.

**Access.** Free account at overleaf.com; start from a template or upload a .zip of an existing project; source and compiled PDF are downloadable at any time.

**Caveats.** Paid plans (Student $8.25/month upward) are needed for more than one collaborator per project, track changes, full version history, longer compile timeouts, and Git/GitHub/Dropbox/Zotero integration; AI features are capped at 5 uses/day on free. Many universities hold site licences worth checking before paying. A local TeX Live install plus git has no limits at all — Overleaf's real value is collaborating with people who will not install LaTeX.

### [PennyLane](https://pennylane.ai)

`Free` · beginner 4/5 · differentiable quantum programming

Xanadu's Python library for quantum computing, quantum machine learning and quantum chemistry: build circuits, differentiate through them like a neural network, and dispatch to 40+ device backends via plugins (Lightning simulators, Qiskit, Cirq, Braket, IonQ). Version 0.45.1, Apache-2.0.

**Access.** `pip install pennylane` (Python 3.11+); free Codebook lessons at pennylane.ai/codebook and runnable tutorial demos at pennylane.ai/qml/demonstrations.

**Caveats.** The library, its local simulators and the learning material are free. Running on real QPUs goes through third-party providers (IBM, AWS Braket, IonQ) with their own accounts, quotas and charges. Statevector simulation is bounded by your own RAM/GPU — roughly 25-30 qubits on a laptop.

### [pymatgen](https://pymatgen.org)

`Free` · beginner 3/5 · materials analysis library

Python Materials Genomics: core objects for elements, sites, molecules and crystal structures, I/O for VASP, ABINIT, CIF, Gaussian and XYZ, phase and Pourbaix diagram construction, diffusion and electronic-structure analysis, and the client layer under the Materials Project API. Version 2026.5.4 (4 May 2026), MIT licence.

**Access.** `pip install pymatgen`; `from pymatgen.core import Structure; s = Structure.from_file('POSCAR')` for local files, or `from mp_api.client import MPRester; MPRester(key).get_structure_by_material_id('mp-149')` against Materials Project.

**Caveats.** Calendar-versioned with frequent API-breaking changes — pin the version in anything you intend to reproduce. Complements ASE rather than replacing it: ASE is better at driving calculators, pymatgen at structure analysis, file handling and phase diagrams.

### [PyMeasure](https://pymeasure.readthedocs.io)

`Free` · beginner 3/5 · lab instrument control and data acquisition

MIT-licensed Python package for running real experiments: community-contributed drivers for a large catalogue of lab instruments (source-measure units, lock-in amplifiers, oscilloscopes, function generators, power supplies) over GPIB/USB/serial/TCP, plus a Procedure/Worker framework with live plotting and CSV logging.

**Access.** `pip install pymeasure`; instantiate a driver (e.g. `Keithley2400('GPIB::24')`) over a PyVISA resource string and script your sweep; the GUI classes wrap a procedure into a live-plot application.

**Caveats.** Needs a VISA backend — `pyvisa-py` works with no vendor drivers, which matters if you cannot buy NI licences. Driver coverage is uneven: check the supported-instruments list before committing, and expect to write or extend a driver. QCoDeS (github.com/microsoft/Qcodes) is the equivalent standard in quantum-transport labs.

### [PYTHIA](https://pythia.org)

`Free` · beginner 2/5 · Monte Carlo event generator

The most widely used general-purpose event generator for high-energy collisions (pp, e+e-, and more), covering hard processes, parton showers, multiparton interactions, hadronization and decays. Current series is Pythia 8.3, GPL v2+.

**Access.** Source tarball from pythia.org; C++ library with Python interface; builds on a laptop in minutes.

**Caveats.** Physics choices (tunes, PDF sets from LHAPDF) matter for results; the online manual is the authoritative reference.

### [Qiskit](https://www.ibm.com/quantum/qiskit)

`Free` · beginner 4/5 · quantum computing SDK

IBM's open-source (Apache-2.0) SDK for building, transpiling and running quantum circuits, with the high-performance Aer simulator for local execution and the qiskit-ibm-runtime client for real IBM hardware.

**Access.** `pip install qiskit qiskit-aer` for local simulation; add `qiskit-ibm-runtime` plus a free IBM account to run on real QPUs.

**Caveats.** The SDK and simulator are fully free with no account; only hardware execution requires IBM registration (see IBM Quantum Platform entry). PennyLane (pennylane.ai, `pip install pennylane`) is the hardware-agnostic alternative if you want autodifferentiation and non-IBM backends.

### [Quantum ESPRESSO](https://www.quantum-espresso.org)

`Free` · beginner 2/5 · DFT / electronic structure

GPL-licensed suite for plane-wave density-functional theory: electronic structure, phonons, and materials modelling at the nanoscale — one of the two dominant open-source DFT codes alongside ABINIT.

**Access.** Source download from quantum-espresso.org or `conda install -c conda-forge qe`; pseudopotential libraries freely downloadable from the same site.

**Caveats.** Small-cell calculations run on a laptop; converged production work often needs a cluster. Commercial competitor VASP is licensed/paid — QE is the standard free route.

### [QuTiP](https://qutip.org)

`Free` · beginner 4/5 · open quantum systems simulation

Open-source Python library for simulating the dynamics of open quantum systems (master equations, Monte Carlo trajectories, arbitrary time-dependent Hamiltonians), standard in quantum optics, superconducting circuits and trapped ions. Version 5.3.1 was released on 4 August 2026; NumFOCUS-affiliated, BSD-licensed.

**Access.** `pip install qutip`; extensive tutorial notebooks at qutip.org.

**Caveats.** Simulations of ~10-20 qubits or modest Hilbert spaces are laptop-friendly; memory grows exponentially with system size.

### [Rivet](https://gitlab.com/hepcedar/rivet)

`Free` · beginner 2/5 · MC generator validation and analysis preservation

Toolkit that preserves collider analysis logic as reusable code and compares Monte Carlo predictions against published measurements; ships hundreds of routines encoding LHC, Tevatron, HERA and LEP analyses, reads HepMC events and writes YODA histograms. Version 4.1.3, GPL-3.0.

**Access.** `docker run -it hepstore/rivet` is the fastest start; otherwise the bootstrap script or a source build against YODA and HepMC. Run `rivet --analysis=<ANALYSIS_ID> events.hepmc` on generator output, then `rivet-mkhtml` for data/MC comparison plots.

**Caveats.** The rivet.hepforge.org site sits behind an anti-bot challenge that blocks scripted access; the GitLab project and hepcedar.gitlab.io/rivet are the reliable entry points. Rivet checks your generator setup, it does not fix it — tunes and PDF choices still dominate agreement with data.

### [ROOT](https://root.cern)

`Free` · beginner 2/5 · HEP data analysis framework

CERN's C++ data-analysis framework — histogramming, fitting (RooFit), I/O for the .root format in which essentially all LHC data is stored — with Python bindings (PyROOT). Open source (LGPL), in continuous development since 1995.

**Access.** `conda install -c conda-forge root`, prebuilt binaries from root.cern, or distro packages; `import ROOT` from Python.

**Caveats.** Steep learning curve; if you only need to read .root files in Python, uproot (Scikit-HEP) is far lighter. The ROOT Forum (root-forum.cern.ch) is an active help channel answered by the developers themselves — the best place to ask ROOT questions.

### [Scikit-HEP](https://scikit-hep.org)

`Free` · beginner 4/5 · Python HEP ecosystem

Community ecosystem of Python packages for particle physics: uproot reads and writes ROOT files with no ROOT installation, awkward handles jagged arrays, plus hist, vector, particle, and iminuit. The practical route into LHC open data for anyone who knows NumPy.

**Access.** `pip install uproot awkward hist vector particle`; each package documented at scikit-hep.org.

**Caveats.** Pure-Python stack that runs anywhere; for very large datasets you still need to think about chunked/streamed reading.

### [SciPy ecosystem](https://scipy.org)

`Free` · beginner 5/5 · scientific Python stack

NumPy, SciPy and Matplotlib — the numerical backbone under nearly every Python-based physics tool listed here, including special functions, ODE solvers, optimisation, FFTs and the CODATA constants in scipy.constants.

**Access.** `pip install numpy scipy matplotlib`; documentation and tutorials at scipy.org.

### [Stim](https://github.com/quantumlib/Stim)

`Free` · beginner 3/5 · stabilizer / quantum error correction simulation

Google Quantum AI's Apache-2.0 fast stabilizer circuit simulator, the de facto standard for quantum error-correction research: simulates surface-code circuits with millions of gates in seconds and emits detector-error models for decoders such as PyMatching.

**Access.** `pip install stim pymatching sinter`; build a circuit with `stim.Circuit`, sample detection events, and decode — everything runs on a laptop CPU.

**Caveats.** Stabilizer (Clifford) circuits only — it cannot simulate universal quantum computation. Threshold estimates that would need a cluster with state-vector methods become a coffee-break job here.

### [TeNPy](https://tenpy.readthedocs.io)

`Free` · beginner 2/5 · tensor networks / many-body quantum

Tensor Network Python: matrix-product-state library for one- and quasi-one-dimensional quantum many-body systems — DMRG ground states, TEBD/TDVP time evolution, finite and infinite chains, built-in Hubbard, Heisenberg and fermionic models. Apache-2.0, actively developed (github.com/tenpy/tenpy).

**Access.** `pip install physics-tenpy`; define a model class or use a built-in one and run DMRG from a Python script or YAML config.

**Caveats.** Spin chains and ladders converge on a laptop; genuinely two-dimensional systems still need large bond dimensions and serious compute. You need to understand MPS/entanglement scaling to trust the output — the docs include an introduction, and QuSpin (exact diagonalisation) is the complementary tool for small systems.

### [Zotero](https://www.zotero.org)

`Free` · beginner 5/5 · reference manager

Free, open-source reference manager with browser connectors that capture citations and PDFs from arXiv, ADS, INSPIRE and publisher pages, a Word/LibreOffice/Google Docs plugin, BibTeX/BibLaTeX export for LaTeX, PDF annotation and shared group libraries. Accounts include 300 MB of free sync storage.

**Access.** Install the desktop app plus the browser connector from zotero.org/download; the Better BibTeX add-on keeps an auto-updating .bib file next to your LaTeX project; a free account enables sync and group libraries.

**Caveats.** The application and unlimited local libraries cost nothing; only cloud file storage above 300 MB is paid ($20/yr for 2 GB up to $120/yr unlimited). Attachments can be linked from a local folder or synced via your own WebDAV instead, which keeps the free tier genuinely workable. The library is a local SQLite database, so data is portable.

## Literature

### [arXiv](https://arxiv.org)

`Free` · beginner 5/5 · preprint server

The spine of physics literature since 1991: nearly 2.4 million preprints across physics, maths and allied fields, with essentially every particle-physics, cond-mat and quantum paper appearing here first. Reading is free with no account.

**Access.** Web, plus free bulk/API access (arXiv API, Kaggle dataset, full-text bulk on S3); submission requires a free account.

**Caveats.** First-time submitters need endorsement per category. Authors with a recognised institutional email address can be auto-endorsed; unaffiliated authors must ask an established arXiv author to endorse them — abstract pages carry a 'Which authors of this paper are endorsers?' link, and arXiv asks that you approach someone who knows you and your subject rather than mass-emailing. A real hurdle, so line up an endorser before you need one.

### [INSPIRE-HEP](https://inspirehep.net)

`Free` · beginner 4/5 · bibliographic database (high-energy physics)

The high-energy physics community's bibliographic database: 1,880,967 literature records (checked August 2026) with citation graphs, author profiles, conference and jobs listings; run by a collaboration including CERN, DESY, Fermilab, IHEP, IN2P3 and SLAC.

**Access.** Web search (powerful query syntax); free REST API documented at github.com/inspirehep/rest-api-doc — no key required, e.g. `https://inspirehep.net/api/literature?q=t+higgs&size=25`.

**Caveats.** Coverage is deep for HEP, nuclear and astro-particle physics but not for condensed matter or general physics — use it for what it is.

### [Living Reviews in Relativity](https://link.springer.com/journal/41114)

`Free` · beginner 3/5 · open-access review journal

Fully open-access review journal on general relativity and gravitational physics whose invited articles are periodically updated by their authors — the standard entry points into topics like tests of GR, numerical relativity, and gravitational-wave theory.

**Access.** All articles free to read/download on SpringerLink.

**Caveats.** Articles are commissioned — this is a reading resource, not a submission venue for most researchers.

### [NASA Astrophysics Data System (ADS / SciX)](https://ui.adsabs.harvard.edu)

`Free` · beginner 4/5 · bibliographic database (astronomy and physics)

NASA-funded literature database operated by the Smithsonian Astrophysical Observatory covering astronomy, astrophysics and physics: journal articles, arXiv e-prints, conference proceedings and scanned historical literature, with citation and reference graphs, full-text search, metrics and links to data and software. Being rebuilt as SciX (scixplorer.org) with added earth, planetary and heliophysics collections.

**Access.** Free web search at ui.adsabs.harvard.edu with a rich query syntax (`author:"^Abbott, B" year:2016 property:refereed`); REST API at api.adsabs.harvard.edu needs a free personal token generated in account settings, sent as `Authorization: Bearer <token>`.

**Caveats.** Reading and searching need no account; only the API, saved libraries and alerts require a free login. API rate limits are per-endpoint daily allowances reported in X-RateLimit headers. Coverage is deepest in astronomy, astrophysics, gravitation and space physics — for condensed matter or nuclear work INSPIRE or OpenAlex serve better. The classic UI is migrating to SciX, so bookmarked URLs may move.

### [OpenAlex](https://openalex.org)

`Free` · beginner 4/5 · open bibliographic index

Fully open index of scholarly works from the non-profit OurResearch and the practical successor to Microsoft Academic Graph: 322,147,582 works as of 28 August 2026, of which about 56.7 million carry the Physics concept, with linked authors, institutions, sources, citation counts and open-access status, all released CC0.

**Access.** REST API at api.openalex.org with no key — e.g. `https://api.openalex.org/works?filter=concepts.id:C121332964&per-page=1`; adding `mailto=you@example.com` puts you in the faster polite pool. Full monthly snapshots download from a public S3 bucket; `pip install pyalex` wraps the API.

**Caveats.** Author disambiguation and topic tagging are automated and make mistakes, so it is better for coverage-scale bibliometrics than as a definitive record of one person's output. Daily and per-second rate limits apply to the free API; take the snapshot for heavy analysis. It is metadata plus OA links, not full text.

### [Unpaywall](https://unpaywall.org)

`Free` · beginner 5/5 · legal open-access lookup

Index of legally posted free versions of paywalled articles, harvested from publisher OA pages, institutional and subject repositories and preprint servers, run by the non-profit OurResearch. Delivered as a browser extension that flags a free copy when you land on a paywalled article, and as a free DOI-keyed REST API.

**Access.** Install the Chrome/Firefox extension; or query `https://api.unpaywall.org/v2/{DOI}?email=you@example.com` and read `best_oa_location.url_for_pdf`; full database snapshots are also released for free.

**Caveats.** Only legal copies — it finds nothing when no author or publisher has posted one. In physics most of what it surfaces is the arXiv version, so checking arXiv first is often quicker; the real value is older or applied-physics literature outside arXiv's habits. The API asks for your email address in the query string rather than a key.

## Compute

### [ACCESS (NSF national cyberinfrastructure allocations)](https://access-ci.org)

`Free, application` · beginner 2/5 · US national HPC and GPU allocations

The NSF programme that allocates time on US national systems (Anvil, Bridges-2, Delta, Expanse, Stampede3, Jetstream2 and others). Four tiers: Explore (400,000 credits, one-page request), Discover (1,500,000 credits, three pages), Accelerate (3,000,000 credits, ten pages, merit panel) and Maximize (awarded in resource units, merit panel). Explore/Discover/Accelerate accept requests at any time; Maximize opens every six months.

**Access.** Create an ACCESS ID with an institutional email at access-ci.org, browse the resource catalogue, then submit an allocation request at allocations.access-ci.org and exchange the awarded credits for time on specific machines. Explore requests can be approved in 1-2 business days.

**Caveats.** Eligibility is limited to US-based PIs at academic, government or non-profit institutions — no route for researchers elsewhere, and student-PI rules are on the eligibility page. Credits buy very different amounts of wall time on different resources, so read the exchange rates. Allocations run for the supporting grant's duration or 12 months, whichever is longer, and carry reporting expectations.

### [EuroHPC JU supercomputer access calls](https://eurohpc-ju.europa.eu/access-our-supercomputers/eurohpc-access-calls_en)

`Free, application` · beginner 2/5 · European HPC allocations

Peer-reviewed allocations on Europe's petascale and pre-exascale systems (LUMI, Leonardo, MareNostrum 5, JUPITER and others). Five access modes were open in August 2026; Benchmark Access and Development Access are continuously open calls with a maximum of two weeks from submission to resource start date, while Regular, Extreme Scale and the AI for Science mode run to cut-off dates.

**Access.** Apply through the EuroHPC access portal linked from each call page — a technical proposal plus a named principal investigator; Development Access is the low-friction route for porting and scaling a code before a large request.

**Caveats.** Eligibility is limited to users established or located in an EU Member State or a country associated with Horizon 2020 — no route for researchers elsewhere. Allocations are awarded on scientific and technical review rather than payment; read each call's text for its conditions, including expectations to publish results.

### [Google Colab (free tier)](https://colab.research.google.com)

`Free tier, email` · beginner 5/5 · free GPU/TPU notebooks

Google-hosted Jupyter notebooks with best-effort free access to NVIDIA GPUs and TPUs. Free sessions run at most 12 hours and are cut short by idleness or heavy usage; the accelerator model offered varies over time and by availability.

**Access.** Sign in with a Google account at colab.research.google.com; pick the accelerator under Runtime > Change runtime type; `!pip install` works inside the session and notebooks save to Google Drive or GitHub.

**Caveats.** Google publishes no fixed free quota — allocation is dynamic and heavy users get throttled or refused a GPU at busy times, which makes it unsuitable for anything on a deadline. Nothing outside the runtime's disk persists after the session ends; mount Drive or push to git. SSH, remote desktops, long unattended jobs and mining are prohibited. Kaggle Notebooks is the alternative with a stated weekly quota.

### [IBM Quantum Platform (Open Plan)](https://quantum.cloud.ibm.com)

`Free tier, api-key` · beginner 4/5 · free quantum hardware access

Free access to IBM's superconducting quantum processors (100+ qubit systems): the Open Plan grants up to 10 minutes of QPU runtime per 28-day rolling window, and from 16 March 2026 active Open Plan users can opt in to an additional 180 minutes spread over 12 months.

**Access.** Register a free IBM Cloud account at quantum.cloud.ibm.com, create an Open Plan instance, then `pip install qiskit qiskit-ibm-runtime` and submit jobs with your API token.

**Caveats.** 10 minutes is QPU execution time, not wall-clock — enough for real small-scale experiments if you simulate first and batch jobs. Open Plan instances are limited to the us-east region and queues on popular systems can be hours. Plan terms have changed before; check the plans-overview docs page for current limits.

### [Kaggle Notebooks](https://www.kaggle.com/code)

`Free (registration), email` · beginner 5/5 · free GPU notebooks

Free hosted Jupyter environment with NVIDIA GPU and TPU accelerators on a fixed weekly quota (30 GPU-hours per week at the time of writing), sessions capped at about 12 hours, and free hosting for datasets you attach — usable from anywhere, with no institutional affiliation needed.

**Access.** Free account at kaggle.com, create a notebook, select the accelerator in the sidebar; `pip install` works inside the session and you can attach public datasets or your own uploads.

**Caveats.** Accelerators require phone verification of the account. Quotas are shown in the notebook editor and do change — check there rather than trusting any published figure. Only /kaggle/working persists as notebook output; everything else is wiped when the session ends. Google Colab's free tier is the obvious alternative: no fixed quota, but GPU access is best-effort, sessions run at most 12 hours and idle notebooks are killed.

### [mybinder.org](https://mybinder.org)

`Free` · beginner 5/5 · free notebook execution

Turns any public Git repository with an environment file into a live, shareable Jupyter environment in the browser — the standard way to make a physics analysis or tutorial reproducible without asking readers to install anything.

**Access.** Paste a repo URL at mybinder.org (or add a launch badge to your README); no account needed.

**Caveats.** Runs on donated cloud resources; total capacity dropped roughly 60% in April 2026 when Google's credits ended, so expect occasional capacity errors. Sessions are ephemeral with modest RAM — for demos and teaching, not production compute.

### [OSG Open Science Pool (OSPool)](https://osg-htc.org/services/ospool/)

`Free, application` · beginner 2/5 · high-throughput computing

Free opportunistic high-throughput computing across US campuses via HTCondor: OSG's own guidance calls jobs ideal when they use 1 CPU or GPU, run under 10 hours and move under 10 GB of input/output, still advantageous up to 12 CPUs or 4 GPUs, 20 hours and 40 GB, and worth discussing beyond that. Well-suited workloads can reach thousands of concurrent cores.

**Access.** Request an account at portal.osg-htc.org; a facilitator meeting follows, then jobs are submitted from an OSG access point with HTCondor.

**Caveats.** Eligibility is restricted to researchers affiliated with a US-based academic, government, or non-profit institution — not available to unaffiliated or non-US researchers. Jobs are preemptible; checkpoint or keep them short.

## Publishing

### [Journal of Open Source Software (JOSS)](https://joss.theoj.org)

`Free, email` · beginner 4/5 · diamond open-access software journal

Peer-reviewed, developer-friendly journal (ISSN 2475-9066) for research software: no fees for authors or readers, review conducted openly in GitHub issues against a published checklist covering the software, its tests and its documentation, and accepted papers get a Crossref DOI and are indexed.

**Access.** Submit at joss.theoj.org with a public repository URL and a short `paper.md` (roughly 250-1000 words); the whole review happens in a public GitHub issue.

**Caveats.** The paper is deliberately minimal — reviewers judge the software, so it must be substantial, open-source and documented, not a script. The practical way to turn a simulation or analysis package into a citable publication with no APC when you have no grant to pay one.

### [Quantum (journal)](https://quantum-journal.org)

`Free, email` · beginner 3/5 · arXiv-overlay journal (quantum science)

Non-profit, community-run arXiv-overlay journal for quantum science founded in 2017. The publication fee is a voluntary article processing charge of €600 with a discounted €100 rate, in force since 1 January 2024; a full waiver is available on request with no justification required.

**Access.** Submit the arXiv version through quantum-journal.org; published papers are free to read (CC-BY) and live on arXiv.

**Caveats.** Selective venue with strong reputation in quantum information; the no-questions-asked waiver makes it genuinely open to unfunded authors.

### [SciPost](https://scipost.org)

`Free, email` · beginner 3/5 · diamond open-access journals

Academic-run diamond OA publisher founded in 2016: no fees for authors or readers, open (published) peer review. Flagship SciPost Physics plus SciPost Physics Core, Lecture Notes, Proceedings and Codebases; funded by voluntary institutional sponsorships at an average cost of about €500 per paper.

**Access.** Submit via scipost.org (arXiv-linked workflow); all published papers and referee reports free on the site.

**Caveats.** SciPost Physics has become a respected venue in theory and cond-mat/quantum; refereeing standards are high and acceptance is selective.

### [SCOAP3](https://scoap3.org)

`Free` · beginner 4/5 · open-access funding consortium (HEP)

CERN-coordinated consortium of 3,000+ libraries and agencies in 44 countries that pays open-access costs centrally so authors pay nothing. Phase 4 (2025-2027) covers 11 journals including JHEP, EPJC, Physics Letters B, Nuclear Physics B, PTEP, Chinese Physics C, and HEP articles in PRL, PRC and PRD.

**Access.** No action needed: publish HEP content in a participating journal and OA fees are covered automatically; articles come out CC-BY with authors retaining copyright.

**Caveats.** Only high-energy-physics articles qualify in the APS journals (coverage per journal ranges from ~9% to 100%); outside HEP the scheme does not apply.

### [Zenodo](https://zenodo.org)

`Free, email` · beginner 5/5 · data and software repository

CERN-operated general-purpose repository (launched 2013, built on InvenioRDM with OpenAIRE/EU backing): free DOIs for datasets, software, posters, and preprints from any discipline, with versioning and a GitHub integration that archives tagged releases automatically.

**Access.** Web upload after free registration; REST API with a personal access token for scripted deposits; the standard limit is 100 files and 50 GB per record, extendable to 200 GB through the storage-quota request process.

**Caveats.** Standard way to make supplementary data and analysis code citable when a journal or field archive has no home for it.

## Funding

### [FQxI (Foundational Questions Institute)](https://fqxi.org)

`Free, application` · beginner 2/5 · foundational physics grants

Funder of research on foundational questions in physics and cosmology: Zenith Grants are periodic international RFPs open to researchers (independent researchers have been funded historically), plus regular essay competitions with cash prizes and member-only Fulcrum Grants of $1,000-$15,000.

**Access.** Apply to open calls announced at fqxi.org/programs; essay competitions run via the FQxI community site.

**Caveats.** As of August 2026 FQxI's own programmes page states it is 'currently raising funds to host future rounds of the Zenith and Fulcrum Grants' — so there is no open grant call right now, and Fulcrum Grants (up to $15K) are for FQxI Members only. Essay and mini-competitions continue to run and are the realistic entry point for an unaffiliated researcher; a February 2026 mini-competition ('How Quantum is Life?', $53,000 across eight winners) shows the programme is still active.

### [Google Summer of Code](https://summerofcode.withgoogle.com)

`Free, application` · beginner 3/5 · paid open-source contribution programme

Google-funded programme that pairs new open-source contributors with mentoring organisations for 8-22 week projects and pays a stipend on completion. Eligibility is being 18 or over, resident in a non-embargoed country, and new to open source — no student status, degree, or institutional affiliation required. Physics and scientific-computing organisations (CERN-HSF among the long-running ones) mentor projects most years.

**Access.** Browse the accepted-organisation list published each spring at summerofcode.withgoogle.com, engage with a project's issue tracker and mentors, then submit a proposal in the contributor application window.

**Caveats.** Stipend size varies by country of residence. Highly competitive, and accepted proposals almost always come from people who contributed a patch or two beforehand. The organisation list is re-chosen every year — never assume a given project will take part again.

### [ICTP — Abdus Salam International Centre for Theoretical Physics](https://www.ictp.it)

`Free, application` · beginner 3/5 · support for physicists from developing countries

Trieste-based UN-family centre whose mission is physics in the developing world: a fully funded one-year Postgraduate Diploma (no fees, scholarship covering travel and living costs, ~10 scholarships per field, 1,000+ alumni from 84 countries), the Associates scheme funding repeated research visits over three years, plus funded schools, workshops and the Physics Without Frontiers programme.

**Access.** Apply to individual programmes at ictp.it (opportunities section); most scientific meetings also stream or post lectures free online.

**Caveats.** Most support is restricted to scientists from developing countries; selection is competitive. Lecture recordings and diploma course materials are freely watchable by anyone.

### [NumFOCUS Small Development Grants](https://numfocus.org/programs/small-development-grants)

`Free, application` · beginner 2/5 · open-source scientific software grants

Grants of up to $10,000, three cycles per year, for development and infrastructure work on NumFOCUS-sponsored or affiliated open-source projects — a realistic funding route for contributors to physics-relevant projects such as QuTiP, NumPy, SciPy and Matplotlib.

**Access.** Proposals submitted through the program's GitHub repository during announced cycles, in coordination with the target project's maintainers.

**Caveats.** Only NumFOCUS-affiliated/sponsored projects are eligible, so the practical path is to propose work with an existing project community rather than for a personal project.

### [Perimeter Scholars International (PSI)](https://perimeterinstitute.ca/psi-masters-program)

`Free, application` · beginner 3/5 · fully funded master's in theoretical physics

One-year master's programme at Perimeter Institute (Waterloo, Canada) taught by working theorists, awarding an MSc in Physics from the University of Waterloo plus a PSI certificate. Scholarships are extended to up to all accepted students and cover full tuition, accommodation, meals, a living stipend, health insurance, IT equipment and learning materials, and a travel supplement.

**Access.** Apply online through the PSI admissions pages at perimeterinstitute.ca during the annual application window; consideration for the full scholarship is part of the admissions process.

**Caveats.** Highly selective, and theory-only (quantum fields and strings, gravity, quantum information, condensed matter, cosmology). Applications for the next cohort open in October 2026 per the programme page. Students are expected to apply for any external funding they qualify for (e.g. NSERC in Canada), and the programme page describes 'options for monetary support' with details on a separate financial-support page rather than guaranteeing a full scholarship to every admit. The lecture courses themselves are separately free to anyone via PIRSA.

### [Unitary Foundation Microgrants](https://unitary.foundation/grants/)

`Free, application` · beginner 4/5 · quantum technology microgrants

$4,000 microgrants for quantum-technology projects — open-source software, education materials, hardware prototypes — awarded to individuals and teams worldwide with no degree or affiliation requirement; over 100 grants across 31+ countries to date. A Deltakit Community Fund ($2,000-$4,000 for open-source quantum error correction work, with Riverlane) launched July 2026.

**Access.** Rolling application via the short form linked from unitary.foundation/grants/.

**Caveats.** Small awards by design — meant to bootstrap a project, not fund a salary. Their Discord is also one of the livelier open quantum-software communities.

## Learning

### [David Tong — Lectures on Theoretical Physics](https://davidtong.org/teaching/)

`Free` · beginner 4/5 · graduate lecture notes

Complete, free PDF lecture notes from Cambridge covering most of the theory curriculum — classical dynamics, electromagnetism, statistical physics, quantum mechanics, quantum field theory, string theory, solid state, general relativity, gauge theory and more — widely treated as de facto textbooks.

**Access.** Direct PDF download, no registration.

**Caveats.** Notes assume the mathematical maturity of a physics degree; the QFT and Statistical Physics sets are the community's most-recommended free treatments of those subjects.

### [How to Become a Good Theoretical Physicist ('t Hooft)](https://www.goodtheorist.science)

`Free` · beginner 4/5 · self-study curriculum

Nobel laureate Gerard 't Hooft's structured self-study roadmap from mathematics and classical mechanics up through quantum field theory, general relativity and string theory, built around links to free online resources and aimed at determined independent learners.

**Access.** Free website; links out to free lecture notes and texts.

**Caveats.** A map, not a course — 't Hooft estimates ~5 years of dedicated work to cover it; some external links age and need hunting down.

### [HSF Training Center](https://hsf-training.org/training-center/)

`Free` · beginner 4/5 · research software training for physics

The HEP Software Foundation's free, self-paced lesson modules — the training the field itself points new students to. Basics (UNIX shell, git, Python, SSH), software development (advanced git, CI/CD on GitHub and GitLab, Docker, Singularity, unit testing, CMake, a full HEP C++ course), HEP tools (ROOT, Scikit-HEP, pyhf, REANA, UnROOT for Julia) and analysis (array-oriented programming, deep learning for particle physicists, ML on GPUs).

**Access.** Work through the lessons in the browser at hsf-training.org; every module is a Carpentries-style page with runnable exercises, sources on GitHub. Live workshops are announced on the same site.

**Caveats.** Assumes you can already program a little. This is the fastest bridge from 'I know some Python' to actually opening LHC open data — start with the Scikit-HEP and ROOT modules if that is the goal.

### [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/en)

`Free` · beginner 5/5 · quantum computing courses

IBM's free course platform (successor to the Qiskit Textbook): 10+ courses including John Watrous's 'Basics of Quantum Information', plus hands-on Qiskit tutorials that run against simulators or real hardware.

**Access.** Browse free on the web; a free IBM account links courses to executable notebooks and the Open Plan hardware tier.

**Caveats.** Content is Qiskit/IBM-centric by design; concepts transfer, tooling is vendor-specific.

### [MIT OpenCourseWare — Physics](https://ocw.mit.edu/search/?d=Physics)

`Free` · beginner 5/5 · university course materials

Free, openly licensed materials for MIT physics courses from introductory mechanics through graduate quantum field theory, many with complete video lectures, problem sets and exams (e.g. 8.04 Quantum Physics I, 8.05/8.06, 8.033 Relativity).

**Access.** Direct browsing and download at ocw.mit.edu; videos also on YouTube; no registration.

**Caveats.** Materials are static snapshots of past course offerings — no instructor interaction or certificates.

### [OpenStax — University Physics](https://openstax.org/subjects/science)

`Free` · beginner 5/5 · open textbooks

Rice University's peer-reviewed, openly licensed (CC-BY) textbooks, including the three-volume calculus-based University Physics and algebra-based College Physics, free as web view and PDF.

**Access.** Read online or download PDF at openstax.org, no registration.

**Caveats.** Introductory level only — the free route for teaching or refreshing fundamentals, not for graduate study.

### [PhET Interactive Simulations](https://phet.colorado.edu)

`Free` · beginner 5/5 · interactive simulations

Browser-based simulations for physics, chemistry, biology, earth science and maths from the University of Colorado Boulder. PhET's own catalogue API lists 246 simulations, 119 of them native HTML5, and the HTML5 titles carry translations in 130 locales.

**Access.** Run any simulation in the browser at phet.colorado.edu; sims can also be downloaded for offline use, and each one has its source repository under github.com/phetsims. The catalogue is queryable as JSON at phet.colorado.edu/services/metadata/1.3/simulations?format=json.

**Caveats.** Simulation source is GPL-3.0 (checked on the phetsims GitHub repos); a free account is only needed to contribute teaching activities. PhET Studio, a separate authoring product, is licensed and paid. The sims are teaching and intuition tools, not research-grade numerics — 48 legacy titles are still Flash-era and 85 are Java, some run only through a compatibility layer.

### [PIRSA — Perimeter Institute Recorded Seminar Archive](https://pirsa.org)

`Free` · beginner 3/5 · research seminar archive

Free, permanent, citable archive of recorded physics seminars and courses from the Perimeter Institute — every talk gets a PIRSA number — including the complete Perimeter Scholars International graduate lecture courses across quantum gravity, quantum information, cosmology, condensed matter and mathematical physics.

**Access.** Stream free at pirsa.org, browsable by field and series; no registration.

**Caveats.** Research-level content; the PSI course collections are the most structured entry point.

### [The Feynman Lectures on Physics](https://www.feynmanlectures.caltech.edu)

`Free` · beginner 5/5 · classic textbook (free online edition)

Caltech's free, high-quality HTML edition of all three volumes of the Feynman Lectures — mechanics, electromagnetism and matter, and quantum mechanics — the field's most famous introduction to physical reasoning.

**Access.** Read free in the browser at feynmanlectures.caltech.edu.

**Caveats.** Online reading only — there is no authorized free PDF/ebook download; print editions remain commercial.

### [The Theoretical Minimum (Susskind)](https://theoreticalminimum.com)

`Free` · beginner 5/5 · video lecture course series

Leonard Susskind's Stanford continuing-studies lecture courses, free in full video: a core sequence of six courses — classical mechanics (2011), quantum mechanics (2012), special relativity and electrodynamics (2012), general relativity (2012), cosmology (2013) and statistical mechanics (2013) — plus supplemental courses on advanced topics including quantum entanglement, string theory and cosmology.

**Access.** Stream free at theoreticalminimum.com, where each course page links its lecture videos, or from Stanford's YouTube channel; no registration.

**Caveats.** Aimed at people who want the actual equations without a full degree — lighter than a graduate course, with no problem sets, assessment or certificates, and recorded over a decade ago. The companion books are commercial. Good as a first pass before Tong's notes or MIT OCW, not as a substitute for them.

### [Topology in Condensed Matter](https://topocondmat.org)

`Free` · beginner 3/5 · online graduate course

Free open-source graduate course on topological phenomena in condensed matter (Majoranas, topological insulators, quantum Hall physics), created by researchers at TU Delft, Maryland and Leiden for edX in 2015 and maintained since, combining theory with runnable Kwant simulations.

**Access.** Read and run everything at topocondmat.org, no registration; source notebooks on GitHub.

**Caveats.** Assumes solid quantum mechanics and some band theory.

## Community

### [Physics Stack Exchange](https://physics.stackexchange.com)

`Free` · beginner 5/5 · Q&A site

The largest active Q&A site for physics, spanning conceptual questions to research-level topics, with many practising researchers among the answerers; the full archive is searchable and CC-licensed.

**Access.** Read without an account; free registration to ask or answer.

**Caveats.** Strict scope rules — homework-style questions must show effort, and open-ended discussion is off-topic; search before asking.

### [PhysicsForums](https://www.physicsforums.com)

`Free, email` · beginner 5/5 · discussion forum

Moderated physics discussion community running since 2001, with dedicated homework-help sections (staffed by mentors), subject forums up to graduate level, and career/academia advice threads.

**Access.** Read free; free registration to post.

**Caveats.** Better than Stack Exchange for extended back-and-forth tutoring on a problem; moderation enforces mainstream-science rules.

### [Quantum Computing Stack Exchange](https://quantumcomputing.stackexchange.com)

`Free` · beginner 4/5 · Q&A site

Q&A community for quantum computing and quantum information where framework developers (Qiskit, QuTiP, PennyLane) and active researchers routinely answer both theory and tooling questions.

**Access.** Read without an account; free registration to participate.

**Caveats.** For live help, the Unitary Foundation Discord covers similar ground with faster turnaround.

### [researchseminars.org](https://researchseminars.org)

`Free` · beginner 4/5 · open seminar and conference listings

Community-maintained, free listing of online and hybrid research seminars, courses and conferences with time-zone-aware schedules and, for most series, public join links; the topic browser showed 85 physics series alongside mathematics, computer science and other fields on 28 August 2026.

**Access.** Browse or search at researchseminars.org with no account; a free account lets you subscribe to series, export to your calendar, and list a seminar of your own.

**Caveats.** Each series sets its own access rules — some need a registration form or a password from the organiser, so a listing is not always an open door. Coverage is strongest in mathematics and mathematical/theoretical physics; experimental series are thinly represented. Still, it is the most practical way for someone with no department to sit in on current research talks.
