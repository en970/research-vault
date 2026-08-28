# Computer science & machine learning

Part of [research-vault](../README.md). 61 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (10) · [Software](#software) (16) · [Literature](#literature) (9) · [Compute](#compute) (3) · [Publishing](#publishing) (5) · [Funding](#funding) (4) · [Learning](#learning) (9) · [Community](#community) (5)

## Data

### [Common Crawl](https://commoncrawl.org/get-started)

`Free` · beginner 2/5 · web crawl corpus

Monthly web crawl archives going back to 2008 (CC-MAIN-2026-34 is a recent snapshot), published as WARC (raw HTTP), WAT (JSON metadata and links) and WET (extracted plaintext). The upstream source of nearly every open LLM pretraining corpus.

**Access.** Free HTTPS download from https://data.commoncrawl.org/ (no AWS account) or anonymous S3: aws s3 cp s3://commoncrawl/... --no-sign-request. Start from the per-crawl warc.paths.gz index and pull a few files; the columnar index supports URL/domain lookups.

**Caveats.** Each monthly crawl is on the order of hundreds of TB — you cannot process it whole on a laptop. Work from a handful of WET segments or use a derived corpus (FineWeb, Common Pile) instead. Content is unfiltered copyrighted web text; Common Crawl provides the crawl, not clearance to redistribute it.

### [Common Pile v0.1](https://blog.eleuther.ai/common-pile/)

`Free` · beginner 2/5 · openly licensed pretraining corpus

8 TB of openly licensed and public-domain text drawn from 30 sources, released by EleutherAI on 2025-06-05, together with Comma v0.1-1T and v0.1-2T (7B models trained on 1T and 2T tokens) that perform comparably to models trained on unlicensed data.

**Access.** Datasets and models on the Hugging Face Hub under the EleutherAI org; load_dataset('common-pile/...'). Filtering/curation code is on GitHub.

**Caveats.** This is the practical successor to The Pile, which EleutherAI no longer distributes in its original form because of copyrighted components (Books3 in particular). Every source here meets the Open Knowledge Foundation's Open Definition, including some share-alike licences — check per-source terms if you redistribute derivatives.

### [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)

`Free` · beginner 3/5 · open LLM pretraining corpus

Deduplicated, filtered English web corpus of 25.9 billion documents built from 114 Common Crawl snapshots (CC-MAIN-2013-20 through CC-MAIN-2025-26), released under ODC-By with a published ablation-driven recipe for every filtering decision.

**Access.** load_dataset('HuggingFaceFW/fineweb', name='sample-10BT', streaming=True). Named subsets of 10B, 100B and 350B tokens exist so you can train at a budget you can afford; individual CC dumps can be selected by name.

**Caveats.** ODC-By covers the dataset compilation, not the copyright status of the underlying web pages. The full corpus is tens of TB — use the sample subsets or streaming. English-only; FineWeb2 covers other languages.

### [Hugging Face Datasets Hub](https://huggingface.co/datasets)

`Free (registration), email` · beginner 4/5 · general ML dataset repository

1,022,008 public datasets as of 2026-08-28, spanning text, image, audio, video and tabular ML, most auto-converted to Parquet with a browsable row-level viewer. The single largest general-purpose ML dataset host.

**Access.** pip install datasets; then load_dataset('HuggingFaceFW/fineweb', 'sample-10BT', streaming=True) — streaming avoids downloading terabytes. Browsing and most downloads work without an account.

**Caveats.** Some datasets are gated and need you to accept terms while logged in. Free accounts get 'best-effort' public storage (no guaranteed quota) and 100 GB private storage if you want to publish your own; hard caps are 500 GB per file, <100k files per repo, <10k entries per folder. Quality is uneven — many uploads are unlicensed re-hosts, so check the dataset card and licence before use.

### [ImageNet](https://www.image-net.org/download.php)

`Free (registration), email` · beginner 3/5 · image classification benchmark

The ILSVRC-2012 subset (1,000 classes; 1,281,167 train / 50,000 val / 100,000 test images) remains the standard vision pretraining and benchmarking set; the full ImageNet with its ~21k WordNet synsets requires a separate access request.

**Access.** ILSVRC-2012 is downloadable from Kaggle with a free Kaggle account, avoiding the ImageNet registration flow. Full ImageNet: register on image-net.org, accept the Terms of Access, then download tar archives. Torch/TF loaders expect the ILSVRC directory layout.

**Caveats.** The Terms of Access restrict use to non-commercial research and education, and bind your employer if you are at a company — this rules out some industry and startup uses. ILSVRC-2012 alone is ~150 GB, so plan storage and bandwidth. Known label-noise and representation problems are well documented; ImageNet-V2 and ReaL labels are the usual correctives.

### [Kaggle Datasets](https://www.kaggle.com/datasets)

`Free (registration), email` · beginner 5/5 · community dataset repository + competitions

Public dataset repository attached to Kaggle's competition platform; also the sanctioned distribution point for the ILSVRC-2012 ImageNet subset. Datasets come with community notebooks showing how they have been used.

**Access.** pip install kaggle, create an API token at kaggle.com/settings (saves kaggle.json to ~/.kaggle/), then: kaggle datasets download -d <owner>/<name> -p ./data --unzip

**Caveats.** A free account is required for the API and for most downloads; phone verification is needed for some features. Licensing is declared by uploaders and is often wrong or absent — verify provenance before publishing results on a Kaggle-hosted copy of a dataset.

### [OpenML](https://www.openml.org/)

`Free (registration), api-key` · beginner 4/5 · benchmark datasets + task/run archive

Open platform pairing datasets with standardised 'tasks' (a dataset plus a fixed train/test split and target metric) and with uploaded runs, so results are directly comparable across papers. Strongest for tabular and classical ML benchmarking.

**Access.** pip install openml; import openml; task = openml.tasks.get_task(32); dataset = task.get_dataset(). Reading needs no key; publishing runs needs a free API key. R, Java and Weka clients also exist, plus a REST API.

**Caveats.** Download and reuse require no registration; only uploading results does. Coverage of deep-learning-scale datasets is thin — this is a tabular/classical-ML benchmarking commons, not a source of pretraining corpora.

### [Re-LAION-5B](https://laion.ai/blog/relaion-5b/)

`Free` · beginner 1/5 · image-text pair index

5,526,641,167 text-to-image-URL pairs released 2024-08-30 under Apache-2.0, replacing the original LAION-5B after 2,236 links matching CSAM hashes from IWF, C3P and the Stanford Internet Observatory were removed.

**Access.** Metadata parquet files from the LAION site and Hugging Face; images must be fetched yourself with img2dataset (pip install img2dataset), which downloads and resizes from the URLs.

**Caveats.** This is an index of URLs, not images — link rot means a meaningful fraction no longer resolve, and downloading billions of images is not a laptop-scale job. The original LAION-5B was withdrawn entirely in December 2023 after Stanford's safety report; cite Re-LAION-5B specifically, and expect ethics review scrutiny for any work using it. The safety cleaning targeted known CSAM hashes only, not the wider NSFW/bias problems the corpus is known to have.

### [The Stack v2](https://huggingface.co/datasets/bigcode/the-stack-v2)

`Free (registration), email` · beginner 2/5 · source-code corpus

3.28 billion unique files from 104.2 million GitHub repositories, 67.53 TB uncompressed, covering over 600 programming and markup languages; built by BigCode from the Software Heritage archive and restricted to permissively licensed or licence-free files.

**Access.** Gated on the Hugging Face Hub — accept the terms while logged in, then load_dataset('bigcode/the-stack-v2', 'Python', streaming=True). The Hub copy holds metadata and file IDs; full file contents come from Software Heritage S3.

**Caveats.** Bulk download of contents requires a separate agreement with Software Heritage/INRIA (datasets@softwareheritage.org) — the Hub gate alone is not enough for the whole corpus. You must honour the original per-file licences including attribution clauses. Developers can opt out via the 'Am I in The Stack?' tool, so pin a version and record which one you used.

### [UCI Machine Learning Repository](https://archive.ics.uci.edu/)

`Free` · beginner 5/5 · classic benchmark datasets

689 curated datasets (as of 2026-08-28), most small enough to fit in memory, with documented variables and citation requests. The default source for teaching examples and classical-ML baselines since 1987.

**Access.** pip install ucimlrepo; from ucimlrepo import fetch_ucirepo; iris = fetch_ucirepo(id=53) returns pandas frames. Direct CSV download also works from each dataset page.

**Caveats.** Datasets are mostly tiny and old; several classics (e.g. Iris, Boston Housing) carry known measurement or fairness problems and should not be used to make substantive empirical claims. Licences vary per dataset and some are only 'cite this paper'.

## Software

### [Aim](https://github.com/aimhubio/aim)

`Free` · beginner 3/5 · experiment tracking (self-hosted)

Apache-2.0 self-hosted experiment tracker whose UI is built for comparing thousands of runs at once, with hyperparameters as first-class searchable objects and a Python query API over logged metrics, images and audio.

**Access.** pip install aim; from aim import Run; run = Run(); run['hparams'] = {...}; run.track(loss, name='loss'). Then aim up to open the local UI.

**Caveats.** No hosted option and no built-in multi-user authentication — you run the server yourself and secure it yourself. Development is less brisk than MLflow's, and integrations with newer frameworks lag; check recent commits before committing a long project to it.

### [Gymnasium](https://gymnasium.farama.org/)

`Free` · beginner 4/5 · reinforcement learning environments

The maintained fork of OpenAI Gym, now the de facto RL API standard, curated by the Farama Foundation. Ships Classic Control, Box2D, Toy Text, MuJoCo and Atari environments behind one reset/step interface.

**Access.** pip install 'gymnasium[classic-control]' (extras: box2d, mujoco, atari, all). import gymnasium as gym; env = gym.make('CartPole-v1'); obs, info = env.reset(); obs, r, term, trunc, info = env.step(a)

**Caveats.** MIT. OpenAI Gym itself is unmaintained — code and tutorials written against gym's old 4-tuple step API will not run; port to the 5-tuple. Classic Control and Toy Text train on a CPU laptop in minutes; Atari and MuJoCo need hours of GPU or many CPU cores.

### [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)

`Free` · beginner 4/5 · pretrained model library

Uniform loading, fine-tuning and inference API over the 3,028,707 models on the Hub (count as of 2026-08-28), covering text, vision, audio and multimodal architectures, with PyTorch as the primary backend.

**Access.** pip install transformers; from transformers import pipeline; pipe = pipeline('text-generation', model='Qwen/Qwen3-8B'). Companion packages: datasets (data), accelerate (multi-GPU/mixed precision), peft (LoRA/QLoRA), trl (SFT/DPO).

**Caveats.** Apache-2.0 for the library; each model carries its own licence and some are gated behind an accepted agreement. The API changes fast — pin versions in any paper's requirements file, because notebooks from two years ago frequently no longer run.

### [JAX](https://docs.jax.dev/en/latest/)

`Free` · beginner 2/5 · array computing / autodiff framework

NumPy-compatible array library with composable function transforms (jit, grad, vmap, pmap/shard_map) compiled through XLA to CPU, GPU and TPU. The default stack for TPU work and for much of the research on scaling and optimisation.

**Access.** pip install jax for CPU/Apple; pip install -U 'jax[cuda12]' for NVIDIA; on Cloud TPU VMs the TPU build is preinstalled. Neural nets are written with Flax (pip install flax) plus Optax for optimisers.

**Caveats.** Apache-2.0. The functional/pure-function style and explicit PRNG keys are a real learning curve if you come from PyTorch, and the third-party ecosystem (data loading, pretrained checkpoints) is much thinner. Best payoff if you get TPU Research Cloud access.

### [Llama (Meta)](https://www.llama.com/)

`Free (registration), email` · beginner 3/5 · open-weight model family

Meta's Llama models (Llama 4 is the current generation) are downloadable weights with a large fine-tuning ecosystem, distributed under the Llama Community License rather than an OSI-approved open-source licence.

**Access.** Accept the licence on the Hugging Face model page (meta-llama/*) or request access via Meta's download form, then load with transformers or run GGUF quantisations under llama.cpp.

**Caveats.** Not open source: the Llama Community License adds an Acceptable Use Policy, a naming/attribution requirement for derivative models, and a monthly-active-user threshold above which you must request a separate licence from Meta. Access is gated — you must accept terms while logged in. For work where licence cleanliness matters (redistribution, derived datasets, commercial spinouts), Qwen, OLMo or gpt-oss under Apache-2.0 are cleaner starting points.

### [llama.cpp](https://github.com/ggml-org/llama.cpp)

`Free` · beginner 4/5 · on-device LLM inference

Dependency-free C/C++ inference for LLMs and vision-language models with 1.5-bit through 8-bit integer quantisation in the GGUF format, CPU+GPU hybrid offload, and backends for ARM NEON, Apple Metal, x86 AVX/AVX2/AVX512/AMX, CUDA, HIP, Vulkan, SYCL and WebGPU.

**Access.** Prebuilt binaries, Docker, or build from source. Run a quantised model with: llama-cli -hf <user>/<repo>:Q4_K_M, or llama-server for an OpenAI-compatible local endpoint. Thousands of ready GGUF quantisations are on the Hugging Face Hub.

**Caveats.** MIT. This is the realistic route to running 7B–30B models on a laptop with no discrete GPU; expect single-digit tokens/second on CPU at 4-bit and quality loss below Q4. Not suitable for high-throughput batch evaluation.

### [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)

`Free` · beginner 3/5 · LLM benchmarking

EleutherAI's unified evaluation framework covering over 60 standard academic benchmarks with hundreds of subtasks; it is the backend behind Hugging Face's Open LLM Leaderboard, which makes its numbers directly comparable to published ones.

**Access.** pip install 'lm_eval[hf]' (add [vllm] or [api] for other backends). Run: lm_eval --model hf --model_args pretrained=Qwen/Qwen3-8B --tasks hellaswag,mmlu --device cuda:0. Backends include HF Transformers, vLLM, SGLang, OpenAI and Anthropic APIs, and ONNX Runtime.

**Caveats.** MIT. Reported scores are sensitive to prompt formatting, few-shot count and harness version — always record the exact commit and task revision, since leaderboard numbers from different versions are not comparable. Full MMLU-scale runs on a small GPU take hours.

### [MLflow](https://mlflow.org/)

`Free` · beginner 4/5 · experiment tracking (self-hosted)

Apache-2.0 platform covering experiment tracking, model registry, prompt versioning, LLM tracing and evaluation with 50+ built-in metrics and LLM judges. Runs entirely on your own machine with a local file or SQLite backend.

**Access.** pip install mlflow; mlflow.autolog() then train as usual; mlflow ui (or mlflow server) serves the dashboard at localhost:5000. No account, no network calls required.

**Caveats.** Fully free and offline-capable — the paid products are managed hostings (Databricks and others), not feature gates. There is no free multi-user hosted instance, so collaborating means running your own server. Aim (github.com/aimhubio/aim, Apache-2.0) is the lighter self-hosted alternative if you mainly want fast run comparison over thousands of runs.

### [OLMo 3](https://allenai.org/olmo)

`Free` · beginner 3/5 · fully open language model

Ai2's 7B and 32B models (Base, Instruct and Think variants, released 2025) shipped with the entire 'model flow': Dolma 3 pretraining data, mid- and post-training sets, OLMo-Core training code, OLMES evaluation code and intermediate checkpoints — not just final weights.

**Access.** Weights on the Hugging Face Hub under allenai/ (e.g. allenai/Olmo-3-7B-Instruct), loadable with transformers; intermediate checkpoints via the revision= argument. Training/eval code on github.com/allenai.

**Caveats.** Apache-2.0 weights, with Ai2's Responsible Use Guidelines attached. This is the only major model family where you can actually audit and re-run the data pipeline, which makes it the right choice for data-attribution, memorisation and training-dynamics research. The pretraining corpus Dolma is ODC-BY; earlier Dolma v1 was 3 trillion tokens.

### [Pythia scaling suite](https://huggingface.co/EleutherAI/pythia-6.9b)

`Free` · beginner 3/5 · interpretability model suite

16 models at eight sizes (70M, 160M, 410M, 1B, 1.4B, 2.8B, 6.9B, 12B), each trained on the Pile in both standard and deduplicated form, with 154 intermediate checkpoints per model and a fixed, published data order.

**Access.** transformers with revision='step3000' etc. to load any checkpoint: AutoModelForCausalLM.from_pretrained('EleutherAI/pythia-410m', revision='step100000'). The 70M–410M models train and probe fine on a laptop or free Colab tier.

**Caveats.** Apache-2.0. Built for scientific study of training dynamics, memorisation and interpretability rather than downstream quality — do not use these as strong baselines for capability claims. They were trained on the original Pile, which EleutherAI no longer distributes; the Common Pile is its openly licensed successor.

### [PyTorch](https://pytorch.org/)

`Free` · beginner 3/5 · deep learning framework

The framework the overwhelming majority of ML papers are implemented in; eager-mode autograd with torch.compile for graph capture, distributed training primitives, and CPU / CUDA / ROCm / Apple MPS backends. Governed by the PyTorch Foundation under the Linux Foundation.

**Access.** pip install torch (CPU wheels work on any laptop; the site's selector gives the right CUDA/ROCm index URL). Minimal loop: model(x).backward(); optimizer.step(). Runs on Apple Silicon via device='mps'.

**Caveats.** BSD-3-Clause. CUDA wheels are multi-GB downloads — on a metered connection install the CPU build first. Training anything transformer-sized needs a GPU you probably do not own; pair with a free cloud tier or with LoRA-style methods.

### [Qwen open-weight models](https://huggingface.co/Qwen)

`Free` · beginner 4/5 · open-weight model family

Alibaba's Qwen family spans dense and mixture-of-experts LLMs from sub-1B to hundreds of billions of parameters plus ASR, TTS, vision-language and image-generation models; the widely used dense releases (e.g. Qwen3-8B, 8.2B params, 32k native context extensible to 131k via YaRN) are Apache-2.0.

**Access.** Load with transformers from the Hub, serve with vLLM, or run quantised GGUF builds under llama.cpp. Small variants (0.6B–8B) fine-tune on a single consumer GPU with peft/Unsloth.

**Caveats.** Licence is per-model — most dense releases are Apache-2.0, but check each model card, since some larger or specialised releases historically shipped under a bespoke Qwen licence. The family iterates fast, so pin an exact model revision in any paper or your results will not be reproducible.

### [scikit-learn](https://scikit-learn.org/stable/)

`Free` · beginner 5/5 · classical machine learning

Consistent fit/predict/transform API over classification, regression, clustering, dimensionality reduction, model selection and preprocessing, with a documentation set that doubles as a textbook of worked examples. Runs comfortably on a laptop CPU.

**Access.** pip install scikit-learn (or conda). from sklearn.ensemble import RandomForestClassifier; clf.fit(X, y). Cross-validation, pipelines and grid search are first-class: cross_val_score(pipe, X, y, cv=5).

**Caveats.** BSD-3-Clause, NumFOCUS-sponsored. Single-machine and mostly single-threaded by design — no GPU support and no out-of-core training for most estimators; datasets beyond a few GB need chunking or a different tool.

### [Unsloth](https://github.com/unslothai/unsloth)

`Free` · beginner 3/5 · efficient LLM fine-tuning

Fused Triton kernels and memory optimisations for LoRA/QLoRA fine-tuning, claiming roughly 2x faster training with about 70% less VRAM at no accuracy loss, with ready-made free Colab notebooks for common model families.

**Access.** pip install unsloth; FastLanguageModel.from_pretrained(...) as a drop-in for transformers, then train with trl's SFTTrainer. The repo's free Colab notebooks fine-tune small models on a T4.

**Caveats.** Core package Apache-2.0; the Unsloth Studio desktop UI is AGPL-3.0. Multi-GPU and NVIDIA/AMD/Intel/CPU/Vulkan support are in the open-source version. Kernel optimisations track specific architectures, so a brand-new model family may fall back to slower paths until support lands.

### [vLLM](https://github.com/vllm-project/vllm)

`Free` · beginner 3/5 · LLM inference server

High-throughput LLM inference and serving engine built on PagedAttention for KV-cache memory management, with continuous batching and INT8/INT4/FP8 quantisation. Started at UC Berkeley's Sky Computing Lab; now has 2000+ contributors.

**Access.** uv pip install vllm (or pip). Serve an OpenAI-compatible endpoint with: vllm serve Qwen/Qwen3-8B, then call it with the openai client against http://localhost:8000/v1. Also usable in-process via the LLM() class.

**Caveats.** Apache-2.0. Supports NVIDIA, AMD, Intel GPUs, x86/ARM/PowerPC CPUs and TPU/Gaudi/Ascend plugins, but CPU-only throughput is poor — for laptop inference use llama.cpp instead. This is the right tool for batch-evaluating a model over thousands of prompts on one rented or granted GPU.

### [Weights & Biases](https://wandb.ai/site/pricing/)

`Free tier, email` · beginner 4/5 · hosted experiment tracking

Hosted experiment tracking, sweeps and artifact lineage. The free personal tier includes 5 GB/month storage, 1 GB/month Weave ingestion and up to 5 model seats; a separate free academic licence grants Pro features with 200 GB storage and up to 100 seats.

**Access.** pip install wandb; wandb login; wandb.init(project='x'); wandb.log({'loss': l}). Sweeps are declared in YAML and run with wandb agent.

**Caveats.** The generous academic tier requires an institutional email address — precisely the thing unaffiliated researchers do not have, so they are held to the 5 GB/month free tier. Overages are billed ($0.03/GB storage). Self-hosting is offered only as a single-seat 'personal' server explicitly barred from corporate use. If you need a free multi-user or fully offline setup, use MLflow or Aim.

## Literature

### [ACL Anthology](https://aclanthology.org/)

`Free` · beginner 5/5 · field-specific open archive

131,027 papers across 3,495 volumes and 532 venues covering 75 years of computational linguistics — ACL, EMNLP, NAACL, EACL, COLING, LREC and their workshops — all free PDFs with no embargo.

**Access.** Web search and browse; per-paper BibTeX on every page; complete bibliographic data as downloadable XML and the anthology's own GitHub repository for bulk work.

**Caveats.** NLP only — no general ML or vision coverage. Licences vary by year and venue; check the per-paper statement before redistributing full text. The bulk XML gives metadata, not PDFs, so full-text mining still means crawling politely.

### [arXiv (cs and stat.ML)](https://arxiv.org/)

`Free` · beginner 5/5 · preprint server

Nearly 2.4 million e-prints; cs.LG, cs.CL, cs.CV and stat.ML are where essentially all ML work appears first, typically months before any conference proceedings. Full text is free with no paywall or account.

**Access.** Web, daily listing emails, RSS per category, or the OAI-PMH and arXiv APIs (pip install arxiv for a Python client). Bulk full text is available via the requester-pays S3 bulk-access buckets.

**Caveats.** Posting a first submission to a cs category requires endorsement by an existing arXiv author — the main friction for an unaffiliated first-time author; ask a collaborator or an author you have corresponded with. Since 2025-10-31, review articles and position papers in cs categories are only accepted if already peer-reviewed, with a journal reference and DOI supplied at submission. No peer review, so quality varies enormously.

### [DBLP](https://dblp.org/)

`Free` · beginner 4/5 · computer science bibliography

Curated bibliography of computer science publications maintained by Schloss Dagstuhl since 2018, with hand-disambiguated author pages — the most reliable way to get a complete, correctly attributed publication list for a CS researcher or venue.

**Access.** Free web search; no account. Bulk XML dump at dblp.org/xml/, RDF dump at dblp.org/rdf/, a JSON search API, and a public SPARQL endpoint at sparql.dblp.org. All metadata is CC0 1.0.

**Caveats.** Metadata only — no abstracts, no full text, no citation counts. Curation is manual, so very recent papers can take weeks to appear, and the team currently reports 8+ week backlogs on correction requests.

### [Distill](https://distill.pub/)

`Free` · beginner 5/5 · archived interactive ML journal

Peer-reviewed journal of interactive, visually explanatory ML articles (feature visualisation, circuits, attention, GNNs). It announced an indefinite hiatus on 2021-07-02; the last articles appeared 2021-09-02 and the full archive remains free and live.

**Access.** Read directly on the site; article sources and figures are on GitHub under the distillpub org, so the interactive diagram code is reusable.

**Caveats.** Not accepting submissions — do not plan a publication around it. The content is dated in places (pre-LLM-era framing) but the explanations of convnet interpretability, momentum and GNNs remain among the clearest available. Articles are CC-BY, so figures can be reused with attribution.

### [Hugging Face Papers](https://huggingface.co/papers/trending)

`Free` · beginner 5/5 · paper-to-code discovery

Daily, weekly and monthly trending lists of ML papers with community upvotes and direct links from each paper to its arXiv entry, GitHub repo, and any models, datasets and Spaces on the Hub. paperswithcode.com now redirects here.

**Access.** Browse without an account; log in only to upvote or subscribe to the daily digest. Author-claimed papers link to Hub artifacts automatically.

**Caveats.** This is the successor by redirect, not by feature parity: Papers with Code's structured SOTA leaderboards, benchmark tables and per-task dataset index are gone, and the surviving surface is popularity-ranked rather than task-indexed. For historical PwC benchmark tables you now need web-archive snapshots. Coverage skews to LLM/generative work with an active social following.

### [NeurIPS Proceedings](https://papers.nips.cc/)

`Free` · beginner 4/5 · open conference proceedings

Complete free archive of Advances in Neural Information Processing Systems from 1987 through 2025, including the Datasets and Benchmarks track that began in 2021, with PDFs, supplementary material and BibTeX per paper.

**Access.** Browse by year; each paper page exposes the PDF, supplemental zip, and a per-paper JSON/BibTeX. Predictable URL structure makes bulk metadata collection straightforward.

**Caveats.** The archive is the camera-ready record only; reviews and rebuttals for recent years live on OpenReview instead. Supplementary archives can be large, so fetch selectively.

### [OpenReview](https://openreview.net/)

`Free` · beginner 4/5 · open peer review archive

Nonprofit submission and review platform used by ICLR, NeurIPS, TMLR, ACL Rolling Review and hundreds of workshops; for many venues the reviews, author rebuttals, scores and public comments are readable alongside the paper.

**Access.** Free browsing at openreview.net/venues; programmatic access via pip install openreview-py (openreview.api.OpenReviewClient) against api2.openreview.net. Submitting requires a free profile.

**Caveats.** Review visibility is set per venue — some conferences publish reviews for accepted papers only, or after decisions. Two API generations coexist (API 2 by default; API 1 for most pre-2024 venues), so scraping historical venues means handling both. Reading needs no account; submission does.

### [Proceedings of Machine Learning Research (PMLR)](https://proceedings.mlr.press/)

`Free` · beginner 4/5 · open conference proceedings

339+ volumes from 2007 to 2026 carrying the official proceedings of ICML, AISTATS, COLT, UAI, CoRL and many workshops; every paper is a free PDF and authors retain copyright. ISSN 2640-3498.

**Access.** Browse by volume; each paper page has PDF, supplementary material and BibTeX. Volume metadata is published as machine-readable files in the PMLR GitHub repos.

**Caveats.** No APCs, but publication here follows acceptance at the associated conference — PMLR is not an independent submission venue. Search is basic; use Semantic Scholar or DBLP to find things, then follow the PMLR link.

### [Semantic Scholar Academic Graph API](https://www.semanticscholar.org/product/api)

`Free (registration), api-key` · beginner 3/5 · open bibliographic API

Programmatic access to 214 million papers, 2.49 billion citations and 79 million authors, including SPECTER2 embeddings, citation contexts, a recommendations endpoint, and bulk datasets (S2AG, S2ORC full-text corpus).

**Access.** REST at https://api.semanticscholar.org/graph/v1/paper/search?query=... — works with no key. Request a free key from the website form for higher limits; pip install semanticscholar wraps it. Bulk snapshots via the Datasets API.

**Caveats.** Unauthenticated calls share a single global pool that is heavily throttled during busy periods; a key is effectively required for anything beyond casual use, and introductory keyed limits start around 1 request/second. S2ORC full text covers open-access papers only. Key approval is manual and can take days.

## Compute

### [Hugging Face ZeroGPU Spaces](https://huggingface.co/docs/hub/spaces-zerogpu)

`Free tier, email` · beginner 3/5 · free on-demand GPU

Dynamically allocated NVIDIA RTX Pro 6000 Blackwell GPUs (48 GB half-card default, 96 GB full-card option) attached to Gradio Spaces. Daily quota: 2 minutes unauthenticated, 5 minutes on a free account, 40 minutes on PRO.

**Access.** Select ZeroGPU hardware in Space settings, then decorate GPU functions: import spaces; @spaces.GPU(duration=120). Free personal accounts in good standing (verified email, account older than 30 days) can host up to 2 ZeroGPU Spaces.

**Caveats.** This is demo and short-inference compute, not training compute — the default per-call runtime is 60 seconds and the free daily budget is 5 minutes of GPU time, resetting 24 hours after first use. Gradio SDK only; torch.compile is unsupported (use ahead-of-time compilation); PyTorch 2.8+ required. Remaining quota determines queue priority, so free accounts wait longest.

### [NAIRR Pilot](https://nairrpilot.org/)

`Free, application` · beginner 2/5 · national compute allocations (US)

NSF-led pilot connecting US researchers, educators and students to HPC and AI compute, curated datasets and pretrained models; 880+ research projects supported and 95 NAIRR Classroom awards made, with State and Regional AI Infrastructure Hubs announced in August 2026.

**Access.** Apply through the resource-request forms on nairrpilot.org (separate tracks for research, classroom and startup allocations). Datasets and models listed in the portal are freely accessible without an allocation.

**Caveats.** Eligibility is US-based: researchers and educators in the 50 states, DC and Puerto Rico. Allocations require a written request and are reviewed, so plan weeks of lead time. As a pilot programme its scope and funding are subject to change — check current call status before building a project timeline around it.

### [TPU Research Cloud (TRC)](https://sites.research.google/trc/about/)

`Free tier, application` · beginner 2/5 · free accelerator programme

Google programme giving accepted researchers free access to a cluster of more than 1,000 Cloud TPU devices for machine learning research, with no institutional affiliation requirement in the application.

**Access.** Fill in the expression-of-interest form on the TRC page describing your project; if accepted you get a quota of TPU VMs in a specified zone. Work in JAX/Flax (best supported) or PyTorch/XLA.

**Caveats.** The TPUs are free; the surrounding Google Cloud resources are not — you pay for Cloud Storage, egress and any non-TPU VMs, which can quietly become real money on large datasets. Access is time-boxed and renewable rather than open-ended, and is granted for a described research project. Expect to publish or otherwise report results. TPU debugging and the JAX/XLA toolchain are a genuine learning cost.

## Publishing

### [ACL Rolling Review](https://aclrollingreview.org/)

`Free, email` · beginner 2/5 · centralised review service (NLP)

Centralised two-month reviewing cycles for the ACL family; you submit once, receive reviews plus a meta-review, then 'commit' the reviewed paper to ACL, EACL, NAACL, EMNLP or a participating workshop. Reviews are decoupled from acceptance decisions.

**Access.** Submit through OpenReview at the cycle deadline listed on aclrollingreview.org/dates; if not committed, resubmit to a later cycle with the previous reviews attached.

**Caveats.** No submission fee, and the resulting papers land in the free ACL Anthology. Conference registration to present is a separate and substantial cost — ACL offers reduced rates and some volunteer/registration support, but budget for it before committing. Cycle deadlines are strict; check the dates page rather than assuming a fixed month.

### [Journal of Machine Learning Research (JMLR)](https://jmlr.org/)

`Free, email` · beginner 2/5 · diamond open-access journal

Volume 27 is running in 2026. All papers are free to read and free to publish — no APCs, no subscriptions — and the MLOSS (Machine Learning Open Source Software) track publishes short, citable papers about research software.

**Access.** Submit through the JMLR site; LaTeX style files provided. MLOSS submissions need a maintained open-source package with documentation plus a 4-page description.

**Caveats.** Genuinely diamond OA: no charge to authors or readers, run by volunteers. Standards are high and review is slow (often 6–12 months), so it is a poor fit for time-sensitive results — but the MLOSS track is one of the few ways an unaffiliated maintainer can get a peer-reviewed, citable record for a library.

### [Journal of Open Source Software (JOSS)](https://joss.theoj.org/)

`Free, email` · beginner 3/5 · software paper venue

Developer-friendly open-access journal for research software with zero APCs and zero subscription fees; 3,693 papers published as of 2026-08-28. Review happens openly in a GitHub issue against the actual repository.

**Access.** Write a ~1000-word paper.md in your repo, submit the repo URL on the JOSS site, then respond to reviewers in the public GitHub review issue. Accepted papers get a DOI and an ISSN-registered record (ISSN 2475-9066).

**Caveats.** Scope is the software, not the science it enables — you need substantial scholarly effort, documentation, tests and an OSI-approved licence, and thin wrapper packages are desk-rejected. Part of Open Journals, a NumFOCUS-sponsored project. Review is fast by journal standards (weeks to a few months) and is a realistic first publication for an unaffiliated maintainer.

### [Transactions on Machine Learning Research (TMLR)](https://jmlr.org/tmlr/)

`Free, email` · beginner 3/5 · diamond open-access journal

Rolling-submission ML journal that judges technical correctness and clear evidence rather than subjective significance or novelty, with double-blind review conducted entirely in public on OpenReview and no article processing charges.

**Access.** Submit at openreview.net/group?id=TMLR any time — no deadlines. Reviews and the action editor's decision appear publicly on the submission page.

**Caveats.** The best realistic venue for solid work that would be rejected from NeurIPS/ICML for 'insufficient novelty' — negative results, careful replications, and thorough empirical studies. No overlap with previously published work is permitted. Accepted TMLR papers can be presented at some ML conferences, but it does not carry conference-acceptance prestige in hiring committees that count venues.

### [Zenodo](https://zenodo.org/)

`Free (registration), email` · beginner 4/5 · data and code archiving with DOIs

General-purpose research repository built and operated by CERN and OpenAIRE on CERN's data centre. Every upload gets a DOI within seconds, with versioned records so each release of a dataset or model keeps its own citable identifier.

**Access.** Web upload, or enable the GitHub integration so each tagged release of a repository is archived automatically with a fresh DOI. REST API for scripted deposition.

**Caveats.** Free with a default limit around 50 GB per record (larger allowances on request) — enough for checkpoints and mid-sized datasets, not for a pretraining corpus. Uploads are intended to be permanent; you can create new versions but not silently delete a published record. Pair a Zenodo DOI with your arXiv preprint so reviewers can cite exactly the code you ran.

## Funding

### [Cohere Labs Scholars Program](https://cohere.com/research/scholars-program)

`Free, application` · beginner 3/5 · paid research fellowship

Full-time, paid, remote-first eight-month research programme starting each January, providing mentorship, large-scale compute and a salary. Explicitly recruits candidates with strong engineering skills and little or no publication record.

**Access.** Applications open annually around August for the following January cohort; apply through the Cohere Labs site. No PhD and no university affiliation required.

**Caveats.** This is a competitive full-time position, not a grant you hold alongside other work — you must be available full-time for eight months. Very high application volume. Check the site for the current cycle; the window is short and closes well before the cohort starts.

### [Google Summer of Code](https://summerofcode.withgoogle.com/)

`Free, application` · beginner 3/5 · stipended open-source contribution

Global online programme paying newcomers a stipend to work 12+ weeks on a project with a mentoring open-source organisation. Many ML-adjacent organisations participate regularly (scikit-learn, PyTorch ecosystem projects, NumFOCUS members).

**Access.** Browse accepted organisations and project ideas when the contributor application window opens, contact mentors early, then submit a proposal through the GSoC site.

**Caveats.** Open to anyone 18+ who is new to the organisation's project — since 2022 it is no longer students-only. Stipend size varies by project size and country of residence. Highly competitive, and organisations expect demonstrated contributions (merged PRs) before the deadline, so start engaging with a project months ahead. Sanctions rules exclude some countries.

### [NLnet Foundation grants (NGI Zero and related funds)](https://nlnet.nl/propose/)

`Free, application` · beginner 2/5 · small open-source research grants

Thematic funds supporting free/open technology projects, including open-source ML tooling. Grants are small and administratively light compared with academic funding, and individuals as well as organisations can apply.

**Access.** Submit a short proposal through nlnet.nl/propose during an open call. The next calls open 3 September 2026 with a deadline of 3 November 2026, 12:00 CEST.

**Caveats.** Releasing the funded software, hardware and content under libre/open licences and using open standards is a hard requirement across all funds. Calls are periodic — proposals cannot be submitted between calls. Use of generative AI in a proposal must be disclosed and documented. Fund scopes vary, so read the call-specific applicant guide; not every ML topic will fit.

### [Outreachy](https://www.outreachy.org/)

`Free, application` · beginner 3/5 · paid remote internship

Three-month remote internships in open source run by Software Freedom Conservancy, with a $7,000 USD total stipend, in cohorts running May–August and December–March. Projects include research, data science, documentation and UX as well as programming.

**Access.** Apply during the initial application window (for the May 2026 cohort: applications 6–13 February 2026, contribution period 17 March–15 April, internship 18 May–17 August), then make contributions to a chosen project during the contribution period.

**Caveats.** Eligibility is limited to people who face underrepresentation, systemic bias or discrimination in tech in their country — this is a targeted programme, not an open call. Selection weights the quality of contributions made during the unpaid contribution period, which is a real time commitment before any money arrives.

## Learning

### [Deep Learning (Goodfellow, Bengio, Courville)](https://www.deeplearningbook.org/)

`Free` · beginner 3/5 · foundational textbook

The 2016 MIT Press textbook, complete and permanently free to read online: applied maths foundations, modern practical deep networks, and a research-oriented part covering probabilistic models, autoencoders and generative models.

**Access.** Read the HTML chapters directly on the site. Exercises and lecture slides for teaching are linked from the same page.

**Caveats.** HTML only — the authors' MIT Press contract forbids distributing a PDF, and the pages carry light copy protection. Published 2016 and only minimally corrected since: nothing on transformers, LLMs, diffusion models or modern scaling. Still the standard reference for the mathematical and probabilistic foundations.

### [Dive into Deep Learning (d2l.ai)](https://d2l.ai/)

`Free` · beginner 4/5 · interactive textbook

Free online textbook of 23 chapters plus appendices where every section is an executable Jupyter notebook, with parallel implementations in PyTorch, JAX, TensorFlow and NumPy/MXNet. Adopted at roughly 500 universities in 70 countries.

**Access.** Read online, or download the notebooks and run locally; each section also has one-click launch on Colab and SageMaker Studio Lab. Printed edition from Cambridge University Press (February 2023) is the paid option.

**Caveats.** Covers maths, code and exercises together, which makes it slower but far more self-sufficient than a video course. Coverage of the newest LLM training and alignment practice is lighter than its coverage of fundamentals. The four framework variants are maintained unevenly — the PyTorch track is the most complete.

### [Hugging Face Learn](https://huggingface.co/learn)

`Free (registration), email` · beginner 5/5 · practical course collection

Twelve free hands-on courses plus the Open-Source AI Cookbook, covering LLMs, deep reinforcement learning, agents, computer vision, audio, diffusion models, robotics (LeRobot), post-training (smol course) and ML for games and 3D.

**Access.** Read chapters directly in the browser; each has runnable Colab notebooks. A free account is needed to submit graded exercises, push models to the Hub, and appear on course leaderboards (the Deep RL and Agents courses use these).

**Caveats.** Written against the Hugging Face libraries throughout, so you learn the ecosystem alongside the concepts — good for getting productive fast, less good for framework-independent understanding. Course quality varies: the LLM and Deep RL courses are well maintained; several community-authored ones are patchier and can lag library changes.

### [Neural Networks: Zero to Hero (Andrej Karpathy)](https://karpathy.ai/zero-to-hero.html)

`Free` · beginner 4/5 · from-scratch implementation course

Eight long-form video lectures (56 minutes to 2h25) building backpropagation, MLPs, batch normalisation, a WaveNet-style model, a GPT and a tokenizer entirely from scratch in Python, with every line typed on screen.

**Access.** Free on YouTube; accompanying code in the micrograd, makemore, nanoGPT and minbpe GitHub repos. Everything runs on a CPU laptop or free Colab — the models are deliberately tiny.

**Caveats.** Assumes solid Python and comfort with derivatives and Gaussians. Slow-going by design: the value is in coding along, not watching. The series is intermittently extended rather than complete, and stops short of modern large-scale training practice.

### [Practical Deep Learning for Coders (fast.ai)](https://course.fast.ai/)

`Free` · beginner 5/5 · applied deep learning course

Nine roughly 90-minute lessons taking a coder from a working image classifier in lesson 1 to building a diffusion model and training from scratch, with a companion book and forums. Recorded in 2022 at the University of Queensland.

**Access.** Free video lessons plus runnable notebooks. The course explicitly recommends running on Kaggle Notebooks or a hosted GPU rather than your own machine, and provides ready-to-fork notebooks for each.

**Caveats.** Prerequisite is about a year of Python plus high-school maths; no ML background needed. The current recording is the 2022 edition, so library APIs and the LLM-era material have moved on — the pedagogy and the top-down method hold up, but expect to patch code. Part 2 (Stable Diffusion from scratch) is the deeper follow-on.

### [Probabilistic Machine Learning (Kevin Murphy)](https://probml.github.io/pml-book/)

`Free` · beginner 2/5 · graduate reference textbooks

Two MIT Press volumes — 'An Introduction' (2022) and 'Advanced Topics' (2023) — whose draft PDFs are free from the book site, giving a probabilistic treatment of ML from linear models to deep generative models and inference.

**Access.** Free draft PDFs (the Introduction draft is dated 2025-04-18) under CC BY-NC-ND; code and per-chapter figure-reproducing Colabs at github.com/probml/pyprobml.

**Caveats.** Assumes comfort with linear algebra, multivariate calculus and probability — this is a reference and a graduate text, not a first course. CC BY-NC-ND on the drafts: no commercial use, no redistributing modifications. Cite the published MIT Press edition, not the draft.

### [Stanford CS224n (NLP with Deep Learning)](https://web.stanford.edu/class/cs224n/)

`Free` · beginner 3/5 · public university course

Stanford's NLP course, most recently Winter 2026, running from word vectors through transformers and large language models in PyTorch. Slides and assignments are updated publicly each year and the Spring 2024 lectures are on YouTube.

**Access.** Slides, notes and assignment handouts are linked from the syllabus page; the course states anyone is welcome to use them. Free reference textbooks (Jurafsky & Martin's Speech and Language Processing, Eisenstein, Goldberg) are linked alongside.

**Caveats.** Self-study only — no grading or credit; the paid XCS224N professional-program version is the credentialed route. Videos are from an earlier year than the current slides. Later assignments assume a GPU (Colab is sufficient) and a solid PyTorch footing.

### [Stanford CS231n (Deep Learning for Computer Vision)](https://cs231n.stanford.edu/)

`Free` · beginner 3/5 · public university course

Stanford's computer-vision course, most recently offered Spring 2026, with public lecture notes and tutorials at cs231n.github.io, assignments that build convnets and training loops from NumPy upward, and archived lecture videos on YouTube.

**Access.** Read the notes at cs231n.github.io, download the assignment notebooks from the course site, and follow along with the YouTube playlist from a previous year. Assignments run on CPU or free Colab.

**Caveats.** Only the materials are public — no grading, no credit, no instructor access, and assignment solutions are not published. Video recordings lag the current syllabus by one or more years, so the slides and notes are the current artefact. The NumPy-from-scratch assignments are the single best exercise for understanding backpropagation concretely.

### [Understanding Deep Learning (Simon Prince)](https://udlbook.github.io/udlbook/)

`Free` · beginner 4/5 · modern textbook with notebooks

MIT Press textbook whose full draft PDF is free from the author's site, covering supervised learning through transformers, diffusion models, reinforcement learning and interpretability, with per-chapter Python notebooks and slide decks.

**Access.** Download the PDF from the book site; notebooks, slides and a student answer booklet are in github.com/udlbook/udlbook (Notebooks/, Slides/). Notebooks are Colab-ready and mostly CPU-runnable.

**Caveats.** Repository materials are CC BY-NC-ND 4.0 — free to read and teach from, but no commercial reuse and no redistributing modified versions. The most current of the free deep-learning textbooks, and the one to prefer over Goodfellow et al. if you need transformers and diffusion covered properly.

## Community

### [Deep Learning Indaba](https://deeplearningindaba.com/)

`Free (registration), application` · beginner 4/5 · regional research community (Africa)

Grassroots movement of African AI researchers running an annual multi-day meeting (2026 edition in Nigeria) with advanced courses and mentorship, the country-level IndabaX events, a year-round mentorship programme, awards and an ideathon.

**Access.** Apply for the annual Indaba when the call opens; IndabaX events are locally organised and usually free or very low cost to attend. Practicals, tutorials and the Sauti Yetu interview series are published openly.

**Caveats.** The flagship meeting is competitive and application-based, with limited travel and accommodation support — apply early and treat funding as uncertain. IndabaX events in your own country are the lower-friction entry point. Focused on the African continent; the published teaching materials are useful to anyone.

### [EleutherAI](https://www.eleuther.ai/)

`Free, email` · beginner 3/5 · open research collective

Nonprofit research lab that began as a public Discord and still runs open, readable research channels on interpretability, alignment, and open language models; producer of the Pile, Pythia, GPT-NeoX, the Common Pile and lm-evaluation-harness.

**Access.** Join the public Discord linked from the site (discord.gg/zBGx3azzUn) and read the working channels; contribute through their GitHub repos. Contact contact@eleuther.ai for research collaboration.

**Caveats.** A place to do research alongside people, not a help desk — showing up with a concrete project and doing the reading gets a far better response than asking for a tutorial. There is no advertised general compute-grant programme for outsiders; compute typically follows from becoming an active contributor on a project. Channel volume is high; use search before asking.

### [Hugging Face Forums](https://discuss.huggingface.co/)

`Free (registration), email` · beginner 5/5 · practitioner Q&A

Discourse forum with categories for Beginners, Research, Models, Datasets, Spaces, the Hub and Show-and-Tell, where library maintainers and Hub staff answer alongside users. The practical place to debug transformers, datasets, Spaces and ZeroGPU problems.

**Access.** Read without an account; a free Hugging Face account lets you post. Include the library version, full traceback and a minimal reproduction — threads with those get answered, threads without them usually do not.

**Caveats.** Answer rates vary a lot by category; deep library bugs are better filed as GitHub issues on the relevant repo, and the Research category is quieter than the tooling ones. Older threads reference deprecated APIs, so check dates before copying code.

### [Masakhane](https://www.masakhane.io/)

`Free, email` · beginner 4/5 · participatory research community (African NLP)

Open grassroots NLP research community for African languages — 'we build together' — producing benchmark datasets and models including MasakhaNER and machine-translation results across dozens of languages, with contributions from the language communities themselves.

**Access.** Join the Slack and the Google Group from the site, attend the weekly meetings, and contribute through the Masakhane GitHub org. No prerequisites beyond the code of conduct — you do not need to be an NLP researcher.

**Caveats.** Genuinely open and participatory, and a rare route to co-authorship for researchers outside well-resourced institutions. Volunteer-driven, so project pace and mentoring depend on who is active in a given cycle. Contributions are expected to be released openly.

### [ML Collective](https://mlcollective.org/)

`Free, email` · beginner 4/5 · research collective for unaffiliated researchers

Independent 501(c)(3) nonprofit whose explicit mission is making ML research opportunities free and available to people without institutional access: free compute for experiments, office hours with experienced researchers, research jams, and the weekly Deep Learning: Classics and Trends reading group.

**Access.** Join the Discord and the calendar of open events from the site; DLCT is open to anyone by subscription. No application or affiliation required; email hello@mlcollective.org to propose a collaboration.

**Caveats.** Small and volunteer-run — compute and mentorship are finite and go to people who show up consistently with a project, not on request. This is the closest thing the field has to a home for genuinely unaffiliated researchers, and DLCT alone is worth attending for the paper-reading practice.
