# Neuroscience & psychology

Part of [research-vault](../README.md). 60 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (16) · [Software](#software) (17) · [Literature](#literature) (7) · [Compute](#compute) (4) · [Publishing](#publishing) (4) · [Funding](#funding) (3) · [Learning](#learning) (6) · [Community](#community) (3)

## Data

### [ABIDE (Autism Brain Imaging Data Exchange) / INDI](https://fcon_1000.projects.nitrc.org/indi/abide/)

`Free` · beginner 3/5 · clinical resting-state fMRI

Aggregated resting-state fMRI, structural MRI and phenotypic data on autism contributed by more than 24 international laboratories across ABIDE I and ABIDE II, shared under the International Neuroimaging Data-sharing Initiative. The Preprocessed Connectomes Project additionally publishes ABIDE preprocessed with several pipelines and derivative connectivity matrices.

**Access.** Preprocessed derivatives download anonymously from AWS: `aws s3 ls --no-sign-request s3://fcp-indi/data/Projects/ABIDE_Initiative/`; raw imaging goes through a free NITRC/NITRC-IR account. The same fcon_1000/INDI umbrella hosts ADHD-200 and the 1000 Functional Connectomes releases.

**Caveats.** Site heterogeneity is the dominant nuisance variable — scanner, sequence and diagnostic criteria differ per site, so any analysis needs site as a covariate or harmonisation. Phenotypic coverage is patchy across sites, and some phenotypic fields are withheld. Licence is non-commercial with attribution.

### [Allen Brain Cell (ABC) Atlas](https://brain-map.org/atlases-and-data/bkp/abc-atlas)

`Free` · beginner 2/5 · single-cell and spatial transcriptomics

Whole-brain single-cell atlas combining scRNA-seq and MERFISH spatial transcriptomics: about 4 million mouse cells organised into 5,322 transcriptomic clusters (34 classes, 338 subclasses, 1,201 supertypes) and over 3 million human cells (31 superclusters, 461 clusters, 3,313 subclusters).

**Access.** Interactive viewer at knowledge.brain-map.org/abcatlas; programmatic access with the `abc_atlas_access` Python package (github.com/AllenInstitute/abc_atlas_access), which pulls the released matrices and cell-metadata tables directly from AWS S3.

**Caveats.** The web viewer is usable on any laptop, but working with the expression matrices locally means tens of GB and comfortable RAM; select a subclass or region first. Cell-type nomenclature changes between releases — pin the release version in your analysis.

### [Allen Brain Map](https://brain-map.org/)

`Free` · beginner 3/5 · reference atlases and mouse/human brain data

Allen Institute's open data portal: reference anatomical atlases for adult and developing mouse and human plus mouse spinal cord, mesoscale mouse connectivity, in situ gene expression and the Brain Observatory physiology surveys. The Institute reports 650 TB of high-resolution 3D imaging data and 700 billion gene expression data points.

**Access.** Web viewers per resource; RESTful API at api.brain-map.org; or `pip install allensdk` and use e.g. `MouseConnectivityCache`, `BrainObservatoryCache`, `CellTypesCache` — the SDK downloads and caches what you request.

**Caveats.** Citation policy and terms of use apply; check them before redistributing derived data. The AllenSDK lags behind newer Allen products (the ABC Atlas has its own package) and pins older scientific-Python versions, so install it in its own environment. Caches grow to tens of GB quickly.

### [CRCNS.org](https://crcns.org/)

`Free (registration), email` · beginner 3/5 · systems-neuroscience recordings

Long-running repository of curated experimental datasets for computational analysis — physiological recordings from sensory, motor and memory systems plus eye-movement data — many of them classic recordings that predate NWB and are hard to find elsewhere. Still actively maintained: bulk downloading via AWS was added in June 2026.

**Access.** Free account, then per-dataset terms acceptance and download from the site or the new AWS-hosted bulk endpoints; most datasets ship with a documentation PDF describing file formats.

**Caveats.** Each dataset has its own bespoke format and its own citation/terms requirement — there is no unified API. Documentation quality varies with the contributing lab and some older sets have effectively no maintainer to answer questions.

### [DANDI Archive](https://dandiarchive.org/)

`Free` · beginner 3/5 · cellular neurophysiology archive

The BRAIN Initiative archive for neurophysiology: electrophysiology, optical physiology, behavioural time series and immunostaining images, standardised as NWB and BIDS microscopy. It reports 1,162 dandisets and 2.2 PB of data across 2,185 users.

**Access.** `pip install dandi` then `dandi download DANDI:000006`; or stream single NWB files over S3 without downloading using `pynwb` + `fsspec`/`remfile`; web browse and a Neurosift viewer at dandiarchive.org.

**Caveats.** Public dandisets download without an account; uploading and embargoed sets need a GitHub login. Individual dandisets run to hundreds of GB or TB — streaming, not downloading, is the realistic route on a laptop. NWB files reward learning the schema first; expect a day of overhead.

### [Human Connectome Project (ConnectomeDB)](https://www.humanconnectome.org/study/hcp-young-adult/data-releases)

`Free (registration), email` · beginner 2/5 · high-quality human MRI

The HCP Young Adult 1200-subject release: behavioural and 3T MRI data from 1,206 healthy young adults scanned 2012-2015, including 1,113 subjects with structural 3T imaging, 184 with 7T multimodal data and 46 retest subjects. Minimally preprocessed derivatives and diffusion bedpostX outputs are distributed alongside the raw data.

**Access.** Register at db.humanconnectome.org, accept the HCP Open Access Data Use Terms, then download packages in the browser or generate AWS credentials from ConnectomeDB and pull from S3 with the AWS CLI.

**Caveats.** Open Access data is free but the Data Use Terms are a real contract: no attempt at re-identification, and you must not redistribute. Restricted variables (family structure, exact age, handedness detail) need a separate application with an institutional signature — effectively closed to unaffiliated researchers. The full release is tens of TB; take single subjects or the group-average packages.

### [International Brain Laboratory (IBL) public data](https://www.internationalbrainlab.com/data)

`Free` · beginner 2/5 · Neuropixels electrophysiology and behaviour

A 22-lab collaboration releasing standardised mouse decision-making data: the Brain Wide Map of Neuropixels recordings, a reproducible-electrophysiology dataset, and the full behavioural training data. Publications and data are CC-BY, software MIT.

**Access.** `pip install ONE-api ibllib`, connect to the public Alyx instance (`ONE(base_url='https://openalyx.internationalbrainlab.org', silent=True)` with the documented public credentials), then `one.search()` and `one.load_object()` to pull spikes, trials and video features; interactive browsing at viz.internationalbrainlab.org.

**Caveats.** The ONE API is the only comfortable route — the underlying files are ALF/Parquet, not NWB, though NWB conversions are also published on DANDI. Expect to read the IBL docs for an afternoon before the first useful query. Data policy is release within 12 months of collection or on publication.

### [ModelDB](https://modeldb.science/)

`Free` · beginner 3/5 · computational model repository

SenseLab's curated repository of roughly 1,930 published computational neuroscience models, from single-channel kinetics through Hodgkin-Huxley compartmental cells to network models, each linked to its source paper and browsable before download.

**Access.** Browse or search by simulator, region, cell type, receptor or currents at modeldb.science; download the model source as a zip and run it in NEURON, NEST, Brian, MATLAB or whatever the author used.

**Caveats.** Model code is archival, not maintained — older NEURON hoc/mod files often need small fixes to compile against current versions, and some entries have no runnable code at all. Curation checks that the model ran once, not that it reproduces every figure.

### [NeuroMorpho.Org](https://neuromorpho.org/)

`Free` · beginner 4/5 · neuronal morphology reconstructions

The standard repository of digitally reconstructed neuronal morphologies: version 8.6.124 (released 2026-08-07) contains 298,339 reconstructions from 1,011 laboratories, spanning 1,543 cell types and 490 brain regions.

**Access.** Search and filter in the browser, add to a download cart and take SWC files; or use the REST API at neuromorpho.org/api/neuron for metadata-driven queries. SWC files load directly into NEURON, NeuroM, navis or Brian-adjacent morphology tools.

**Caveats.** Reconstructions carry the original labs' tracing conventions — soma representation, shrinkage correction and truncation differ, so morphometric comparisons across labs need care. Metadata completeness varies by contribution. Attribution to the original publication is expected.

### [Neurosynth](https://neurosynth.org/)

`Free` · beginner 5/5 · fMRI coordinate meta-analysis

Automated meta-analysis over the published fMRI literature: 507,891 activation coordinates extracted from 14,371 studies, with prebuilt meta-analytic maps for 1,334 terms and coactivation maps for over 150,000 brain locations. Neurosynth Compose extends it to custom, curated meta-analyses.

**Access.** Type a term in the browser and get an association map you can download as NIfTI, or click a coordinate to see what it is associated with; programmatically via `pip install nimare` and `nimare.extract.fetch_neurosynth()`, then run the MKDA/ALE/chi-square estimators locally.

**Caveats.** The corpus is automatically text-mined, so term-study associations are noisy and the database has not been fully re-harvested in years — treat maps as hypothesis generators, not evidence. Reverse-inference maps are routinely over-interpreted; read the caveats on the site. Neurosynth Compose needs an account.

### [NeuroVault](https://neurovault.org/)

`Free` · beginner 4/5 · statistical brain maps

Public repository of unthresholded statistical maps, parcellations and atlases from MRI and PET studies; as of 2026-08 it holds 17,794 collections and 713,915 images. Unthresholded maps are what make image-based meta-analysis and map comparison possible without re-running anyone's pipeline.

**Access.** Browse and view maps in the browser; open REST API (`https://neurovault.org/api/collections/?format=json`, `/api/images/`); or fetch programmatically with Nilearn: `from nilearn.datasets import fetch_neurovault_ids`.

**Caveats.** Metadata quality is uneven — many collections lack the contrast descriptions, sample size or template space you need for meta-analysis, so filter hard. Uploading requires a free account. Maps are in whatever space the authors used; check MNI vs. native before combining.

### [Open Science Framework (OSF)](https://osf.io/)

`Free tier, email` · beginner 5/5 · project repository and preregistration

The de facto home for psychology materials, data, analysis code and preregistrations, run by the non-profit Center for Open Science. Free accounts get 5 GB per private project or component and 50 GB per public one, with a 5 GB maximum single file, and no overall per-user cap.

**Access.** Free account at osf.io; create a project, add components, register a preregistration from a community template (AsPredicted-style, Registered Report, secondary-data templates) to get a timestamped, citable, DOI-bearing record. Command line: `pip install osfclient` then `osf -p <project_id> clone`.

**Caveats.** Storage caps bite on neuroimaging — connect a third-party add-on (S3, Google Drive, Dropbox, GitHub, Dataverse, figshare) whose space does not count toward the OSF cap, or put imaging on OpenNeuro and link it. Registrations are permanent and cannot be deleted, only withdrawn with a public tombstone.

### [OpenNeuro](https://openneuro.org/)

`Free` · beginner 5/5 · BIDS neuroimaging archive

Free archive of BIDS-formatted human neuroimaging datasets covering fMRI, structural and diffusion MRI, EEG, MEG, iEEG and PET; all public datasets are released under CC0 and new datasets are deposited every few days. Its EEG/MEG/iEEG slice alone (indexed by the NEMAR portal) is 755 datasets and about 39,000 participants.

**Access.** Browse and download in the browser; or anonymous S3: `aws s3 ls --no-sign-request s3://openneuro.org/` and `aws s3 sync --no-sign-request s3://openneuro.org/ds000117 .`; or `pip install openneuro-py` then `openneuro-py download --dataset=ds000117`; each dataset is also a git/DataLad endpoint (`datalad install https://github.com/OpenNeuroDatasets/ds000117.git`) for versioned, file-on-demand clones.

**Caveats.** Downloading needs no account; uploading does. Datasets are contributor-curated, so BIDS compliance and defacing quality vary — validate before trusting. Whole datasets are often tens to hundreds of GB, so use the CLI/DataLad to fetch only the subjects you need rather than the browser zip.

### [PhysioNet](https://physionet.org/about/database/)

`Free` · beginner 4/5 · physiological signal databases

MIT-hosted archive of physiological signal databases including the EEG staples used across the machine-learning literature: CHB-MIT Scalp EEG, Siena Scalp EEG, EEG Motor Movement/Imagery, Sleep-EDF and Sleep-EDF Expanded, CAP Sleep, and gait-in-neurodegenerative-disease recordings.

**Access.** Open-access databases download directly (`wget -r -N -c -np https://physionet.org/files/sleep-edfx/1.0.0/`); read signals with `pip install wfdb`. Restricted and credentialed databases require a free account, a signed data use agreement and, for credentialed tiers, completion of human-subjects research training.

**Caveats.** Access is tiered: open, restricted (DUA), credentialed (training plus DUA, and credentialing asks for a reference — awkward for unaffiliated researchers). Most of the classic EEG and sleep sets are in the open tier. Records are in WFDB or EDF, not BIDS.

### [PsychArchives](https://www.psycharchives.org/)

`Free` · beginner 4/5 · psychology disciplinary repository

Disciplinary repository for psychology and neighbouring fields run by the Leibniz Institute for Psychology (ZPID, Trier), accepting 20 digital research object types: articles, preprints, research data, code, supplements, preregistrations, test instruments and multimedia. Everything gets a DOI.

**Access.** Search and download in the browser; deposit through the ZPID submission workflow. The associated Research Data Centre (rdc-psychology.org, formerly PsychData) curates reusable psychological datasets and runs PsychOpen CAMA for community-augmented meta-analyses.

**Caveats.** Strong German-language and European coverage — a genuine complement to, not a substitute for, OSF. Some archived datasets carry access conditions set by the depositor rather than being straight open download; test instruments in particular may have use restrictions.

### [TUH EEG Corpus (Temple University Hospital)](https://isip.piconepress.com/projects/nedc/html/tuh_eeg/)

`Free (registration), application` · beginner 2/5 · clinical EEG corpus

The largest openly available clinical EEG archive: 26,846 recordings collected at Temple University Hospital between 2002 and 2017, with annotated subsets for normal/abnormal classification (TUAB), seizures (TUSZ), artifacts (TUAR), events (TUEV), slowing (TUSL) and an epilepsy cohort (TUEP, 100 epilepsy and 100 non-epilepsy subjects).

**Access.** Complete the registration form on the site and email it to help@nedcdata.org; approval typically takes 24-48 hours, after which you receive SSH credentials and pull data with `rsync` (MobaXterm on Windows).

**Caveats.** No browser download — rsync only, and the full corpus is multiple TB, so start from an annotated subset. The team tracks who downloads; the form asks for a real postal address. Clinical EEG means non-uniform montages, referential channels and recording lengths from minutes to days.

## Software

### [AFNI](https://afni.nimh.nih.gov/)

`Free` · beginner 3/5 · fMRI analysis suite

NIMH's C/Python/R suite for analysis and display of multiple MRI modalities, freely available as source and precompiled binaries for research use, with afni_proc.py generating complete, documented single-subject preprocessing and regression pipelines plus strong interactive visualisation.

**Access.** Install with the maintained setup scripts (`@update.afni.binaries -package linux_ubuntu_24_64 -do_extras`), no registration; runs on Linux, macOS and Windows Subsystem for Linux. Support is the very active message board at discuss.afni.nimh.nih.gov.

**Caveats.** Free for research purposes; not a general-purpose licence for commercial products. The learning curve is command-line and the naming conventions are idiosyncratic, but the AFNI bootcamp materials and the message board (answered by the developers themselves, usually within a day) are the field's best support experience.

### [Brian 2](https://briansimulator.org/)

`Free` · beginner 4/5 · spiking network simulator

Free, open-source spiking neural network simulator in Python (version 2.10, December 2025) where models are specified as plain differential equations in mathematical notation and compiled to C++ at runtime; it covers everything from leaky integrate-and-fire to Hodgkin-Huxley and arbitrary custom synapse models.

**Access.** `pip install brian2` or `conda install -c conda-forge brian2`; the documentation ships runnable tutorials, and the Neuronal Dynamics exercises use it directly.

**Caveats.** Runs on any laptop — no data, no hardware, no institutional access required, which makes it the most accessible route into original computational neuroscience. Large networks benefit from the C++ standalone device or Brian2CUDA; the pure-Python runtime mode is slow for big simulations.

### [brms](https://paulbuerkner.com/brms/)

`Free` · beginner 2/5 · Bayesian multilevel modelling in R

GPL-2 R package that fits Bayesian generalised (non-)linear multivariate multilevel models with Stan using lme4-style formula syntax: ordinal, count, survival, response-time, zero-inflated, mixture and distributional models, plus splines, autocorrelation, censoring and missing-data imputation.

**Access.** `install.packages("brms")` from CRAN (needs a C++ toolchain: Rtools on Windows, Xcode command-line tools on macOS), then `brm(rt ~ condition + (condition | subject), data = d, family = lognormal())`. Extensive vignettes via `vignette(package = "brms")`.

**Caveats.** Compilation of each new model takes a minute or two; sampling for realistic psychology multilevel models takes minutes to hours on a laptop. You need to understand priors and convergence diagnostics — this is not a point-and-click substitute. Pair it with Statistical Rethinking for the conceptual grounding.

### [DeepLabCut](https://mlabofai.org/deeplabcut)

`Free` · beginner 3/5 · markerless pose estimation

LGPL-v3 toolbox for 2D and 3D markerless pose tracking of animals and humans by transfer learning, typically reaching human-level labelling accuracy from 50-200 labelled frames. SuperAnimal models give zero-shot inference with no training at all: SuperAnimal-Quadruped (40,000+ images, 39 keypoints, mouse to elephant) and SuperAnimal-TopViewMouse (5,000+ mouse videos, 26 keypoints).

**Access.** `pip install deeplabcut` (conda environment files provided) with a napari-based GUI, or run the official Colab notebooks — including a one-click SuperAnimal inference notebook — on Google's free GPU tier without installing anything.

**Caveats.** Training from scratch really wants a GPU; the free Colab tier works but sessions time out, so checkpoint to Drive. SuperAnimal inference is the genuinely laptop-friendly path. Behavioural analysis after tracking is your problem — DeepLabCut gives coordinates, not behaviour labels.

### [EEGLAB](https://sccn.ucsd.edu/eeglab/)

`Free` · beginner 4/5 · EEG analysis toolbox

UCSD SCCN's interactive toolbox for continuous and event-related EEG, MEG and other electrophysiological data — ICA decomposition, time-frequency analysis, artefact rejection, source localisation and study-level statistics — extended by over 120 plug-ins including ICLabel, AMICA, clean_rawdata and the BIDS tools.

**Access.** Download and add to the MATLAB path, then `eeglab` for the GUI; every GUI action prints the equivalent command so you can build scripts by doing. A compiled standalone build runs without a MATLAB licence.

**Caveats.** Academic free software. The standalone removes the MATLAB dependency but is less flexible for scripting than the toolbox; Octave support exists for parts of EEGLAB but is not complete. ICA on long high-density recordings is memory-hungry — downsample and high-pass first.

### [fMRIPrep](https://fmriprep.org/)

`Free` · beginner 3/5 · preprocessing pipeline

Apache-2.0 robust preprocessing pipeline for task and resting-state fMRI (version 25.2.5, March 2026) that takes a BIDS dataset and returns preprocessed images in the spaces you ask for, plus confound regressors and a per-subject visual QC report. It removes most of the discretion — and most of the errors — from preprocessing.

**Access.** Run the container: `pip install fmriprep-docker` then `fmriprep-docker bids_dir out_dir participant --fs-license-file license.txt`, or `apptainer run fmriprep.sif ...` on a cluster. A manually prepared Python 3.10+ environment is possible but not recommended.

**Caveats.** Needs a free FreeSurfer licence file. Realistically 8-16 GB RAM and several hours per subject; `--fs-no-reconall` cuts most of that if you do not need surfaces. The container image is several GB. Version-pin it: outputs differ across releases, and the docs ask you to report the exact version.

### [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/)

`Free (registration), email` · beginner 2/5 · cortical surface reconstruction

The standard pipeline for cortical surface reconstruction, subcortical segmentation, cortical thickness and surface-based group analysis from T1 images; its outputs are the substrate for most structural-MRI morphometry in the field and are required by several other tools.

**Access.** Download the binary release for Linux/macOS, register on the site to receive a free `license.txt` licence key by email, place it in the FreeSurfer directory, then `recon-all -s subj -i T1.nii.gz -all`.

**Caveats.** The licence key is free but mandatory and is also what fMRIPrep asks for. `recon-all` takes roughly 6-12 hours per subject on one core — plan for a cluster, a cloud VM, or the faster FastSurfer reimplementation if you have more than a handful of subjects. Outputs need visual QC; automated failures are common in clinical and paediatric scans.

### [FSL](https://fsl.fmrib.ox.ac.uk/fsl/docs/)

`Free (registration), email` · beginner 3/5 · fMRI/DTI analysis suite

Oxford FMRIB's analysis library for functional, structural and diffusion MRI: FEAT (GLM), MELODIC (ICA), FIRST/FAST (segmentation), FNIRT/FLIRT (registration), FDT and probtrackx (tractography), randomise (permutation inference) and TBSS.

**Access.** Download and run `python fslinstaller.py` (Linux/macOS; Windows via WSL); command-line tools plus GUIs, callable from shell scripts or Nipype pipelines.

**Caveats.** Free for academic and non-commercial research; commercial use requires a paid licence from Oxford University Innovation, and the download form asks who you are. The install is ~10 GB and several pipelines are slow on a laptop — randomise with many permutations is an overnight job. Some components (e.g. parts built on other packages) carry their own terms.

### [JASP](https://jasp-stats.org/)

`Free` · beginner 5/5 · GUI statistics (Bayesian and frequentist)

Free, open-source cross-platform statistics program from the University of Amsterdam that offers standard analyses in both classical and Bayesian form (Bayes factors for t-tests, ANOVA, regression, correlation, contingency tables), with APA-formatted tables and dynamically updating results.

**Access.** Download the installer for Windows, macOS or Linux; drag-and-drop spreadsheet interface, optional R syntax mode, and OSF integration for opening and saving data directly from a project.

**Caveats.** Analyses run in memory, so very large datasets are better handled in R. Modules beyond the core set are installed from the JASP library. jamovi (jamovi.org) is the closely comparable free alternative if you prefer its R-syntax mode; both are genuine substitutes for SPSS licences that unaffiliated researchers cannot buy.

*Also listed under: social.*

### [JATOS](https://www.jatos.org/)

`Free` · beginner 3/5 · online study hosting

Apache-2.0 server software for hosting and managing online studies written in jsPsych, lab.js, OSWeb/OpenSesame or plain HTML/JS: it serves the study, issues participant links, manages batches and workers, and stores the result data.

**Access.** Self-host by unzipping the release and running `./loader.sh start` (Java) or via Docker, on a laptop for testing and on any small VPS for real data collection. For researchers with no server at all, JATOS on MindProbe (jatos.mindprobe.eu) is a sponsored free instance backed by ESCoP, the Journal of Cognition and OpenSesame.

**Caveats.** Self-hosting means you own the HTTPS certificate, backups and GDPR/ethics responsibility for the data on your box. The free MindProbe instance is a courtesy, not an SLA — publish-critical data should be exported and backed up promptly. JATOS recruits nobody; it only hosts.

### [jsPsych](https://www.jspsych.org/)

`Free` · beginner 4/5 · browser-based experiments

JavaScript framework for behavioural experiments that run in a web browser, built from a plugin library (keyboard/button responses, categorisation, surveys, visual search, audio, canvas drawing) assembled into a timeline. The standard tool for online cognitive psychology.

**Access.** Load from a CDN in a plain HTML file for the quickest start, or `npm install jspsych @jspsych/plugin-html-keyboard-response` for a bundled project; data comes back as JSON/CSV that you route to your own server, JATOS, or a recruitment platform.

**Caveats.** jsPsych only runs the experiment — you still need hosting and, if you want participants, a recruitment route. Prolific and MTurk integrations are documented but those services charge for participants. Browser timing varies by device and refresh rate; use the built-in timing calibration and expect noisier RTs than in-lab.

### [MNE-Python](https://mne.tools/stable/)

`Free` · beginner 4/5 · M/EEG analysis

Open-source Python package (version 1.12.1) for MEG, EEG, sEEG, ECoG and fNIRS: filtering, ICA artefact removal, epoching, evoked responses, time-frequency analysis, source estimation (MNE/dSPM/beamformers), connectivity and decoding, with permutation cluster statistics built in.

**Access.** `pip install mne` (or the `mne` conda environment for the full ecosystem incl. mne-bids, mne-connectivity); `mne.datasets.sample.data_path()` downloads the sample MEG/EEG dataset so every tutorial runs without your own recordings.

**Caveats.** Source localisation needs an anatomical MRI and a FreeSurfer reconstruction; the fsaverage template is the fallback when you have EEG but no individual MRI. Reads most vendor formats, but some (e.g. certain proprietary EEG systems) need extra packages. The tutorial set is long but is the intended entry point.

### [Nilearn](https://nilearn.github.io/stable/)

`Free` · beginner 4/5 · Python neuroimaging analysis

BSD-licensed Python library for statistical and machine learning analysis of brain volumes and surfaces: first- and second-level GLMs, decoding with scikit-learn, functional connectome extraction, masking/resampling, and the plotting functions that produce most of the field's figures.

**Access.** `pip install nilearn`; fetchers download example data on demand (`fetch_haxby()`, `fetch_atlas_schaefer_2018()`, `fetch_development_fmri()`, `fetch_oasis_vbm()`), so the tutorials run end to end on a laptop with no data of your own.

**Caveats.** Nilearn analyses preprocessed data; it does not preprocess (pair it with fMRIPrep). The bundled atlases carry the licences of their original authors. The examples gallery is the real documentation — start there rather than the API reference.

### [OpenSesame](https://osdoc.cogsci.nl/)

`Free` · beginner 5/5 · experiment builder

GPL3 graphical experiment builder for psychology, neuroscience and experimental economics, current stable release 4.1 ("Neonatal Nightingale"), running on Windows, macOS and Linux with optional Python and JavaScript for anything the GUI cannot express. Supports eye trackers (EyeLink, Tobii), button boxes, EEG triggers and joysticks.

**Access.** Download the installer for your platform; build the experiment in the GUI; use the OSWeb back-end to export the same experiment to the browser and deploy it through JATOS for online data collection.

**Caveats.** OSWeb supports a subset of desktop features — check that your plugins and timing requirements survive the export before committing to an online study. Hardware integrations depend on vendor drivers you may not have. Community support is a forum, not a helpdesk.

### [PsychoPy](https://www.psychopy.org/)

`Free` · beginner 4/5 · experiment builder

Open-source stimulus presentation and experiment control for psychology and neuroscience, with a drag-and-drop Builder for non-programmers and a Python Coder view underneath; the same experiment can be exported to JavaScript (PsychoJS) to run in a browser. Millisecond-level timing is the reason the field uses it.

**Access.** Standalone installers for Windows/macOS/Linux, or `pip install psychopy` into a dedicated environment. Builder experiments export to PsychoJS for online running; you can host the generated JS yourself or on Pavlovia.

**Caveats.** The desktop app is fully free for in-lab studies. Pavlovia, the hosting service that funds development, is a paid credit system — but PsychoJS output is open source, so you can host it on your own server or through JATOS instead of paying. Timing on consumer laptops and in browsers is worse than on a lab machine; measure it if reaction time is your dependent variable.

### [SpikeInterface](https://spikeinterface.readthedocs.io/)

`Free` · beginner 2/5 · spike sorting and curation

Python framework that unifies extracellular electrophysiology: reads many recording formats, runs and compares 13+ spike sorters (Kilosort 1-4, MountainSort 4-5, SpyKING CIRCUS, Tridesclous, IronClust, HerdingSpikes, WaveClus and others), then post-processes, computes quality metrics and exports for curation.

**Access.** `pip install spikeinterface[full]`; sorters run either from a local install or inside their official Docker/Apptainer images so you never fight their dependencies. `spikeinterface-gui` provides manual curation.

**Caveats.** SpikeInterface is free, but some wrapped sorters have their own licences and a couple historically needed MATLAB (Kilosort 4 is pure Python and GPU-based). Sorting Neuropixels-scale data needs a GPU and lots of disk. Reanalysing public IBL or DANDI recordings is the realistic entry point without a rig.

### [SPM](https://www.fil.ion.ucl.ac.uk/spm/)

`Free` · beginner 3/5 · statistical parametric mapping

The original mass-univariate analysis package for fMRI, PET, SPECT, EEG and MEG from the Wellcome Centre for Human Neuroimaging: segmentation, normalisation to tissue-probability templates, the GLM, random-field-theory inference, DCM and the whole ecosystem of third-party toolboxes built on it (CAT12, Marsbar, conn).

**Access.** Download the release zip from the site and add it to your MATLAB path, then `spm fmri`. MATLAB is the usual dependency, but a precompiled standalone that runs against the free MATLAB Runtime, and partial GNU Octave compatibility, both remove the MATLAB licence cost.

**Caveats.** SPM itself is free and open source; MATLAB is not, so use the standalone or Octave route unless you have a licence. Octave support is incomplete for some toolboxes. Batch scripting through matlabbatch is the only sane way to run more than a few subjects.

## Literature

### [bioRxiv](https://www.biorxiv.org/)

`Free` · beginner 5/5 · biology/neuroscience preprint server

Cold Spring Harbor Laboratory's preprint server for the biological sciences, with neuroscience consistently among its largest subject collections — the daily feed is dominated by systems, cellular and imaging neuroscience. Posting is free and preprints get a DOI and a choice of Creative Commons licence.

**Access.** Read and download without an account; submit through the bioRxiv site (a screening check, not peer review, precedes posting). Programmatic access via api.biorxiv.org and per-collection RSS/XML feeds (`https://connect.biorxiv.org/biorxiv_xml.php?subject=neuroscience`); content is also indexed in Europe PMC.

**Caveats.** Screening filters out non-scientific and dangerous content but does not check the science. Some authors post with an "all rights reserved" default rather than a CC licence, which blocks text mining and reuse — choose CC BY when you post. For human-subjects clinical work, medRxiv is the correct sibling server.

### [Europe PMC](https://europepmc.org/)

`Free` · beginner 4/5 · life-science literature search and API

EMBL-EBI's life-science literature platform covering research articles, reviews, protocols, books and preprints from 34 preprint servers, with text-mined annotations (1.3 billion annotations across 42 concept types) and linked grant and dataset records.

**Access.** Web search; free RESTful Articles API with no key (`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=fmri%20AND%20SRC:PPR&format=json&pageSize=100`), plus Annotations and Grants APIs, an OAI service and bulk downloads.

**Caveats.** Its preprint coverage and cursor-based pagination make it better than PubMed for automated corpus building; the annotations API is the cheapest route to entity extraction without running your own NLP. Full text is only available where the publisher deposited it.

### [OpenAlex](https://openalex.org/)

`Free` · beginner 4/5 · open bibliographic database

Free, fully open index of scholarly works, authors, sources, institutions, topics and funders — 322,147,582 works as of 2026-08-28 — with citation links, open-access status and author disambiguation. It is the practical replacement for Web of Science and Scopus for anyone without a subscription.

**Access.** Free REST API with no key: `https://api.openalex.org/works?filter=concepts.id:C169760540,publication_year:2025&mailto=you@example.org` (the mailto puts you in the faster polite pool). Python clients (`pip install pyalex`) and a complete CC0 snapshot on AWS S3 for offline work.

**Caveats.** Data is CC0, so you can redistribute derived datasets. Author disambiguation and topic assignment are automated and imperfect — verify before making claims about individuals. Very heavy users are asked to take the snapshot rather than hammer the API; a premium tier exists for higher-throughput commercial use but the public API is not crippled.

### [PsyArXiv](https://osf.io/preprints/psyarxiv/)

`Free` · beginner 5/5 · psychology preprint server

The psychology preprint server, hosted on OSF Preprints and holding 63,154 preprints as of 2026-08-28. It is where most psychology preprints, registered-report stage-1 protocols and postprints of paywalled articles are posted, with DOIs and versioning.

**Access.** Read and download anything with no account; to post, sign in with a free OSF account, upload the PDF, choose a licence and a subject, and it appears after a light moderation check. Metadata is queryable through the OSF API (`https://api.osf.io/v2/preprints/?filter[provider]=psyarxiv`).

**Caveats.** Free to read and free to post. Preprints are moderated for scope, not peer reviewed. Check your journal's preprint policy before posting (most psychology journals allow it; a few still do not). Hosting on OSF Preprints is a Center for Open Science service — the community has periodically discussed migration, so watch for platform announcements.

### [PsychPorta (ZPID)](https://psychporta.org/)

`Free` · beginner 4/5 · psychology discovery portal

The Leibniz Institute for Psychology's search portal covering PSYNDEX publication metadata from German-speaking psychology, PSYNDEX Tests (test instrument references), PsychArchives research documents and datasets, and author profiles. Portal metadata is released under CC0.

**Access.** Free web search at psychporta.org, no account; records link out to full text, DOIs and archived materials in PsychArchives.

**Caveats.** This replaces PubPsych, which ZPID took offline in June 2026 — old bookmarks and citations to pubpsych.eu now 404. PsychPorta covers ZPID's own databases; the third-party sources PubPsych federated (MEDLINE, ERIC and others) must now be searched separately. Strongest for German-language and European psychology.

### [PubMed and PubMed Central (PMC)](https://pmc.ncbi.nlm.nih.gov/)

`Free` · beginner 5/5 · biomedical literature and full-text archive

NLM's free full-text archive of biomedical and life-science literature, over 10 million full-text records spanning material from the late 1700s to the present, alongside PubMed's abstract index. The Open Access Subset within PMC is explicitly cleared for bulk retrieval and text mining.

**Access.** Search at pubmed.ncbi.nlm.nih.gov and pmc.ncbi.nlm.nih.gov; programmatically via E-utilities (`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term=...&retmode=json`); bulk via the PMC FTP service, OAI-PMH service or the cloud (AWS) service for the OA subset.

**Caveats.** Being in PMC does not mean an article is reusable — only the Open Access Subset permits bulk download and redistribution, and individual licences within it vary (some are CC BY-NC-ND). E-utilities are rate limited to 3 requests/second without a free NCBI API key, 10 with one.

*Also listed under: medicine.*

### [The Wikipedia Library](https://wikipedialibrary.wmflabs.org/)

`Free (registration), credentialing` · beginner 3/5 · paywalled journal access for the unaffiliated

Free access to more than 100 subscription databases, with content in 32 languages, for qualifying Wikipedia editors — including publishers that carry most of the paywalled psychology and neuroscience literature (Wiley, SAGE, Springer, Nature, ProQuest, JSTOR, BMJ).

**Access.** Log in with a Wikipedia account that meets the criteria; some collections are instantly available through the library card platform, others require a short per-publisher application. Access is via the platform's proxied links.

**Caveats.** Eligibility is real work: 500+ edits, 6+ months of account age, 10+ edits in the last 30 days and no active blocks. Access is granted for improving Wikipedia; using it is legitimate but the expectation of contribution is genuine. Collection membership changes as publisher agreements lapse, and APA's PsycINFO/PsycARTICLES are not among the standard offerings.

## Compute

### [brainlife.io](https://brainlife.io/)

`Free (registration), email` · beginner 4/5 · free cloud neuroimaging platform

Open-source, free platform for reproducible MRI, EEG and MEG analysis that runs over 400 community-contributed processing Apps on donated and NSF-funded compute, with cloud storage through the AWS Open Data Program; it reports over 2,000 users.

**Access.** Sign in with ORCID, GitHub or Google in the browser, upload or import a dataset (including straight from OpenNeuro), then chain Apps — fMRIPrep, FreeSurfer, MRtrix tractography, network analyses — into a pipeline that runs on their HPC with no local install.

**Caveats.** Compute is donated, so queue times vary and there is no throughput guarantee; heavy users are expected to bring their own allocation eventually. Not suitable for identifiable or restricted clinical data — check your ethics approval before uploading. Apps are contributed, so read the App's provenance before trusting the output.

### [EBRAINS](https://www.ebrains.eu/)

`Free (registration), email` · beginner 3/5 · European brain research infrastructure

Open research infrastructure grown out of the Human Brain Project offering multi-species 3D brain atlases (human, macaque, marmoset, rat, mouse), a shared data and model knowledge graph, simulation tools (The Virtual Brain, NEST, Arbor), collaborative Jupyter workspaces and access to HPC and neuromorphic computing.

**Access.** Free EBRAINS account opens the Collaboratory (hosted Jupyter notebooks with the tools preinstalled), the Knowledge Graph search and the atlas services; `pip install siibra` gives programmatic access to the atlases and linked datasets from your own machine.

**Caveats.** Registration and the basic Collaboratory are free and open to researchers anywhere; substantial HPC and neuromorphic hardware time is allocated through calls and proposals, not on sign-up. Some datasets in the Knowledge Graph are under controlled access with their own agreements. The platform is broad and the entry points are not always obvious — start from siibra or a specific atlas.

### [Neurodesk](https://www.neurodesk.org/)

`Free` · beginner 4/5 · containerised analysis environment

Free, fully open-source containerised environment bundling 100+ neuroimaging and biomedical imaging tools (FSL, AFNI, FreeSurfer, MRtrix, ANTs, SPM, fMRIPrep and more) so that the same analysis runs identically on a laptop, an HPC cluster or in a browser.

**Access.** Neurodesk Play runs a full desktop in the browser with no install; or `docker run -p 8888:8888 vnmd/neurodesktop:latest` locally; or pull individual Neurocontainers with Docker/Apptainer on a cluster; NeurodeskApp is the native desktop client.

**Caveats.** Solves the install problem, not the compute problem — Neurodesk Play sessions are time- and resource-limited and are for learning and light work, not for preprocessing a cohort. Container images are large; a first pull on a slow connection takes a while. FreeSurfer inside the container still needs your own licence file.

### [Neuroscience Gateway (NSG)](https://www.nsgportal.org/)

`Free (registration), email` · beginner 3/5 · free HPC for neuroscience

NSF-funded portal that gives neuroscientists free access to national HPC, high-throughput and academic cloud resources via ACCESS allocations, with simulation and analysis tools (NEURON, NEST, Brian, PyNN, MOOSE, EEGLAB and others) preinstalled and tuned on the machines.

**Access.** Register for an NSG user account, upload your model or data and a job configuration through the web portal (or the NSG REST API), and NSG distributes the job to ACCESS, OSG or cloud resources and returns the results — no cluster account or scheduler knowledge needed.

**Caveats.** Explicitly not unlimited: NSG states it allocates compute on a fair-share basis from the allocation it receives each year, and users who outgrow it are directed to apply for their own ACCESS allocation. Accounts are reviewed. Best fit for network simulations and batch EEG processing, less so for interactive work. NEMAR (nemar.org) routes OpenNeuro EEG/MEG datasets straight onto NSG compute.

## Publishing

### [DOAJ (Directory of Open Access Journals)](https://doaj.org/)

`Free` · beginner 4/5 · no-APC journal finder

Community-curated index of vetted peer-reviewed open access journals worldwide, free to use and free for publishers to join. Its journal search can be filtered to titles that charge no article processing charges, which is the practical way to find legitimate psychology and neuroscience venues you can actually afford.

**Access.** Search journals at doaj.org/search/journals and apply the "without APCs" and subject filters; article-level search and a free public API (`https://doaj.org/api/search/journals/...`) are also available, plus full metadata dumps.

**Caveats.** DOAJ inclusion is a quality signal (it screens editorial process and transparency) but not a guarantee of prestige or indexing in PubMed/Scopus — check those separately. APC data is publisher-reported and can lag; confirm on the journal's own site before submitting. Being no-APC often means a small society or university press with slower production.

### [Journal of Open Source Software (JOSS)](https://joss.theoj.org/)

`Free, email` · beginner 3/5 · software paper, diamond OA

Diamond open-access journal (ISSN 2475-9066) that publishes short, citable papers about research software, reviewed openly in public GitHub issues so the full review record stays permanently accessible. It is the standard way to make a neuroscience or psychology toolbox citable.

**Access.** Put the software in a public repository with an OSI-approved licence, add a `paper.md` of roughly 250-1000 words plus a bib file, and submit at joss.theoj.org/papers/new; review happens in the open reviews repository with a checklist-driven editor and reviewers.

**Caveats.** No fees to publish or read. Scope is strict: the software must be feature-complete, have obvious research application, show at least six months of public development history and community adoption, and not be a minor utility or single-function wrapper. Review targets the software, so expect requests to add tests, docs and installation instructions.

*Also listed under: physics, astronomy, chemistry, earth, cs-ml.*

### [Meta-Psychology](https://open.lnu.se/index.php/metapsychology)

`Free, email` · beginner 3/5 · diamond OA methods journal

Diamond open-access journal published by Linnaeus University Press with no publication fee, dedicated to work the mainstream journals resist: systematic reviews, meta-analyses, replicability reports and replication studies, registered reports, null results, methodological tutorials, commentaries, and history and philosophy of psychology.

**Access.** Submit through the journal's Open Journal Systems site; review is open and non-anonymous, papers are circulated publicly for community comment, and substantial contributors are credited as reviewers in the published article.

**Caveats.** Free to publish and free to read. Open non-anonymous review is a real consideration — your reviewers' names and your responses are public. It is a small journal with modest visibility; weigh that against the zero cost and the fit for replications and null results that have nowhere else to go.

### [PCI Registered Reports (Peer Community In)](https://rr.peercommunityin.org/)

`Free, email` · beginner 3/5 · free peer review and diamond OA

One of 21 thematic Peer Community In platforms, this one dedicated to Registered Reports, preregistrations, replications and negative results. PCI as a whole has recommended 1,051 preprints with 2,800+ recommenders, over 100 PCI-friendly journals accept its recommendations, and the associated diamond open-access Peer Community Journal has published 532 articles.

**Access.** Post your Stage 1 protocol as a preprint (PsyArXiv or OSF), submit it to PCI RR, and editors organise free peer review; on in-principle acceptance you collect data, submit Stage 2, and then either publish free of charge in Peer Community Journal or take the recommendation to any PCI RR-friendly journal.

**Caveats.** The entire PCI and Peer Community Journal process is free for authors — no APCs at any stage, which makes it the most realistic registered-report route for anyone without publication funds. Review is thorough and slow; Stage 1 review can take months. Not every journal in your subfield is PCI-friendly, so check the list before starting.

## Funding

### [Grass Fellowship in Neuroscience (MBL)](https://grassfoundation.org/)

`Free, application` · beginner 2/5 · independent summer research fellowship

A 14-week funded summer fellowship at the Marine Biological Laboratory in Woods Hole running from Memorial Day to the Saturday before Labor Day, in which fellows pursue their own independent research project with MBL housing provided, up to $5,000 for research supplies, loaned microscopes and equipment, childcare coverage for children aged 4-14, and access to animal facilities.

**Access.** Apply through grassfoundation.org with a research proposal that is feasible in 14 weeks, two letters of reference and a current research supervisor; applications close in early December for the following summer.

**Caveats.** Highly competitive, and the design assumes you already have a project and the skills to run it independently. Practical gates: a valid US visa is required (or agreement to obtain one), and the foundation does not provide health or accident insurance, so you must arrange your own. Verify the exact deadline on the site — it moves by a few days each year.

### [IBRO grants, fellowships and schools](https://ibro.org/)

`Free, application` · beginner 3/5 · international neuroscience funding

The International Brain Research Organization funds travel grants, FENS/IBRO-PERC exchange fellowships (next deadline 15 October 2026), the IBRO-Wellcome Neuroscience Capacity Accelerator, society meeting support, and a programme of neuroscience schools with training grants covering course and travel costs. It reports funding over 70% of these initiatives from journal proceeds.

**Access.** Apply through the grants and training pages on ibro.org; regional committees for Africa, Asia-Pacific, Latin America, Pan-Europe and US/Canada run their own calls with region-specific eligibility.

**Caveats.** This is the most realistic funding family for neuroscientists at under-resourced institutions and in low- and middle-income regions — the regional committees exist precisely for that. Awards are small (travel, course fees, short exchanges) rather than project budgets. Deadlines are per-programme and shift annually; check the specific call page rather than relying on last year's date.

### [SIPS Grants-in-Aid](https://improvingpsych.org/grants/)

`Free, application` · beginner 3/5 · micro-grants for open psychology

Small grants from the Society for the Improvement of Psychological Science for projects that lower barriers to better psychological science — educational resources, interactive media, preconferences, small gatherings — with requests of up to $2,500 and roughly $5,000 committed across 2-10 awards per cycle.

**Access.** Apply through the SIPS grants page; the lead applicant must be a SIPS member, and membership dues waivers are available on request.

**Caveats.** Explicitly prioritises scholars from underrepresented groups, early-career researchers, those outside wealthy nations and those facing resource constraints. Will not fund salaries or institutional overhead, and human/animal research needs ethics approval before funds are released; applications and outputs are shared publicly. The published deadline information on the page has been stale before — confirm the current cycle by email.

## Learning

### [Andy's Brain Book](https://andysbrainbook.readthedocs.io/)

`Free` · beginner 5/5 · fMRI analysis tutorials

Free step-by-step neuroimaging course for beginners, sponsored by the University of Michigan and paired with the Andy's Brain Blog video series: complete short courses in FSL, SPM, AFNI, FreeSurfer, MRtrix diffusion analysis and ASL, plus units on the CONN toolbox, parametric modulation, machine learning and statistics.

**Access.** Read free online at readthedocs; each course walks through downloading a public dataset and running the full pipeline command by command, with a matching YouTube video per chapter. Citable via DOI 10.5281/zenodo.5879293.

**Caveats.** The most forgiving on-ramp for someone who has never touched an fMRI dataset, and it teaches the GUI-and-command-line packages rather than Python. Some chapters trail the current versions of FSL and SPM, so menu names occasionally differ. Pair it with DartBrains if you want the Python route.

### [DartBrains](https://dartbrains.org/)

`Free` · beginner 3/5 · fMRI data analysis in Python

Dartmouth's open fMRI course covering MR signal and physics, preprocessing, the general linear model, and advanced methods including connectivity and representational similarity analysis, taught entirely in Python with numpy, nibabel, nilearn, fmriprep and nltools. CC BY-SA 4.0.

**Access.** Read and run online at dartbrains.org; notebooks are executable and the accompanying dataset is hosted on HuggingFace, so exercises run on a laptop or in Colab. Version 2.0 (2026) moved from Jupyter Book to interactive marimo notebooks.

**Caveats.** Assumes basic Python. The full dataset download is several GB — check disk before starting the preprocessing chapters. The 2026 platform change means older bookmarks and some third-party links point at the retired Jupyter Book version.

### [Learning Statistics with R (Navarro)](https://learningstatisticswithr.com/)

`Free` · beginner 5/5 · free statistics textbook

Danielle Navarro's complete introductory-to-intermediate statistics textbook, written from psychology lecture notes: R basics, descriptive statistics and graphing, probability, estimation, hypothesis testing, chi-square, t-tests, ANOVA, linear regression and an introduction to Bayesian methods. Released CC BY-SA 4.0 in HTML and PDF.

**Access.** Read free online or download the PDF at learningstatisticswithr.com; the open licence has produced community adaptations for other software, including a widely used jamovi version.

**Caveats.** Free in every sense, including reuse in your own teaching. The author notes it is an artefact of its time — the R idioms predate much of the tidyverse, and some sections reflect an earlier stage of the replication-crisis debate. Still the most humane first statistics book for psychology students.

### [Neuromatch Academy](https://neuromatch.io/courses/)

`Freemium, application` · beginner 4/5 · computational neuroscience curriculum

Three-week intensive summer courses in Computational Neuroscience, Deep Learning, NeuroAI and Computational Tools for Climate Science (a Computational Behaviour course launches July 2027). The Computational Neuroscience curriculum runs from modelling and machine learning through dynamical systems, stochastic processes and network causality, with daily Jupyter tutorials.

**Access.** All course content — notebooks, slides and videos — is permanently free at compneuro.neuromatch.io, deeplearning.neuromatch.io and the related sites, and runs in Colab or locally. The live course, with pods, TAs and a mentored group project, requires an application and a country-adjusted tuition fee.

**Caveats.** Materials are CC BY 4.0 (software BSD-3), so self-study costs nothing and is a genuinely complete curriculum. The live programme is not free: tuition is adjusted by cost of living with additional hardship discounts and waivers, but a non-refundable processing fee applies to everyone. 2026 courses ran 6-24 July (NeuroAI and Climate 13-24 July); 2026 applications are closed and 2027 applications open in February 2027.

### [Neuronal Dynamics (Gerstner, Kistler, Naud & Paninski)](https://neuronaldynamics.epfl.ch/)

`Free` · beginner 2/5 · theoretical neuroscience textbook

The standard graduate textbook on computational and theoretical neuroscience — Hodgkin-Huxley and integrate-and-fire models, dendrites, noise, generalised linear models, network dynamics, plasticity, Hopfield networks and decision theory — with the full text free online, a free video lecture series by Wulfram Gerstner, and Python exercises built on the Brian simulator.

**Access.** Read the complete book at neuronaldynamics.epfl.ch; run the accompanying Python/NumPy/Brian exercises from neuronaldynamics-exercises; free 15-week teaching materials are provided for instructors.

**Caveats.** Aimed at advanced undergraduates and beginning graduate students and it assumes differential equations and probability — it is not a first neuroscience book. The free online version is the full text; the Cambridge print edition costs money. Exercises need only a laptop with Python.

### [Statistical Rethinking (McElreath)](https://xcelab.net/rm/)

`Free` · beginner 3/5 · Bayesian statistics and causal inference

The course psychology and neuroscience have converged on for Bayesian data analysis and causal inference: a full lecture series on YouTube with slides, homework and solutions posted per cohort on GitHub, plus the `rethinking` R package and community code translations for brms/tidyverse, Python/PyMC, NumPyro and Julia.

**Access.** Watch the lecture playlist on the author's YouTube channel; clone the current course repository (e.g. github.com/rmcelreath/stat_rethinking_2024) for slides, homework and solutions; `devtools::install_github("rmcelreath/rethinking")` for the package.

**Caveats.** The lectures, slides, homework and code are free; the textbook itself is a paid Cambridge/CRC title with only sample chapters free, though the lectures stand alone. A third edition is in progress with no announced date. Budget real time — this is a semester course, not a weekend tutorial.

## Community

### [Brainhack](https://brainhack.org/)

`Free, email` · beginner 3/5 · hackathons and open-science training

A global network of hackathon-style neuroimaging events combining hands-on project work with interactive training: Brainhack Global runs hybrid and in-person events in cities worldwide each autumn and winter, alongside the OHBM Brainhack satellite and the intensive Brainhack School.

**Access.** Find a local or virtual event on brainhack.org, register (most local Brainhacks are free or nominal cost), and join a project — projects are proposed openly in advance on GitHub, and remote participation is normal.

**Caveats.** Local event costs, dates and virtual options are set by each organiser, so confirm on the specific event page; the site's event listings can lag the current season. Most useful if you arrive with a concrete question or a dataset — passive attendance gets much less out of it than joining a project.

### [Neurostars](https://neurostars.org/)

`Free, email` · beginner 4/5 · Q&A forum

The question-and-answer forum for neuroscience researchers, infrastructure providers and software developers, managed by INCF and running on Discourse; the Neuro Questions category alone holds around 6,900 topics and Software Support around 2,000. It is where the fMRIPrep, BIDS, Nilearn, MNE, DataLad and OpenNeuro developers actually answer.

**Access.** Read anything without an account; register free to post, and tag your question with the tool name (`fmriprep`, `bids`, `mne-python`, `datalad`) so the right maintainers see it. Include your command, the version and the error text.

**Caveats.** The single highest-value venue for a researcher with no local methods expert — but it rewards well-formed questions and ignores vague ones. Search first; most beginner preprocessing questions are already answered. Response time on niche tools can be days or never.

### [Psychological Science Accelerator](https://psysciacc.org/)

`Free, email` · beginner 3/5 · distributed research network

A globally distributed network of laboratories that pools intellectual and material resources to run large multi-site psychology studies, with a portfolio of a dozen or more projects (infant-directed speech, moral decision-making across cultures, stereotype threat, COVID-19 framing effects) and data deposited openly on OSF.

**Access.** Join through the membership page at no cost; members can propose studies, sit on committees, review submissions, or contribute data collection to an ongoing project. Completed project data and materials are on the PSA's OSF repository.

**Caveats.** The realistic route to authorship on large-sample cross-cultural work for a researcher with a small or non-existent participant pool — data-collection contributions are credited. It is volunteer-run, so timelines are long and committee work is a real time commitment. Contributing data still requires local ethics approval and some participant access.
