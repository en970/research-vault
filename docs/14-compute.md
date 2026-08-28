# Free compute & storage

Part of [research-vault](../README.md). 62 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (10) · [Software](#software) (5) · [Compute](#compute) (36) · [Publishing](#publishing) (6) · [Funding](#funding) (2) · [Learning](#learning) (1) · [Community](#community) (2)

## Data

### [Academic Torrents](https://academictorrents.com/)

`Free` · beginner 4/5 · peer-to-peer dataset distribution

Community-maintained distributed repository making over 298 TB of research data available over BitTorrent, with datasets, papers and course collections. Uploading lets you distribute a large public dataset worldwide without paying for bandwidth.

**Access.** Browse and download with any BitTorrent client (transmission-cli, aria2c with the magnet link) — no account needed to download. Register to upload a torrent for your own dataset.

**Caveats.** Availability depends entirely on seeders: an unpopular dataset can effectively go dark, and there is no curation, no DOI and no preservation guarantee. Useful as a bandwidth-free mirror alongside an archival copy in a repository, and as a way to distribute datasets too big for free repository tiers. Some institutional networks block BitTorrent.

### [Backblaze B2](https://www.backblaze.com/cloud-storage/pricing)

`Free tier, email` · beginner 3/5 · cheap S3-compatible archival storage

Object storage where the first 10 GB is always free, egress is free up to three times your average monthly stored volume, Class A/B/C API calls are free and the first 2,500 Class D calls per day are free. Beyond the free tier, storage is $6.95/TB/month with overage egress at $0.01/GB.

**Access.** S3-compatible: rclone (rclone config, type s3, provider Backblaze), the b2 CLI, or boto3 with the s3.<region>.backblazeb2.com endpoint.

**Caveats.** The realistic use is a cheap second copy of data you cannot afford to lose, not a free host — 10 GB free is a starting allowance, and a terabyte costs about $83/year. Egress is free through partner CDNs (Cloudflare, Fastly, bunny.net), which is worth wiring up if you publish data. No minimum file size or retention fees, so it suits many small files.

### [Cloudflare R2](https://developers.cloudflare.com/r2/pricing/)

`Free tier, email` · beginner 3/5 · S3-compatible object storage with free egress

Object storage with a permanent free monthly allowance of 10 GB-month of Standard storage, 1 million Class A operations and 10 million Class B operations — and, unusually, no egress charges at all: 'There are no charges for egress bandwidth for any storage class.'

**Access.** Create a bucket in the Cloudflare dashboard, generate S3 credentials, then use any S3 client: aws s3 --endpoint-url https://<account>.r2.cloudflarestorage.com, boto3, or rclone. Public buckets can serve data over a custom domain.

**Caveats.** Zero egress is the reason to pick R2 for a dataset people will download repeatedly — the same download pattern on S3 can produce a four-figure bill. But 10 GB free is small, and the free tier covers Standard storage only, not Infrequent Access. If you connect other metered services to the bucket, those services still bill you. No DOI, no preservation guarantee: this is hosting, not archiving.

### [EUDAT B2DROP](https://www.eudat.eu/services/b2drop)

`Free (registration), email` · beginner 5/5 · European research file sync-and-share

Nextcloud-based sync-and-share service run by the EUDAT collaborative data infrastructure, with a default quota of 20 GB per user free of charge, offered 'for any researcher', reachable through the web GUI, desktop clients and WebDAV.

**Access.** Register at b2drop.eudat.eu with a B2ACCESS identity, then sync with the Nextcloud desktop or mobile client, or mount over WebDAV. Files can be pushed on to B2SHARE when a dataset is ready to be published with a persistent identifier.

**Caveats.** 20 GB is for active working data and collaborator sharing, not archiving: B2DROP makes no preservation commitment and is not a repository — publish through B2SHARE or Zenodo instead. Larger quotas require a premium or community arrangement negotiated with EUDAT. The service is aimed at European researchers and its continuity depends on EU project funding.

### [Globus](https://www.globus.org/subscriptions)

`Free tier, credentialing` · beginner 3/5 · large-scale research file transfer

Managed, restartable, high-throughput file transfer between research storage systems. Users at non-profit research institutions get 'unlimited transfers between Globus Connect Server endpoints and between a server and personal endpoint' at no cost; subscriptions are sold to organisations, not individuals.

**Access.** Log in at app.globus.org, install Globus Connect Personal to turn a laptop or lab server into an endpoint, then drag-and-drop between collections. Scripted: pip install globus-cli, globus transfer <src-ep>:<path> <dst-ep>:<path> --recursive.

**Caveats.** This is the tool that makes moving a multi-terabyte dataset off an HPC system survivable — it retries, resumes and verifies checksums without you babysitting an scp. Free only if you are at a non-profit research institution; commercial affiliation generally needs a subscription. Premium connectors (cloud storage at scale), automation/flows, HTTPS upload-download and metadata search are subscription features.

### [Hugging Face Hub (dataset and model storage)](https://huggingface.co/docs/hub/storage-limits)

`Free tier, email` · beginner 4/5 · free hosting for public datasets and models

Free accounts get 100 GB of private storage and 'best-effort' public storage, with an explicit expectation that large public uploads are genuinely useful to the community. Hard limits: no single file over 500 GB, recommended under 100k files per repo, under 10k entries per folder and chunks under 200 GB.

**Access.** pip install huggingface_hub; hf auth login; hf upload <user>/<repo> ./data --repo-type=dataset. Consumers load with datasets.load_dataset('user/name') or stream Parquet directly.

**Caveats.** Read the wording carefully: public storage is best-effort, not a guarantee, and Hugging Face reserves the right to require a paid plan for large uploads — they also offer case-by-case storage grants for high-impact open work (contact datasets@ or models@ with download/citation evidence). A dataset card is required for large datasets, and Parquet or WebDataset formats are expected. Not a preservation archive: no DOI, no commitment to keep anything. Mirror anything citable to Zenodo.

### [Internet Archive](https://archive.org/)

`Free (registration), email` · beginner 4/5 · free unlimited public file hosting

Nonprofit archive that hosts uploaded public items — datasets, scans, audio, video, software — at no charge; its help pages state 'At this time we have no fees for uploading and preserving materials' and that 'as an archive our intention is to store and make materials in perpetuity'. The Archive estimates permanent storage costs it about $2 per gigabyte.

**Access.** Free account at archive.org, then the web upload form, or scripted with the official client: pip install internetarchive; ia upload <identifier> data/*.csv --metadata='title:My dataset' --metadata='licenseurl:https://creativecommons.org/licenses/by/4.0/'. Every item gets a permanent details page plus direct HTTPS download URLs under archive.org/download/<identifier>/.

**Caveats.** No DOI, no dataset versioning, no curation and no contractual preservation guarantee — 'intention' is not a commitment, and items can be removed on copyright or policy grounds, so deposit only material you hold rights to and mirror anything citable to Zenodo. Items are public by default. Filenames must be plain ASCII (letters, digits, dash, underscore, period) and the identifier must be unique; use the CLI, not the browser, for bulk or multi-GB uploads.

*Also listed under: humanities.*

### [Open Storage Network (OSN)](https://www.openstoragenetwork.org/get-involved/get-an-allocation/)

`Free tier, application` · beginner 2/5 · large S3-compatible research storage allocations

Distributed storage cloud for the US research community. Allocations of a minimum 10 TB and a maximum 50 TB, supporting up to 1.6 million files, can be requested through the ACCESS allocation process; storage is issued as standalone S3 buckets independent of any HPC allocation.

**Access.** Request through allocations.access-ci.org as a storage resource; then use any S3 client (rclone, aws-cli, boto3) against the assigned OSN pod endpoint.

**Caveats.** Gated by ACCESS eligibility, so a US institutional affiliation is required in practice. It is active/staging/sharing storage, not an archive: no DOIs, no curation and no long-term preservation commitment, so do not treat an OSN bucket as the permanent home of a published dataset. Requests over 50 TB mean hosting your own pod.

### [rclone](https://rclone.org/)

`Free` · beginner 3/5 · multi-cloud file transfer and sync

Open-source command-line tool for managing files on over 70 cloud storage products (S3-compatible object stores, Google Drive, Dropbox, WebDAV, SFTP and others), with one-way sync, bidirectional bisync, mounting remote storage as a local disk, MD5/SHA1 integrity checks on every transfer and server-side copies that avoid routing data through your machine.

**Access.** curl https://rclone.org/install.sh | sudo bash, then rclone config to define a remote, and e.g. rclone sync ./data r2:my-bucket --progress --checksum. rclone mount remote:path /mnt/point exposes remote storage as a filesystem; rclone check verifies two locations match.

**Caveats.** This is the practical glue between the free storage tiers listed here — moving a dataset from an institutional share to Cloudflare R2, Backblaze B2 or an OSN bucket without staging it on your laptop. Credentials in the config file are obscured, not encrypted, unless you set a config password. Server-side copy only works within one provider; anything cross-provider transits the machine running rclone, so run long moves on a server or inside tmux, not on a laptop that sleeps.

### [Registry of Open Data on AWS](https://registry.opendata.aws/)

`Free` · beginner 3/5 · sponsored hosting and anonymous access for large public datasets

Index of public datasets held in AWS S3 (NOAA, NASA, NIH, EPA, Sentinel, Allen Institute and others) that can be read anonymously from the buckets. The linked AWS Open Data Sponsorship Program 'covers the cost of storing and sharing publicly available, high-value, cloud-optimized datasets' for data providers, with application decisions generally within two weeks.

**Access.** Find the bucket on registry.opendata.aws, then read without credentials: aws s3 ls --no-sign-request s3://<bucket>/ , or boto3 with botocore.UNSIGNED. Many datasets also expose STAC catalogues or Parquet for direct querying. Providers apply at application.opendata.aws.

**Caveats.** Reading the data is free; computing over it is not — the design assumes you run EC2/Athena/SageMaker in the same region, and cross-region or to-internet egress from your own account is billed to you. AWS states that the datasets 'are not provided and maintained by AWS': licences, update cadence and documentation quality vary per dataset. Sponsorship is granted per dataset and periodically renewed, so this is hosting, not preservation.

## Software

### [Apptainer](https://apptainer.org/)

`Free` · beginner 3/5 · containers for HPC clusters

Linux Foundation container system (formerly Singularity), BSD 3-clause licensed, built for shared HPC systems: an immutable single-file SIF image format supporting cryptographic signatures and encryption, and a security model where 'you are the same user inside a container as outside, and cannot gain additional privilege on the host system by default'.

**Access.** Install from your distribution's packages, then convert and run any Docker/OCI image: apptainer pull docker://python:3.12 produces python_3.12.sif, and apptainer exec --nv image.sif python script.py runs it with GPU passthrough. The .sif is one file you can scp to a cluster and cite alongside a paper.

**Caveats.** Most HPC sites refuse Docker because it needs a privileged daemon, so Apptainer (or the Singularity CE / SingularityPRO forks, whose commands are near-identical but versions differ) is what is actually installed — check which your site runs. Building images generally needs root or --fakeroot on a machine you control, so the usual pattern is build locally, copy the SIF up. Bind mounts of site filesystems are configured by the sysadmin, not by you.

*Also listed under: workflow-tools.*

### [Google AI Studio / Gemini API free tier](https://ai.google.dev/pricing)

`Free tier, api-key` · beginner 5/5 · free LLM API for research assistance

Google AI Studio is free to use, and several Gemini Flash and Flash-Lite class models plus embedding models have a free API tier with rate limits rather than token charges.

**Access.** Get an API key at aistudio.google.com/apikey; pip install google-genai, then client.models.generate_content(model='gemini-flash-lite', contents=...). Rate limits are visible on the AI Studio rate-limit dashboard.

**Caveats.** The decisive caveat for researchers: Google's pricing page states that free-tier content is 'used to improve our products' (paid tiers say no). Never paste unpublished manuscripts, participant data, embargoed results or anything covered by a data-use agreement into the free tier. Free-tier rate limits are per-minute and per-day, change frequently, and free-tier model availability is rotated — if reproducibility matters, record the exact model string and date.

### [llama.cpp](https://github.com/ggml-org/llama.cpp)

`Free` · beginner 3/5 · local LLM inference on modest hardware

MIT-licensed C/C++ inference engine for open-weight language models, with 1.5- to 8-bit integer quantisation and backends for x86 CPUs (AVX/AVX2/AVX-512/AMX), RISC-V, Apple Silicon (NEON/Accelerate/Metal), CUDA, HIP, Vulkan and SYCL, including CPU+GPU hybrid inference for models larger than available VRAM.

**Access.** brew install llama.cpp, or build from source; pull GGUF weights straight from Hugging Face and serve an OpenAI-compatible endpoint: llama-server -hf <org>/<model>-GGUF --port 8080. Then point any OpenAI client at http://localhost:8080/v1.

**Caveats.** The honest comparison for research assistance: a 7–8B model at 4-bit quantisation runs on a laptop with roughly 8 GB of free RAM and is genuinely useful for bulk classification, extraction and drafting over sensitive or embargoed corpora that must never leave your machine — no per-token cost, no data-sharing question. It is not competitive with frontier hosted models on hard reasoning or long-context synthesis, and aggressive quantisation degrades quality. Check each model's weight licence before publishing outputs.

*Also listed under: cs-ml.*

### [nf-core](https://nf-co.re/)

`Free` · beginner 3/5 · portable, reproducible analysis pipelines

Community collection of 156 curated Nextflow pipelines (RNA-seq, variant calling, metagenomics, proteomics, single-cell and more) built to shared guidelines and MIT licensed, with dependencies resolved automatically through Docker, Singularity/Apptainer or Conda and releases tested on AWS.

**Access.** curl -s https://get.nextflow.io | bash, then: nextflow run nf-core/rnaseq --input samplesheet.csv --outdir results --genome GRCh38 -profile singularity. Execution profiles retarget the same command at a laptop, a Slurm/PBS cluster, Kubernetes or AWS/Azure/Google batch without editing the pipeline.

**Caveats.** The pipelines are free, the compute is not: they are designed to be pointed at whatever allocation you have, and a full human-scale run costs tens to hundreds of core-hours plus multi-GB reference downloads. Check nf-core/configs for a ready-made institutional profile for your cluster before hand-tuning resource requests. Scope is overwhelmingly bioinformatics; Nextflow itself is general-purpose.

*Also listed under: biology.*

### [Ollama](https://ollama.com/)

`Freemium` · beginner 5/5 · local model runner

One-command local runner for open-weight models, wrapping the same GGML/llama.cpp stack behind a model library and an OpenAI-compatible local API. The site reports more than 9 million developers.

**Access.** Download from ollama.com, then: ollama run qwen3:8b for a chat session, or ollama serve plus http://localhost:11434/v1 as an OpenAI-compatible base URL from Python.

**Caveats.** What is free is the local runtime and the model downloads; Ollama also now sells a hosted cloud tier with paid usage, and the front page markets that heavily — do not confuse the two. Local inference sends nothing anywhere. Model licences vary by model (some restrict commercial or derivative use), so read the card before building results on one.

## Compute

### [ARDC Nectar Research Cloud](https://ardc.edu.au/services/ardc-nectar-research-cloud/)

`Free tier, credentialing` · beginner 3/5 · Australian national research cloud

Australia's national OpenStack research cloud, free at the point of use: institutional login gives an immediate trial project, and a project allocation requested through the Nectar dashboard runs for up to 12 months with renewals possible.

**Access.** Sign in at the Nectar dashboard (dashboard.rc.nectar.org.au) through the Australian Access Federation, then launch VMs from Horizon, the OpenStack CLI or Terraform. University of Auckland credentials also work for New Zealand users.

**Caveats.** Gated on an Australian (or the specified New Zealand) institutional identity through AAF; researchers without one must go through an alternative eligibility route and may not qualify at all. Allocations expire after at most 12 months and must be renewed with a short justification. As with any IaaS cloud, a running instance consumes the allocation whether or not it is busy — shelve or delete when idle. GPU flavours are limited and requested separately.

### [AWS Free Tier](https://aws.amazon.com/free/)

`Free tier, email` · beginner 2/5 · cloud free tier (credit-based)

New accounts get $100 in credits immediately and can earn up to $100 more; the account closes six months after opening or when credits run out, whichever comes first. More than 30 AWS services also carry always-free monthly usage limits on both Free and Paid plans.

**Access.** Sign up at aws.amazon.com, then aws-cli or boto3. For research the practical uses are S3 for data staging, EC2 spot for short batch runs, and Athena/Open Data on AWS for querying hosted public datasets.

**Caveats.** This is the post-2025 model and it is materially worse for researchers than the old 12-month free tier: a credit balance with a hard six-month clock rather than a recurring monthly allowance. AWS states the account 'closes on its own 6 months after you open it or when your credits run out, whichever comes first' and that 'you won't be charged unless you convert to a Paid plan' — so the failure mode is losing the account, not a surprise bill, provided you never convert. Export anything you care about before the clock runs out. AWS's dedicated 'Cloud Credit for Research' programme page no longer resolves — do not plan on it; route research credit requests through CloudBank or an institutional agreement instead.

### [Azure for Students](https://azure.microsoft.com/en-us/free/students)

`Free tier, email` · beginner 3/5 · student cloud credit

$100 of Azure credit valid for 12 months with no credit card required, renewable annually while you remain a student, plus free monthly amounts on 20+ services for 12 months and 65+ always-free services.

**Access.** Sign up with your institutional email at azure.microsoft.com/free/students; verification is automatic for supported domains. Then portal.azure.com or the az CLI.

**Caveats.** Only for verifiably enrolled full-time students at a recognised institution — useless to independent researchers, and the domain check fails for plenty of legitimate universities, in which case you must submit documentation. $100 buys very little GPU time; it is best spent on storage, small VMs and managed services rather than training.

### [brainlife.io](https://brainlife.io/about/)

`Free (registration), email` · beginner 4/5 · neuroimaging pipelines with donated compute

Free, open-source platform for reproducible MRI, EEG and MEG analysis that runs over 400 published Apps on 'millions of free computing hours supported by NSF and donated cycles', with storage and access to several major HPC resources included on registration. Reports over 2,000 users worldwide.

**Access.** Sign up at brainlife.io, upload or import a BIDS dataset, then run Apps (fMRIPrep, FreeSurfer, tractography and others) from the web interface; every run is versioned and citable.

**Caveats.** Funded by NSF, DoD, Kavli and NIH awards, so capacity depends on grants continuing. Queue times vary with donated-cycle availability. Best for standard, already-packaged pipelines; if you need a bespoke tool you must package it as an App first. Check data-governance terms before uploading identifiable human imaging.

*Also listed under: neuro-psych.*

### [Chameleon Cloud](https://www.chameleoncloud.org/)

`Free tier, application` · beginner 2/5 · bare-metal experimental testbed

NSF testbed of 400+ nodes across three sites where you get bare-metal, root-level control of the hardware — useful for systems, networking, edge and reproducibility research. New projects receive 20,000 service units for six months, renewable; 1 SU is one hour on a base bare-metal server, with GPU nodes (A100, H100) charged at a 2–4× multiplier.

**Access.** Register at chameleoncloud.org and create a project; reserve nodes through the GUI or scripted with python-chi (pip install python-chi). Experiment images and Jupyter-based 'trovi' artifacts make published experiments re-runnable.

**Caveats.** Scope is narrower than people assume: it is 'broadly available to members of the US Computer Science research community and its international collaborators working in the open community on cloud research'. International researchers can apply independently only with a strong record of publications in open venues. Students cannot be PIs. Commercial projects are not eligible. Bare metal means you handle the OS — expect a real learning curve.

### [CHPC South Africa (Lengau)](https://www.chpc.ac.za/)

`Free, application` · beginner 2/5 · African national HPC with free academic access

South Africa's national supercomputing centre, funded by the Department of Science and Innovation. Its Lengau cluster is a petascale Dell system with 30 NVIDIA V100 GPU nodes and 4 PB of parallel Lustre storage, and has served over 2,000 active users who have consumed more than a billion core-hours.

**Access.** Apply for an account through the CHPC user portal at users.chpc.ac.za; work is then submitted over SSH to the cluster's batch scheduler. Free academic access covers universities, research institutions, public non-commercial public-interest projects and NGOs.

**Caveats.** Access is re-evaluated for renewal every six months. Commercial users pay R0.45 + VAT per core-hour under a 12-month agreement. The public pages do not spell out whether applicants outside South Africa qualify — ask before planning around it, and expect a South African host institution to be the practical route. GPU capacity (30 V100 nodes) is modest and contended, and this is a conventional batch cluster, so Linux and scheduler competence is assumed.

### [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/)

`Free tier, email` · beginner 4/5 · free Earth observation data plus hosted processing

The full Copernicus Sentinel-1/2/3/5P archive plus Copernicus service products (land, marine, atmosphere, emergency), free and open, with registered access to co-located processing: JupyterLab, the openEO API, Sentinel Hub APIs, a STAC browser and on-demand product generation.

**Access.** Register at dataspace.copernicus.eu, then either the browser JupyterLab, or from your own machine: pip install openeo and connect('openeo.dataspace.copernicus.eu').authenticate_oidc(), which pushes the computation to their cluster.

**Caveats.** Data download is free but metered, and the free-tier numbers are published: 12 TB/month of transfer for immediately-available data (0.1 TB/month for deferred/offline data), after which bandwidth is throttled to 1 MB/s; 4 concurrent S3/OData/STAC connections; 10,000 openEO processing units per month with 12 requests and 300 processing units per minute; 50,000 Sentinel Hub requests per month; 2 concurrent processing jobs. That is enough to develop and run modest area/time studies, not a continental time series. Larger quotas are a paid plan.

*Also listed under: earth.*

### [CyVerse](https://cyverse.org/subscribe)

`Free tier, email` · beginner 4/5 · life-science analysis platform

NSF-originated open science workspace with the Discovery Environment (containerised analysis apps) and VICE (interactive Jupyter/RStudio/VS Code). A free basic account provides 'several hundred compute hours in the Discovery Environment and 5 Gigabytes of data storage on the Data Store'.

**Access.** Create a free account at user.cyverse.org, request access to the Discovery Environment, then launch apps or VICE sessions from de.cyverse.org.

**Caveats.** CyVerse's own pricing table puts a Basic account at 200 compute units per year alongside the 5 GB Data Store quota, so read 'several hundred compute hours' conservatively. The free tier was cut back in 2025 and you should know how: since June 2025 basic accounts cannot share files or create public links, and since March 2025 data quotas are enforced with automatic sweeps that permanently delete over-quota data ('Data removed by automatic sweep cannot be recovered'). Paid add-ons are $100 per 5,000 compute hours and $250/TB/year for storage. CyVerse also removes inactive accounts and their data after notice.

### [Digital Research Alliance of Canada](https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources)

`Free tier, credentialing` · beginner 3/5 · Canadian national HPC

Every activated account gets default access with no competition: 1 TB of /project storage on most clusters and opportunistic (unprioritised, uncapped) CPU and GPU use. Rapid Access Service adds more /project and /nearline storage plus basic cloud resources on request; the annual Resource Allocation Competition is the only route to compute priority.

**Access.** Apply for a CCDB account at ccdb.alliancecan.ca, then ssh into a cluster (Fir, Rorqual, Nibi, Trillium) and submit with Slurm: sbatch --gpus-per-node=1 --time=3:00:00 job.sh.

**Caveats.** Requires a Canadian academic affiliation; RAS and RAC requests can only be led by faculty, adjunct faculty or librarians, so students apply under a sponsoring PI. 'Opportunistic' means genuinely unprioritised — default-access jobs can wait a long time behind allocated projects during busy periods. RAC opens each autumn.

### [DiRAC (UK)](https://dirac.ac.uk/getting-access/)

`Free tier, application` · beginner 2/5 · UK theoretical-science HPC

The UK's HPC facility for the STFC theory community, spanning four services: data-intensive (Cambridge, Leicester), memory-intensive (Durham) and extreme scaling (Edinburgh). Access is via the STFC Resource Allocation Committee's annual full-proposal call, plus year-round Director's Discretionary applications and a Seedcorn Time programme for small, ad-hoc or urgent requests.

**Access.** Apply through dirac.ac.uk/getting-access. Seedcorn is the low-friction entry point for testing whether your code scales before committing to a RAC proposal.

**Caveats.** Scope is narrow: particle physics, astronomy, cosmology and nuclear physics theory, with a UK-based PI. Free at the point of use but competitive; the RAC call is annual (RAC19 proposals closed 17 September 2026), so missing it means waiting or using Seedcorn/Director's Discretionary. Seedcorn is capped at 100,000 x86 core-hours or 1,000 GPU hours, to be used within three months of allocation — enough to benchmark and scale-test a code, not to run a campaign. DiRAC also runs a Research Software Engineering team and training academy that allocated projects can draw on.

### [EGI Notebooks](https://www.egi.eu/service/notebooks/)

`Free tier, credentialing` · beginner 4/5 · European federated JupyterHub with sponsored quota

JupyterHub service operated by the EGI federation for European research. The pre-configured offer gives each user 4 vCPU cores, 6 GB RAM and 10 GB block storage, with Julia, Python, R, Octave and MATLAB kernels and real-time collaborative editing; scientific communities can get customised deployments with their own hardware and authentication.

**Access.** Log in with an EGI Check-in identity and request the sponsored quota from egi.eu/service/notebooks; the notebook environment mounts EGI storage so data can stay in the federation. The sister EGI Cloud Compute service offers trial VMs of up to 4 vCPU, 8 GB RAM and 100 GB block storage.

**Caveats.** The sponsored quota is small and granted per user or per project rather than published as a standing entitlement; sustained work is expected to move to a community allocation or a negotiated 'custom access' agreement. Login goes through EGI Check-in, which in practice favours researchers with an institutional or EU-project identity. No GPU in the default offer, and 10 GB of block storage means results must be exported.

### [EOSC EU Node](https://open-science-cloud.ec.europa.eu/)

`Free tier, credentialing` · beginner 3/5 · European open science cloud services

The first operational node of the EOSC Federation, in production, offering a credit-based set of services: OpenStack virtual machines including GPU clusters, a cloud container platform, Jupyter-based interactive notebooks, file sync-and-share, and large/bulk file transfer, alongside the EOSC Resource Catalogue.

**Access.** Log in at open-science-cloud.ec.europa.eu with home institutional credentials (eduGAIN federation) and request services from the marketplace; each service is metered against a credit balance.

**Caveats.** Credits are assigned automatically when you first log in, so you discover your personal allowance only after registering, and it is modest; coordinators of European Commission-funded research and innovation projects can request up to 40,000 credits. Federated login effectively assumes an institutional or eduGAIN-recognised identity, which is a barrier for unaffiliated researchers. The node is new and the Commission does not publish forward service timelines, so treat long-term availability as unsettled.

### [EuroHPC Joint Undertaking](https://eurohpc-ju.europa.eu/access-our-supercomputers/access-policy-and-faq_en)

`Free tier, application` · beginner 2/5 · European supercomputing allocations

Access to Europe's petascale, pre-exascale and exascale systems (LUMI, Leonardo, MareNostrum 5, JUPITER and others) via several modes: Benchmark and Development Access are continuously open calls with a maximum time to resource access of two weeks; Regular, Extreme Scale and 'AI for Science' modes run on scheduled cut-offs. EuroHPC states that 'currently access is free of charge'.

**Access.** Apply at eurohpc-ju.europa.eu; Development and Benchmark applications are short and continuous, which is the realistic starting point for porting and scaling tests before a Regular request.

**Caveats.** Eligibility is geographic, not institutional prestige: researchers from academia, research institutes, public authorities and industry 'established or located in an EU Member State or in a Participating State or in a third country associated to the Digital Europe Programme or to Horizon Europe'. You must acknowledge the resources in publications and file completion reports. Development/Benchmark allocations are small and time-boxed by design — they exist to prepare a Regular proposal.

### [Galaxy (usegalaxy.org)](https://galaxyproject.org/main/)

`Free (registration), email` · beginner 5/5 · bioinformatics workbench with free compute

Free web platform running thousands of bioinformatics tools on someone else's cluster. Registered users of usegalaxy.org get 250 GB of storage (5 GB unregistered), with concurrency limits of 6 standard jobs and 1–4 high-memory jobs (tools needing more than 8 GB RAM or multiple CPUs).

**Access.** Web interface at usegalaxy.org — register, upload or fetch data by URL, chain tools into a workflow, share the workflow by link. A Python API client exists (pip install bioblend) for scripted submission.

**Caveats.** The terms warn that 'data transfer and data storage are not encrypted' — do not upload restricted human-subject data without checking with your IRB; use a Galaxy instance with appropriate controls instead. Creating multiple accounts to dodge quotas can get you terminated. Sister servers usegalaxy.eu and usegalaxy.org.au have their own quotas and tool sets, often larger for European/Australian users.

### [GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions)

`Free tier, email` · beginner 3/5 · CI runners as batch compute

Standard GitHub-hosted runners are free without limit for public repositories; private repositories on personal accounts get 2,000 minutes/month (Free) or 3,000 (Pro), with 500 MB / 1 GB of artifact storage and 10 GB of cache per repository.

**Access.** Add a workflow YAML under .github/workflows/. Use 'on: schedule: - cron:' for recurring analyses and actions/upload-artifact to keep outputs.

**Caveats.** Legitimate for reproducible pipelines attached to your repo (rebuilding a figure set, re-running tests on a dataset); GitHub's acceptable-use terms prohibit using Actions as a general-purpose compute farm unrelated to the repository. Larger runners are always charged, even on public repos. No GPU on standard runners. Self-hosted runners are free, which is a good way to attach your own machine.

### [GitHub Codespaces](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)

`Free tier, email` · beginner 4/5 · cloud development environments

Cloud dev containers attached to a repository. GitHub Free personal accounts get 120 core-hours plus 15 GB-month of storage each month; GitHub Pro gets 180 core-hours and 20 GB-month.

**Access.** Press '.' on any GitHub repo, or Code > Codespaces > Create codespace. Pin the environment with .devcontainer/devcontainer.json so collaborators get an identical machine.

**Caveats.** Core-hours, not wall-clock hours: 120 core-hours is 60 h on a 2-core machine or 30 h on a 4-core one. No GPU at any tier that is free. With no payment method on file, usage is simply blocked when the quota runs out — you can still export changes to a branch. Stop codespaces manually; idle ones keep billing storage.

### [GitLab CI/CD free tier](https://docs.gitlab.com/ci/pipelines/compute_minutes/)

`Free tier, email` · beginner 3/5 · CI runners as batch compute

Free-tier GitLab.com namespaces receive 400 compute minutes per month on GitLab-hosted shared runners. Public projects accepted into the GitLab for Open Source program are charged at a 0.5 cost factor (1 quota minute per 2 minutes of job time) and public forks of those projects at 0.008 (1 minute per 125 minutes of job time).

**Access.** Add .gitlab-ci.yml at the repo root; use 'rules:' or pipeline schedules for recurring analyses and 'artifacts:' to keep outputs. Registering your own machine as a project runner (gitlab-runner register) makes execution free of quota entirely.

**Caveats.** Materially smaller than GitHub Actions: 400 minutes/month versus 2,000, and there is no blanket free allowance for public repositories unless you are admitted to the GitLab for Open Source programme. No GPU on shared runners. Same acceptable-use limit as any CI service — this is for pipelines attached to your repository, not a general compute farm. Self-hosted runners are the realistic route to sustained capacity.

### [Google Cloud Free Tier](https://docs.cloud.google.com/free/docs/free-cloud-features)

`Free tier, email` · beginner 3/5 · cloud free trial and always-free products

$300 in welcome credit valid for 90 days for new customers, plus Always Free monthly allowances that persist: one non-preemptible e2-micro VM in a US region with 30 GB standard persistent disk, 5 GB-month regional Cloud Storage, 1 TiB of BigQuery queries and 10 GiB of BigQuery storage, and 2 million Cloud Run requests.

**Access.** console.cloud.google.com; gcloud CLI for VMs. The genuinely useful research piece is BigQuery: 1 TiB/month of free querying over public datasets via the console or `pip install google-cloud-bigquery`.

**Caveats.** The free trial is once per person and requires a card. The Always Free e2-micro is tiny (2 shared vCPU, 1 GB) and US-region only, with just 1 GB/month of North American egress. No free GPU. Watch BigQuery: a careless SELECT * over a large public table can burn the monthly free terabyte in one query — always use --dry_run or the byte estimate first.

### [Google Colab (free tier)](https://colab.research.google.com/)

`Free (registration), email` · beginner 5/5 · hosted notebooks with free GPU

Hosted Jupyter notebooks with intermittent free GPU and TPU runtimes. Google's own FAQ states notebooks run 'for at most 12 hours, depending on availability and your usage patterns', that idle runtimes are terminated and VMs deleted, and that the limits are deliberately unpublished because they fluctuate.

**Access.** Web interface; open any .ipynb from Google Drive or a GitHub URL (colab.research.google.com/github/<user>/<repo>/blob/<branch>/nb.ipynb). Runtime > Change runtime type to pick a GPU. Install per session with !pip install; mount Drive with google.colab.drive for anything that must survive.

**Caveats.** The single most important caveat: the free tier is not a place to run long jobs. Google explicitly says access to GPUs is 'heavily restricted' on the free plan, and heavy users get downgraded to CPU-only for hours at a time. SSH/remote desktops, distributed computing and mining are prohibited by the FAQ. Checkpoint to Drive every few minutes or expect to lose work.

### [Google Earth Engine (noncommercial access)](https://earthengine.google.com/noncommercial/)

`Free (registration), application` · beginner 4/5 · planetary-scale geospatial analysis

Petabyte-scale satellite and geospatial catalogue with server-side parallel computation, free for students, faculty and staff at academic or educational institutions, nonprofits doing noncommercial work, news media, certain government agencies, and individuals for noncommercial purposes.

**Access.** Register a noncommercial project at code.earthengine.google.com (JavaScript Code Editor), or Python: pip install earthengine-api, then ee.Authenticate(); ee.Initialize(project='your-project'). Exports go to Google Drive or Cloud Storage.

**Caveats.** The restriction that catches people: free users 'may not use Earth Engine for fee-for-service activities' or take compensation for applications or data made with it — an academic doing paid consultancy needs a commercial licence. Project registration is reviewed, not instant. Compute and export quotas are per-project and large exports queue for hours; there is no way to buy your way past them on the free tier.

### [Hugging Face Spaces + ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu)

`Free tier, email` · beginner 4/5 · free GPU for demos and short inference

Free CPU Spaces (2 vCPU, 16 GB) plus ZeroGPU, which allocates NVIDIA RTX Pro 6000 Blackwell GPUs on demand (48 GB for the default 'large' size, 96 GB for 'xlarge'). Daily GPU quota is 2 minutes unauthenticated, 5 minutes for a free account, 40 minutes for PRO.

**Access.** Create a Space at huggingface.co/new-space (Gradio SDK), import spaces and decorate the GPU function: @spaces.GPU(duration=120). Models must be moved to cuda at module level, not inside the decorated function.

**Caveats.** ZeroGPU is for interactive inference, not training: quota is measured in minutes of GPU time per day and resets 24 h after first use. Gradio SDK only; torch.compile is unsupported (use ahead-of-time compilation). Free personal accounts may host at most 2 ZeroGPU Spaces, and only if the account has a verified email and is over 30 days old. Free Spaces sleep when idle.

*Also listed under: cs-ml.*

### [IBM Quantum (Open Plan)](https://quantum.cloud.ibm.com/docs/guides/plans-overview)

`Free tier, api-key` · beginner 3/5 · free quantum processor time

IBM's Open Plan gives no-cost access to IBM Quantum QPUs, capped at up to 10 minutes of QPU execution time per 28-day rolling window; as of 2026 active Open Plan users can additionally opt in to 180 extra minutes spread over 12 months. IBM positions it for people 'learning quantum computing and exploring IBM quantum technology'.

**Access.** Create an account at quantum.cloud.ibm.com to get an API token, then pip install qiskit qiskit-ibm-runtime and submit through QiskitRuntimeService with the Sampler or Estimator primitives. Local simulation with qiskit-aer is unlimited and needs no account.

**Caveats.** The 10 minutes is metered device execution, not wall-clock: it goes a long way for small circuits with few shots and evaporates on large batched jobs, and queue waits on shared open devices can run to hours. Which QPUs are reachable on the Open Plan changes over time, so record backend name and calibration date for reproducibility. Sustained or large-scale work needs the paid Pay-As-You-Go plan or an academic/network agreement.

*Also listed under: physics, chemistry.*

### [Jetstream2](https://jetstream-cloud.org/)

`Free tier, application` · beginner 3/5 · NSF cloud (VMs, GPUs) for researchers

NSF-funded OpenStack cloud (award 2005506) offering on-demand virtual machines including NVIDIA A100 GPU and large-memory flavours, with discipline-specific images. Access is granted through ACCESS or NAIRR Pilot allocations rather than purchased.

**Access.** Get an ACCESS allocation, exchange credits for Jetstream2 service units, then launch VMs through the Exosphere web UI at jetstream2.exosphere.app or the OpenStack CLI/Horizon. No queue: instances start immediately.

**Caveats.** Inherits ACCESS eligibility, so US affiliation is required. Unlike a batch cluster, a running VM consumes service units continuously whether or not it is busy — shelve or delete instances when you stop working. Persistent volumes and object storage are allocated separately from compute.

### [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/)

`Free` · beginner 4/5 · in-browser notebooks (WebAssembly)

A JupyterLab distribution that runs entirely in the browser with no server, using WebAssembly kernels (Pyodide, xeus-python, xeus-R) as Web Workers. It is served as static files, so it can be hosted free on GitHub Pages or any static host.

**Access.** Try it at jupyter.org/try-jupyter. To publish your own: pip install jupyterlite-core && jupyter lite build --contents notebooks/, then push the _output directory to GitHub Pages.

**Caveats.** Zero infrastructure cost is the point, and the limits follow from that: browser memory ceilings, no access to your filesystem or arbitrary network calls, and only packages available as pure-Python wheels or Pyodide builds (numpy, pandas, matplotlib, scikit-learn yes; anything needing compiled extras outside Pyodide, no). The right tool for interactive supplementary material and teaching; not for computation.

### [Kaggle Notebooks](https://www.kaggle.com/code)

`Free (registration), email` · beginner 5/5 · hosted notebooks with weekly GPU/TPU quota

Free hosted notebooks with a fixed weekly accelerator quota (NVIDIA GPU and TPU VM options), sessions capped at 12 hours, and public datasets attachable directly to the session so multi-GB inputs are never downloaded over your own connection.

**Access.** Web interface: New Notebook > Settings > Accelerator, and 'Add Data' to attach any Kaggle dataset or competition data at /kaggle/input. Scripted use: pip install kaggle, then kaggle kernels push / kaggle datasets download -d <owner>/<slug> with an API token from your account page.

**Caveats.** Phone verification is required before the GPU/TPU and internet toggles appear at all — a real barrier in some countries. The remaining weekly quota is displayed in the session sidebar; treat that number as authoritative, because Kaggle has changed the allowance before and its documentation sits behind a bot wall. Quota resets weekly, not monthly, and idle sessions burn it.

### [Modal](https://modal.com/pricing)

`Free tier, email` · beginner 3/5 · serverless GPU compute

Serverless Python compute where you decorate a function and it runs in a container in the cloud. The Starter plan includes $30/month of free credits, with limits of 100 containers and 10 concurrent GPUs.

**Access.** pip install modal && modal setup, then decorate: @app.function(gpu="A10G", image=modal.Image.debian_slim().pip_install("torch")) and run modal run script.py. Volumes persist data between runs.

**Caveats.** $30/month resets and does not roll over. At Modal's per-second GPU rates that is on the order of a few hours on a mid-range card, or minutes on an H100 — enough for prototyping and small batch jobs, not for training runs. Everything past the credit is billed per second, so set a spend limit before you launch anything unattended.

### [mybinder.org](https://mybinder.org/)

`Free` · beginner 5/5 · one-click reproducible notebook sessions

Turns any public Git repository with an environment specification into a running Jupyter session in the browser, with no account. Documented limits: at least 1 GB and at most 2 GB of RAM, up to one CPU-hour for heavier sessions, shutdown after 10 minutes of inactivity, and roughly six hours of session time.

**Access.** Point mybinder.org at a public repo URL containing environment.yml, requirements.txt or a Dockerfile; add the generated Binder badge to your README so reviewers can run your figures.

**Caveats.** Be honest with yourself about what this is for. mybinder.org 'relies on the generosity of donors and volunteers', runs entirely on donated cloud resources, and offers 'no persistent storage of any sort' — everything is destroyed at logout. It is a superb demo and teaching layer for a paper, and a bad place to compute. Capacity varies; first builds of a repo can take many minutes.

*Also listed under: physics, mathematics, learning, workflow-tools.*

### [NAIRR Pilot](https://nairrpilot.org/)

`Free tier, application` · beginner 3/5 · US national AI research resource

US pilot that brokers AI compute, data and models to researchers and educators; the site reports 880+ supported research projects across 50 states plus DC and Puerto Rico, 95 classroom awards and 23 demonstration projects. Programmes include Research Resources, Educational Resources, Deep Partnerships and Start-Up Projects, with a curated set of datasets and pre-trained models usable without any application.

**Access.** Apply through the opportunity pages at nairrpilot.org; awarded compute is delivered on partner systems (Jetstream2, Delta, industry partners). The Data/Models section and the community Slack are open without an application.

**Caveats.** It is still formally a pilot: funding and programme structure are decided year to year, so do not build a multi-year plan on it without checking the current call. Eligibility follows the US research-and-education pattern of its partner systems. Deep Partnership awards depend on individual company terms, which can include usage reporting.

*Also listed under: cs-ml.*

### [nanoHUB](https://nanohub.org/)

`Free (registration), email` · beginner 5/5 · browser-run simulation tools (nanoscience, materials)

Free platform running simulation tools in the cloud through a browser for nanotechnology, materials science and related fields, operating since 2002 and serving over a million visitors a year. Tools published on nanoHUB are indexed in Web of Science and citable as publications.

**Access.** Create a free account at nanohub.org and launch any tool from the browser — nothing to install. Simulation runs on nanoHUB's own infrastructure.

**Caveats.** Explicitly open to everyone: 'No cost, no licence, no institutional affiliation required' — one of very few compute platforms in this list with no affiliation gate at all. Scope is domain-bounded (device physics, materials, nanoelectronics); tool sessions have resource ceilings suited to teaching and modest research runs, not large parameter sweeps.

### [National Research Platform (Nautilus)](https://nrp.ai/)

`Free tier, credentialing` · beginner 2/5 · shared Kubernetes GPU cluster

NSF-funded Kubernetes cluster (Nautilus) pooling GPUs and storage across 70+ institutions on three continents, 400+ nodes, free to US nonprofit research and education including community colleges. You can request individual GPU cards or reserve whole 4- and 8-GPU nodes, and filter by GPU product, CUDA runtime or region.

**Access.** Sign in with your institutional identity at the NRP portal, then either use the hosted JupyterHub or submit Kubernetes manifests with kubectl (Jobs for batch, Deployments for services). Persistent volumes via Ceph.

**Caveats.** Login is federated institutional identity, so a researcher with no eligible affiliation cannot self-serve. Much of the capacity is opportunistic: contributed nodes are yours only while their owners are idle, and pods can be evicted — checkpoint, and keep nothing important outside a persistent volume. You need to be comfortable writing Kubernetes YAML; there is no batch scheduler to hide it.

### [NSF ACCESS (Advanced Cyberinfrastructure Coordination Ecosystem)](https://allocations.access-ci.org/project-types)

`Free tier, application` · beginner 3/5 · US national HPC allocations

The front door to US national supercomputing. Four tiers: Explore (400,000 credits, 1-page proposal), Discover (1,500,000 credits, 3 pages), Accelerate (3,000,000 credits, 10 pages plus panel review) and Maximize (awarded in resource units, panel review twice a year). Explore, Discover and Accelerate accept requests at any time; Explore can be live in 1–2 business days.

**Access.** Register at access-ci.org, submit an allocation request at allocations.access-ci.org, then exchange ACCESS credits for time on specific resources (Anvil, Bridges-2, Delta, Expanse, Jetstream2, OSN and others).

**Caveats.** Read the eligibility rule before you invest time: the PI must be 'a U.S-based researcher or educator, at the graduate-student level or higher', affiliated with an eligible US organisation and using a matching organisational email. Unaffiliated researchers are explicitly not eligible ('not eligible for support if the individual is not employed by or affiliated with an eligible organization'), and non-US researchers must work under a US PI. Graduate students can be PIs on Explore and Discover with an advisor as co-PI, which is the realistic route for a student.

### [Oracle Cloud Always Free](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm)

`Free tier, email` · beginner 3/5 · always-free Arm VMs and storage

Perpetually free Arm compute: the first 1,500 OCPU-hours and 9,000 GB-hours per month on VM.Standard.A1.Flex, which Oracle's docs describe as 'equivalent to 2 OCPUs and 12 GB of memory' for Always Free tenancies, plus two AMD micro VMs, 200 GB total block volume, 20 GB object/archive storage, 10 TB/month outbound transfer and two Autonomous Databases (1 OCPU, 20 GB each).

**Access.** Sign up at oracle.com/cloud/free, then create a VM.Standard.A1.Flex instance in your home region from the OCI Console. Standard Ubuntu/Oracle Linux images; ssh in and treat it as an ordinary always-on Linux box.

**Caveats.** Verify the numbers yourself before planning around them: the widely repeated '4 OCPU / 24 GB' figure is out of date — Oracle's current docs say 1,500 OCPU-hours and 9,000 GB-hours, i.e. about 2 OCPUs and 12 GB run continuously. A credit or debit card is required for identity verification (prepaid and virtual cards are refused), one account per person, and accounts 'left idle for 30 days or more may be deemed abandoned' and suspended. 'Out of host capacity' errors for A1 shapes are common in popular regions.

### [OSG OSPool](https://portal.osg-htc.org/documentation/)

`Free tier, application` · beginner 2/5 · high-throughput computing (many small jobs)

A distributed pool of opportunistic capacity contributed by US campuses, for high-throughput workloads. OSG's own fit guidance: ideal jobs use a single core, no GPU, under 10 hours of walltime, a few GB of RAM, under 500 MB of input and under 1 GB of output, run as 1000s of concurrent jobs; still advantageous up to 8 cores, 1 GPU, 20 hours, 40 GB RAM and 10 GB of input/output.

**Access.** Request an account at portal.osg-htc.org, then submit HTCondor jobs from an OSG access point: condor_submit job.sub with 'queue 10000' over a parameter list. Containers via Apptainer.

**Caveats.** Restricted to 'US-affiliated academic, government, and non-profit research projects'. This is the opposite of a tightly coupled HPC cluster: MPI across nodes will not work, jobs can be preempted and restarted anywhere, and the win comes entirely from parallelising over many independent tasks. If your problem is one long simulation, this is the wrong tool; if it is 50,000 short ones, nothing free comes close.

### [SciServer](https://www.sciserver.org/)

`Free (registration), email` · beginner 3/5 · data-co-located JupyterHub (astronomy, simulations, Earth science)

Johns Hopkins/NSF platform built to 'bring the analysis to the data': free Jupyter containers with domain software images, persistent storage volumes, and CasJobs SQL access to large catalogues (SDSS and others) plus turbulence and cosmological simulation datasets held on the same infrastructure.

**Access.** Register at apps.sciserver.org, then SciServer Compute for notebooks (Python/R with astronomy stacks preinstalled) and CasJobs for asynchronous SQL over the catalogues. SciScript client libraries exist for Python and R.

**Caveats.** Per-user storage and container sizes are not advertised on the public pages and are modest; idle containers are reclaimed. No GPU. The payoff is entirely about co-location — if the dataset you need is already there, you avoid downloading terabytes; if it is not, this offers you little.

*Also listed under: astronomy.*

### [TIKE (Timeseries Integrated Knowledge Engine, MAST)](https://outerspace.stsci.edu/display/MASTDOCS/TIKE)

`Free (registration), email` · beginner 4/5 · free JupyterHub next to NASA archive data

STScI-operated JupyterHub for analysing TESS and Kepler/K2 data, with numpy, scipy, matplotlib, astropy, astroquery and lightkurve preinstalled and MAST holdings readable directly from cloud storage rather than downloaded.

**Access.** Log in at timeseries.science.stsci.edu with a MyST account and open a notebook; read data with lightkurve/astroquery pointed at the cloud URIs so nothing transits your own connection.

**Caveats.** Home-directory space is small and sessions are reclaimed when idle, so treat it as scratch and push results out. No GPU. Documented resource ceilings are thin — assume a few cores and a modest RAM allowance. Ideal for exoplanet/variable-star light-curve work where the archive is the bottleneck; poor for anything compute-heavy.

### [TPU Research Cloud (TRC)](https://sites.research.google/trc/about/)

`Free tier, application` · beginner 2/5 · application-based free TPU access

Google grants accepted researchers no-cost access to a cluster of more than 1,000 Cloud TPU devices, usable from JAX, PyTorch/XLA, TensorFlow or Julia. In return participants must share results publicly (peer-reviewed papers, open source, blog posts) and give Google feedback.

**Access.** Apply through the interest form on the TRC site. On acceptance, TPU quota is attached to a Google Cloud project that you own and you drive TPU VMs with gcloud compute tpus tpu-vm create / ssh.

**Caveats.** The TPUs are free; the Google Cloud project around them is not. Cloud Storage buckets, egress and any non-TPU VMs bill to your own card, which is how people get surprised. Grants are time-limited (typically a fixed number of months) and renewal is discretionary. If you only want to try a TPU once, Colab offers TPU runtimes with no application.

*Also listed under: cs-ml.*

## Publishing

### [Dryad](https://datadryad.org/costs)

`Freemium, email` · beginner 4/5 · curated data repository (fee-based, waivers available)

Curated, journal-integrated data repository. Unsponsored authors pay a Data Publishing Charge on a published scale effective May 2025: $150 up to 5 GB, $180 up to 10 GB, $520 up to 50 GB, rising to $6,077 for 1 TB. Authors affiliated with a Dryad partner institution or journal have the DPC sponsored, covering submissions up to 10 GB.

**Access.** Submit at datadryad.org; check the partner list first. Optional 'Private for Peer Review' costs $50, credited against the DPC when the dataset publishes.

**Caveats.** Included here only because of the waiver policy: 'any author may request one', via the Fee waiver application form, which must be approved before you submit. Waivers are not granted above 10 GB. Invoicing instead of card payment adds a $199 administration fee. If you have no partner and no waiver, Zenodo is free and does the same job without curation.

### [Figshare (free individual account)](https://figshare.com/)

`Freemium, email` · beginner 5/5 · data and figure repository with DOI

Free repository for individual researchers that mints DOIs for publicly published datasets, figures, posters and code, with versioning, embargoes and an OAI-PMH/REST API. Figshare+ is the paid tier for large deposits.

**Access.** Web upload at figshare.com, a desktop uploader for large files, or the REST API at api.figshare.com with a personal token.

**Caveats.** Verify the current caps yourself before planning a big deposit: Figshare's public help pages were unreachable at the time of writing (August 2026), and the free account's private-workspace allowance and per-file ceiling have both changed in the past. Large datasets require the paid Figshare+ tier. Many institutions run a Figshare instance that covers their researchers — check before paying personally.

### [Harvard Dataverse](https://dataverse.harvard.edu/)

`Free (registration), email` · beginner 4/5 · open data repository (social science and general)

Free, open repository running the Dataverse software, open to researchers worldwide regardless of affiliation. Mints DOIs, versions datasets, ingests tabular files into a variable-level format with per-variable metadata, and exposes a full REST API.

**Access.** Deposit via the web interface at dataverse.harvard.edu, or the API (pip install pyDataverse) for scripted upload. Anyone can create a personal 'dataverse' collection.

**Caveats.** Per-file and per-dataset size limits apply and larger deposits need prior approval from Harvard support — I could not retrieve the current figures (the FAQ returned 403 in August 2026), so confirm before uploading anything large. Many national and institutional Dataverse installations exist; depositing in your own country's instance is often faster and better supported.

*Also listed under: social.*

### [Open Science Framework (OSF)](https://osf.io/)

`Free (registration), email` · beginner 5/5 · project storage, preregistration and DOIs

Free project workspace from the Center for Open Science combining file storage, preregistration, version history and DOI minting. OSF Storage is capped at 5 GB per private project or component and 50 GB per public project or component.

**Access.** Web interface at osf.io; osfclient (pip install osfclient) for command-line push/pull; add-ons connect Google Drive, Dropbox, S3, GitHub and figshare so large files can live elsewhere while the project stays the index.

**Caveats.** The caps are per component, not per account, so a large study can be split across components — this is the intended workaround, not a loophole. OSF encourages storage add-ons for anything bigger, which means the underlying cost moves to whatever service you connect. Making a project public is what unlocks the 50 GB tier.

### [Software Heritage](https://archive.softwareheritage.org/)

`Free` · beginner 4/5 · source code archive and persistent code identifiers

Universal archive that harvests and preserves source code with its full development history from GitHub, GitLab, PyPI, Debian and other forges, and issues SWHID persistent identifiers so a paper can cite an exact file, directory or commit rather than a URL that may rot.

**Access.** 'Save Code Now' form at archive.softwareheritage.org/save/ to archive a repository on demand; REST API at archive.softwareheritage.org/api/1/ for programmatic lookup; copy the SWHID from any archived object to cite it.

**Caveats.** It archives code, not data, and it is a preservation archive rather than a DOI service — a SWHID is citable but is not a DOI, so for a formal software citation most people pair Software Heritage with a Zenodo release (or deposit through HAL). Archiving is free and needs no account; on-demand saves of unusual forge types can require moderation.

### [Zenodo](https://zenodo.org/)

`Free (registration), email` · beginner 5/5 · general-purpose repository with DOI

CERN-operated repository that mints a DOI for any research output — data, code, slides, negative results. Each record comes with a default storage quota of 50 GB, plus up to 150 GB of additional allowance you can distribute across records from the storage-management interface.

**Access.** Web upload, or the REST API at https://zenodo.org/api/deposit/depositions with a personal access token. The GitHub integration mints a fresh DOI on every release, plus a concept DOI that always points at the latest version.

**Caveats.** The default per-record allowance is 100 files and 50 GB; through the storage-management interface a record can be raised to 200 GB total, and anything beyond that needs a support request explaining the case. Zenodo does not curate — metadata quality is entirely on you, and a bad record is a permanent bad record since DOIs are not withdrawn. Choose the licence at upload; changing it later on a published record is awkward.

## Funding

### [CloudBank](https://www.cloudbank.org/)

`Free tier, application` · beginner 3/5 · NSF-funded commercial cloud access

NSF-supported service that provisions no-cost commercial cloud accounts (AWS and others) for US researchers and educators, with a helpdesk, cost estimation, spending alerts and curated training. Access flows through NSF's ACCESS programme and the NAIRR Pilot.

**Access.** Request access via cloudbank.org/options-requesting-cloud-resources; accounts are provisioned with your existing institutional credentials and appear as ordinary cloud consoles.

**Caveats.** The value here is as much the cost consulting as the credit — CloudBank staff will review an architecture before you spend. In practice you need to be eligible for the upstream NSF programme (US institutional affiliation), and community-college educators are explicitly served. Allocations are finite and tied to a specific project.

### [Google Cloud research credits](https://cloud.google.com/edu/researchers)

`Free tier, application` · beginner 2/5 · cloud credits for academic research

Google Cloud runs an application for $5,000 in research credits for academic researchers, alongside the Google Public Sector Program for Accelerated Research (GPAR), which offers discounted GPU/TPU pricing and early access to accelerators and models.

**Access.** Apply through the 'Apply for $5,000 in research credits' link on cloud.google.com/edu/researchers; credits land in an existing Google Cloud billing account.

**Caveats.** GPAR is stated on Google's own page to be 'currently only available in the United States'. Credits expire (typically within a year), cover Google Cloud usage only, and do not stop you being billed once exhausted — set a budget alert on day one. Award amounts and eligibility change; confirm on the page before writing them into a grant application.

## Learning

### [HPC Carpentry: Introduction to High-Performance Computing](https://carpentries-incubator.github.io/hpc-intro/)

`Free` · beginner 3/5 · HPC cluster fundamentals

CC-BY 4.0 lesson, designed for about two days of teaching, covering connecting to a cluster over SSH, transferring files, submitting and monitoring jobs with a scheduler, understanding parallel execution, and judging which problems belong on a cluster at all.

**Access.** Free web material; work through it self-paced, or run the episodes on any cluster you have access to (it is written to be scheduler-agnostic with Slurm examples).

**Caveats.** Still a Carpentries Incubator lesson in beta — polished enough to teach from, but expect occasional rough edges and check the Slurm syntax against your own site's documentation. Assumes basic Unix shell competence; do the Software Carpentry shell lesson first if that is missing.

## Community

### [ACCESS Support](https://support.access-ci.org/)

`Free, email` · beginner 4/5 · research computing help desk and mentoring

The support layer around the US national cyberinfrastructure: a knowledge base of guides and code snippets, a ticket system, regular office hours for individual systems (Anvil, Pegasus workflows and others), MATCH services pairing researchers with experienced mentors for short-term help, and the Cyberinfrastructure Student Support Network.

**Access.** Open a ticket or browse the knowledge base at support.access-ci.org; office-hours sessions are listed on the site and are drop-in.

**Caveats.** Free to participate, and the MATCH mentoring is the genuinely underused part — a facilitator will sit with you on a specific problem rather than just answering a ticket. Practically oriented toward people using or applying for ACCESS resources, so the eligibility limits of ACCESS itself apply to the compute even where the advice is open.

### [Ask.CI (Ask.Cyberinfrastructure)](https://ask.cyberinfrastructure.org/)

`Free (registration), email` · beginner 4/5 · Q&A forum for research computing

Discourse-based Q&A site for researchers, facilitators and sysadmins doing research computing, with categories for general questions, open-ended discussion, NSF ACCESS support, campus research computing resources and how-to guides.

**Access.** Web forum; read without an account, register to post. Search first — many recurring cluster, scheduler and software-environment questions are already answered.

**Caveats.** Traffic is modest compared with Stack Overflow, so expect hours to days for a reply, and skewed toward US campus infrastructure. For a problem on one specific machine, the operator's own ticket system is almost always faster; Ask.CI is better for 'how do people usually do X' questions that no single help desk owns.
