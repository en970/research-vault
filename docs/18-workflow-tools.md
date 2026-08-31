# Research workflow software

Part of [research-vault](../README.md). 80 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (1) · [Software](#software) (48) · [Literature](#literature) (7) · [Compute](#compute) (4) · [Publishing](#publishing) (6) · [Funding](#funding) (4) · [Learning](#learning) (6) · [Community](#community) (4)

## Data

### [OSF (Open Science Framework)](https://osf.io/)

`Free (registration), email` · beginner 5/5 · project management and preregistration

Free research project workspace from the Center for Open Science: versioned file storage, wiki, components, contributor roles, time-stamped preregistrations and registrations with DOIs, and add-ons that connect Dropbox, Google Drive, GitHub, Dataverse and figshare. Storage is capped at 5 GB per private project or component and 50 GB per public one, with a 5 GB per-file limit.

**Access.** Free account, then the web interface; API at https://api.osf.io/v2/; command-line upload with osfclient ('pip install osfclient', 'osf upload local.csv osfstorage/'). Preregister via the Registries section using OSF, AsPredicted-style or discipline templates.

**Caveats.** Caps apply per project AND per component, so large studies are split into components or pushed to third-party storage add-ons. Registrations are permanent: they can be withdrawn (leaving a tombstone) but never deleted. Data are held in the United States, which matters for some GDPR/ethics arrangements.

*Also listed under: neuro-psych, compute, publishing.*

## Software

### [Apptainer (formerly Singularity)](https://apptainer.org/)

`Free` · beginner 3/5 · HPC containers

Linux Foundation container platform for shared clusters (v1.5.3, July 2026): an image is one portable SIF file, the process runs as your own user with no daemon and no privilege escalation, and your files and GPUs are visible inside by default — which is why HPC centres that forbid Docker allow this.

**Access.** Usually already installed on clusters ('module load apptainer'); locally via distro packages. Convert and run a Docker image: 'apptainer build r.sif docker://rocker/r-ver:4.4', then 'apptainer exec --nv r.sif Rscript analysis.R' ('--nv' passes through NVIDIA GPUs) or 'apptainer shell r.sif'.

**Caveats.** Open source under a BSD-3-Clause-style licence; root is not needed to run if user namespaces are enabled. Building from a definition file usually still needs root or '--fakeroot', so many people build on a laptop and copy the .sif to the cluster. Sylabs' SingularityCE/SingularityPRO is the forked sibling with near-identical commands — check which one your cluster runs before writing docs for collaborators.

### [ASReview LAB](https://asreview.nl/)

`Free` · beginner 3/5 · systematic review screening

Apache-2.0 active-learning tool from Utrecht University (asreview 3.0.8 on PyPI, June 2026) for title/abstract screening: you label a few relevant and irrelevant records, and the model reorders the remaining thousands so relevant papers surface early; it also has a simulation mode to benchmark models against an already-screened dataset.

**Access.** 'pip install asreview' (Python 3.10+), then 'asreview lab' opens the interface in your browser; import a RIS/CSV/Excel/TSV export from PubMed, Scopus, Web of Science or a reference manager, screen interactively, and export the labelled dataset.

**Caveats.** Everything runs locally, so confidential or embargoed record sets never leave the machine. Active learning changes the screening order, not the inclusion criteria: you still decide when to stop, and stopping rules are a live methodological debate — report the model, the seed set and the stopping criterion in the methods. No built-in dual-reviewer conflict resolution in the way Rayyan or Covidence provide it.

### [bibliometrix / biblioshiny](https://www.bibliometrix.org/)

`Free` · beginner 3/5 · R bibliometrics

Open-source R package on CRAN for science mapping — descriptive bibliometrics, co-citation and coupling networks, collaboration maps, thematic and conceptual-structure maps, Lotka's law — with 'biblioshiny', a Shiny front end that runs the whole workflow without writing code; imports Scopus, Web of Science, PubMed, Dimensions, Lens, Cochrane and OpenAlex data.

**Access.** 'install.packages("bibliometrix")'; then 'library(bibliometrix); biblioshiny()' opens the GUI in a browser, or script it: 'M <- convert2df(file, dbsource = "pubmed", format = "pubmed"); results <- biblioAnalysis(M)'.

**Caveats.** Needs R, and the richest inputs (Scopus, Web of Science) require subscription access to export — PubMed, OpenAlex and Lens keep it usable without one. Results are highly sensitive to deduplication and author-name normalisation, so check the merged records before reporting counts. Cite Aria & Cuccurullo (2017), Journal of Informetrics 11(4), 959-975.

### [Bioicons](https://bioicons.com/)

`Free` · beginner 5/5 · scientific illustration assets

Free library of roughly 2,800 scientific illustration icons (molecular biology, cells, organisms, lab equipment, machine learning, geography) downloadable as SVG, each labelled with its licence: CC0, CC BY, CC BY-SA or MIT.

**Access.** Web interface: search, click an icon to download the SVG, then place it in Inkscape, PowerPoint or a figure script. No account.

**Caveats.** Icons under CC BY / CC BY-SA require attribution and, for ShareAlike, affect how derived figures may be licensed — the site lists the licence and author per icon. A genuinely free-licence alternative to subscription illustration tools whose free tiers restrict publication use. SciDraw (scidraw.io) covers neuroscience-style figures under similar licences.

### [ColorBrewer](https://colorbrewer2.org/)

`Free` · beginner 5/5 · colour palettes

Palette selector by Cynthia Brewer and Mark Harrower (Penn State) for sequential, diverging and qualitative colour schemes, with explicit filters for colourblind-safe, print-friendly and photocopy-safe options; the same palettes ship in matplotlib, ggplot2 and QGIS.

**Access.** Web interface: pick class count and scheme type, copy HEX/RGB values or export; in R via 'RColorBrewer::brewer.pal()' or 'scale_fill_brewer()', in Python via matplotlib's colormap names.

**Caveats.** Built for maps and categorical data; for continuous scientific data the perceptually uniform viridis family (matplotlib's default) is usually the better choice. Colourblind-safe filtering covers the common deuteranopia case — still check final figures with a simulator, and never encode a variable by colour alone.

### [conda-forge and Miniforge](https://conda-forge.org/)

`Free` · beginner 3/5 · scientific package channel

Community-run conda channel (a NumFOCUS fiscally sponsored project) providing cross-platform builds of scientific packages including compiled non-Python dependencies; Miniforge is the BSD-3 minimal installer that sets conda-forge as the only default channel.

**Access.** Install Miniforge from github.com/conda-forge/miniforge, then 'conda create -n proj python=3.12 gdal r-base' and 'conda env export --from-history > environment.yml' for a shareable environment (this is also what Binder reads).

**Caveats.** Prefer Miniforge over the Anaconda Distribution: Anaconda's terms require a paid Business licence for users inside organisations with 200+ employees/contractors (their pricing page exempts academic institutions and non-profit research organisations), while conda-forge carries no such condition. Environment solving can be slow — pixi or the mamba solver are faster front-ends to the same packages.

### [DataLad](https://www.datalad.org/)

`Free` · beginner 2/5 · data versioning and provenance

Layer over git and git-annex for version-controlling arbitrarily large files and nested dataset hierarchies without a central server: content is fetched on demand, and 'datalad run' records the exact command that produced an output so results can be recomputed.

**Access.** 'pip install datalad' (also conda-forge, apt, Homebrew) plus git-annex; then 'datalad create', 'datalad save -m', 'datalad get <file>', 'datalad run -o out.csv python analyse.py'.

**Caveats.** git-annex must be installed separately and is the main friction on Windows and macOS. The conceptual load is higher than DVC's; the free DataLad Handbook is the practical entry point. Used to distribute large neuroimaging collections (e.g. OpenNeuro datasets).

*Also listed under: neuro-psych.*

### [Docker (Engine and Desktop)](https://docs.docker.com/desktop/)

`Freemium` · beginner 2/5 · containers

Containers freeze an entire software environment, OS libraries included, so an analysis runs identically on your laptop, a collaborator's machine and a reviewer's. Docker Engine on Linux is open source (Apache-2.0); Docker Desktop for macOS/Windows is free for personal use, education, non-commercial open source, and small businesses under 250 employees AND under $10M annual revenue.

**Access.** Write a Dockerfile, 'docker build -t myproj .', then 'docker run --rm -v $PWD:/work myproj'; ready-made research images exist (Rocker for R, jupyter/docker-stacks for Python) and images are shared via Docker Hub or ghcr.io.

**Caveats.** Organisations above the size thresholds need a paid Desktop subscription (Engine on Linux is unaffected). Docker Hub rate-limits anonymous pulls. Most HPC clusters forbid Docker: use Apptainer/Singularity, which converts Docker images and needs no root. Podman is a daemonless, fully open-source drop-in for most commands.

### [DVC (Data Version Control)](https://dvc.org/)

`Free` · beginner 3/5 · data versioning and pipelines

Apache-2.0 Git companion (3.67.1) that keeps large data and model files out of the repository: Git tracks small .dvc pointer files while the content lives in an S3, Google Cloud Storage, Azure, Google Drive, SSH/SFTP, WebDAV or HTTP remote, and 'dvc repro' reruns only the pipeline stages whose dependencies changed; it also tracks experiments and metrics.

**Access.** 'pip install dvc' plus a remote extra ('pip install "dvc[s3]"'); then 'dvc init', 'dvc add data/raw.csv', 'git commit', 'dvc remote add -d store s3://bucket/path', 'dvc push'. Collaborators clone the Git repo and run 'dvc pull'.

**Caveats.** DVC is free but you supply the storage, and free-tier cloud buckets are small; a university S3-compatible store or a plain SSH remote is the cheapest route. The repository now lives at github.com/treeverse/dvc (it moved from Iterative), and the hosted Studio dashboard is a separate commercial product. For fetch-on-demand access to very large nested datasets, DataLad is the more common choice in academia; DVC is more ML-flavoured.

### [eLabFTW](https://www.elabftw.net/)

`Free` · beginner 2/5 · electronic lab notebook

AGPLv3 electronic lab notebook and inventory system (5.6.x, August 2026) with timestamped and signable experiment entries, reusable templates, a resources database for plasmids, chemicals, antibodies and equipment, a booking scheduler, fine-grained permissions, and export to PDF, ZIP and the .eln interchange format. No features are held back behind a paywall.

**Access.** Self-hosted: run the elabftw/elabimg container with Docker or Podman on a lab server or VPS behind HTTPS, then everyone works in the browser. Deltablot (the developers) sell hosted instances and support for groups without sysadmin capacity.

**Caveats.** Somebody has to run, update and back up the server — the real blocker for a lone researcher, so ask whether your institution already operates an instance. Trusted RFC 3161 timestamping is built in, but some timestamping authorities charge. It is an ELN, not a LIMS: sample logistics and instrument integration are basic compared with dedicated systems.

### [ELAN](https://archive.mpi.nl/tla/elan)

`Free` · beginner 3/5 · audio/video annotation

GPL-3 annotation tool from The Language Archive at the Max Planck Institute for Psycholinguistics: an unlimited number of time-aligned annotations on hierarchically related tiers, several synchronised media files at once, controlled vocabularies, and export to CSV, Praat, subtitles and other formats.

**Access.** Download for Windows/macOS/Linux (Java); .eaf annotation files are XML, so they can be scripted and version-controlled alongside the media.

**Caveats.** The Java interface is dated and the tier/type model takes real time to learn. Standard in linguistics, gesture, sign language and interaction research; overkill if you only need interview transcripts.

*Also listed under: humanities.*

### [faster-whisper (OpenAI Whisper models)](https://github.com/SYSTRAN/faster-whisper)

`Free` · beginner 3/5 · speech-to-text library

MIT-licensed CTranslate2 reimplementation of OpenAI's Whisper speech recognition that is up to about 4x faster than openai/whisper at the same accuracy while using less memory, and runs usably on CPU with int8 quantization. Whisper models range from tiny (39M parameters, ~1 GB VRAM) to large (1550M, ~10 GB) and turbo (809M, ~6 GB).

**Access.** 'pip install faster-whisper'; then 'from faster_whisper import WhisperModel; model = WhisperModel("small", device="cpu", compute_type="int8")' and iterate over 'model.transcribe("interview.m4a")'.

**Caveats.** Model weights are MIT-licensed and downloaded once (hundreds of MB to several GB). Accuracy varies sharply by language, accent and recording quality, and Whisper hallucinates plausible text over silence or noise — always check against the audio. GPU use requires matching cuBLAS/cuDNN libraries. For a GUI use noScribe; whisper.cpp is another CPU-friendly route.

### [G*Power](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower)

`Free` · beginner 4/5 · statistical power analysis

Free power-analysis program from Heinrich Heine University Düsseldorf (3.1.9.7 for Windows, March 2020; 3.1.9.6 for macOS, February 2020) covering a priori, post hoc, sensitivity and criterion analyses for t, F, chi-square, z and exact tests — including ANOVA/ANCOVA designs, correlations, and linear, logistic and Poisson regression — with plots of power against sample size.

**Access.** Download the Windows or macOS binary from the department page (no account); choose test family, statistical test and type of power analysis, enter effect size, alpha and desired power to get N, and use 'X-Y plot for a range of values' to produce the power curve figure a grant or preregistration needs.

**Caveats.** Free for everyone including commercial users, but closed source and redistribution is prohibited. No native Apple Silicon build yet (an Intel build under Rosetta is the current route), and there is no scripting layer, so record your inputs manually in the preregistration for reproducibility. For designs it does not cover — multilevel/mixed models, SEM, complex simulations — use R (pwr, simr, WebPower) instead.

*Also listed under: neuro-psych.*

### [Git](https://git-scm.com/)

`Free` · beginner 3/5 · version control

The GPL-2 distributed version control system underneath nearly every reproducible-research workflow; works fully offline with local repositories, and every clone contains the entire history.

**Access.** 'apt install git' / 'brew install git' / winget, or the Xcode command line tools; core loop is 'git init', 'git add -p', 'git commit -m', 'git log', and branches for exploratory analyses.

**Caveats.** Binary files (Word documents, large data, images) version poorly and bloat repositories permanently: use git-annex/DataLad or a data repository for those, and never commit credentials or participant data. The learning curve is real; Pro Git and Happy Git with R (both catalogued here) are the standard free routes in.

### [GitHub Free](https://github.com/)

`Free (registration), email` · beginner 4/5 · code hosting and CI

Free personal plan with unlimited public and private repositories and unlimited collaborators, 2,000 GitHub Actions minutes per month and 500 MB of storage shared between Actions artifacts and Packages for private repos (Actions is unmetered on public repos), plus GitHub Pages for public repositories.

**Access.** Create a repo in the browser or with the gh CLI, push over HTTPS/SSH; automate tests, manuscript builds or data pipelines with .github/workflows/*.yml; publish project sites with Pages.

**Caveats.** Protected branches, required reviewers, wikis and repository insight graphs need Pro/Team on private repos. GitHub is not an archive: pair releases with Zenodo (DOI) or Software Heritage for preservation. Codeberg (non-profit, Forgejo) and GitLab Free (400 CI compute minutes/month on gitlab.com) are alternatives if you would rather not host research code with Microsoft.

### [Inkscape](https://inkscape.org/)

`Free` · beginner 3/5 · vector graphics

GPL vector graphics editor whose native format is SVG, with PDF and EPS import/export, node editing, path operations and a LaTeX-aware PDF+LaTeX export mode; the standard free tool for assembling multi-panel figures and cleaning up plots before submission.

**Access.** Install from inkscape.org or via apt/brew/flatpak; command line conversion works too: 'inkscape figure.svg --export-type=pdf --export-filename=figure.pdf'.

**Caveats.** Editing a PDF exported by matplotlib or ggplot2 works, but text can arrive as outlines or shift if fonts are not embedded; export plots as SVG or PDF with fonts embedded. Large documents can be slow. For quick boxes-and-arrows diagrams, diagrams.net (draw.io) or Excalidraw (MIT) are lighter.

### [jamovi](https://www.jamovi.org/)

`Freemium` · beginner 5/5 · statistics GUI

Free and open statistics package with a spreadsheet interface designed to be familiar to SPSS users, built on R; every analysis can display the equivalent R syntax, and community modules extend it to mediation, SEM, survival and more.

**Access.** Download the desktop app for Windows/macOS/Linux; imports CSV plus SPSS, Stata and SAS files; install extra analyses from the in-app jamovi library.

**Caveats.** The desktop app is the free route; jamovi Cloud (browser version) has paid tiers. Module quality varies because modules are community-contributed R wrappers — check the underlying package and cite it.

*Also listed under: medicine, neuro-psych, social.*

### [JASP](https://jasp-stats.org/)

`Free` · beginner 5/5 · statistics GUI

Free AGPL-3 statistics package (version 0.98.1, July 2026) from the University of Amsterdam with a point-and-click interface over R, offering frequentist and Bayesian versions of t-tests, ANOVA, regression, mixed models, meta-analysis, SEM and network analysis, with APA-formatted output tables.

**Access.** Download the installer for Windows 10/11, macOS 14+, Linux (Flatpak) or ChromeOS; opens CSV, SPSS .sav and other formats; results, data and annotations save into a single .jasp file.

**Caveats.** Needs about 4 GB RAM and 4 GB disk. Analyses run in R but there is no scripting layer, so a JASP analysis is reproducible mainly by shipping the .jasp file. Some modules are marked experimental; check what the underlying R package does before reporting results.

*Also listed under: neuro-psych, social.*

### [JupyterLab](https://jupyter.org/)

`Free` · beginner 5/5 · notebooks

Free BSD-licensed browser-based notebook environment and IDE supporting Python, R, Julia and 100+ other kernels; runs locally, on a shared server (JupyterHub), or through Binder and other hosted services.

**Access.** 'pip install jupyterlab' or 'conda install -c conda-forge jupyterlab', then 'jupyter lab'; notebooks are .ipynb JSON files that can be executed headlessly with nbconvert or papermill.

**Caveats.** Notebooks diff and merge badly in git — use jupytext, nbdime, or write in Quarto .qmd instead. Out-of-order execution is a common source of irreproducible results: restart and run all before sharing, and keep heavyweight computation in scripts called by a pipeline.

### [KoboToolbox](https://www.kobotoolbox.org/)

`Free tier, email` · beginner 4/5 · field data collection

Open-source data-collection platform built for fieldwork: XLSForm-based questionnaires, the KoboCollect Android app and web forms that work fully offline, GPS/photo/audio/barcode questions, skip logic, and REST API plus CSV/XLS/SPSS export. The hosted 'Community' plan is free.

**Access.** Register on eu.kobotoolbox.org (EU) or kf.kobotoolbox.org (global), build a form in the browser or upload an XLSForm, deploy, and collect via the Android app or a web link; data via /api/v2/ or direct export.

**Caveats.** The free plan enforces monthly submission, storage and transcription/translation limits (they have been tightened over time — check the current pricing page before planning a large study). Exceeding limits blocks new submissions, and storage over the limit for more than 90 days leads to deletion of media attachments, though not of submissions. Self-hosting the open-source stack removes the caps but requires Docker and sysadmin time.

*Also listed under: medicine, social.*

### [LanguageTool](https://languagetool.org/)

`Freemium` · beginner 5/5 · grammar and style checking

Multilingual grammar, spelling and style checker covering 25+ languages, with an LGPL open-source core that can be run offline as a local server and free integrations for browsers, LibreOffice, Obsidian and Zettlr.

**Access.** Use the web editor or browser extension, or self-host: download the standalone package and run 'java -jar languagetool-server.jar --port 8081', then point your editor's LanguageTool plugin at http://localhost:8081.

**Caveats.** The hosted free service checks a limited amount of text per request and rate-limits heavy use; 'Picky mode' and the advanced style/rephrasing suggestions are Premium-only. Self-hosting removes the text limits and keeps unpublished manuscripts off third-party servers, but the strongest models remain in the paid product.

### [LimeSurvey Community Edition](https://community.limesurvey.org/)

`Free` · beginner 2/5 · self-hosted surveys

Free, self-hostable open-source survey platform (stable 7.0.11 as of August 2026) with a wide range of question types, multilingual questionnaires, quotas, expression-based branching and piping, anonymous and token-based participation, and export to CSV, SPSS, R and Stata.

**Access.** Download the CE archive and deploy on PHP + MySQL/MariaDB hosting (many low-cost shared hosts suffice); design surveys in the browser and export responses directly to R or SPSS syntax.

**Caveats.** Self-hosting means you own updates, backups, TLS and the data-protection/ethics obligations — which is also why it is often the only option that satisfies an ethics committee. Some features and all support are reserved for the paid LimeSurvey Cloud.

*Also listed under: social.*

### [marimo](https://marimo.io/)

`Free` · beginner 4/5 · reactive Python notebook

Apache-2.0 Python notebook that stores each notebook as a plain .py file and re-runs dependent cells automatically when an upstream cell changes, so there is no stale hidden state; deleting a cell also removes its variables. The same file can be run as a script, imported as a module, served as an interactive web app, or exported to WebAssembly-powered HTML, and it has built-in SQL and UI widgets.

**Access.** pip install marimo, then marimo edit to open the browser editor or marimo run to serve a notebook as an app. Source at github.com/marimo-team/marimo.

**Caveats.** Notebooks are pure Python rather than .ipynb, which is what makes them diff-able in Git, but it also means collaborators need marimo to open them as notebooks and that existing Jupyter notebooks have to be converted. Reactive execution re-runs downstream cells on every change, so long-running or expensive cells need caching or explicit gating. It is a much younger project than Jupyter, so the extension ecosystem and institutional documentation are thinner.

### [Nextflow](https://www.nextflow.io/)

`Free` · beginner 2/5 · workflow manager

Apache-2.0 dataflow workflow engine (v26.04.6, July 2026) that runs the same pipeline unchanged on a laptop, on SLURM/SGE/LSF/PBS/HTCondor clusters, on Kubernetes and on AWS/Azure/Google Cloud, with per-process Conda, Docker or Apptainer environments and '-resume' caching of completed tasks; the nf-core community publishes ready-made pipelines such as nf-core/rnaseq and nf-core/sarek.

**Access.** 'curl -s https://get.nextflow.io | bash' (or 'conda create --name nf-env bioconda::nextflow'); needs Bash 3.2+ and Java 17-26. Run an existing pipeline with 'nextflow run nf-core/rnaseq -profile singularity -resume', or write your own main.nf of processes and channels.

**Caveats.** The Groovy-based DSL2 is a steeper climb than Snakemake's Python for people who only know Python/R, and Java 17+ is a hard requirement (support for older Java was dropped in 25.04). The engine and all nf-core pipelines are free; the Seqera Platform (hosted monitoring and launching, from the company that employs the core developers) is a separate commercial product with a limited free tier.

### [noScribe](https://github.com/kaixxx/noScribe)

`Free` · beginner 5/5 · offline interview transcription

GPL-3 desktop app that transcribes interviews entirely on your own machine using faster-whisper plus pyannote speaker diarization, and includes an editor that keeps the audio and the transcript in sync for correction. Windows, macOS (Intel and Apple Silicon) and Linux.

**Access.** Download the installer for your platform, pick the audio/video file, choose the 'precise' or 'fast' model, then correct the result in the built-in editor and export to DOCX/VTT/plain text.

**Caveats.** Slow on CPU-only laptops — up to about three hours for a one-hour interview — and the download is several GB because models are bundled. Diarization and punctuation need manual correction. The decisive advantage for interview research is that nothing leaves the machine, which fits confidentiality and ethics constraints that cloud transcription services do not. aTrain is a comparable Windows-focused alternative.

### [Obsidian](https://obsidian.md/)

`Freemium` · beginner 5/5 · notes and PKM

Local-first note-taking app over a plain folder of Markdown files, with backlinks, tags, graph view, canvas, and a large community plugin ecosystem (Zotero integration, citations, Pandoc export, dataview). Free for every purpose including commercial use, with no account required.

**Access.** Download the desktop or mobile app and point it at a folder of .md files; version the folder with git or sync it with Nextcloud/Dropbox/Syncthing for free.

**Caveats.** The app itself is proprietary, though your notes stay as portable Markdown files. Optional paid services: Sync at $4-5/month and Publish at $8-10/month per site; neither is needed if you use git or another file-sync tool. Plugins are community-maintained and vary in quality and longevity.

### [OCRmyPDF](https://ocrmypdf.readthedocs.io/)

`Free` · beginner 4/5 · OCR for scanned PDFs

MPL-2.0 command-line tool that adds a searchable, selectable text layer under the original page images of a scanned PDF using Tesseract, with deskew, rotation, optimisation and validated PDF/A output, and parallel processing across cores.

**Access.** 'apt install ocrmypdf' / 'dnf install ocrmypdf' / 'brew install ocrmypdf'; then 'ocrmypdf -l eng+fra --deskew --output-type pdfa in.pdf out.pdf'; language packs install separately (e.g. tesseract-ocr-fra).

**Caveats.** Output quality depends on scan resolution (300 dpi or better) and on having the right Tesseract language pack; handwriting and complex historical typefaces still do badly. Tesseract itself (Apache-2.0, 100+ languages) can be used directly on loose images.

### [OpenRefine](https://openrefine.org/)

`Free` · beginner 4/5 · data cleaning

BSD-3-Clause desktop tool (3.10.x, 2026) for messy tabular data: faceting, clustering of near-duplicate values (fingerprint, n-gram, phonetic), GREL transformations, splitting and reshaping columns, and reconciliation of free-text names against Wikidata and other reconciliation services. Data are processed locally and every step is recorded as a replayable JSON operation history.

**Access.** Download for Windows (bundled Java), macOS or Linux (needs a Java runtime), run it, and work at http://127.0.0.1:3333; import CSV/TSV/Excel/JSON/XML/RDF, clean, then export the cleaned table and the operation history JSON so the same cleaning can be replayed on the next batch.

**Caveats.** Nothing is uploaded anywhere, which makes it usable for sensitive data. It is memory-bound: the default JVM heap comfortably handles a few hundred thousand rows, and larger files need the heap raised in the settings. Save the operation history alongside the raw file — that, not the cleaned CSV, is the reproducible artefact.

*Also listed under: humanities.*

### [Overleaf (free plan)](https://www.overleaf.com/)

`Free tier, email` · beginner 5/5 · collaborative LaTeX editor

Browser LaTeX editor with a preconfigured TeX Live, thousands of journal and thesis templates, and unlimited projects on the free plan; free compiles time out at 10 seconds (paid plans get 240 s), one collaborator per project, and document history limited to the previous 24 hours.

**Access.** Web interface with a free account; write, compile and download the PDF or the project .zip; per-project limits are 2,000 files, 7 MB of editable material and 50 MB per upload.

**Caveats.** The 10-second compile timeout is the real constraint: book-length documents, big TikZ figures or large bibliographies will fail on the free plan. Git/GitHub/Dropbox integration, track changes and full version history are paid. The Community Edition (AGPL) can be self-hosted, and some universities hold site licences that upgrade personal accounts. For offline work, a local TeX Live plus git avoids all of these limits.

*Also listed under: physics, mathematics, publishing.*

### [Pandoc](https://pandoc.org/)

`Free` · beginner 3/5 · document conversion

GPL document converter between Markdown, LaTeX, HTML, DOCX, ODT, EPUB, JATS, reStructuredText and dozens of other formats, with CSL citation processing (--citeproc) and a filter/template system; PDF output via pdflatex, lualatex, xelatex, tectonic, typst, weasyprint and others.

**Access.** 'brew install pandoc' / 'apt install pandoc' / winget; then e.g. 'pandoc paper.md --citeproc --bibliography=refs.bib --csl=apa.csl -o paper.docx'.

**Caveats.** Journal DOCX templates and complex LaTeX macros rarely survive conversion untouched; budget time for cleanup. PDF output needs a separate engine installed (TeX Live, Typst or a HTML-to-PDF tool).

### [Podman](https://podman.io/)

`Free` · beginner 3/5 · containers for reproducible environments

Apache-2.0 daemonless engine for OCI containers and images, with a command set that mirrors Docker's (podman run, build, pull, push) and support for running containers rootless as an ordinary user. Podman Desktop adds a GUI on Linux, macOS and Windows.

**Access.** Install from your Linux distribution's package manager, Homebrew on macOS, or the installers on podman.io; existing docker command lines generally work unchanged, and many users alias docker to podman.

**Caveats.** The practical reason to prefer it over Docker Desktop is licensing: Podman and Podman Desktop are open source with no commercial subscription tier, whereas Docker Desktop's licence has paid conditions that an unaffiliated researcher or small company has to check. On macOS and Windows it runs containers inside a managed Linux VM, so start-up time and volume-mount behaviour differ from native Linux. Docker Compose files need extra setup (podman-compose, or Podman's Docker-compatible socket) rather than working out of the box.

### [PsychoPy](https://www.psychopy.org/)

`Free` · beginner 4/5 · experiment builder

GPL-3 application for building and running behavioural experiments (2026.2.3, August 2026) with a graphical Builder, a Python Coder view and frame-accurate stimulus timing on standard hardware; the same study exports to JavaScript (PsychoJS) so it can be run in a browser for online data collection.

**Access.** Standalone installer for Windows/macOS, or 'pip install psychopy' into a dedicated environment; assemble routines and loops in Builder, press Run, and trial data are written as CSV plus a full log. 'Sync to Pavlovia' publishes the online version.

**Caveats.** The desktop app is free and open source; running studies online through Pavlovia costs per-participant credits or an institutional licence, and self-hosting the generated PsychoJS is possible but fiddly. Timing accuracy depends on your monitor, OS and drivers — run the bundled timing tests rather than assuming it. Free alternatives: OpenSesame (GPL) for desktop, jsPsych or lab.js for browser studies.

*Also listed under: neuro-psych.*

### [QualCoder](https://github.com/ccbogel/QualCoder)

`Free` · beginner 3/5 · qualitative analysis

LGPL-3 desktop QDA application (latest release 3.8.2, 26 February 2026) in Python/Qt that codes text (txt, docx, odt, html, md, epub, rtf, PDF) plus images, audio and video, with hierarchical codes, memos, case and attribute management, coder comparison with kappa, and visual reports.

**Access.** Download from GitHub releases: Windows installer or portable exe, a macOS app bundle for Apple Silicon, and a Linux (Ubuntu) executable; or run from source in a virtualenv ('pip install -r requirements.txt'). Each project is a local folder with an SQLite database, and projects can be imported from Taguette .sqlite3 files.

**Caveats.** Functional rather than polished, and there is no cloud collaboration — team coding means passing the project folder around. The optional AI features call external LLM APIs; sending interview transcripts to a third-party API may breach your ethics approval, so leave them off unless cleared.

*Also listed under: social.*

### [Quarto](https://quarto.org/)

`Free` · beginner 4/5 · reproducible publishing

MIT-licensed publishing system built on Pandoc that renders .qmd documents mixing prose with R, Python, Julia or Observable code into articles, PDFs, websites, books, slides and journal templates; the v1.10 line is current in August 2026.

**Access.** Install the CLI (installers, Homebrew, or 'quarto install tinytex' for PDF), then 'quarto render report.qmd' / 'quarto preview'; editors: VS Code, RStudio, JupyterLab, Positron, or any text editor.

**Caveats.** Needs a working R or Python install for code execution and TeX (TinyTeX is enough) for PDF. Journal article templates ('quarto use template') exist for a limited set of publishers; anything else still needs manual reformatting at submission.

### [Rayyan (free plan)](https://www.rayyan.ai/)

`Free tier, email` · beginner 4/5 · systematic review screening

Web tool for collaborative title/abstract screening: import RIS/EndNote/CSV exports, blind two-reviewer screening with conflict resolution, duplicate detection, keyword highlighting and relevance predictions. The free plan allows 3 active reviews, 2 invited reviewers and 1 sample.

**Access.** Web interface with a free account; upload the search exports from each database, invite collaborators, screen with include/exclude/maybe labels and reasons, then export decisions as RIS or CSV for the PRISMA count.

**Caveats.** The free tier is much narrower than it used to be: PRISMA flow diagrams, auto-resolving duplicates, unlimited samples and more than 3 active reviews start at $4.99/seat/month billed annually, and AI extraction features are dearer. Records are stored on Rayyan's servers, which some ethics approvals do not permit. ASReview is the fully local, fully free alternative if you can install Python.

### [renv](https://rstudio.github.io/renv/)

`Free` · beginner 4/5 · R environment management

Records the exact versions of every R package a project uses in renv.lock and installs them into a project-private library, so a collaborator (or you in a year) can rebuild the same environment.

**Access.** 'install.packages("renv")'; run 'renv::init()' inside the project, 'renv::snapshot()' after adding packages, and 'renv::restore()' on another machine; commit renv.lock to git.

**Caveats.** Pins packages, not R itself or system libraries, so full reproducibility still needs a container or a Rocker image. Restoring old versions may require compiling from source, which can fail without build tools installed.

### [RStudio Desktop (open source)](https://docs.posit.co/ide/user/)

`Free` · beginner 5/5 · IDE

Free AGPL desktop IDE for R (and usable with Python) from Posit: editor, console, environment and plot panes, package management, a Git pane, and one-click rendering of R Markdown and Quarto documents; Windows, macOS and Linux.

**Access.** Install R from CRAN first, then the RStudio Desktop open-source build; use Projects plus renv for per-project libraries and the Git pane (or the terminal) for version control.

**Caveats.** R must be installed separately. Posit's server products (Workbench, Connect) are commercial, and Posit Cloud's free tier caps monthly project hours. Posit's newer Positron IDE is also free to download but is not OSI open source.

### [SingleFile](https://github.com/gildas-lormeau/SingleFile)

`Free` · beginner 5/5 · web page archiving

AGPL browser extension for Chrome, Firefox, Edge, Safari, Brave, Vivaldi and Opera that saves a complete web page — CSS, images, fonts, frames — into one self-contained HTML file, so an online source can be cited and re-read exactly as it appeared on the day you used it.

**Access.** Install from your browser's extension store and click the toolbar icon (or use auto-save rules); batch capture with the separate single-file-cli ('npx single-file <url>').

**Caveats.** Pages behind logins, paywalls or infinite scroll may capture incompletely, and video/audio is not preserved. For a publicly verifiable snapshot, also submit the URL to the Internet Archive's Save Page Now and cite that timestamped link. Saved files can be several MB each.

### [Snakemake](https://snakemake.readthedocs.io/en/stable/)

`Free` · beginner 2/5 · workflow manager

Python-based, Make-like workflow engine (version 9.26.1 in August 2026) that reruns only steps whose inputs or code changed and runs the same workflow on a laptop, a Slurm/SGE cluster or the cloud without editing the rules; per-rule conda environments or containers pin software.

**Access.** 'conda install -c conda-forge -c bioconda snakemake' or 'pip install snakemake'; write a Snakefile of input/output rules and run 'snakemake --cores 4 --software-deployment-method conda'.

**Caveats.** Cluster and cloud execution now live in separate executor plugins that must be installed alongside. Wildcard and DAG errors are the usual stumbling block for newcomers. Cite Moelder et al. (2021), F1000Research 10:33.

*Also listed under: biology.*

### [Tabula](https://tabula.technology/)

`Free` · beginner 4/5 · extracting tables out of PDFs

MIT-licensed tool, originally built by and for journalists, that pulls tables out of text-based PDFs into CSV or Excel. It runs entirely on your own machine as a local server driven from your browser, so the PDFs are never uploaded anywhere.

**Access.** Download the macOS, Windows or Linux build from tabula.technology (Java is required on Windows and Linux), run it, then open http://127.0.0.1:8080 and drag a selection over each table to export it.

**Caveats.** Only works on PDFs that contain a real text layer: scanned pages must be OCRed first (OCRmyPDF is the usual route) and even then extraction is unreliable. Selection is manual, so it suits tens of tables rather than thousands; for batch work the underlying tabula-java and tabula-py libraries are the scripting route. Development is slow, with the last repository activity in March 2025, but the released builds still work.

### [Taguette](https://www.taguette.org/)

`Free` · beginner 4/5 · qualitative coding

BSD-3 qualitative coding tool: import documents (PDF, DOCX, HTML, TXT), highlight passages, apply a hierarchical codebook, and export coded excerpts and codebooks to CSV, DOCX or HTML. Runs locally or on a free hosted server at app.taguette.org.

**Access.** 'pip install taguette' then run 'taguette' (opens in your browser), or use the Windows/macOS installers, or register on app.taguette.org for the hosted version; projects are single SQLite files you can back up and move.

**Caveats.** Deliberately minimal: no auto-coding, no inter-rater reliability statistics, no audio/video coding. Development is volunteer and donation-funded (OpenCollective), so releases are slower than commercial QDA tools. Treat the hosted server as a convenience, not an archive — export your project regularly.

### [targets (R)](https://docs.ropensci.org/targets/)

`Free` · beginner 3/5 · R pipeline tool

rOpenSci's MIT-licensed Make-like pipeline package for R: declares a dependency graph of targets, skips steps whose code and upstream data are unchanged, caches results as R objects, and scales out to parallel or cluster execution through the crew package.

**Access.** 'install.packages("targets")'; define a _targets.R script, then 'tar_make()' to run and 'tar_visnetwork()' to inspect the dependency graph; 'tar_read(name)' pulls a cached result into the session.

**Caveats.** R-only. Works properly only when the analysis is written as functions rather than top-to-bottom scripts, so adopting it usually means restructuring existing code. The free 'targets' user manual is the reference.

### [TeX Live / MacTeX](https://tug.org/texlive/)

`Free` · beginner 2/5 · LaTeX distribution

The reference free LaTeX distribution maintained by the TeX user groups: pdfTeX, XeTeX and LuaTeX engines, the CTAN package collection, BibTeX/Biber, and the tlmgr package manager, released annually. MacTeX is the same release packaged for macOS.

**Access.** Run the install-tl network installer for a chosen scheme, or install distro packages (texlive-full on Debian/Ubuntu, mactex on Homebrew); add packages later with 'tlmgr install <package>' and read package docs with 'texdoc <package>'.

**Caveats.** A full installation is several gigabytes and slow to download on poor connections; texlive-scheme-basic plus tlmgr keeps it to a few hundred MB. Distro packages are often a year behind CTAN. If a local install is impractical, use Overleaf or Typst.

*Also listed under: mathematics.*

### [Typst](https://typst.app/)

`Free` · beginner 4/5 · typesetting system

Markup-based typesetting system positioned as a LaTeX alternative; the compiler is Apache-2.0, ships as a single binary and recompiles incrementally for near-instant preview. The hosted web app's free tier allows 200 MB of storage and up to 100 files per project.

**Access.** CLI: 'brew install typst' / 'winget install Typst.Typst' / 'cargo install --locked typst-cli', then 'typst watch paper.typ' for live preview; or use typst.app in the browser with a free account.

**Caveats.** The compiler is fully free; only the web app has tier limits (extra storage and some collaboration features are paid). Few journals accept .typ source, so submission usually still means LaTeX or Word; the package ecosystem is far smaller than CTAN, though it now covers most common needs.

### [uv](https://docs.astral.sh/uv/)

`Free` · beginner 4/5 · Python environment management

Rust-written Python package and project manager that replaces pip, pip-tools, pipx, poetry, pyenv, twine and virtualenv with one very fast tool; it installs Python versions itself and writes a universal lockfile for reproducible environments.

**Access.** 'curl -LsSf https://astral.sh/uv/install.sh | sh' (or PowerShell on Windows); then 'uv init', 'uv add pandas', 'uv run analysis.py'; 'uv pip install' works as a drop-in for pip.

**Caveats.** Young compared with pip and conda, and it does not solve non-Python system dependencies (GDAL, CUDA, BLAS variants) — for those, conda-forge or a container is still the practical route. Made by a venture-funded company (Astral), though the tool itself is permissively licensed.

### [Vale](https://vale.sh/)

`Free` · beginner 3/5 · prose linter for writing style

MIT-licensed command-line linter that checks prose against configurable editorial rules entirely offline. It parses twelve markup formats, including Markdown, reStructuredText, MyST, Quarto, Typst, AsciiDoc, HTML, XML and Org, and can lint comments inside nineteen programming languages; ready-made style packages include Microsoft, Google and Red Hat house styles.

**Access.** A single Go binary, installable from GitHub Releases, Homebrew, conda-forge, npm, PyPI, Chocolatey, WinGet, Snap or Docker Hub. Add a .vale.ini, run vale sync to fetch style packages, then vale <file>.

**Caveats.** It does almost nothing until you configure it: the useful part is choosing or writing a style, and house styles built for software documentation will flag things that are normal in an academic manuscript. It is a rule-based linter rather than a grammar checker, so it complements something like LanguageTool instead of replacing it. There is a separate hosted commercial product; the CLI described here is the MIT-licensed open-source one.

### [VOSviewer](https://www.vosviewer.com/)

`Free` · beginner 4/5 · bibliometric mapping

Free tool from CWTS, Leiden University (1.6.21, June 2026) for building and visualising co-authorship, co-citation, bibliographic-coupling and keyword co-occurrence maps; it reads Web of Science, Scopus, Dimensions and Lens exports and queries Crossref, Europe PMC, Semantic Scholar and OpenAlex directly through their APIs. VOSviewer Online renders and shares the same maps in a browser.

**Access.** Download the Java application for Windows/macOS/Linux (no account) or use app.vosviewer.com; 'Create > Create a map based on bibliographic data' from a downloaded export or an API query, then tune clustering resolution and export the map as PNG/SVG or a shareable .json.

**Caveats.** Free of charge but not open source — it is freeware, so you cannot inspect or fork the clustering implementation. Web of Science, Scopus and Dimensions inputs need a subscription to export; OpenAlex, Crossref and Europe PMC keep the whole workflow free. Maps are exploratory: cluster count and boundaries move with the resolution parameter, so report the settings you used.

### [Zettlr](https://www.zettlr.com/)

`Free` · beginner 4/5 · academic Markdown editor

Free open-source Markdown writing environment built for academics: citations from a Zotero/JabRef library with 9,000+ CSL styles, Pandoc-driven export profiles for journal and conference templates, Zettelkasten-style linking, LaTeX rendering and LanguageTool integration.

**Access.** Download for Windows/macOS/Linux, open a folder of .md files, and point it at a BibTeX or CSL-JSON file exported from Zotero (Better BibTeX auto-export keeps it current).

**Caveats.** Export depends on Pandoc (and a TeX installation for PDF) being installed separately. Smaller plugin ecosystem than Obsidian, and no mobile app.

## Literature

### [Better BibTeX for Zotero](https://retorque.re/zotero-better-bibtex/)

`Free` · beginner 3/5 · Zotero plugin

Zotero plugin that generates stable, collision-free citation keys and keeps a .bib file auto-exported and in sync with a collection, plus HTML/LaTeX and Unicode/LaTeX conversion on export.

**Access.** Download the .xpi from the GitHub releases page, install via Zotero Tools > Plugins, then right-click a collection > Export Collection > Better BibTeX with 'Keep updated' ticked so the .bib in your LaTeX repo stays current.

**Caveats.** Current builds require a recent Zotero (8 or later); version 8.0.25 is the last build with limited Zotero 7 support and gets no further updates. Recent Zotero versions store citation keys natively, so key-pinning behaviour differs from older setups.

### [Hypothesis](https://web.hypothes.is/)

`Freemium, email` · beginner 4/5 · web and PDF annotation

Open-source annotation layer (the 'h' server is BSD-2-Clause) for highlighting and commenting on web pages and PDFs, with private, group, or public annotations that stay attached to the source document.

**Access.** Free account plus browser extension, or prefix a URL with the via proxy; annotations are searchable and exportable through the API; the server and client can be self-hosted with Docker.

**Caveats.** Individual and group annotation is free; the paid product is the institutional LMS/courseware integration. Annotations are stored on Hypothesis servers unless you self-host, so treat confidential material accordingly.

### [JabRef](https://www.jabref.org/)

`Free` · beginner 4/5 · BibTeX reference manager

Free open-source desktop reference manager whose library format is plain BibTeX/BibLaTeX text, so the bibliography can live in the same git repository as the LaTeX manuscript; fetches metadata from DOI, ISBN, arXiv and PubMed identifiers.

**Access.** Install from jabref.org (Windows/macOS/Linux, also Flatpak and Homebrew) and open or create a .bib file; browser extension pushes references from publisher pages.

**Caveats.** No paid tier and no vendor cloud: syncing is your job (git, Nextcloud, or a shared SQL database). PDF management is weaker than Zotero's; many people run JabRef only for the LaTeX-side bibliography.

### [OpenAlex](https://openalex.org/)

`Free tier, email` · beginner 4/5 · bibliographic database and API

Open catalogue of scholarship from the non-profit OurResearch and the successor to Microsoft Academic Graph: 322 million works and 126 million author records (checked 28 August 2026) plus sources, institutions, topics, funders and citation links, released as a CC0 public-domain dataset.

**Access.** REST API, e.g. 'https://api.openalex.org/works?filter=doi:10.1038/nature12373' or filters on institution, year and topic; add '&mailto=you@example.org' for the polite pool. Python client: 'pip install pyalex'. For bulk work take the free full snapshot from the s3://openalex bucket rather than paging the API; web interface at openalex.org.

**Caveats.** The API is now metered: an account gets $1 of API usage per day free (calls are priced at $0.0001, i.e. roughly 10,000 calls/day), resetting at 00:00 UTC, and anonymous requests get far less (response headers showed a $0.10/day ceiling on 28 Aug 2026); beyond that it is prepaid credit in $1 increments or annual Member plans from $5,000/yr. The data themselves remain free and CC0, so the snapshot is the route for large analyses. Author disambiguation, affiliations and abstracts (stored as inverted indexes) all contain errors — verify before publishing counts.

### [Sioyek](https://github.com/ahrm/sioyek)

`Free` · beginner 3/5 · PDF reader for papers

GPL-3 PDF reader built for research papers and textbooks: jump to a cited reference or figure even when the PDF has no embedded links, 'portals' that show a related part of a document in a second window, marks and named bookmarks, and searchable highlights.

**Access.** Installers for Windows/macOS/Linux from GitHub releases, or 'brew install --cask sioyek' / distro packages; keybindings and behaviour configured in a plain-text prefs file.

**Caveats.** Keyboard-driven and vim-flavoured; there is no annotation sync or library management, so pair it with Zotero (whose built-in reader covers ordinary highlighting) or, on macOS, Skim. Maintenance has slowed sharply: the last stable release is v2.0.0 from December 2022, with only a 'sioyek3' alpha since and several hundred open issues, so treat it as a stable-but-static tool rather than an actively developed one.

### [Unpaywall](https://unpaywall.org/)

`Free, email` · beginner 5/5 · open-access discovery

Browser extension and REST API from the non-profit OurResearch that resolves a DOI against publisher and repository records and links to a legally posted free full text when one exists.

**Access.** Install the Chrome/Firefox extension and a tab appears on article pages when a free copy exists; API: GET https://api.unpaywall.org/v2/{doi}?email=you@example.org returns JSON with the best OA location.

**Caveats.** Finds only legally posted copies (publisher OA, author manuscripts, repository and preprint versions); a large share of paywalled literature has none. The API requires an email address in every request and is intended for moderate use; heavy users should take the data dump instead of hammering the endpoint.

### [Zotero](https://www.zotero.org/)

`Freemium` · beginner 5/5 · reference manager

Open-source (AGPL) reference manager, desktop release Zotero 10 as of 2026, with a built-in PDF reader and annotation, browser connectors for Chrome/Firefox/Edge/Safari, word processor plugins for Word/LibreOffice/Google Docs, and free unlimited syncing of bibliographic data.

**Access.** Download the desktop app plus the browser connector; add items with the connector or by DOI/ISBN/arXiv ID via 'Add Item by Identifier'; cite from Word/LibreOffice/Google Docs or export BibTeX/CSL-JSON for LaTeX and Pandoc.

**Caveats.** Local use needs no account. A free account syncs bibliographic data with no limit but only 300 MB of attachment storage; paid tiers are 2 GB $20/yr, 6 GB $60/yr, unlimited $120/yr. Attachments can instead be synced through your own WebDAV server at no cost (WebDAV does not work for group libraries, and group storage is billed to the group owner).

## Compute

### [Binder (mybinder.org)](https://mybinder.org/)

`Free` · beginner 4/5 · ephemeral notebook sessions

Turns a public Git repository with an environment file into a live JupyterLab or RStudio session in the browser. Free sessions get 1-2 GB RAM, up to roughly one CPU-hour, are culled after 10 minutes of inactivity, and last at most about six hours, with no persistent storage.

**Access.** Paste a repository URL at mybinder.org; add environment.yml, requirements.txt or install.R to the repo; embed the generated 'launch binder' badge in the README so readers can run your analysis without installing anything.

**Caveats.** Everything is destroyed when the session ends, so download results. It runs on donated resources from a volunteer federation: capacity fluctuates, builds can be slow, and it is unsuitable for heavy computation, long jobs, or confidential data.

### [GitHub Codespaces (free tier)](https://github.com/features/codespaces)

`Free tier, email` · beginner 4/5 · cloud development environment

Cloud VS Code environments defined by a devcontainer.json in the repository; personal GitHub Free accounts include 120 core-hours and 15 GB of storage per month, i.e. 60 hours on a 2-core machine.

**Access.** From any repo: Code > Codespaces > Create codespace, or 'gh codespace create'; commit a .devcontainer/devcontainer.json so collaborators and reviewers get an identical environment.

**Caveats.** The quota is core-hours, so a 4-core machine burns it twice as fast as a 2-core one. Codespaces stop after 30 minutes idle by default and unused ones are deleted after a retention period; commit and push anything you care about. No GPU on the free tier, and usage beyond the quota is only billable if you add a payment method.

### [Google Colab (free tier)](https://colab.research.google.com/)

`Free tier, email` · beginner 5/5 · hosted notebooks with GPU

Hosted Jupyter notebooks stored in Google Drive and executed on Google VMs. Free sessions run for at most 12 hours, idle sessions are reclaimed, and GPU access is free but rationed: Google states that access to GPUs is 'heavily restricted' on the free tier and deliberately does not publish the quota, which fluctuates with demand.

**Access.** Web interface with a Google account; open any .ipynb from Drive or GitHub (colab.research.google.com/github/<user>/<repo>/blob/main/nb.ipynb), then Runtime > Change runtime type to request a GPU. Install extras per session with '!pip install' and persist outputs by mounting Drive ('from google.colab import drive; drive.mount("/content/drive")').

**Caveats.** Nothing survives the session except what you write to Drive, and a free session can be cut off mid-run when demand is high, so checkpoint long jobs. Notebooks execute on Google infrastructure outside your institution — check ethics and data-protection constraints before uploading participant data. Colab Pro, Pro+ and pay-as-you-go compute units are the paid escape hatch; Binder and Kaggle are the free alternatives when Colab is throttled.

### [Kaggle Notebooks](https://www.kaggle.com/code)

`Free tier, email` · beginner 4/5 · hosted notebooks with GPU/TPU

Free hosted Python/R notebooks with a published weekly accelerator quota (30 GPU hours per week at the time of writing, plus a separate TPU allowance), sessions capped at around 12 hours, background 'Save & Run All' execution, and free hosting for datasets that any notebook can attach.

**Access.** Free account, then Create > Notebook; Settings > Accelerator picks GPU or TPU and Settings > Internet enables package installs; attach a Kaggle Dataset or upload your own, and use 'Save & Run All (Commit)' so the run continues after you close the browser. Notebooks and datasets are shareable by URL or downloadable as .ipynb.

**Caveats.** Quotas are set unilaterally by Kaggle and have changed repeatedly — the live remaining hours are shown in the session sidebar, and the docs are behind a bot check, so verify before planning around a number. Phone verification is required before a notebook may use an accelerator or reach the internet. Sessions are ephemeral apart from /kaggle/working output, and uploaded data sit on US infrastructure (public datasets are visible to everyone), so it is unsuitable for confidential material.

*Also listed under: physics, chemistry, medicine, cs-ml, social, compute.*

## Publishing

### [Journal of Open Source Software (JOSS)](https://joss.theoj.org/)

`Free, email` · beginner 4/5 · diamond open-access journal

Developer-friendly open-access journal for research software with roughly 3,700 papers published and no article processing charges or subscription fees; the paper is a short Markdown file, and what is actually reviewed is the software, openly, in a GitHub issue.

**Access.** Submit at joss.theoj.org with a repository URL and a paper.md plus paper.bib; the review runs as a public GitHub issue with named reviewers; accepted papers get a Crossref DOI and are indexed in DOAJ and Scopus.

**Caveats.** Scope is real software of scholarly value: it needs documentation, tests, contribution guidelines and an OSI-approved licence, and a single analysis script will be rejected as out of scope. Review is volunteer-run, so timelines vary from weeks to months. Sister journals (JOSE for educational material) use the same model.

### [ORCID](https://orcid.org/)

`Free, email` · beginner 5/5 · researcher identifier

Free persistent 16-digit identifier from a non-profit registry, used by most publishers, funders and repositories to attach works, affiliations, funding and peer-review activity to the right person and to survive name changes, transliteration and namesakes; the researcher controls per-item visibility and can export the record.

**Access.** Register free at orcid.org/register with an email address, add works by DOI search-and-link (Crossref/DataCite) or BibTeX import, then paste the iD into manuscript submission and grant systems; public records are readable at https://pub.orcid.org/v3.0/{orcid}/record and an annual public data file is released for bulk use.

**Caveats.** Free for individuals permanently — institutions pay membership for the Member API that writes into records, which is why some universities auto-populate yours. Token access to the Public API needs registered client credentials. Only what you mark public is visible, and auto-population depends on publishers pushing data, so most records still need manual curation.

### [protocols.io (Open Research plan)](https://www.protocols.io/)

`Free tier, email` · beginner 4/5 · protocol and methods sharing

Platform for writing, versioning, running and publishing step-by-step experimental protocols. The free 'Open Research' plan is $0 forever with unlimited public protocols that receive DOIs, up to 2 private protocols, and long-term preservation via CLOCKSS plus mirroring to the Internet Archive and GitHub.

**Access.** Free account, then write or fork an existing protocol, keep it private while you iterate, and publish to mint a citable DOI you reference in the methods section; published protocols are readable without an account, and a REST API is available for programmatic access.

**Caveats.** Only 2 private protocols on the free plan — unlimited private protocols, team workspaces, SAML SSO, audit trails and 21 CFR Part 11 signatures are the paid Enterprise product. Publishing is irreversible: a published protocol gets a DOI and is archived, so check for unpublished methods, personal data and institutional restrictions first. It replaces a supplementary-methods PDF, not a lab notebook — for daily bench records use an ELN such as eLabFTW.

*Also listed under: biology, publishing.*

### [rOpenSci Software Peer Review](https://ropensci.org/software-review/)

`Free` · beginner 3/5 · open software peer review

Free, fully open peer review of R packages in two streams — scientific data lifecycle packages and statistical software — conducted by volunteer editors and reviewers in public GitHub issues; accepted packages join the rOpenSci suite and can be fast-tracked to a JOSS paper.

**Access.** Read the dev guide, check scope, then open a submission issue at github.com/ropensci/software-review; reviewers use a public checklist covering documentation, tests and API design.

**Caveats.** R packages only, and the scope is genuinely restricted (data access, manipulation, visualization for science; statistical algorithms). Timelines depend on volunteer availability. The review is a quality process, not itself a journal — the citable output comes via JOSS.

### [Software Heritage](https://www.softwareheritage.org/)

`Free` · beginner 3/5 · source code archive

Non-profit universal archive of publicly available source code, built with Inria and supported by UNESCO, that continuously harvests GitHub, GitLab and other forges and issues intrinsic identifiers (SWHIDs) so a paper can cite an exact revision, directory or single file rather than a URL that may rot.

**Access.** Submit a public repository URL through 'Save Code Now' at archive.softwareheritage.org, then copy the SWHID from the archived object and cite it; Zenodo/GitHub release archiving also feeds records into the archive.

**Caveats.** Only publicly accessible repositories can be archived — nothing private or behind a login. Save Code Now requests are queued and rate-limited, and large repositories take time to appear. A SWHID identifies code, not a citable landing page with rich metadata, so pair it with Zenodo when you need a DOI.

### [Zenodo](https://zenodo.org/)

`Free (registration), email` · beginner 5/5 · data and software archiving with DOI

CERN-operated general-purpose repository that mints DOIs for datasets, software releases, figures, slides, theses and preprints; default limits are 50 GB and 100 files per record (up to 200 GB on request), with versioned records under a concept DOI that always points to the latest version.

**Access.** Web upload with a free account, the REST API, or the GitHub integration: link your account, flip the switch for a repository, and each new GitHub release is archived automatically with its own DOI (records are also propagated to Software Heritage).

**Caveats.** No charge to depositors, funded through CERN and EU projects. Published files cannot be edited or removed — only superseded by a new version — so check licences, consent and personal data before publishing. Where a domain-specific repository exists (GenBank, PDB, OpenNeuro, ICPSR), use that instead or as well.

## Funding

### [Google Summer of Code](https://summerofcode.withgoogle.com/)

`Free, application` · beginner 3/5 · paid open-source project

Google-funded programme that pairs newcomers to open source with a mentoring organisation for a 12+ week project sized at roughly 90, 175 or 350 hours, with a stipend on passing evaluations; many mentoring organisations are scientific software projects (NumFOCUS, Bioconductor-adjacent tools, astronomy and neuroscience stacks).

**Access.** Browse the annual organisation list, start contributing to an org early, then submit a project proposal in the spring application window at summerofcode.withgoogle.com.

**Caveats.** Open to anyone 18+ who is new to open source — not only students — but it is highly competitive, and proposals from people who have already contributed to the org do far better. Stipends vary by country of residence, and there are limits on repeat participation.

### [NumFOCUS Small Development Grants](https://numfocus.org/programs/small-development-grants)

`Free, application` · beginner 2/5 · small project grants

Grants of up to $10,000 for concrete work on open-source scientific software — code, documentation, website work, workshops and sprints — awarded in two rounds per year, with at most two grants per project per calendar year and work that must finish within a year.

**Access.** Proposals are submitted by (or through) the maintainers of an eligible project during the call window announced on the NumFOCUS site.

**Caveats.** Only NumFOCUS fiscally sponsored or affiliated projects are eligible, one proposal per project per round, so an individual contributor has to apply via such a project rather than directly. Amounts suit focused tasks, not salaries.

### [Outreachy](https://www.outreachy.org/)

`Free, application` · beginner 3/5 · paid internship

Software Freedom Conservancy internship programme for people who face underrepresentation or systemic bias in tech: three-month remote internships with a $7,000 total stipend, covering coding, documentation, UX, data science, research and marketing projects across open-source communities.

**Access.** Apply during the initial application window (roughly February and August), then complete a public contribution period with a mentor before the final application; the May 2026 and December 2026 cohorts are the current cycles.

**Caveats.** Eligibility is based on underrepresentation and on being free to work full time during the internship, not on being enrolled anywhere. The mandatory contribution phase takes weeks of unpaid work before selection, which is a real cost to weigh.

### [Software Sustainability Institute Fellowship](https://www.software.ac.uk/programmes/fellowship-programme)

`Free, application` · beginner 2/5 · fellowship

Fellowship providing a flexible package worth GBP 4,000 to spend over 15 months on activities that improve research software practice — running training, building communities, travel to relevant events — rather than on research itself.

**Access.** Apply in the annual call advertised on software.ac.uk; contact fellows-management@software.ac.uk for the current round's dates and criteria.

**Caveats.** UK-centred: check the current call for country and affiliation eligibility before building plans around it. It funds activity, not salary or equipment, and the cohort is small and competitive.

## Learning

### [Happy Git and GitHub for the useR](https://happygitwithr.com/)

`Free` · beginner 5/5 · book

Jenny Bryan's free online book (with the STAT 545 TAs and Jim Hester) covering Git and GitHub installation, credentials and PATs, RStudio integration, and the daily workflows and failure modes that actually trip up scientists.

**Access.** Read at happygitwithr.com; the troubleshooting chapters double as a reference for authentication and merge problems.

**Caveats.** Licensed CC BY-NC 4.0. R and RStudio-centric in its examples, though the setup and troubleshooting material applies to anyone using Git.

### [learnlatex.org](https://www.learnlatex.org/)

`Free` · beginner 5/5 · LaTeX tutorial

Short, example-driven LaTeX course written by experienced LaTeX developers in which every example can be compiled directly in the browser, so a beginner writes and typesets real code without installing anything; translated into 16 languages.

**Access.** Web interface, no account: work through the lessons in order, editing and running the examples online, then move the same code into Overleaf or a local TeX Live.

**Caveats.** Deliberately short and opinionated toward current practice, which is its main virtue given how much outdated LaTeX advice circulates. For depth, read package documentation locally with 'texdoc <package>'.

### [Pro Git](https://git-scm.com/book/en/v2)

`Free` · beginner 4/5 · book

Chacon and Straub's Pro Git (2nd edition), the standard free Git reference, running from basics and branching through remotes, tooling and internals; readable online, downloadable as PDF/EPUB, and fully translated into 18 languages.

**Access.** Read at git-scm.com/book, download PDF or EPUB, or build from the source repository at github.com/progit/progit2.

**Caveats.** CC BY-NC-SA 3.0. Reference-style and engineer-oriented rather than task-driven, so pair it with Happy Git with R for setup and everyday research workflows.

### [The Carpentries lessons](https://carpentries.org/lessons/)

`Free` · beginner 5/5 · hands-on lessons

Openly licensed (CC-BY) lesson materials from Software Carpentry, Data Carpentry and Library Carpentry covering the Unix shell, Git, Python, R, MATLAB, SQL, Make, OpenRefine and domain data skills (ecology, genomics, geospatial, social science, image processing), each lesson self-contained with data and exercises.

**Access.** Read and work through the lesson websites directly at your own pace; every lesson includes downloadable data, setup instructions and solutions.

**Caveats.** Materials are written for instructor-led workshops, so a few passages assume a helper in the room; the exercises still work solo. Official certified workshops are organised and paid for by host institutions — the lessons themselves cost nothing.

### [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)

`Free` · beginner 5/5 · course

MIT course (2026 edition) of nine lectures with videos, notes and exercises on the shell, the command-line environment, development environment and tools, debugging and profiling, version control with Git, packaging and shipping code, agentic coding, 'beyond the code', and code quality — precisely the tooling research training skips.

**Access.** Watch the lecture videos on YouTube and work the exercises in the notes on the site; no enrolment, no account.

**Caveats.** Licensed CC BY-NC-SA, with community translations into 19+ languages. Assumes a Unix-like shell, so Windows users should work inside WSL. Earlier-year lectures on data wrangling, security and automation remain archived on the site.

*Also listed under: learning.*

### [The Turing Way](https://book.the-turing-way.org/)

`Free` · beginner 5/5 · handbook

Community-written, CC-BY-4.0 online handbook (code MIT) with guides to reproducible research, project design, communication, collaboration and ethical research, plus a community handbook — the closest thing to a standard free reference for research workflow practice.

**Access.** Read the whole book online for free; each chapter is citable and the book has a Zenodo DOI; contributions are made through GitHub pull requests.

**Caveats.** Very broad — start with the Guide for Reproducible Research rather than reading front to back. Written largely by a UK/EU data-science community, so some infrastructure examples assume resources an unaffiliated researcher will not have.

## Community

### [Cross Validated](https://stats.stackexchange.com/)

`Free (registration), email` · beginner 4/5 · Q&A site

Stack Exchange site for statistics, study design, machine learning and data analysis — the venue where methodological questions ('is this the right model for this design?') get answered by working statisticians rather than by a supervisor you may not have.

**Access.** Search first, then ask with the design, sample size, variables and what you have already tried; free account required to post.

**Caveats.** Content is CC BY-SA. Vague 'which test should I use?' questions attract closure; software-specific coding errors belong on Stack Overflow instead. Answers are individual opinions of varying quality — check the reasoning and cited sources.

### [Posit Community](https://forum.posit.co/)

`Free (registration), email` · beginner 4/5 · R and Quarto forum

Discourse forum for R, RStudio, the tidyverse, Shiny, Quarto/R Markdown, package development and Positron, with tens of thousands of topics and frequent participation by package authors and Posit staff.

**Access.** Free account to post; produce a small reproducible example first (the reprex package formats one for pasting).

**Caveats.** R-centric. Questions without a reprex get much slower and vaguer answers. Issues with commercial Posit products are routed to their support channels rather than answered by the community.

### [TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/)

`Free (registration), email` · beginner 4/5 · Q&A site

Q&A site for TeX, LaTeX and friends where package authors themselves regularly answer; in practice the fastest route from a broken layout or package clash to a working example.

**Access.** Search the archive first (most problems are already solved), then ask with a minimal working example; a free account is needed to post.

**Caveats.** Answers are CC BY-SA licensed, so reuse requires attribution. Questions without a compilable minimal working example usually stall or get closed; read the site's 'how to ask' guidance before posting.

### [Zotero Forums](https://forums.zotero.org/)

`Free (registration), email` · beginner 5/5 · official support forum

Official Zotero support forum where the developers themselves (alongside long-time users) answer sync failures, plugin breakage, citation-style problems and data recovery questions, usually within a day.

**Access.** Free account to post; search first, and for sync or crash issues generate a Debug ID in Zotero (Help > Debug Output Logging) and include it in the thread.

**Caveats.** Zotero-specific, and threads are public — do not paste library contents that contain sensitive information. Citation-style requests are handled through the separate CSL style repository.
