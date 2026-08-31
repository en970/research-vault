# Chemistry & materials science

Part of [research-vault](../README.md). 85 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (25) · [Software](#software) (27) · [Literature](#literature) (9) · [Compute](#compute) (5) · [Publishing](#publishing) (8) · [Funding](#funding) (3) · [Learning](#learning) (5) · [Community](#community) (3)

## Data

### [AFLOW](https://aflow.org/)

`Free` · beginner 3/5 · high-throughput DFT repository

Duke-led high-throughput DFT repository of inorganic compound prototypes with computed thermodynamic, electronic, elastic and thermal properties, built on the AFLOW automatic workflow framework and searchable by composition, space group and Pearson symbol.

**Access.** AFLUX search API, no key - https://aflow.org/API/aflux/?species(Fe,Si),nspecies(2),$paging(1,3) returns JSON (verified working 2026-08-28). Also a per-entry REST API keyed on AFLOW unique identifiers (auid), plus the `aflow` Python package.

**Caveats.** The AFLUX query syntax is idiosyncratic and shell-hostile - URL-encode or quote the $ and parentheses. The website carries little documentation; the tutorials and school pages hold the real instructions. Bulk export is awkward compared with Materials Project or NOMAD, and its OPTIMADE endpoint returned an unfiltered count of 0 on 2026-08-28.

### [Alexandria Materials Database](https://alexandria.icams.rub.de/)

`Free` · beginner 3/5 · DFT-relaxed crystal structures

Open high-throughput database of DFT-relaxed inorganic crystals with PBE, PBEsol, SCAN and MatPES geometries, convex hulls, phonons and benchmarks. The PBE OPTIMADE endpoint returned 5,779,351 structures on 2026-08-28 - roughly an order of magnitude more entries than Materials Project.

**Access.** Web explorer (query by composition, space group, stability), on-demand 2-4 element convex-hull phase diagrams, dataset downloads, and OPTIMADE at https://alexandria.icams.rub.de/pbe/v1/structures .

**Caveats.** Much of the content is machine-generated, including structures proposed by the group's Matra-Genoa generative model, so entries are predictions rather than measurements - treat stability numbers as screening signals. The site notes some data is unreleased and available only by contacting the group. Check the About page for the current licence and citation before redistributing.

### [Basis Set Exchange](https://www.basissetexchange.org/)

`Free` · beginner 5/5 · Gaussian basis sets

Curated library of Gaussian basis sets and effective core potentials, maintained jointly by MolSSI and PNNL/EMSL, with export to about 25 quantum-chemistry input formats including NWChem, Gaussian, Psi4, ORCA, CP2K, Molpro, Turbomole, GAMESS, CFOUR, Dalton, FHI-aims and QCSchema JSON.

**Access.** Web interface - pick basis set, elements and program format, then paste the block into your input. Also a documented REST API and `pip install basis_set_exchange` for scripted retrieval. The whole library downloads as tar.bz2 or zip.

**Caveats.** Basis sets carry the citation obligations of their original papers; BSE metadata gives you the references and you are expected to cite them. Format converters are good but not infallible - sanity-check the first calculation against a small reference system.

### [BindingDB](https://www.bindingdb.org/)

`Free` · beginner 4/5 · protein-ligand binding affinities

Public database of measured binding affinities (Ki, Kd, IC50, EC50) between drug-like small molecules and protein targets, reporting 3.2 million data points for 1.4 million compounds and 11,500 targets, of which 1.6 million data for 772,000 compounds and 4,800 targets have passed curator review.

**Access.** Web search by target, compound, structural similarity or substructure; a RESTful API under /rwd/servlet/; and free bulk downloads as SDF, TSV and an Oracle/MySQL dump from the Downloads page. No account required.

**Caveats.** Complements ChEMBL rather than duplicating it - BindingDB pulls in US patent and PDB-derived affinities that ChEMBL does not curate, and cross-links to both. Affinities come from heterogeneous assays; IC50 values in particular are not comparable across papers without the assay conditions. Data is free for use with attribution but check the current terms before redistributing a derived database.

### [CAS Common Chemistry](https://commonchemistry.cas.org/)

`Free` · beginner 5/5 · authoritative CAS Registry Number lookup

CAS's open resource giving verified CAS Registry Numbers, systematic and common names, synonyms, structures, InChI/SMILES and basic properties for about 500,000 commonly encountered and regulated substances - the only free, authoritative source for CAS RNs, which are otherwise behind SciFinder.

**Access.** Web search by name, CAS RN, SMILES or InChI, plus a documented public API at https://commonchemistry.cas.org/api/search?q=aspirin and /api/detail?cas_rn=50-78-2 - no key needed.

**Caveats.** Licensed CC BY-NC 4.0, so commercial reuse is not covered - a real constraint if you are building a product. 500,000 substances is a curated slice; CAS's full registry of 165+ million substances stays behind paid CAS products, so uncommon compounds simply will not be there. PubChem is broader but its CAS numbers are depositor-supplied and less reliable, which is exactly why this entry matters.

### [CCDC Access Structures](https://www.ccdc.cam.ac.uk/structures/)

`Free` · beginner 4/5 · crystal structure retrieval

Free CCDC and FIZ Karlsruhe service to look up and download individual deposited structures by identifier, compound name, DOI, author, unit cell or formula. Searches the entire published collection, the Cambridge Structural Database, the Inorganic Crystal Structure Database and a curated teaching subset.

**Access.** Web interface at ccdc.cam.ac.uk/structures - search by CCDC number or DOI, then download the CIF. No account needed for single-structure retrieval.

**Caveats.** Deliberately a one-structure-at-a-time service. Systematic searching, geometry mining, ConQuest, WebCSD's advanced modes and the CSD Python API all sit behind a paid CSD-Core or ICSD licence, so a large-scale statistical study of the CSD is NOT free this way. See the CCDC FAIRE entry for a route to a free licence.

### [ChEMBL](https://www.ebi.ac.uk/chembl/)

`Free` · beginner 4/5 · bioactivity database

EMBL-EBI's manually curated bioactivity database. Release ChEMBL_37 (2026-05-01) contains 2,921,148 distinct compounds, 24,527,044 activity measurements, 18,552 targets and 101,100 curated publications (figures read from the live ChEMBL status endpoint on 2026-08-28).

**Access.** `pip install chembl-webresource-client`, then `from chembl_webresource_client.new_client import new_client; new_client.molecule.filter(pref_name='ASPIRIN')`. Full PostgreSQL/MySQL/SQLite dumps and RDF are on the EBI FTP site; a SQLite dump runs fine on a laptop.

**Caveats.** CC BY-SA 3.0 - the ShareAlike clause propagates to derived databases, which matters if you plan to redistribute. Activity values are extracted from the literature and inherit the assay conditions of the source paper; check the assay description before pooling values across documents. Pin the release number in published analyses.

### [ChemSpider](https://www.chemspider.com)

`Free` · beginner 5/5 · chemical structure database

The Royal Society of Chemistry's aggregated structure database; the site describes itself as offering free text and structure search over more than 130 million structures from hundreds of data sources, with experimental and predicted properties, spectra, identifiers and supplier links.

**Access.** Free web search by name, synonym, trade name, CAS registry number, SMILES, InChI or formula, plus structure and substructure drawing; structures download as MOL files. Programmatic access is the compounds API on the RSC developer portal (developer.rsc.org) with a registered key.

**Caveats.** Web searching needs no account. The API is metered — the site's own service listing advertises free access at 1,000 requests per month with a registered key, above which it is a commercial arrangement — and there is no bulk dump of the database. Deposited records vary in quality and carry source-specific terms, and predicted properties (ACD/Labs) are clearly the weakest part.

### [Crystallography Open Database (COD)](https://www.crystallography.net/cod/)

`Free` · beginner 4/5 · crystal structures

Open collection of experimental crystal structures of organic, inorganic, metal-organic compounds and minerals (biopolymers excluded). 534,681 entries as of the latest deposition on 2026-08-25; everything is dedicated to the public domain under CC0.

**Access.** Web search, or REST-style JSON: https://www.crystallography.net/cod/result?format=json&text=quartz . Full mirror by `svn co svn://www.crystallography.net/cod` or rsync; also an OPTIMADE endpoint (534,832 structures on 2026-08-28).

**Caveats.** CC0 removes legal barriers but the project asks you to cite the original structure authors. A full checkout is tens of gigabytes; take the cif/ subdirectory or a mirror if bandwidth is limited. Coverage is broad but not exhaustive - it does not replace CSD or ICSD for systematic searching.

*Also listed under: physics.*

### [JARVIS (NIST)](https://jarvis.nist.gov/)

`Free (registration), email` · beginner 3/5 · materials datasets and ML benchmarks

NIST infrastructure combining DFT (JARVIS-DFT), force-field (JARVIS-FF), machine-learning (JARVIS-ML), quantum-computation and experimental datasets, with web apps and leaderboards for materials property prediction.

**Access.** `pip install jarvis-tools`, then `from jarvis.db.figshare import data; d = data('dft_3d')` pulls the dataset from Figshare without an account. A web query builder and an OPTIMADE endpoint also exist.

**Caveats.** The site now states that 'access to the database and web apps requires user credentials', though registration is free - so the browser route is gated even where the Python/Figshare route is not. Its OPTIMADE endpoint returned an unfiltered count of 0 on 2026-08-28, so prefer jarvis-tools.

### [MassBank (Europe)](https://massbank.eu/MassBank/)

`Free` · beginner 3/5 · mass spectra

Open repository of curated reference mass spectra contributed by academic and public-sector labs, released as versioned datasets. Release 2026.03 was published 2026-04-15 and added spectra from Eawag's CyanoMetDB, the Mass Spectrometry Society of Japan, Qingdao University and the Shim-MassBank project.

**Access.** Web search by spectrum, peak list, compound or precursor m/z; the entire record set is a plain-text Git repository at github.com/MassBank/MassBank-data with tagged releases you can clone and parse directly.

**Caveats.** Individual records carry contributor-specified licences, mostly CC BY or CC BY-NC - check per record before reuse, especially the NC ones. The web front end is a JavaScript app; for programmatic work take the GitHub repository rather than scraping the site.

### [MassBank of North America (MoNA)](https://mona.fiehnlab.ucdavis.edu/)

`Free` · beginner 4/5 · mass spectra aggregation

Fiehn Lab (UC Davis) aggregator of publicly available mass spectral libraries, holding 3,596,790 spectra (count from its own REST endpoint on 2026-08-28) drawn from MassBank, GNPS, HMDB, ReSpect and in-silico predicted collections.

**Access.** REST API without a key: https://mona.fiehnlab.ucdavis.edu/rest/spectra/count and the query endpoints under /rest/spectra; bulk downloads as MSP, JSON and SDF from the Downloads page.

**Caveats.** A large share of the spectra are predicted rather than experimental - filter on the metadata before treating MoNA as a ground-truth reference set. Because it aggregates other libraries, licences are heterogeneous and inherited from upstream sources.

### [Materials Project](https://next-gen.materialsproject.org/)

`Free (registration), api-key` · beginner 4/5 · computed materials properties

US DOE database of DFT-computed properties for inorganic crystals and molecules - formation energies, band structures, elastic tensors, phase diagrams, XRD patterns. Database version 2026.04.13 went live 2026-06-08 and added 74,052 new GNoME materials at the r2SCAN level (117k GNoME materials total); its OPTIMADE endpoint reports 154,387 structures.

**Access.** `pip install mp_api`, take a free key from your profile dashboard after login, then `from mp_api.client import MPRester; with MPRester(key) as mpr: mpr.materials.summary.search(elements=['Li','Fe','O'])`. Bulk data also sits in the AWS Open Data buckets materialsproject-{raw,parsed,build} (us-east-1), readable without a key.

**Caveats.** Login is via GitHub/Google/Microsoft/Amazon or an email link; the key is free but per-account, and logging in a different way silently creates a second account. Data is under Materials Project terms, not a standard open licence. Since the 2026.04 release the storage layer moved to Delta tables on S3 and the docs warn the bucket organisation 'is still in flux and can change without notice' - pin workflows to the API client, not raw bucket paths.

*Also listed under: physics.*

### [MolSSI QCArchive](https://qcarchive.molssi.org/)

`Free` · beginner 3/5 · quantum chemistry reference data

MolSSI's distributed compute and database platform for quantum chemistry, hosting a public server of millions of completed single-point, optimisation, torsion-drive and reaction datasets computed with Psi4, PySCF, Q-Chem, Terachem and others - the reference data behind the Open Force Field parameterisations. Client package qcportal 0.70 (2026-08-17), BSD-3-Clause.

**Access.** `pip install qcportal`, then `from qcportal import PortalClient; c = PortalClient('https://api.qcarchive.molssi.org'); c.list_datasets()` - read access is anonymous. QCFractal lets you stand up your own server for a group's calculations.

**Caveats.** Anonymous read is fine; submitting compute to the public server needs credentials from MolSSI. The data model (datasets, records, specifications) takes some reading before queries feel natural - start from the QCPortal tutorials. Useful mainly if you need consistent, reproducible reference energies rather than experimental values; check the method and basis of each dataset before pooling.

### [NIST Chemistry WebBook (SRD 69)](https://webbook.nist.gov/chemistry/)

`Free` · beginner 5/5 · evaluated thermochemistry and spectra

NIST Standard Reference Database 69: critically evaluated thermochemical data for neutral species, ions and clusters, thermophysical fluid properties, gas- and condensed-phase IR, mass spectra with retention indices, UV/Vis spectra, vibrational and electronic energy levels, ion energetics, Henry's law constants and diatomic constants. The site's own footer reads 'Last update to the site: March, 2025'; DOI 10.18434/T4D303.

**Access.** Web interface only - search by name, formula, IUPAC identifier, CAS number or structure, then read tables and spectra per species.

**Caveats.** No API and no bulk download - a per-species lookup service, and scripted scraping runs against the terms. NIST states explicitly that it 'reserves the right to charge for access to this database in the future'. Name search covers only a subset of common names; fall back to formula or CAS search when a name lookup fails.

### [nmrshiftdb2](https://nmrshiftdb.nmr.uni-koeln.de/)

`Free` · beginner 4/5 · NMR spectra and prediction

Open web NMR database for organic structures: 271,817 structures, 70,030 measured spectra and 396,583 calculated spectra as of 2026-08-28, with peer-reviewed fully assigned datasets including raw data and peak lists. Also predicts 13C, 1H and other-nucleus shifts from a drawn structure.

**Access.** Web interface for search, 'Quick Check' verification of an assignment, and prediction. Database dumps and the open-source server code are downloadable from the project pages.

**Caveats.** An account is needed only to submit data, not to search or predict. The interface is dated and the docs warn about browser compatibility. Prediction is statistics-based over the deposited spectra, so accuracy degrades for chemistry poorly represented in the 271k structures. Now part of the NFDI4Chem infrastructure.

### [NOMAD](https://nomad-lab.eu/nomad-lab/)

`Free` · beginner 3/5 · computational materials archive

Open repository for raw and normalised computational materials data: 19,425,275 uploaded entries covering 4,346,100 distinct materials and 129.3 TB of files, parsed from more than 80 simulation-code output formats. Its OPTIMADE endpoint reports 18,836,371 structures.

**Access.** Web search and download, a documented REST API, and OPTIMADE at https://nomad-lab.eu/prod/v1/optimade/v1/structures . Upload your own calculations through the web UI or API; NOMAD Oasis is a self-hosted deployment for a group's own server.

**Caveats.** Browsing and download need no account; uploading and managing datasets do. Published data is CC BY 4.0. Value depends on the parser supporting your code - check the supported-format list before assuming your VASP/CP2K/FHI-aims output will normalise cleanly.

### [Open Quantum Materials Database (OQMD)](https://oqmd.org/)

`Free` · beginner 3/5 · DFT thermodynamics

Northwestern's database of DFT-calculated thermodynamic and structural properties, built largely on ICSD-derived and prototype-decorated structures, widely used for formation energies and convex-hull stability screening.

**Access.** Normally a REST API (https://oqmd.org/oqmdapi/formationenergy), an OPTIMADE endpoint, downloadable full database dumps, and the `qmpy` Python package from github.com/wolverton-research-group/qmpy.

**Caveats.** Honest status check: on 2026-08-28 oqmd.org, its REST API (/oqmdapi/formationenergy) and its OPTIMADE endpoint were all unreachable - HTTP 502 on first attempt and connection timeouts on re-check later the same day. The qmpy codebase was last pushed 2026-06-29 and is clearly maintained, so this reads as a sustained server outage rather than an abandoned project - but do not build a live-API dependency on OQMD right now; use the downloadable database dumps, or Materials Project and Alexandria for convex-hull screening in the meantime.

*Also listed under: physics.*

### [Open Reaction Database (ORD)](https://open-reaction-database.org/)

`Free` · beginner 3/5 · reaction data

Open-access chemical reaction database built for machine learning on reaction prediction and synthesis planning, using a strict protocol-buffer schema that captures reagents, conditions, workup and outcomes rather than just reactant-product SMILES. The Hugging Face mirror is tagged in the 1M-10M record size band and licensed CC BY-SA 4.0.

**Access.** `pip install ord-schema` for the reader and validator; data via `git clone https://github.com/open-reaction-database/ord-data` (Git LFS redirected to a Hugging Face CDN mirror) or `pip install huggingface_hub` plus the repo's download script for a subset. Interactive reaction editor and browser on the website.

**Caveats.** Coverage is uneven: large donated pharma and US-patent datasets dominate, so the reaction-class distribution is skewed and negative results are scarce. The protobuf schema has a real learning curve compared with a CSV of SMILES. The website is a JavaScript app and does not degrade without JS.

### [OpenKIM](https://openkim.org/)

`Free` · beginner 3/5 · interatomic potentials repository

NSF-funded curated repository of conventional and machine-learned interatomic potentials with a plug-and-play API, hosting roughly 1,531 potentials, 40 model drivers, 220,789 tests and 135,220 computed reference material properties, each model verified and benchmarked against known properties.

**Access.** No account needed to browse or download. In LAMMPS use `kim init <model-name> metal` and `kim interactions`; in Python `pip install kimpy ase` then the ASE KIM calculator. Also works from DL_POLY, GULP, QUIP and pyiron.

**Caveats.** The sweep's LAMMPS entry says 'the learning curve is in the potential, not the code' but points nowhere for potentials - this is where they live, with published property tests so you can see how a potential behaves for lattice constants, elastic constants and surface energies before you trust it. Individual models carry their own licences (mostly CDDL or LGPL) and their own citations. Verification tests tell you a potential is self-consistent, not that it is right for your system.

### [OPTIMADE](https://www.optimade.org/)

`Free` · beginner 3/5 · federated materials query API

Common REST API and filter language that lets one query run unchanged against many materials databases. The provider index listed 29 implementations on 2026-08-28, including Materials Project, COD, NOMAD, AFLOW, OQMD, JARVIS, Alexandria, Materials Cloud, 2DMatpedia, MPDS, odbx and TCOD.

**Access.** `pip install optimade` for client and validator tools, or query any endpoint directly, e.g. https://www.crystallography.net/cod/optimade/v1/structures?page_limit=5 . Machine-readable provider list at https://providers.optimade.org/providers.json .

**Caveats.** Implementations differ in completeness: some providers expose only the mandatory structure fields, provider-specific fields are prefixed and non-portable, and some endpoints return nothing useful. Verified live on 2026-08-28: Materials Project 154,387 structures, COD 534,832, NOMAD 18,836,371, Alexandria (PBE) 5,779,351; AFLOW and JARVIS returned 0 on an unfiltered count and OQMD was down.

### [PseudoDojo](https://www.pseudo-dojo.org/)

`Free` · beginner 3/5 · plane-wave pseudopotentials

Curated, systematically validated pseudopotential tables covering H through Og in norm-conserving scalar-relativistic and fully-relativistic ONCVPSP flavours (v0.3-v0.5), NC SR 3+, and PAW (JTH 1.0/1.1), each at low, normal and high accuracy hints with published delta-gauge and ghost-state test results.

**Access.** Web periodic table - choose flavour, format and accuracy, then download the whole table or a single element as psp8, UPF, PSML or XML for ABINIT, Quantum ESPRESSO, SIESTA or CP2K. Full HTML test reports per element show the validation data.

**Caveats.** The sweep has Basis Set Exchange for Gaussian basis sets but nothing for plane-wave pseudopotentials - this and Materials Cloud's SSSP fill that hole. Never mix pseudopotentials from different tables in one calculation. The recommended cutoff hints are a starting point, not a substitute for your own convergence test. Cite van Setten et al., Comput. Phys. Commun. 226, 39 (2018).

### [PubChem](https://pubchem.ncbi.nlm.nih.gov/)

`Free` · beginner 5/5 · small-molecule database

NIH/NCBI chemical database holding 124,598,147 compounds, 349,238,714 substance records and 1,980,801 bioassays, plus 83,167,183 linked patent documents (counts pulled from PubChem's own statistics endpoint on 2026-08-28). Aggregates depositions from chemical vendors, curation efforts, journals and government bodies.

**Access.** PUG REST, no key: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/property/MolecularFormula,MolecularWeight/JSON . Bulk SDF/XML via the FTP site; `pip install pubchempy` for a Python wrapper.

**Caveats.** PUG REST asks for no more than 5 requests/second and 400 requests/minute; heavy users should take the FTP dumps instead. Data quality varies with the depositor - vendor-supplied structures are not curated to the level of ChEMBL. Individual depositor records may carry their own terms.

### [SDBS - Spectral Database for Organic Compounds (AIST)](https://sdbs.db.aist.go.jp/)

`Free` · beginner 4/5 · multi-technique organic spectra

Free spectral database run by Japan's National Institute of Advanced Industrial Science and Technology, giving 1H and 13C NMR, EI mass spectra, ESR, IR and Raman spectra for organic compounds, each collection compiled by a named AIST team.

**Access.** Web interface: search by compound name, molecular formula, CAS number, or by spectral features such as chemical shift or m/z peaks, then view spectra per compound.

**Caveats.** Strictly a per-compound lookup tool - there is no API and no bulk download, and AIST's terms prohibit systematic downloading and redistribution. The interface is an old CGI frameset. Best used as an experimental cross-check on an assignment, not as a training corpus.

### [ZINC (files.docking.org)](https://files.docking.org/)

`Free` · beginner 3/5 · purchasable compound libraries for docking

UCSF Shoichet lab's free distribution of commercially available compounds prepared for virtual screening: ZINC-20/15 collections (2D SMILES, 3D multi-protomer/multi-conformer files for docking, building blocks, vendor catalogues, benchmark sets) and the billion-scale ZINC-22 tranches, all as static downloadable files.

**Access.** Browse and download directly from files.docking.org - no login for the static files. Interactive subset selection and per-molecule lookup run through cartblanche.docking.org and zinc.docking.org (the latter puts a captcha in front of automated clients).

**Caveats.** The file index was last updated 2024-08-13, so check tranche dates against your needs. The site states you may not redistribute major portions without written permission from John Irwin, and gives no guarantee of molecule quality or purchasability - vendor availability drifts. Full ZINC-22 is terabyte-scale; take a tranche by molecular weight and logP band rather than the whole thing. This is the standard source for a docking screen library and there is no free equivalent.

## Software

### [AiiDA](https://www.aiida.net/)

`Free` · beginner 2/5 · computational workflow manager

MIT-licensed Python workflow engine that submits, monitors and retries high-throughput calculations on Slurm, PBS, SGE, LSF and Torque clusters while recording every input, code and output in a queryable provenance graph. Over 100 community plugins including aiida-quantumespresso, aiida-vasp, aiida-cp2k and aiida-shell for arbitrary executables.

**Access.** `pip install aiida-core`, then `verdi presto` for a zero-config profile, `verdi computer setup` for your cluster, and submit WorkChains from Python. Plugin registry and tutorials at aiida.net.

**Caveats.** Pays for itself only above a few hundred calculations - for ten runs a shell script is faster to write. Real setup cost: a PostgreSQL/RabbitMQ service plus SSH access to your scheduler. It is the engine behind Materials Cloud's curated datasets, so an AiiDA archive is a directly publishable provenance record. Steep concept load (nodes, links, calcjobs, workchains) before the first useful result.

### [AiZynthFinder](https://github.com/MolecularAI/aizynthfinder)

`Free` · beginner 3/5 · retrosynthesis planning

AstraZeneca's open-source retrosynthetic planning tool: Monte Carlo tree search (plus retro* and depth-first options) over neural-network-ranked reaction templates, terminating on a stock file of purchasable building blocks. Public release v4.4.1 (2025-12-09), MIT licence.

**Access.** `pip install aizynthfinder`, then `download_public_data .` to fetch the USPTO-trained expansion policy and a ZINC stock file, and `aizynthcli --config config.yml --smiles "O=C(Nc1ccccc1)c1ccccc1"` or the Jupyter GUI.

**Caveats.** The sweep has the Open Reaction Database as reaction data but no synthesis-planning tool - this is the open counterpart to Reaxys and SciFinder retrosynthesis. The public models are trained on US patent reactions, so routes skew to patent-common chemistry and ignore stereo- and chemoselectivity subtleties; treat output as suggestions for a chemist to triage. Stock files determine what counts as 'solved' - swap in your own supplier catalogue for realistic routes.

### [ASE (Atomic Simulation Environment)](https://ase-lib.org/)

`Free` · beginner 4/5 · atomistic simulation framework

Python framework for setting up, running, visualising and analysing atomistic simulations, with a uniform Calculator interface to dozens of DFT and force-field codes (VASP, Quantum ESPRESSO, GPAW, CP2K, ORCA, LAMMPS, xtb, machine-learned potentials). Version 3.29.0, LGPL licensed.

**Access.** `pip install ase`, then `from ase.build import bulk; from ase.optimize import BFGS; a = bulk('Cu'); a.calc = SomeCalculator(); BFGS(a).run(fmax=0.01)`. Ships the `ase gui` viewer and an `ase` CLI.

**Caveats.** ASE only orchestrates - you still need the underlying code installed and, for plane-wave DFT, real compute. Some Calculator interfaces are far better maintained than others; check the calculator's own page before trusting defaults. Governance now sits with an ASE Steering Committee and development is on GitLab.

### [AutoDock Vina](https://vina.scripps.edu/)

`Free` · beginner 3/5 · molecular docking

Open-source protein-ligand docking program from Scripps, Apache-2.0 licensed, the most cited free docking engine. The maintained line is Vina 1.2.x (Eberhardt et al. 2021) with multi-ligand docking, macrocycle sampling and a Python API; AutoDock-GPU covers the GPU-accelerated AutoDock4 scoring function.

**Access.** Download binaries or source from github.com/ccsb-scripps/AutoDock-Vina releases (no registration), then `vina --receptor rec.pdbqt --ligand lig.pdbqt --center_x .. --size_x .. --out out.pdbqt`. Prepare PDBQT inputs with Meeko (`pip install meeko`) or AutoDockTools.

**Caveats.** The 2011 v1.1.2 material on vina.scripps.edu is legacy - take 1.2.x from GitHub. Scoring functions rank poses far better than they predict affinity; treat scores as an enrichment filter, not a binding constant. Input preparation (protonation, tautomers, flexible residues, box placement) is where most published docking errors originate. Cite Eberhardt et al., J. Chem. Inf. Model. 61, 3891 (2021) and Trott and Olson, J. Comput. Chem. 31, 455 (2010).

### [Avogadro 2](https://two.avogadro.cc/)

`Free` · beginner 5/5 · molecular editor and visualiser

Free and open-source cross-platform molecular editor and 3D visualiser: build and clean up structures, handle molecules, crystals, biomolecules and surfaces, generate input files for common quantum chemistry codes, and render publication figures.

**Access.** Download installers for Windows, macOS and Linux from two.avogadro.cc; plugin scripts add input generators for ORCA, Psi4, Gaussian, NWChem and others.

**Caveats.** The fastest path from 'I have a molecule in mind' to 'I have a sane starting geometry'. Avogadro 1 and Avogadro 2 are separate codebases with different feature sets and some Avogadro 1 features were never ported. Not a replacement for a proper conformer search - pair it with CREST.

### [CCDC Mercury](https://www.ccdc.cam.ac.uk/solutions/software/free-mercury/)

`Free, email` · beginner 5/5 · crystal structure visualisation

CCDC's free crystal structure visualiser and analyser: opens CIF, RES and mol2 files, builds packing diagrams and slices along planes, computes voids and intermolecular contacts, simulates powder XRD patterns from a structure, and exports publication-quality images.

**Access.** Download the free Mercury installer for Windows, macOS or Linux from the CCDC downloads page (an email/account step is used to issue the download), then open a CIF and use Packing/Slicing, Contacts and the Powder Pattern tool.

**Caveats.** Free Mercury is the viewer plus analysis tools; CSD searching, the Materials Module, full-interaction maps and the CSD Python API sit behind a paid CSD-Core licence - the same split as the Access Structures entry. The CCDC website renders client-side and its product pages did not resolve to a plain HTTP fetch on 2026-08-28, so confirm the current free-feature list in a browser before relying on a specific tool. Cite Macrae et al., J. Appl. Cryst. 53, 226 (2020).

### [checkCIF (IUCr)](https://checkcif.iucr.org/)

`Free` · beginner 4/5 · crystallographic data validation

IUCr's free validation service for crystal structure CIFs: checks CIF syntax, cell and geometry consistency, space-group symmetry, displacement parameters, structure factors and possible duplicate structures, returning alerts graded A (serious), B and C. Every crystallography-publishing journal expects a checkCIF report with the submission.

**Access.** Web form at checkcif.iucr.org - upload the CIF, optionally the .fcf structure factors, choose the alert level (A only, A+B, or A+B+C) and get an HTML or PDF report back. No account needed.

**Caveats.** Run it before submission, not after review. Alerts are diagnostics, not verdicts - a level A alert can be legitimate for genuinely unusual chemistry, but you must write a validation response explaining it. The service is a front end to PLATON, so the same checks run locally if you install PLATON. Structure-factor checks only fire if you upload the .fcf.

### [CP2K](https://www.cp2k.org/)

`Free` · beginner 2/5 · condensed-phase DFT and MD

GPL package for atomistic simulation of solid-state, liquid, molecular, periodic and biological systems using the Gaussian-and-plane-waves method, with linear-scaling DFT, ab initio molecular dynamics, metadynamics, QM/MM and post-Hartree-Fock methods. Version 2026.2 released 2026-07-15.

**Access.** `conda install -c conda-forge cp2k`, or precompiled binaries and containers from the download page; input is a structured text file. GPU (CUDA/HIP) builds are supported.

**Caveats.** The input format is deep and unforgiving for beginners - work from the official exercises and HOWTOs rather than from scratch. Strong on liquids and large periodic systems, less natural than Psi4 or ORCA for isolated-molecule property work.

### [DeepChem](https://deepchem.io/)

`Free` · beginner 3/5 · molecular machine learning

MIT-licensed Python library for deep learning in drug discovery, quantum chemistry, materials science and biology, bundling molecular featurisers (ECFP, graph convolutions, ConvMol, SMILES tokenisers), model implementations, and loaders for standard benchmark datasets including MoleculeNet. Last pushed 2026-08-20; ~7,000 GitHub stars.

**Access.** `pip install deepchem`, then `import deepchem as dc; tasks, datasets, transformers = dc.molnet.load_delaney(featurizer='GraphConv')` and fit one of the bundled models. Tutorials run in Colab with no local install.

**Caveats.** The fastest route from a SMILES column to a validated model, and its scaffold-split utilities push you toward honest evaluation - random splits inflate molecular ML scores badly. The library is broad and unevenly maintained: some models and featurisers are stale, and dependency pinning (TensorFlow vs PyTorch backends) is a recurring install headache. Pair it with RDKit for the chemistry.

### [FAIR Chemistry (fairchem)](https://fair-chem.github.io/)

`Free (registration), email` · beginner 3/5 · machine-learned interatomic potentials

Meta FAIR Chemistry's models and datasets for materials and quantum chemistry, including the UMA universal interatomic potentials, covering heterogeneous catalysis (the Open Catalyst OC20/OC22 line), inorganic materials, molecules and polymers, molecular crystals, and MOFs for direct air capture (OpenDAC).

**Access.** `pip install fairchem-core`; model weights are pulled from Hugging Face (free account plus licence acceptance), then used as an ASE calculator for relaxations and property prediction.

**Caveats.** Model weights sit behind Hugging Face licence acceptance rather than an unconditional download, and terms differ per model release - read them if your use is commercial. Inference on modest systems is fine on a CPU or a free-tier GPU; fine-tuning is not. The older opencatalystproject.org site is largely superseded by this one.

### [GROMACS](https://www.gromacs.org/)

`Free` · beginner 2/5 · biomolecular and soft-matter molecular dynamics

Free and open-source molecular dynamics engine, the standard code for solvated biomolecules, lipids, polymers and liquids, with heavily hand-tuned SIMD kernels and CUDA/SYCL GPU offload. Version 2026.3 released June 2026 (2026.2 on 2026-05-06); LGPL-2.1.

**Access.** `conda install -c conda-forge gromacs`, or build from source from gitlab.com/gromacs/gromacs; run `gmx pdb2gmx -f protein.pdb`, `gmx grompp -f md.mdp -c conf.gro -p topol.top -o md.tpr`, then `gmx mdrun -deffnm md`. `gmx` also ships ~100 analysis tools.

**Caveats.** The sweep covers LAMMPS (materials MD) but nothing for solvated molecular systems - this is that gap. Force field and water model choice dominates the result, not the code; GROMACS ships AMBER, CHARMM, OPLS-AA and GROMOS ports but you must supply small-molecule parameters yourself (CGenFF, GAFF/acpype, OpenFF). Conda builds are generic and noticeably slower than a source build tuned to your CPU. Justin Lemkul's tutorials are the de facto onboarding path.

### [GSAS-II](https://advancedphotonsource.github.io/GSAS-II-tutorials/)

`Free` · beginner 2/5 · powder diffraction and Rietveld refinement

Open-source Python crystallography package from Argonne National Laboratory for determination of crystal structures and diffraction-based materials characterisation: Rietveld and Le Bail refinement of x-ray and neutron powder data, single-crystal data, sequential and parametric refinements, small-angle scattering and image-plate integration. Documentation built from commit dcd09e, 2026-08-25.

**Access.** Install with the GSAS2MAIN installer (Windows, macOS, Linux), or via pixi or pip; run the GUI, or script refinements headlessly with the `GSASIIscriptable` module. Tutorials with data files are on the project site.

**Caveats.** The sweep has crystal-structure databases and DFT codes but nothing that turns a measured powder pattern into a refined structure - this is that tool, and it is free where TOPAS and HighScore are not. Rietveld refinement is unforgiving: background, peak-shape and preferred-orientation choices can produce a beautiful fit to a wrong model. Work through the official tutorials in order; the interface is functional rather than modern.

### [LAMMPS](https://www.lammps.org/)

`Free` · beginner 2/5 · classical molecular dynamics

GPL-2 classical molecular dynamics code focused on materials modelling, scaling from a single laptop core to large parallel machines, with a very large library of interatomic potentials including machine-learned potentials via the OpenKIM and ML-IAP interfaces. Current stable line stable_22Jul2025, update 5 released 2026-08-08.

**Access.** `conda install -c conda-forge lammps` or build from source; run `lmp -in in.script`. A Python module and the LAMMPS-GUI are available; user support lives on matsci.org.

**Caveats.** The learning curve is in the potential, not the code - a run completes happily with a physically wrong force field. Check a potential's published validation range before trusting results outside it. GPU acceleration requires the right package build.

*Also listed under: physics.*

### [MACE](https://github.com/ACEsuit/mace)

`Free` · beginner 4/5 · machine-learned interatomic potentials

Reference implementation of higher-order equivariant message-passing interatomic potentials, plus the widely used foundation models: MACE-MP-0 (89 elements, trained on ~1.6M Materials Project bulk structures, MIT licence) for inorganic materials and MACE-OFF (10 organic elements) for molecules, crystals and liquids.

**Access.** `pip install mace-torch`, then `from mace.calculators import mace_mp; atoms.calc = mace_mp(model='medium', device='cuda')` and drive it with any ASE optimiser or MD engine. Weights download automatically from the mace-foundations releases; `mace_run_train` fine-tunes on your own data.

**Caveats.** Complements the fairchem/UMA entry, and unlike UMA the MACE-MP-0 weights are MIT and need no Hugging Face licence acceptance - the practical default for someone who wants DFT-quality forces on a laptop GPU today. MACE-OFF is released under an Academic Software Licence, so commercial use differs from MACE-MP. Foundation models are trained on PBE-level data and inherit its errors; they extrapolate badly to chemistry absent from training (unusual oxidation states, charged defects, reactive transition states).

### [MDAnalysis](https://www.mdanalysis.org/)

`Free` · beginner 4/5 · trajectory analysis library

Python library that reads, writes and analyses MD trajectories in a common object model across GROMACS, AMBER, NAMD, CHARMM, LAMMPS, DL_POLY and PDB formats, exposing coordinates as NumPy arrays with a text atom-selection language. Release package-2.10.0 (2025-10-17), LGPLv3+ (some parts LGPLv2.1+); NumFOCUS-sponsored.

**Access.** `pip install MDAnalysis`, then `import MDAnalysis as mda; u = mda.Universe('topol.tpr','traj.xtc'); u.select_atoms('protein and name CA').positions`. Analysis modules cover RDF, RMSD/RMSF, hydrogen bonds, contacts and density.

**Caveats.** Frame-by-frame iteration is pure Python and slow on multi-microsecond trajectories - use the parallel backends or MDTraj/`gmx` tools for heavy reductions. Topology readers vary in what metadata they recover, so charges or bonds present in one format may be absent in another. Pin the version: selection and analysis APIs have changed across 1.x to 2.x.

### [Olex2](https://www.olexsys.org/olex2/)

`Free` · beginner 4/5 · small-molecule crystal structure solution and refinement

Integrated environment for small-molecule crystallography - structure solution, least-squares refinement, disorder and restraint handling, and publication CIF/report generation - wrapping SHELXT/SHELXL, olex2.refine and other engines behind one GUI. Official release version 1.5, for Windows, macOS and Linux.

**Access.** Download the installer from olexsys.org (Windows, macOS, Linux) and open your .hkl/.ins or CIF; solve with SHELXT, refine with SHELXL or olex2.refine, then export the CIF straight into checkCIF.

**Caveats.** OlexSys state Olex2 is 'completely free for anyone - industry, academia or students. No catch, no licence fees.' The bundled SHELX binaries carry their own licence terms from the SHELX distributor - academic use is free but registration at shelx.uni-goettingen.de is expected. The sweep listed crystal-structure databases but no refinement software; this plus checkCIF is the working half of that pipeline. It will happily refine a chemically nonsensical model - the software does not replace crystallographic judgement.

### [Open Babel](https://openbabel.org/)

`Free` · beginner 4/5 · file format conversion

Chemical file-format translator and toolbox reading and writing over 110 formats, with SMARTS filtering, 3D coordinate generation, force-field optimisation, conformer search and descriptor calculation. Latest release openbabel-3-2-1 (2026-07-11), GPL licensed.

**Access.** CLI: `obabel input.sdf -O output.xyz --gen3d`; Python bindings via `pip install openbabel-wheel` or conda; C++ API for embedding.

**Caveats.** Format breadth is its strength; perception of aromaticity, bond orders and protonation states is its weakness, and round-tripping through Open Babel can silently change a molecule. Use RDKit for serious cheminformatics and reach for Open Babel when RDKit cannot read the format.

### [OpenMM](https://openmm.org/)

`Free` · beginner 3/5 · GPU molecular dynamics library

MIT/LGPL molecular simulation toolkit driven from Python rather than input files, with custom force expressions evaluated on GPU, and hooks for ML/MM hybrid potentials. Version 8.6.0 released 2026-08-19, adding ReplicaExchangeSampler and ExpandedEnsembleSampler for multistate free-energy work.

**Access.** `conda install -c conda-forge openmm`, then `from openmm.app import *; sim = Simulation(topology, system, integrator); sim.step(10000)`. `python -m openmm.testInstallation` checks which GPU platforms are live.

**Caveats.** The natural host for machine-learned potentials in MD (openmm-torch, openmm-ml) and for alchemical free-energy protocols, which is why it sits alongside rather than under GROMACS. CustomForce expressions are powerful and easy to get subtly wrong - validate energies against a reference implementation. A single consumer GPU gets you real throughput; CPU-only runs are slow.

### [ORCA](https://www.faccts.de/orca/)

`Free (registration), email` · beginner 3/5 · quantum chemistry (molecular)

Widely used quantum chemistry package from the Neese group covering semiempirical methods through DFT to DLPNO-CCSD(T), with strong molecular-property and spectroscopy support (EPR, NMR, MCD, VCD), NEB-TS transition-state search, native MD and QM/MM. FACCTs reports more than 100,000 registered academic users; ORCA 6.1.0 was released 2025-06-17.

**Access.** Register on the ORCA Forum at orcaforum.kofo.mpg.de and download precompiled binaries for Linux, macOS and Windows; run from a plain-text input file. Drivable from ASE, Avogadro or the Python OPI interface.

**Caveats.** Free for academic and personal use - it is NOT open source, ships as binaries, and commercial or industrial use requires a paid FACCTs licence. FACCTs state on faccts.de/orca that 'ORCA is and will remain free for academic and personal use' (checked 2026-08-28), so a personal, non-commercial user without an affiliation is covered; read the current EULA before any commercially adjacent use. Support is the community forum, not a helpdesk.

### [Psi4](https://psicode.org/)

`Free` · beginner 3/5 · quantum chemistry (molecular)

Open-source ab initio molecular quantum chemistry package covering HF, DFT, MP2, SAPT and coupled cluster, with density fitting and multi-core parallelism, and a C++ core loadable as a Python module. Version 1.11 released 2026-06-30 under LGPL-3.

**Access.** `conda install -c conda-forge psi4`, then either a plain text input file (`psi4 input.dat`) or the Python API: `import psi4; psi4.geometry('...'); psi4.energy('scf/cc-pVDZ')`.

**Caveats.** Genuinely free software under LGPL-3, unlike ORCA - important if you are unaffiliated or want to redistribute. Conda is by far the smoothest install; building from source is painful. Correlated methods beyond roughly 30 heavy atoms will exceed a typical laptop's memory.

### [pymatgen](https://pymatgen.org/)

`Free` · beginner 3/5 · materials analysis library

Python Materials Genomics: structure and molecule objects, symmetry analysis, phase diagrams, Pourbaix and Ellingham diagrams, electronic-structure analysis, diffraction pattern simulation, and input/output for VASP, Quantum ESPRESSO, ABINIT, CP2K, LAMMPS and Gaussian. Version 2026.5.4, MIT licensed.

**Access.** `pip install pymatgen`, then `from pymatgen.core import Structure; s = Structure.from_file('POSCAR')`. It is also the analysis layer beneath the Materials Project API client.

**Caveats.** The API surface is large and moves quickly - modules get relocated between releases, so pin a version. Some functionality (energy corrections, compatibility schemes) assumes Materials Project calculation settings and gives misleading results on calculations run with different parameters.

*Also listed under: physics.*

### [PySCF](https://pyscf.org/)

`Free` · beginner 3/5 · quantum chemistry in Python

Apache-2.0 Python electronic-structure library covering HF, DFT, MP2, CCSD(T), CASSCF/CASCI, DMRG interfaces and periodic (Gamma-point and k-point) calculations, designed to be used and extended as ordinary Python rather than driven by input files. Version 2.14.0 released 2026-07-18.

**Access.** `pip install pyscf`, then `from pyscf import gto, scf; mol = gto.M(atom='H 0 0 0; F 0 0 0.917', basis='cc-pvdz'); scf.RHF(mol).kernel()`.

**Caveats.** The most method-development-friendly quantum chemistry package here: intermediates are NumPy arrays you can inspect and modify. That flexibility is also the risk - it is easy to write a calculation that runs and is wrong. Less black-box-safe for routine production chemistry than ORCA or Psi4.

### [Quantum ESPRESSO](https://www.quantum-espresso.org/)

`Free` · beginner 2/5 · plane-wave DFT

GPL suite for electronic-structure calculations and materials modelling with plane waves and pseudopotentials: ground-state DFT, structural relaxation, phonons via DFPT, nudged elastic band, spectroscopies and time-dependent DFT.

**Access.** Source from the QEF GitLab/GitHub repositories (`git clone`, `./configure && make all`), or `conda install -c conda-forge qe`. A free input generator and standard k-point paths (SeeK-path) are hosted on Materials Cloud.

**Caveats.** The official website's download page requires creating an account; the Git repositories do not, so use those for registration-free access. Plane-wave DFT is the genuinely compute-hungry item here - small unit cells run on a laptop, anything with a supercell needs an HPC allocation (see the EuroHPC and ACCESS entries). Cutoff and k-point convergence testing is on you.

*Also listed under: physics.*

### [RDKit](https://www.rdkit.org/)

`Free` · beginner 4/5 · cheminformatics toolkit

The default open-source cheminformatics toolkit: substructure and SMARTS matching, fingerprints, descriptors, conformer generation, 2D depiction, reaction handling, scaffold analysis and ML featurisation, with a C++ core and Python API. Release 2026_03_6 was cut 2026-08-28 under BSD-3-Clause.

**Access.** `pip install rdkit` (or `conda install -c conda-forge rdkit`), then `from rdkit import Chem; m = Chem.MolFromSmiles('CC(=O)Oc1ccccc1C(=O)O')`. Also has KNIME nodes and a PostgreSQL cartridge.

**Caveats.** Runs comfortably on a laptop. The API is broad and the official docs assume some cheminformatics vocabulary - the RDKit Cookbook and Greg Landrum's blog hold most practical recipes. Descriptor and fingerprint defaults do change between releases, so pin the version in reproducible work.

### [SwissADME](https://www.swissadme.ch/)

`Free` · beginner 5/5 · ADME and drug-likeness web tool

Free web tool from the Molecular Modelling Group of the University of Lausanne and the SIB Swiss Institute of Bioinformatics that computes physicochemical descriptors, lipophilicity (five logP models), water solubility, pharmacokinetics (GI absorption, BBB permeation, P-gp substrate, CYP inhibition), drug-likeness filters (Lipinski, Ghose, Veber, Egan, Muegge) and medicinal-chemistry alerts (PAINS, Brenk) from SMILES.

**Access.** Paste a list of SMILES into the web form at swissadme.ch and read the BOILED-Egg plot and per-molecule table; results download as CSV. No account needed.

**Caveats.** Predictions come from QSAR models trained on drug-like chemical space - they degrade sharply for inorganics, organometallics, very large molecules and unusual scaffolds, and they are a triage filter, not experimental data. Batch submissions are limited in practice by the browser form; there is no documented public API. Free for academic and commercial users; cite Daina, Michielin and Zoete, Sci. Rep. 7, 42717 (2017).

### [VESTA](https://jp-minerals.org/vesta/en/)

`Free` · beginner 4/5 · crystal structure visualisation

3D visualisation program for structural models, volumetric data (electron and nuclear densities, ELF, potentials) and crystal morphologies, with lattice transformations, superlattice and sublattice construction, arithmetic between volumetric files, and publication-quality rendering.

**Access.** Download binaries for Windows, macOS and Linux from jp-minerals.org; opens CIF, VASP CHGCAR/POSCAR, Gaussian cube, XSF and many other formats directly.

**Caveats.** Free of charge but NOT open source - binaries only, no source distribution, and redistribution is restricted. It is the de facto standard for crystal-structure figures in the materials literature. Cite Momma and Izumi, J. Appl. Cryst. 44, 1272 (2011).

### [xtb and CREST](https://xtb-docs.readthedocs.io/)

`Free` · beginner 4/5 · semiempirical tight binding

Grimme group's extended tight-binding package: GFN0/GFN1/GFN2-xTB and the GFN-FF force field deliver geometries, frequencies, implicit solvation and molecular dynamics for systems of hundreds to thousands of atoms in seconds to minutes on a laptop. CREST adds metadynamics-driven conformer and tautomer ensemble generation. Latest tagged release v6.7.1 (2024-07-23), LGPL-3.

**Access.** `conda install -c conda-forge xtb crest`, then `xtb mol.xyz --opt --gfn 2 --alpb water` or `crest mol.xyz --gfn2`. Python bindings and an ASE calculator are available.

**Caveats.** The best value-for-compute tool in this catalogue for someone without a cluster - but it is semiempirical, so absolute energies are not comparable to DFT and reaction energies can be badly wrong for unusual bonding. Use it to pre-screen conformers, then refine the survivors with DFT.

## Literature

### [arXiv (cond-mat and physics.chem-ph)](https://arxiv.org/list/cond-mat.mtrl-sci/recent)

`Free` · beginner 5/5 · preprint server

The preprint server where most materials science and physical chemistry work appears first: cond-mat.mtrl-sci alone listed 50 new submissions for 2026-08-28. Relevant categories are cond-mat.mtrl-sci, cond-mat.soft, physics.chem-ph and physics.comp-ph; all full texts are free with no account.

**Access.** Browse or search on arxiv.org; programmatic access via the arXiv API (http://export.arxiv.org/api/query?search_query=cat:cond-mat.mtrl-sci) or the full-text bulk data on AWS S3 (requester-pays). `pip install arxiv` wraps the API.

**Caveats.** ChemRxiv covers synthetic and molecular chemistry; arXiv covers the computational, materials and physical-chemistry half, and the sweep had no entry for it. Posting needs an account and, for a first submission in a category, endorsement by an established author. No peer review - screening only. The API returns at most 2,000 results per request and asks for a 3-second delay between calls.

### [ChemRxiv](https://chemrxiv.org/)

`Free` · beginner 5/5 · preprint server

The chemistry preprint server, co-owned by the ACS, RSC, Chinese Chemical Society, German Chemical Society and Chemical Society of Japan. Crossref lists 55,230 records under its 10.26434 DOI prefix (counted 2026-08-28), roughly 8,600 of them posted in 2026.

**Access.** Free full-text reading and download on the web; a public REST API under /engage/chemrxiv/public-api/v1/items for programmatic search. Posting a preprint is free after creating an account.

**Caveats.** Reading needs no account; posting does. Submissions are screened, not peer reviewed. The site sits behind Cloudflare, so scripted access from a plain HTTP client is frequently challenged - use a browser or a proper client. Check your target journal's preprint policy first; most chemistry journals accept ChemRxiv preprints, but not all.

### [Directory of Open Access Journals (DOAJ)](https://doaj.org/)

`Free` · beginner 4/5 · journal index

Curated, community-vetted index of open-access journals with per-journal metadata on article processing charges, licensing, peer-review model and archiving - the practical way to find diamond (no-APC) chemistry journals instead of guessing from publisher marketing.

**Access.** Web search with an APC filter, or the free API: https://doaj.org/api/search/journals/%22Chemical%20Science%22 returns a per-journal apc object with has_apc true or false. Full metadata dumps are downloadable.

**Caveats.** APC data is publisher-reported and can lag actual policy - confirm on the journal's own author page before submitting. DOAJ inclusion is a signal about transparency, not about scientific standards; judge the editorial board and published content too.

### [Europe PMC](https://europepmc.org/)

`Free` · beginner 5/5 · life-science and chemistry literature search

EMBL-EBI-hosted free literature database indexing abstracts and open-access full text from PubMed, PubMed Central, Agricola, patents, preprints and theses, with text-mined chemical, gene and disease annotations. A single search term returned 1,771,122 hits on 2026-08-28; full text is searchable, not just abstracts.

**Access.** REST API with no key: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22ionic%20liquid%22&format=json&pageSize=25 . Also an Annotations API for mined chemical entities, an OAI-PMH service and bulk open-access full-text downloads by FTP.

**Caveats.** Stronger than OpenAlex for full-text search and for chemistry-in-biology literature; weaker for pure materials and physical chemistry, where arXiv and OpenAlex cover more. Only the open-access subset is full-text searchable and downloadable - abstracts only for the rest. Rate limits are informal; keep bulk requests polite and use the FTP dumps for text mining.

### [OpenAlex](https://openalex.org/)

`Free` · beginner 4/5 · open bibliographic database

Free and open index of scholarly works, authors, institutions, sources and topics from OurResearch, containing 322,147,582 works of which 7,816,777 are classified in the Chemistry field (counts from the OpenAlex API on 2026-08-28), with open-access status and citation links.

**Access.** REST API with no key; add your email for the polite pool: https://api.openalex.org/works?filter=primary_topic.field.id:fields/25,is_oa:true&mailto=you@example.org . Full monthly snapshots download from S3; `pip install pyalex` wraps the API.

**Caveats.** The free tier is generous (100,000 calls/day in the polite pool) but a paid Premium tier exists for higher throughput and faster snapshots. Topic classification is automated and imperfect at sub-field level, and author disambiguation still merges and splits some names. Abstracts are stored as inverted indexes, not plain text.

### [Organic Syntheses](https://www.orgsyn.org)

`Free` · beginner 5/5 · independently checked synthetic procedures

Free full text of every Organic Syntheses preparation since 1921: 103 annual volumes (through Volume 103, 2026) plus 12 collective volumes. Every procedure and its characterisation data are peer reviewed and reproduced in the laboratory of a member of the Board of Editors before publication, and from 2026 the checkers are credited as coauthors.

**Access.** Search by structure, reaction type, reagent, author or volume at orgsyn.org; each preparation reads as HTML and downloads as a PDF with no account or subscription.

**Caveats.** Published by Organic Syntheses, Inc., a non-profit; text stays copyrighted, so it is free to read and work from but not to redistribute wholesale. Coverage is deliberately narrow — only submitted, checked procedures — so treat it as a reliability filter for known preparations, not a comprehensive reaction database.

### [Research4Life](https://www.research4life.org/)

`Free tier, credentialing` · beginner 2/5 · subscription journal access for low-income countries

Public-private partnership of UN agencies (WHO, FAO, UNEP, WIPO, ILO), Cornell and Yale universities and 200+ publishers giving institutions in eligible low- and middle-income countries free or low-cost access to subscription journals, books and databases through five programmes: Hinari (health), AGORA (agriculture), OARE (environment), ARDI (innovation and technology, the one that carries most chemistry and materials titles) and GOALI (law).

**Access.** Institutional, not individual: a university, research institute, government office, hospital or national library in an eligible country registers, and staff and students then log in through the Research4Life portal. Registration and eligibility checking are done on research4life.org.

**Caveats.** Honest status check: research4life.org, its eligibility page and portal.research4life.org all returned HTTP 403 to automated fetches on 2026-08-28, so the current country lists, resource counts and fees could NOT be verified here - treat the URL as an entry point and confirm in a browser. Structurally, Group A countries get free access and Group B countries pay a modest annual institutional fee; individuals and institutions in high-income countries are not eligible, and unaffiliated researchers cannot register. Where it applies it is the single largest legal fix for paywalled chemistry literature, which is why it belongs in this catalogue despite the verification gap.

### [The Wikipedia Library](https://wikipedialibrary.wmflabs.org/)

`Free (registration), credentialing` · beginner 3/5 · subscription database access

Gives active Wikipedia editors free accounts on more than 100 subscription-only research databases with content in 32 languages, organised by subject including Physical Sciences and Technology. The pool includes major science and chemistry publishers.

**Access.** Log in with your Wikipedia account; some collections unlock instantly if you meet the criteria, others are applied for individually through the Library Card platform.

**Caveats.** Automatic access requires 500+ edits, 6+ months of editing, 10+ edits in the last 30 days and no active blocks - a route you must build toward, not one you can use today. Access is granted for improving Wikipedia; bulk downloading and systematic text mining breach the publisher terms. Which chemistry publishers are in the pool changes over time.

### [Unpaywall](https://unpaywall.org/)

`Free, email` · beginner 5/5 · open-access full text finder

OurResearch service that resolves a DOI to a legal free full-text copy where one exists, drawing on publisher OA versions and repository deposits. Available as a browser extension that adds a green tab on paywalled article pages, and as a DOI-keyed API.

**Access.** Install the Chrome or Firefox extension, or call the API: https://api.unpaywall.org/v2/10.1038/nature12373?email=you@example.org returns is_oa, oa_status and best_oa_location.

**Caveats.** Legal routes only - it finds author manuscripts and publisher OA copies, never pirated PDFs, which is exactly why it belongs here. The API needs an email parameter but no key. Some fields in current responses are marked 'deprecated' as OurResearch consolidates the data into OpenAlex; for bulk work use the OpenAlex snapshots instead.

## Compute

### [ACCESS (NSF)](https://allocations.access-ci.org/)

`Free, application` · beginner 2/5 · national HPC allocations

The NSF-funded successor to XSEDE, allocating time on US national computing, GPU, large-memory and storage systems. Its own dashboard reported 628 projects awarded to 614 researchers at 231 institutions in the latest month across 18 contributing resources. The entry-level tier is approved quickly and requires no NSF award.

**Access.** Create an ACCESS ID via CILogon, then submit an allocation request - the smallest tier is a short form with rapid approval. Once granted you get scheduler access to systems running VASP, Quantum ESPRESSO, CP2K, LAMMPS and GROMACS.

**Caveats.** ACCESS states plainly that 'it costs you nothing (really!), and you don't need an NSF award' - but eligibility is tied to US institutions and US-based researchers, so it does not help an unaffiliated researcher outside the US. You are expected to report resulting publications, and larger tiers require a reviewed proposal.

### [EuroHPC JU access calls](https://eurohpc-ju.europa.eu/access-our-supercomputers/eurohpc-access-calls_en)

`Free, application` · beginner 2/5 · European HPC allocations

Continuously open calls for time on EuroHPC pre-exascale and petascale supercomputers, with tiers from Benchmark Access (small, fast-turnaround allocations for code testing and scaling) and Development Access through Regular Access to Extreme Scale Access for very large allocations.

**Access.** Submit a proposal through the EuroHPC peer-review portal for the tier you need. Benchmark and Development Access have light applications and short evaluation cycles; Regular and Extreme Scale run on cut-off dates.

**Caveats.** Open to researchers from academia, research institutes, public authorities and industry established or located in an EU Member State or a country associated with Horizon 2020 - eligibility is geographic, not means-tested, so it is a strong route for a European researcher at a poorly resourced institution and no route at all outside that area. Benchmark Access is the realistic starting point: prove your code scales before requesting a Regular allocation.

*Also listed under: physics.*

### [Google Colab (free tier)](https://colab.research.google.com/)

`Free tier, email` · beginner 5/5 · hosted notebooks with GPU

Hosted Jupyter notebooks with free CPU or GPU runtimes, pre-installed scientific Python, and one-line installs of RDKit, xtb, Psi4 and ASE - the standard way to run a cheminformatics or semiempirical workflow with no local hardware.

**Access.** Open colab.research.google.com with a Google account; `!pip install rdkit` or `!mamba install -c conda-forge xtb` in the first cell. Runtime > Change runtime type selects a GPU.

**Caveats.** Free-tier resources are not guaranteed and are dynamically adjusted; Colab explicitly prioritises users actively typing in a notebook, and free runtimes 'may be terminated at any time without warning'. SSH and remote-desktop access, running distributed-computing workers and using multiple accounts to dodge limits are all prohibited. Runtimes are ephemeral - push results out before the session dies. Not suitable for multi-hour plane-wave DFT.

### [IBM Quantum Open Plan](https://quantum.cloud.ibm.com/)

`Free tier, api-key` · beginner 3/5 · quantum hardware access

Free access to IBM's utility-scale quantum processors: up to 10 minutes of QPU time per 28-day rolling window, plus - as of 16 March 2026 - an opt-in additional 180 minutes spread over the following 12 months for active Open Plan users. Relevant to quantum chemistry work on VQE-style ground- and excited-state algorithms.

**Access.** Create a free account, take the 44-character API key from the Platform dashboard, then `pip install qiskit qiskit-ibm-runtime` and `QiskitRuntimeService.save_account(token=..., plans_preference="['open']")`. Qiskit Nature supplies the chemistry problem mappings.

**Caveats.** Open Plan instances can only be created in the us-east region. Ten minutes is a hard cap - develop against local simulators and spend hardware time only on final runs. Noise on current hardware means quantum chemistry results are demonstrations, not production numbers; do not present them as competitive with classical methods.

### [Kaggle Notebooks](https://www.kaggle.com/docs/notebooks)

`Free tier, email` · beginner 4/5 · hosted notebooks with GPU/TPU

Free hosted notebook environment with weekly-quota GPU and TPU accelerators, persistent attached datasets and a versioned notebook model - a practical alternative to Colab for training molecular ML models or running fairchem and DeepChem inference without local hardware.

**Access.** Create a free Kaggle account, start a notebook, and enable an accelerator in the notebook settings sidebar. Attach data from Kaggle Datasets or upload your own.

**Caveats.** Accelerator time is capped on a weekly quota and sessions have a maximum runtime; phone verification is required before GPUs unlock. Exact current quota figures could not be verified here because the docs page renders entirely client-side - the notebook settings panel shows your remaining quota live, so check there. Internet access inside notebooks must be explicitly enabled.

## Publishing

### [Beilstein Journal of Organic Chemistry](https://www.beilstein-journals.org/bjoc/)

`Free, email` · beginner 4/5 · diamond open-access journal

Peer-reviewed organic chemistry journal published by the non-profit Beilstein-Institut with no article processing charges and no subscription fees; DOAJ records it as has_apc false under a CC BY licence (checked 2026-08-28). Its sister title, the Beilstein Journal of Nanotechnology, runs the same model.

**Access.** Submit through the journal website; read and download all content free without an account. Thematic issues are a good entry route for early-career authors.

**Caveats.** The single most useful publishing route here for an unfunded organic chemist: genuinely free to publish and free to read, funded by the Beilstein-Institut endowment rather than by authors. Scope is strictly organic chemistry and nanotechnology respectively, and it will desk-reject out-of-scope work. Standard peer review applies - free does not mean easy.

### [CCDC structure deposition](https://www.ccdc.cam.ac.uk/deposit/)

`Free, email` · beginner 4/5 · crystal structure deposition

Free deposition service for small-molecule crystal structures. Depositing a CIF returns a CCDC number and a DOI, makes the structure retrievable by anyone through Access Structures, and satisfies the deposition requirement of essentially every crystallography-publishing journal.

**Access.** Upload the CIF, and optionally structure factors, through the CCDC deposit web form; structures can be held private until the associated paper publishes.

**Caveats.** Deposition is free even though searching the full CSD is not. Structures are validated in checkCIF style and problems are flagged back to you. Once released, the entry is permanent. Inorganic and extended structures generally go to ICSD or COD instead.

### [Chemical Science (RSC)](https://pubs.rsc.org/en/journals/journalissues/sc)

`Free, email` · beginner 3/5 · diamond open-access journal

The Royal Society of Chemistry's flagship general chemistry journal, published fully gold open access with no article processing charge - DOAJ records eISSN 2041-6539 as has_apc false, with the RSC covering costs.

**Access.** Submit through the RSC manuscript system; all articles are free to read on pubs.rsc.org with no subscription.

**Caveats.** Highly selective - it targets high-impact work across chemistry, so acceptance rates are low and it is not a general-purpose outlet. Verified via DOAJ on 2026-08-28; the RSC's own pages sit behind a bot challenge, so confirm the current waiver on the journal's author page before submitting. Other RSC journals do charge APCs; this waiver is specific to Chemical Science.

### [Chemotion Repository](https://www.chemotion-repository.net/)

`Free, email` · beginner 3/5 · chemistry data repository

Field-specific chemistry repository at KIT, part of the German NFDI4Chem infrastructure, for depositing samples, reactions and the analytical data behind them - mass spectrometry (mzML, mzXML, JCAMP-DX, vendor formats), NMR (Bruker, JCAMP-DX), IR, Raman, XRD, UV-Vis and cyclic voltammetry. Deposition is free and DOIs are assigned automatically.

**Access.** Register on the repository and submit through the web interface, or push directly from the Chemotion electronic lab notebook. Metadata is exposed via DataCite and OAI-PMH; content can be published as open access or registered access.

**Caveats.** This is where raw spectra belong when a journal only wants a PDF of the supporting information. Format support is oriented to synthetic and molecular chemistry - not the right home for large simulation trajectories. The web app requires JavaScript. Best used together with the Chemotion ELN rather than as a one-off upload target.

### [Journal of Open Source Software (JOSS)](https://joss.theoj.org/)

`Free, email` · beginner 4/5 · software paper, no APC

Developer-friendly open-access journal for research software packages with zero article processing charges and no subscription fees; 3,693 papers published as of 2026-08-28. Review happens openly in a GitHub issue and focuses on the software itself rather than a narrative manuscript.

**Access.** Write a short paper.md, open a submission at joss.theoj.org (log in with ORCID), and respond to reviewers in the public GitHub thread. Accepted papers get a DOI and are indexed.

**Caveats.** Your software must be open source under an OSI-approved licence, be substantial rather than a thin script, and have documentation and tests. JOSS recently updated its submission scope requirements - read the current version before starting. Gives a citable object for a chemistry tool that would otherwise go uncredited.

### [Living Journal of Computational Molecular Science (LiveCoMS)](https://livecomsjournal.org/)

`Free, email` · beginner 4/5 · diamond open-access, living documents

Community-run diamond open-access journal for computational molecular science with 'no charges for submissions or for readers', publishing best-practices guides, tutorials, perpetual reviews, software comparisons and lessons-learned articles that are updated over time. Volume 7, Issue 1 is current (2026); CC BY 4.0, published by the University of Colorado Boulder.

**Access.** Submit through the journal site; author instructions and templates at livecomsjournal.github.io. Reading requires nothing. It runs a dedicated student-reviewer category if you want review experience.

**Caveats.** Article types are unusual - the right home for a rigorous methods tutorial or best-practices guide, not for a primary research result. The 'living' model means committing to maintain the document. Small and community-funded, so turnaround depends on volunteer editors.

### [Materials Cloud](https://www.materialscloud.org/)

`Free, email` · beginner 4/5 · computational materials platform and archive

EPFL-hosted open platform for computational materials science with four layers: LEARN (lectures and tutorials), WORK (browser tools including a Quantum ESPRESSO input generator, SeeK-path k-point paths and the SSSP pseudopotential library), DISCOVER (curated datasets such as MC3D), and ARCHIVE, a moderated open repository that mints DOIs for research data.

**Access.** All tools are browser-based and free; the Archive accepts uploads after registration and exposes a REST API (https://archive.materialscloud.org/api/records) and an OPTIMADE endpoint.

**Caveats.** Archive deposits are moderated, so publication is not instant. The browser tools are the fastest legitimate way to generate a sane Quantum ESPRESSO input without installing anything. Services are hosted at CSCS and go down for scheduled maintenance. Cite Talirz et al., Sci. Data 7, 299 (2020) if you use the platform.

### [Zenodo](https://zenodo.org/)

`Free (registration), email` · beginner 5/5 · general-purpose data and software repository

Open repository built and operated by CERN and OpenAIRE, running on CERN's data centre, that mints a DOI for every upload within seconds and versions records. The default home for chemistry data that has no domain repository - simulation trajectories, analysis notebooks, raw instrument files, software snapshots.

**Access.** Register with an email, ORCID or GitHub account and upload through the web form, or use the REST API with a personal access token. GitHub integration archives a repository release automatically and returns a citable DOI.

**Caveats.** Default per-record limit is 50 GB (larger by request); it is not a substitute for NOMAD or Materials Cloud when a domain repository exists, because Zenodo does not parse or index your file contents. You choose the licence, so choose deliberately - CC BY or CC0 for data, an OSI licence for code. Records are permanent once published; only new versions, not deletions, are possible.

## Funding

### [CCDC FAIRE programme](https://www.ccdc.cam.ac.uk/community/ccdc-for-the-community/faire-grants/)

`Free, application` · beginner 2/5 · free software licence grants

The Frank H. Allen International Research and Education (FAIRE) programme awards free Cambridge Structural Database software licences to academic institutions in countries that cannot fund a commercial subscription, unlocking the searching and analysis capability that Access Structures deliberately withholds.

**Access.** Apply through the CCDC community pages; applications come from an institution or a named academic rather than from an individual hobbyist.

**Caveats.** The current eligible-country list, award terms and deadlines could not be verified - the CCDC site renders client-side and the FAIRE page body did not resolve on 2026-08-28. Treat the URL as an entry point and confirm terms with CCDC directly. Even so this is the most important single route here for a crystallographer at an institution that cannot afford a CSD subscription.

### [RSC Research Fund](https://www.rsc.org/prizes-funding/funding/find-funding/research-fund/)

`Free, application` · beginner 2/5 · small research grant

Royal Society of Chemistry grant of up to GBP 5,000 to start a new project, aimed explicitly at members 'with limited access to research funds', particularly those at less well-funded institutes, in developing countries, and early-career researchers.

**Access.** Apply through the RSC funding portal during an open round; you need Head of Department support and applications are limited to one per department.

**Caveats.** Two real gates: you must already hold paid RSC membership at Associate Member (AMRSC), Member (MRSC) or Fellow (FRSC) level before submitting - student, affiliate and partner-scientist grades are explicitly ineligible - and you must hold an independent research post, which rules out unaffiliated researchers. Applications were closed when checked on 2026-08-28; the fund runs on an annual cycle.

### [TWAS Research and Project Grants](https://twas.org/opportunities/research-grants)

`Free, application` · beginner 2/5 · grants for developing-country researchers

The World Academy of Sciences awards research grants to individual scientists and research groups in developing countries, specifically to buy specialised equipment and consumable supplies and to support MSc students - precisely the categories that block experimental chemistry at under-resourced institutions.

**Access.** Apply online through the TWAS opportunities portal, which filters open calls by country and programme. Applications are free to submit.

**Caveats.** Eligibility is by country and normally requires affiliation to a research institution in an eligible developing country - not open to unaffiliated researchers or to those in high-income countries. Individual programmes open and close on their own cycles, so check the Deadlines page rather than assuming a call is live. Grant sizes are modest and equipment-focused.

*Also listed under: earth.*

## Learning

### [LibreTexts Chemistry](https://chem.libretexts.org/)

`Free` · beginner 5/5 · open textbook library

The largest free chemistry textbook library, part of the LibreTexts non-profit OER platform, which reports over 3,000 textbooks and more than 1.5 million pages of open content across its libraries. The chemistry library spans general, organic, physical, analytical, inorganic and biological chemistry with worked problems and interactive elements.

**Access.** Read directly in a browser - no account, no paywall. Books can be remixed into a custom text and exported to PDF for offline use, which matters on a poor connection.

**Caveats.** Licensing varies per page, mostly CC BY-NC-SA and CC BY-SA - check the page footer before reuse. Quality is uneven because content comes from many instructors: the flagship general and organic texts are solid, some specialist corners are thin. The chemistry subdomain was intermittently unreachable from this machine on 2026-08-28.

### [MIT OpenCourseWare - Chemistry](https://ocw.mit.edu/search/?d=Chemistry)

`Free` · beginner 5/5 · university course materials

97 chemistry courses (count from the MIT Learn API on 2026-08-28) published with lecture notes, problem sets with solutions, exams and, for many courses, full video lectures - covering general, organic, physical and inorganic chemistry, thermodynamics, kinetics and quantum mechanics for chemists.

**Access.** Browse and download directly; most materials are also packaged for offline download. No registration, no enrolment, no deadlines.

**Caveats.** CC BY-NC-SA licensed. No instructor, no grading and no certificate - this is self-study. Course vintages vary widely and some are over a decade old, which matters more for methods courses than for thermodynamics.

### [MolSSI Education](https://education.molssi.org/)

`Free` · beginner 4/5 · computational chemistry software training

Free lesson materials from the NSF-funded Molecular Sciences Software Institute, taught in the Carpentries style: 'Python Data and Scripting for Computational Molecular Science' assumes no programming experience, and the Software Development Best Practices track covers environments, packaging, version control, testing and documentation with a hands-on Python example.

**Access.** Work through the lessons in a browser at your own pace; all materials, exercises and data files are downloadable. MolSSI also runs in-person and online workshops.

**Caveats.** This is the material the computational chemistry community itself points newcomers to. It teaches software practice using chemistry examples rather than teaching chemistry - pair it with a quantum chemistry text. Workshops are mostly US-located, but the written lessons are self-contained and work anywhere.

### [ORCA tutorials and manual](https://www.faccts.de/docs/orca/tutorials/)

`Free` · beginner 3/5 · quantum chemistry practice

The official ORCA tutorial set and manual: worked, copy-pasteable input files for geometry optimisation, frequencies and thermochemistry, transition-state search with NEB-TS, implicit and explicit solvation, DLPNO-CCSD(T) benchmarking, and calculation of spectroscopic properties including UV/Vis, NMR, EPR and VCD.

**Access.** Read online free at faccts.de/docs - no account needed for the documentation, even though downloading the ORCA binary requires forum registration.

**Caveats.** These tutorials are the de facto standard reference for practical quantum chemistry input choices and are worth reading even if you run Psi4 or PySCF instead. They assume you already know what a basis set and a functional are. The manual is very long - start from the tutorials.

### [TeachOpenCADD](https://projects.volkamerlab.org/teachopencadd/)

`Free` · beginner 4/5 · computer-aided drug design tutorials

Open teaching platform of executable 'talktorials' - Jupyter notebooks that teach a concept and implement it - covering compound data acquisition from ChEMBL and PubChem, molecular filtering, fingerprints and similarity, clustering, machine learning, structure-based docking and kinase-focused workflows. Documentation version 2026.4.1.

**Access.** The site states 'this website is free and open to all users and there is no login requirement'. Read online, or clone the repository and run the notebooks locally or in Colab with RDKit and the listed packages.

**Caveats.** Written by students for students, which makes it unusually approachable, but the depth is introductory and it will not substitute for a medicinal chemistry course. Several talktorials call live web services (ChEMBL, KLIFS, PubChem), so they need a connection and can break when an upstream API changes.

## Community

### [Chemistry Stack Exchange](https://chemistry.stackexchange.com/)

`Free` · beginner 5/5 · Q&A site

General chemistry Q&A with 47,521 questions and 55,127 answers from 187,744 registered users as of 2026-08-28, covering mechanism, spectroscopy interpretation, thermodynamics, laboratory technique and safety. The archive is often more valuable than posting - most standard questions are already answered.

**Access.** Read without an account; register free to ask and answer. Content is CC BY-SA and fully indexed by search engines.

**Caveats.** Homework-style questions are closed unless you show your reasoning, and moderation is strict about scope. For computational and materials questions, Matter Modeling Stack Exchange is the better venue. 9,200 questions remain unanswered, so specialist topics may get no response.

### [matsci.org (Materials Science Community Discourse)](https://matsci.org/)

`Free, email` · beginner 4/5 · code support forum

Discourse forum co-managed by the Materials Project and the OpenKIM project, hosting the official user-support categories for LAMMPS, Materials Project (including its new Arrow and data-lakehouse layer), pymatgen, GPUMD, icet and a range of other atomistic simulation codes.

**Access.** Read anonymously; register free with an email to post. Each code has its own category and developers answer in most of them.

**Caveats.** This is where the maintainers actually are for LAMMPS and Materials Project - a bug report or API question here is far more likely to be answered than the same question on a general Q&A site. Activity varies sharply by category and some smaller code sections are quiet.

### [Matter Modeling Stack Exchange](https://mattermodeling.stackexchange.com/)

`Free` · beginner 4/5 · Q&A site

Q&A site for atomistic and materials modelling with 5,179 questions, 4,965 answers and 15,160 registered users as of 2026-08-28. Method developers and code authors answer here, so questions about DFT functional choice, basis-set convergence, pseudopotentials, MD force fields and specific code errors get expert-level answers.

**Access.** Read without an account; register free (email or an existing Stack Exchange login) to ask, answer and vote. All content is CC BY-SA.

**Caveats.** Traffic is modest - 1,051 of the 5,179 questions are unanswered - so a niche question can sit for days. Questions that show your input file, the actual error and what you already tried get answered; 'which functional should I use' with no context does not. Read the site's scope and homework policies before posting.
