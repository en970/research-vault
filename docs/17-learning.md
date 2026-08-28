# Learning materials

Part of [research-vault](../README.md). 59 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (1) · [Literature](#literature) (1) · [Compute](#compute) (1) · [Publishing](#publishing) (2) · [Funding](#funding) (3) · [Learning](#learning) (49) · [Community](#community) (2)

## Data

### [The On-Line Encyclopedia of Integer Sequences (OEIS)](https://oeis.org/)

`Free` · beginner 5/5 · integer sequence database

Database of 398,735 integer sequences as of 28 August 2026, each with terms, formulas, references, links, programs (PARI, Mathematica, Maple, Python) and cross-references. Maintained by the OEIS Foundation; the interface is translated into roughly 45 languages.

**Access.** Search by pasting terms at oeis.org, or query the JSON API: https://oeis.org/search?q=1,1,2,3,5,8&fmt=json ; contributing requires a free account.

**Caveats.** The classic research move — paste your unexplained sequence and discover it is already known — works in under a minute. Reuse is governed by the OEIS Foundation licence agreement linked in the site footer; check it before bulk-redistributing. Contributions are editorially reviewed, which is slow by design.

*Also listed under: mathematics.*

## Literature

### [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)

`Free` · beginner 5/5 · peer-reviewed open-access encyclopedia

A continuously maintained, editorially refereed reference work in philosophy and adjacent fields (logic, philosophy of science, ethics, philosophy of mind and language), with entries commissioned from specialists and revised over time.

**Access.** Web interface, no account, no advertising; every entry has a stable citable URL, a dated revision history and an archived-edition system for citing a specific version.

**Caveats.** Funded by Stanford, the National Endowment for the Humanities, library memberships and the Friends of the SEP Society rather than by subscriptions, which is why it is free without being fragile. Entries are long-form survey articles, so cite them as tertiary literature, not as the primary source.

## Compute

### [Binder (mybinder.org)](https://mybinder.org/)

`Free` · beginner 5/5 · free notebook execution for tutorials

Public service that builds a container from any Git repository containing an environment file and launches it as a live Jupyter session in the browser — the mechanism by which most of the open curricula in this list can be run without installing anything. Sessions get 1-2 GB RAM, up to about one CPU-hour of intensive use, and up to roughly six hours in total.

**Access.** Paste a repository URL at mybinder.org (or click a 'launch binder' badge in a tutorial's README); no login, no install.

**Caveats.** Everything is destroyed when you disconnect — no persistent storage, and sessions are culled after 10 minutes of inactivity. No GPU. It is donated capacity from a federation of operators, so build times and availability vary and heavy use is discouraged. Fine for working through a lesson; wrong for real analysis.

## Publishing

### [Journal of Open Source Education (JOSE)](https://jose.theoj.org/)

`Free, email` · beginner 4/5 · diamond open-access journal for teaching materials

Open Journals title (NumFOCUS-sponsored) publishing short papers for open-source educational software and open course modules; 91 papers published to date, with CC BY 4.0 licensing, author-retained copyright, CrossRef DOIs and Portico archiving. Review happens in the open on GitHub.

**Access.** Submissions go through jose.theoj.org/papers/new with the material in a public repository; there are no publication or subscription fees.

**Caveats.** Important as of 28 August 2026: the journal's front page states 'JOSE is not accepting submissions while the board deliberates on eligibility changes'. Check before planning a submission. Requirements are strict — materials must be feature-complete, openly licensed (CC-BY for text, OSI-approved for code) and genuinely computational.

### [OER Commons](https://www.oercommons.org/)

`Free (registration), email` · beginner 4/5 · OER repository and authoring platform

Public digital library of open educational resources run by ISKME, organised by subject and education level from preschool through graduate/professional, with curated Hubs and Groups. Its Open Author tool lets anyone write and publish a standalone learning module, lesson, assignment or assessment.

**Access.** Browse and download without an account; a free account unlocks Open Author for publishing your own material, or 'Add Link' to submit an existing resource for librarian review.

**Caveats.** Quality varies enormously and K-12 material dominates the index — filter by education level or you will drown. The value for a researcher is the publishing side: a free, indexed, citable home for teaching materials without running your own site.

## Funding

### [Google Summer of Code](https://summerofcode.withgoogle.com/)

`Free, application` · beginner 3/5 · paid open-source mentorship

A 12+ week online programme placing newcomers on open-source projects with mentors, scoped as roughly 90 hours (small), 175 hours (medium) or 350 hours (large). Stipends are set from a base of $3,000 USD for medium and $6,000 USD for large projects, adjusted by country purchasing-power parity within floors and caps of $1,500-$3,300 and $3,000-$6,600 respectively.

**Access.** Apply through summerofcode.withgoogle.com during the annual application window by proposing a project to a participating open-source organisation; no fee.

**Caveats.** No longer students-only — open to anyone new to open source who is 18+ at registration. Participants from Russia, Belarus, the DNR/LNR regions and US-embargoed countries are excluded. Many scientific software projects (NumFOCUS, Bioconductor, Julia, Astropy and similar) participate, which makes this a realistic paid entry route into research software for an unaffiliated developer.

### [ICTP (Abdus Salam International Centre for Theoretical Physics)](https://www.ictp.it/)

`Free, application` · beginner 2/5 · funded training for developing-country scientists

UNESCO Category 1 institute in Trieste, governed with the IAEA and Italy, whose entire mission is training scientists from developing countries: a postgraduate Diploma Programme with financial support, a year-round calendar of schools and workshops with tuition covered and travel/living support, an Associates Programme for repeat visits, and online seminar programmes.

**Access.** Apply through the activity pages on ictp.it — each school, workshop and programme has its own deadline and application form; financial support is requested in the same application.

**Caveats.** Competitive, and support is explicitly targeted at scientists from developing countries — eligibility varies by activity, so read each call. Physics and mathematics dominate, with growing quantitative biology, climate and HPC activity. Visa and travel logistics are the practical obstacle, not the money; some programmes now run partly online.

*Also listed under: physics, funding.*

### [Outreachy](https://www.outreachy.org/)

`Free, application` · beginner 3/5 · paid open-source internships

Software Freedom Conservancy programme offering fully remote three-month open-source internships with a $7,000 USD total stipend, for people who face underrepresentation, systemic bias or discrimination in the technical industry. The May 2026 cohort ran applications 6-13 February 2026 with internships 18 May-17 August 2026; the December 2026 cohort takes applications in early-to-mid August, with internships from early December 2026 to early March 2027.

**Access.** Apply at outreachy.org during a round's initial application window, then complete contributions to a project before the final application.

**Caveats.** The site is currently seeking sponsorship for the December 2026 cohort, so that round's size is not guaranteed — confirm before planning around it. The initial application asks about your circumstances and time availability; you must be free of other major commitments during the internship. Several science and research-infrastructure projects participate each round.

*Also listed under: cs-ml, funding, workflow-tools.*

## Learning

### [3Blue1Brown](https://www.3blue1brown.com/)

`Free` · beginner 5/5 · mathematical intuition (video)

Grant Sanderson's animated mathematics series, indexed by topic on the site: Essence of Linear Algebra, Essence of Calculus, Neural Networks, Differential Equations, Probability, Group Theory and Physics, with written lesson pages accompanying many videos.

**Access.** Free on YouTube and on the site's per-lesson pages; the animation engine, Manim, is open source (MIT, community edition installable with `pip install manim`).

**Caveats.** Builds intuition; it is not a substitute for working problems, and no exercises or assessment are provided. A Patreon tier buys early access and perks, not content — nothing is paywalled after release.

### [AIM Open Textbook Initiative](https://textbooks.aimath.org/)

`Free` · beginner 4/5 · curated open textbooks (mathematics)

The American Institute of Mathematics maintains an editorial-board-vetted list of roughly 80 approved open mathematics textbooks spanning 20+ course levels, from pre-calculus through linear algebra, abstract algebra, real and complex analysis, combinatorics and machine learning. Many titles are flagged as WCAG-accessible.

**Access.** Web list; each title links to the author's own site for free PDF, HTML and (often) LaTeX source.

**Caveats.** A curation layer rather than a host — AIM vouches for the books but does not serve them, so individual licences and formats vary. The board approves against published evaluation criteria, which is the point: it is a filter over the much noisier general OER pile.

*Also listed under: mathematics.*

### [Algorithms (Jeff Erickson)](https://jeffe.cs.illinois.edu/teaching/algorithms/)

`Free` · beginner 3/5 · algorithms textbook

A 472-page algorithms textbook (1st edition, June 2019) covering recursion, backtracking, dynamic programming, greedy algorithms, graphs, shortest paths, minimum spanning trees, maximum flows and NP-hardness, released under CC BY 4.0 with the full-colour electronic version free indefinitely.

**Access.** Direct PDF download of the whole book or individual chapters, plus free lecture notes on FFT, randomised and approximation algorithms, and a full archive of past homework, exams and lab handouts.

**Caveats.** Assumes discrete mathematics and basic data structures. The book is CC BY 4.0 but the supplementary lecture notes are CC BY-NC-SA. A cheap paperback exists; the free PDF is the same content in colour.

### [An Introduction to Statistical Learning](https://www.statlearning.com/)

`Free` · beginner 4/5 · statistical learning textbook

James, Witten, Hastie and Tibshirani's standard first course in statistical learning, with free official PDFs of the R editions (1st, 2013; 2nd, 2021, corrected June 2023) and the Python edition ISLP (2023). Every chapter ends in a computational lab.

**Access.** Direct PDF download from statlearning.com; labs use the `ISLR2` R package or `pip install ISLP` for the Python edition.

**Caveats.** The publisher (Springer) permits the free PDF; that arrangement is the authors', not a general Springer policy. Deliberately light on theory — its heavier sibling, The Elements of Statistical Learning, is also free from Hastie's Stanford page. Laptop-scale throughout.

### [CESSDA Data Management Expert Guide](https://dmeg.cessda.eu/Data-Management-Expert-Guide)

`Free` · beginner 5/5 · research data management (social sciences)

Seven-chapter guide for social science researchers applying FAIR principles across the data lifecycle: Plan, Organise & Document, Process, Store, Protect, Archive & Publish, Discover. Produced by the CESSDA Training Team (2017-2022).

**Access.** Read online with no registration; download the whole guide from Zenodo for offline study, or individual chapter PDFs.

**Caveats.** CC BY-SA 4.0. Written around European social-science archives and GDPR, so repository and legal examples are Europe-centric. The content dates from 2017-2022 and has not been substantially revised since, which shows in the tooling recommendations more than in the principles.

### [Cochrane Learning Resources](https://www.cochrane.org/learn)

`Free (registration), email` · beginner 4/5 · evidence synthesis and systematic review training

Cochrane's free training collection: Evidence Essentials (a beginner's guide to health evidence), 'Key Steps in a Systematic Review' short videos, 23 online learning modules on review methods, scoping and PICO, risk of bias, patient involvement and software, plus an archive of around 230 webinars from the past decade.

**Access.** Free Cochrane account, then work through the modules in the browser; the Cochrane Handbook for Systematic Reviews of Interventions is linked as the accompanying reference.

**Caveats.** These free modules are separate from Cochrane's paid interactive-learning product and from RevMan/Cochrane Library access, which in many countries depends on a national licence or institutional subscription. Health-research framing throughout, though the review methodology transfers to other fields. The best free grounding available in evidence synthesis if you have no methods supervisor.

### [Complexity Zoo](https://complexityzoo.net/Complexity_Zoo)

`Free` · beginner 2/5 · reference wiki (computational complexity)

A wiki catalogue of 551 computational complexity classes with definitions, containments and literature references, opened by Scott Aaronson in 2002, made a wiki in 2005, hosted at the University of Waterloo from 2012 to 2020 and now maintained by the LessWrong community.

**Access.** Web interface, no account to read; classes are alphabetised with cross-links, and editing requires a free account.

**Caveats.** The definitive index of what a class means and what is known about it, but not a course — definitions are terse and assume complexity theory basics. Its hosting has moved several times, so archive anything you cite heavily.

### [Convex Optimization (Boyd & Vandenberghe)](https://web.stanford.edu/~boyd/cvxbook/)

`Free` · beginner 2/5 · optimisation textbook

The standard graduate text on convex optimisation, kept on the web with the publisher's agreement, together with free lecture slides (updated summer 2023) and a GitHub repository of additional exercises.

**Access.** Direct PDF download of the full book and slides; pair it with `pip install cvxpy` to work the modelling exercises.

**Caveats.** Complete solutions are restricted — obtainable by email only for instructors teaching the material, not for self-learners. Mathematically demanding; expect to need linear algebra and real analysis first.

### [Coursera (free enrolment and financial aid)](https://www.coursera.org/)

`Freemium, email` · beginner 3/5 · MOOC platform — free tier

MOOC platform whose free route has narrowed. Coursera's own course FAQ states: 'To access course materials, assignments, and earn a Certificate, you'll need to purchase the Certificate experience when you enroll in a course... Some courses may also offer a Full Course, No Certificate option. This lets you access course materials, submit required assessments, and receive a final grade, but you won't be able to earn or purchase a Certificate.'

**Access.** Free account; on an individual course page look for the 'Full Course, No Certificate' option, or apply for financial aid, which Coursera says is available 'in select learning programs' where a link to apply appears.

**Caveats.** The old blanket 'Audit' button is no longer universal — on courses checked in August 2026 the word 'audit' does not appear at all, and enrolment defaults to a paid certificate experience or a trial. Guided Projects, Professional Certificates and most Specializations have no free path. Financial aid is per-course, needs an application, and takes roughly two weeks. Treat Coursera as a fallback after MIT OCW and the field-specific curricula in this list.

### [CS50x (Harvard)](https://cs50.harvard.edu/x/)

`Free (registration), email` · beginner 5/5 · intro CS course with free certificate

Harvard's introduction to computer science: eleven weeks of lectures, sections, shorts and problem sets in C, Python, SQL, HTML/CSS/JavaScript, with a final project. The 2026 edition is live, and prior years' work carries over.

**Access.** Free at cs50.harvard.edu/x with no payment; create a free edX account to submit problem sets and get automated feedback via the CS50 autograder.

**Caveats.** Unusual among MOOCs: a free CS50 certificate is issued to anyone scoring at least 70% on every problem set and lab plus the final project. The separate edX 'verified certificate' costs money and adds nothing pedagogically. Everything runs in a browser-based codespace, so no local install and no GPU needed.

### [Data-Driven Science and Engineering (Brunton & Kutz)](https://www.databookuw.com/)

`Freemium` · beginner 3/5 · data-driven modelling and control

Companion site to Brunton and Kutz's textbook (Cambridge, 2019), covering SVD, Fourier and wavelet transforms, sparsity and compressed sensing, regression and model selection, clustering, neural networks, data-driven dynamical systems, control and reduced-order models. Free lecture videos, MATLAB and Python code, datasets and problem sets are published for every chapter.

**Access.** Watch the chapter lecture videos linked from databookuw.com (Steve Brunton's YouTube channel), download the MATLAB/Python code and datasets, and work the posted problem sets.

**Caveats.** Be clear about the boundary: the videos, code, datasets, problem sets and the extra 'Deep Learning in Fluid Mechanics' course materials are free, but the textbook itself must be bought from Cambridge. The video series is coherent enough to follow without the book.

### [Dive into Deep Learning (d2l.ai)](https://d2l.ai/)

`Free` · beginner 3/5 · deep learning textbook

Interactive open textbook in 23 chapters from linear regression through transformers, reinforcement learning, optimisation and recommender systems, with every example implemented in PyTorch, NumPy/MXNet, JAX and TensorFlow. Adopted at 500 universities across 70 countries.

**Access.** Read free at d2l.ai; download per-chapter Jupyter notebooks, or `pip install d2l` to use the book's helper library alongside them.

**Caveats.** The full online version stays free; a Cambridge University Press print edition is sold separately. Early chapters run comfortably on a CPU laptop; the vision, NLP and pretraining chapters realistically want a GPU (Colab/Kaggle suffice for most).

*Also listed under: cs-ml.*

### [edX (audit track)](https://www.edx.org/)

`Free (registration), email` · beginner 4/5 · MOOC platform — free tier

University MOOC platform whose free audit track gives, in edX's own words, 'readings, video lectures, discussions, and ungraded assignments'. edX also states that 'in the free audit track you may not be able to access and complete course materials including, but not limited to, graded assignments and exams'.

**Access.** Free account, then choose 'Continue with audit track' at enrolment instead of the verified certificate option.

**Caveats.** Audit access is time-boxed: edX states auditors 'can only access the materials for as long as the course is active, generally 4-12 weeks', after which the course closes to you. No graded work in most courses, no instructor feedback, no certificate. edX's own site currently announces a forthcoming subscription plan, so the free tier's shape may change again; check the enrolment box before investing time in a course.

### [Elsevier Researcher Academy](https://researcheracademy.elsevier.com/)

`Free (registration), email` · beginner 4/5 · publishing skills e-learning

Free e-learning modules on the mechanics of publishing: manuscript preparation and technical writing, finding the right journal, going through peer review, becoming a reviewer (including a Certified Peer Reviewer Course), research metrics, open science and publishing ethics including plagiarism.

**Access.** Some modules are viewable directly; a free account unlocks unlimited access to all modules and progress tracking.

**Caveats.** Produced by a commercial publisher, so the framing of peer review, metrics and open access reflects Elsevier's perspective — useful for learning the machinery, less so for critical views of it. Genuinely free, with no institutional affiliation required, which is rare for publisher training.

### [EQUATOR Network](https://resources.equator-network.org/)

`Free` · beginner 4/5 · reporting guidelines and writing resources

Searchable library of 700+ reporting guidelines (CONSORT, PRISMA, STROBE, ARRIVE, CARE, SPIRIT and hundreds more) covering study types across health research, alongside toolkits for researchers, editors, peer reviewers and guideline developers.

**Access.** Web search of the guideline library with no account; pick the guideline matching your study design and use its checklist and flow diagram while writing.

**Caveats.** Health-research focused, but the discipline of writing to a checklist transfers. The library and the online toolkits are free; the UK EQUATOR Centre's taught Publication School and other in-person courses are separate offerings with their own conditions. Using the right checklist before submission is the cheapest possible improvement to a manuscript.

*Also listed under: medicine.*

### [fast.ai — Practical Deep Learning for Coders](https://course.fast.ai/)

`Free` · beginner 4/5 · deep learning course

Part 1 is nine ~90-minute lessons recorded at the University of Queensland (2022 edition); Part 2, 'Deep Learning Foundations to Stable Diffusion', adds 25+ lessons building diffusion models from scratch. The companion book is freely readable online as executable notebooks.

**Access.** Watch on the course site or YouTube with no registration; run the notebooks on Kaggle Notebooks or a cloud GPU — the course explicitly advises against configuring GPU drivers on your own machine unless you already know how.

**Caveats.** Part 1's videos date from 2022 and some library APIs have moved; the accompanying notebooks in the repo are updated more often than the videos. Top-down teaching order (train a model in lesson 1, understand it later) suits some people and frustrates others. No certificate.

*Also listed under: cs-ml.*

### [Galaxy Training Network](https://training.galaxyproject.org/)

`Free (registration), email` · beginner 5/5 · bioinformatics training

Open repository of 536 hands-on tutorials across 35 topics (genome assembly, variant calling, RNA-seq, single-cell, proteomics, ecology, climate, machine learning), built by 539 contributors over more than a decade.

**Access.** Web tutorials with 'run it on Galaxy' buttons that open the analysis on a public Galaxy server; free accounts on usegalaxy.org / .eu / .org.au give you the compute to actually complete them.

**Caveats.** CC BY 4.0. The killer feature for unaffiliated researchers is that the exercises run on public Galaxy servers rather than your machine — but those servers impose per-user storage and CPU quotas and can queue during busy periods. Tutorials also work as plain reading if you have your own compute.

*Also listed under: biology.*

### [Green Tea Press (Allen Downey's 'Think' series)](https://greenteapress.com/wp/)

`Free` · beginner 5/5 · free programming and statistics books

A dozen free books under open licences that permit copying and modification: Think Python (3rd ed), Think Stats (3rd ed), Think Bayes (2nd ed), Think DSP, Think Complexity (2nd ed), Think Data Structures, Think Java (2nd ed), Modeling and Simulation in Python, Elements of Data Science and Astronomical Data in Python.

**Access.** Direct download in several electronic formats; several titles ship as runnable Jupyter notebooks (Elements of Data Science, Astronomical Data in Python, Modeling and Simulation in Python).

**Caveats.** Genuinely modifiable licences, so these are the easiest open books to adapt for teaching in your own institution. Aimed at the level between beginner and competent practitioner — Think Stats and Think Bayes are computational rather than theoretical, which is a feature or a limitation depending on what you need. Hard copies are sold separately.

### [Hugging Face Learn](https://huggingface.co/learn)

`Free (registration), email` · beginner 4/5 · machine learning courses

A dozen free hands-on courses maintained alongside the libraries they teach: the LLM Course, Deep RL Course, Audio Course, Diffusion Course, Agents Course, Computer Vision Course, Robotics (LeRobot) Course, ML for Games, ML for 3D, a Context Engineering course, 'a smol course' on post-training, and the Open-Source AI Cookbook.

**Access.** Read in the browser; notebooks open directly in Colab. A free Hugging Face account is needed for the hands-on parts that push models or run Spaces.

**Caveats.** Courses track fast-moving libraries, so the written material is usually current but occasionally ahead of or behind the installed package version — pin versions from the course's requirements file. Several courses have optional certification that requires completing graded exercises and a free account. Serious fine-tuning exercises need a GPU (Colab free tier is usually enough for the tutorials as written).

*Also listed under: cs-ml.*

### [LibreTexts](https://libretexts.org/)

`Free` · beginner 4/5 · open textbook platform

Non-profit platform hosting 3,000+ open textbooks and 1,500,000+ pages across 17 subject libraries (biology, chemistry, engineering, geosciences, humanities, mathematics, physics, statistics, social sciences and others), plus 300,000+ homework questions in its ADAPT system.

**Access.** Web interface, no account to read; every page and book can be exported to PDF, and whole books can be remixed into your own version via the built-in remixer.

**Caveats.** Quality is genuinely uneven — the corpus is community-remixed, so a polished text sits next to a stub with the same styling. Licences vary per text (commonly CC BY-NC-SA); check before reusing. The ADAPT homework system requires an account.

### [MANTRA — Research Data Management Training](https://mantra.ed.ac.uk/)

`Free` · beginner 5/5 · research data management course

Free self-paced course from the University of Edinburgh Research Data Service in eight units: research data in context, data management planning, organising data, preparing data for archiving, keeping research data safe, protecting sensitive data, FAIR sharing and access, plus hands-on data handling tutorials in R, SPSS, ArcGIS and NVivo. Last updated May 2025.

**Access.** Web interface, no registration, no login; work through units in any order.

**Caveats.** UK/EU-flavoured on legal and ethical points (GDPR, UK funder expectations) — adapt the compliance sections to your jurisdiction. The software practicals assume access to SPSS, ArcGIS and NVivo, which are not free; the R practical is the one you can complete with no licences.

### [Mathematics for Machine Learning](https://mml-book.github.io/)

`Free` · beginner 3/5 · mathematical foundations

Deisenroth, Faisal and Ong (Cambridge, April 2020): seven chapters of mathematical foundations (linear algebra, analytic geometry, matrix decompositions, vector calculus, probability, continuous optimisation) then five chapters applying them to regression, PCA, Gaussian mixture models and SVMs. The authors state they will keep PDFs freely available.

**Access.** Direct PDF download from mml-book.github.io; free Jupyter tutorials with solutions for linear regression, PCA and GMMs, plus extra exercises with solutions hosted on Overleaf.

**Caveats.** Explicitly the prerequisite book, not an ML book — it teaches the mathematics so you can read the others. The instructor's solutions manual is available only from Cambridge on request; the student-facing exercise solutions are free.

### [MIT 18.06 Linear Algebra (Gilbert Strang)](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)

`Free` · beginner 4/5 · video lecture course (mathematics)

Gilbert Strang's full linear algebra course as taught at MIT in Spring 2010: complete lecture videos, problem sets with solutions, and exams with solutions. It is the course most quantitative fields point newcomers to for the linear algebra they actually use.

**Access.** Web interface, no account; stream or download the lecture videos from the course page or the OCW YouTube playlist, and work the posted problem sets against the published solutions.

**Caveats.** CC BY-NC-SA 4.0. Recorded in 2010; the accompanying Strang textbook is a separate paid purchase, though the course is self-contained without it. No feedback loop — you grade yourself against the solutions.

### [MIT OpenCourseWare](https://ocw.mit.edu/)

`Free` · beginner 5/5 · open courseware archive

Publishes materials from more than 2,500 MIT undergraduate and graduate courses: lecture notes, problem sets with solutions, exams with solutions, and full video lecture series for a subset. The site and its YouTube channel report over 500 million lifetime visits.

**Access.** Web interface, no account; each course page has a downloadable ZIP of all materials, and video courses are mirrored on the MIT OpenCourseWare YouTube channel.

**Caveats.** Licensed CC BY-NC-SA 4.0 — non-commercial reuse only. No credit, no certificate, no instructor contact and no grading. Only a minority of the 2,500+ courses have complete video; many pages are course snapshots from earlier years with dated software instructions. MIT's separate Open Learning Library (openlearning.mit.edu) adds ~60 courses with auto-graded interactive exercises, also free and also without certificates.

*Also listed under: social.*

### [Neural Networks: Zero to Hero (Andrej Karpathy)](https://karpathy.ai/zero-to-hero.html)

`Free` · beginner 3/5 · build-from-scratch deep learning

Eight long-form lectures that construct neural networks from nothing in plain Python: backpropagation (micrograd), character-level language modelling (makemore), MLPs, activations/gradients/BatchNorm, manual backprop, a WaveNet-style architecture, a GPT, and a tokenizer.

**Access.** Free YouTube videos plus the matching GitHub repositories (micrograd, makemore, nanoGPT, minbpe); each lecture has a runnable notebook.

**Caveats.** Assumes fluent Python and comfort with calculus notation. Everything trains on a CPU or a small GPU — that is deliberate. The last item in the syllabus is marked ongoing, so the series is not a finished, closed curriculum.

*Also listed under: cs-ml.*

### [Neuromatch Academy](https://neuromatch.io/courses/)

`Freemium, application` · beginner 3/5 · computational science summer schools

Global non-profit running intensive summer schools in Computational Neuroscience and Deep Learning (6-24 July 2026), NeuroAI and Computational Tools for Climate Science (13-24 July 2026), with Computational Behaviour launching July 2027. Curricula are short video introductions plus interactive Python notebooks, and the organisation reports 13,217 students, 1,262 TAs and participants from 137 countries.

**Access.** Course notebooks are published openly and runnable in Colab/Binder without enrolling; live enrolment goes through neuromatch.io with pod placement and a TA.

**Caveats.** The materials are genuinely free and self-studiable. The live programme is not: tuition is set by cost of living in your country, with tuition waivers and hardship discounts available on request, and a non-refundable processing fee applies to everyone including waiver recipients. The live value — daily TA time, a global pod, a mentored project — is what you lose by self-studying.

*Also listed under: neuro-psych.*

### [NIST Digital Library of Mathematical Functions (DLMF)](https://dlmf.nist.gov/)

`Free` · beginner 3/5 · reference work (special functions)

NIST's 36-chapter reference on mathematical functions and their properties — the modern successor to Abramowitz and Stegun and the companion to the NIST Handbook of Mathematical Functions. Current release: version 1.2.7, dated 2026-06-15.

**Access.** Web interface, no account; formulas have permanent equation identifiers for citation, and the site provides interactive plots and a software index pointing to implementations.

**Caveats.** Free to read and cite, but NIST's terms of use govern redistribution — check the copyright page before republishing content. It is a reference, not a tutorial: you need to already know which function you want.

*Also listed under: mathematics.*

### [nLab](https://ncatlab.org/nlab/show/HomePage)

`Free` · beginner 1/5 · reference wiki (category theory and mathematical physics)

Collaborative research wiki covering mathematics, physics and philosophy from a higher-category-theoretic and homotopy-theoretic perspective: foundations, category theory, topology, geometry, algebra, Lie theory, quantum field theory, gauge theory and string theory.

**Access.** Web interface, no account to read; discussion and coordination happen on the linked nForum.

**Caveats.** No formal licence — the site operates on an academic honour system: reuse and distribution are encouraged provided you acknowledge the source. Coverage is deep but uneven and written in a specific idiom; entries assume you already speak category theory. The domain is owned by Urs Schreiber and the server is hosted at Carnegie Mellon.

*Also listed under: mathematics.*

### [Open Textbook Library](https://open.umn.edu/opentextbooks)

`Free` · beginner 5/5 · open textbook index

Curated index of 1,873 open textbooks maintained by the Open Education Network at the University of Minnesota, with faculty-written reviews attached to many titles.

**Access.** Web interface; each entry links to a direct PDF/EPUB download or the publisher's copy. No account needed to read.

**Caveats.** It is an index, not a host — availability depends on the upstream site. Coverage is weighted to undergraduate courses; graduate-level titles are sparse. Only a fraction of titles carry reviews, and submitting a review requires a free account.

### [Open Yale Courses](https://oyc.yale.edu/)

`Free` · beginner 5/5 · video lecture archive (humanities and social sciences)

A fixed selection of introductory Yale College courses recorded in the classroom, each published as video, audio and full text transcripts — strongest in philosophy, political science, history, literature and economics, where free lecture video is otherwise scarce.

**Access.** Web interface, no account; stream or download video/audio and read transcripts per lecture.

**Caveats.** CC BY-NC-SA 3.0 with some third-party content excluded. Explicitly no credit, degree or certificate. It is a closed selection of introductory courses, not a growing library, and nothing here is at graduate seminar level.

### [OpenStax](https://openstax.org/)

`Free` · beginner 5/5 · open textbooks (introductory)

Rice University's openly licensed, peer-reviewed textbook programme; its public CMS API currently lists 129 book records across sciences, mathematics, social sciences, business and humanities. OpenStax reports use by 59,000+ instructors and 43.3 million students in more than 160 countries.

**Access.** Read in the browser or download the PDF at openstax.org/subjects with no account; the book catalogue is queryable at https://openstax.org/apps/cms/api/v2/pages/?type=books.Book

**Caveats.** Titles are overwhelmingly first- and second-year undergraduate; there is almost nothing at graduate level. Instructor resources (answer keys, test banks, slides) require a verified-instructor account. Print copies cost money. Most titles are CC BY 4.0 but check each book's licence page.

### [PIRSA (Perimeter Institute Recorded Seminar Archive)](https://pirsa.org/)

`Free` · beginner 2/5 · physics seminar and course video archive

A permanent, free, searchable and citable archive of recorded seminars, conference talks, full PSI graduate courses and public lectures from Perimeter Institute, running since 2002 and covering condensed matter, cosmology, mathematical physics, particle physics, quantum fields and strings, quantum foundations, quantum gravity, quantum information and strong gravity.

**Access.** Web interface, no account; every talk carries a unique PIRSA number so you can cite a specific seminar, and search filters by subject, speaker, date and talk type.

**Caveats.** Research-seminar level for the most part — the PSI graduate course recordings are the part usable as structured self-study. No problem sets, no assessment, no interaction with lecturers.

*Also listed under: physics.*

### [Programming Historian](https://programminghistorian.org/)

`Free` · beginner 5/5 · digital humanities tutorials

Peer-reviewed, open-access tutorial journal with 123 English lessons organised by research phase (acquire, transform, analyse, present, sustain), covering Python, APIs, web scraping, mapping, text analysis, data visualisation and machine learning for humanities data. Parallel editions in Spanish, French and Portuguese, each with its own ISSN.

**Access.** Web interface, no account; each lesson is a self-contained tutorial with sample data you can run on a laptop.

**Caveats.** CC BY. It is also a realistic publication venue: anyone may propose a lesson, editors work with you through open peer review, and there are no fees. The English call for submissions closes 15 February 2026; the Spanish, French and Portuguese editions accept submissions year-round. Older lessons can bit-rot — check the lesson's stated revision date against current library versions.

*Also listed under: humanities.*

### [Project Pythia](https://projectpythia.org/)

`Free` · beginner 4/5 · geoscientific Python curriculum

The education arm of Pangeo: a Foundations book covering the core scientific Python stack for geoscience, plus community-contributed Cookbooks with domain-specific analysis workflows (ocean, atmosphere, climate, remote sensing).

**Access.** Read the executable Jupyter Book at projectpythia.org/foundations; every notebook can be downloaded and run locally or on Binder/a JupyterHub.

**Caveats.** Code is Apache-2.0, prose CC BY 4.0. Cookbooks vary in maintenance — check the last-updated date before relying on one. Some workflows expect cloud-hosted datasets (S3/OSN) and will be slow on a thin connection; the Foundations book itself runs fine on a laptop.

*Also listed under: earth.*

### [Purdue OWL (Online Writing Lab)](https://owl.purdue.edu/)

`Free` · beginner 5/5 · academic writing and citation reference

Purdue's free writing resource covering APA (7th and 6th), MLA, Chicago, IEEE, AMA and ASA citation styles; grammar, punctuation and mechanics; conducting research and avoiding plagiarism; subject-specific writing including engineering, healthcare and journalism; graduate writing and thesis/dissertation guidance; and ESL/multilingual writer support.

**Access.** Web interface, no account; the citation-style sections are the reference practitioners keep open in a tab while writing.

**Caveats.** US-academic conventions throughout. It answers formatting and mechanics questions definitively; it does not teach scientific argument structure — pair it with a field-specific writing course. Note that no institutional login is needed, which is unusual among writing-centre resources.

### [QuantEcon lectures](https://quantecon.org/lectures/)

`Free` · beginner 3/5 · computational economics

Eight open lecture series covering Python programming for economics and finance, a first course in quantitative economics, intermediate and advanced quantitative economics, quantitative economics with JAX, continuous-time Markov chains, quantitative economics with Julia, and an introduction to economic modeling and data science.

**Access.** Read online; each lecture page offers a downloadable Jupyter notebook and the whole series as PDF. Companion library: `pip install quantecon` (e.g. `qe.MarkovChain(P).stationary_distributions`).

**Caveats.** Written by the QuantEcon group (Sargent, Stachurski and collaborators) and widely used as graduate coursework. The JAX series expects a GPU to be worth running; everything else is laptop-scale. No certificates, no assessment.

*Also listed under: econ-finance.*

### [R for Data Science (2nd edition)](https://r4ds.hadley.nz/)

`Free` · beginner 5/5 · data analysis in R

Wickham, Çetinkaya-Rundel and Grolemund's tidyverse-based introduction: data visualisation, transformation, tidying, strings, dates, factors, databases, web scraping, iteration and communication with Quarto. The website is free and the authors state it will stay that way.

**Access.** Read online at r4ds.hadley.nz; `install.packages("tidyverse")` in R and work the in-chapter exercises.

**Caveats.** Licensed CC BY-NC-ND 3.0 — you may read and share but not remix or use commercially. Teaches the tidyverse dialect specifically; base-R idioms are largely out of scope. A paid O'Reilly print edition exists but adds nothing over the website.

### [Reinforcement Learning: An Introduction (Sutton & Barto)](http://incompleteideas.net/book/the-book-2nd.html)

`Free` · beginner 3/5 · reinforcement learning textbook

The canonical RL text, 2nd edition (MIT Press, 2018), with the complete PDF published free by the authors alongside code, errata, slides, teaching aids, a LaTeX notation style file, and links to PDFs of the cited literature.

**Access.** Direct PDF download from the authors' page; exercise solutions are obtained by sending in your own solutions for a chapter.

**Caveats.** The host's HTTPS certificate is invalid, so the page and PDF are effectively served over plain HTTP — download and verify rather than browsing casually. Official solutions are incomplete and only exchanged for your own attempts. Covers tabular and function-approximation RL; nothing on modern deep RL implementations.

### [Rising Scholars (formerly AuthorAID)](https://risingscholars.net/)

`Free (registration), email` · beginner 5/5 · research writing courses and mentoring (Global South)

INASP's platform for researchers in low- and middle-income countries, rebranded from AuthorAID: free Moodle-based online courses in research writing, proposal writing and community-engaged research; free one-to-one mentoring matching with experienced researchers; and around 900 curated toolkits, videos and guides. Reports over 14,000 members from 175 countries.

**Access.** Free registration at risingscholars.net, then enrol in a course run or request a mentor; the resource library is browsable after sign-up.

**Caveats.** Note the URL change — authoraid.info now redirects here, and old bookmarks and citations point at the former name. Courses run in cohorts rather than continuously, so check the schedule. The mentoring is the distinctive part: it is the closest thing to a free supervisor for an unaffiliated or isolated researcher.

### [Scientific Python Lectures](https://lectures.scientific-python.org/)

`Free` · beginner 4/5 · scientific Python curriculum

Community-maintained tutorial series on the scientific Python ecosystem, each chapter a 1-2 hour course from beginner to expert: the Python language, NumPy, Matplotlib, SciPy, then debugging, optimising code, image processing, mathematical optimisation, statistics with statsmodels, symbolic maths with SymPy, scikit-image and scikit-learn.

**Access.** Read online, download the full PDF, or clone the source repository; every example runs on a plain laptop install.

**Caveats.** Maintained by the Scientific Python developer community with regular releases, so it tracks current library versions better than most tutorials. No exercises with solutions and no assessment; it is a structured reference rather than a course with a spine.

### [Seeing Theory](https://seeing-theory.brown.edu/)

`Free` · beginner 5/5 · interactive probability and statistics

Six interactive chapters built at Brown University — basic probability, compound probability, probability distributions, frequentist inference, Bayesian inference and regression analysis — each with manipulable D3 visualisations rather than static figures.

**Access.** Web interface, no account; a draft PDF textbook version is downloadable from the site.

**Caveats.** Deliberately shallow: it fixes intuitions about sampling distributions, priors and the CLT in an afternoon but does not teach you to do statistics. Best used before or alongside a real course, not instead of one.

### [Stanford Engineering Everywhere](https://see.stanford.edu/)

`Free` · beginner 4/5 · video lecture archive (CS and engineering)

Stanford's legacy open-courseware archive covering four course sequences — Introduction to Computer Science, Artificial Intelligence, Linear Systems and Optimization, and Logic — with complete lecture videos (streamable or downloadable), syllabi, handouts, homework and exams.

**Access.** Web interface, no account; videos can be downloaded for offline viewing, which matters on unreliable connections.

**Caveats.** Creative Commons licensed. This is an unchanging archive: no new courses, no assessments, no instructor contact, no certificate. The CS course material predates modern toolchains, so treat the code environments as historical. Still the free route to Andrew Ng's original CS229 and the CS106 sequence.

### [Statistical Rethinking (Richard McElreath)](https://xcelab.net/rm/)

`Freemium` · beginner 3/5 · applied Bayesian statistics

The most widely recommended free route into applied Bayesian modelling for empirical scientists: McElreath's full lecture video series, course repository with slides, homework and solutions (most recent full run: Rethinking 2024), and free sample chapters, plus community code ports to R, Python, Julia and Stan/brms.

**Access.** Videos on the @rmcelreath YouTube channel; slides, homework and solutions in the Rethinking course GitHub repositories; the `rethinking` R package installs from GitHub.

**Caveats.** The lectures, slides, homework and solutions are free; the textbook (CRC Press, 2nd edition) is paid, and only chapters 1-2 are free. A 3rd edition is in progress with no announced date. Doing the homework requires installing Stan or an equivalent — feasible on a laptop but the least frictionless part.

*Also listed under: neuro-psych.*

### [StatQuest](https://statquest.org/)

`Freemium` · beginner 5/5 · statistics and ML explainers

Josh Starmer's video series decomposing statistics, machine learning and neural network methods into step-by-step explanations — the channel most commonly recommended when someone needs to actually understand a method before applying it.

**Access.** Free videos on the StatQuest YouTube channel; free study guides linked from statquest.org.

**Caveats.** The boundary is clean: videos and some study guides are free; the illustrated guide books and the structured courses in the StatQuest store are paid. Conceptual rather than mathematical — you will still need a textbook for proofs and for anything beyond the standard method catalogue.

### [The Carpentries (Software, Data and Library Carpentry)](https://carpentries.org/)

`Free` · beginner 5/5 · research computing curricula

Three lesson programmes — Software Carpentry (shell, Git, Python/R), Data Carpentry (domain-specific data handling) and Library Carpentry (skills for librarians and information workers) — with all lesson material published openly. The organisation reports 5,500 instructors, 185 trainers, 5,014 workshops delivered and reach in 72 countries.

**Access.** Read and work through any lesson directly at carpentries.org/lessons; every lesson is a static website with setup instructions, sample data and exercises you can do alone.

**Caveats.** Self-study on the lessons is completely free. Attending an *official* workshop is not: hosts pay a workshop fee, and Instructor Training is a paid, seat-limited service (see the site's pricing page). The lessons assume a laptop on which you can install software — that is the only hardware barrier.

### [The Feynman Lectures on Physics (online edition)](https://www.feynmanlectures.caltech.edu/)

`Free` · beginner 3/5 · physics lectures

The complete three-volume Feynman Lectures published as a free, high-quality HTML edition with typeset equations, hosted by Caltech — the standard free reference for undergraduate and early-graduate physics intuition.

**Access.** Read in the browser, no account; volumes and chapters are individually addressable URLs suitable for citation.

**Caveats.** Reading only — the edition is browser-based, with no PDF or EPUB download for offline study, which is a real problem on intermittent connections. The site sits behind Cloudflare and was returning a block page to automated/atypical clients when checked on 2026-08-28; ordinary browsers are unaffected. Problem sets are not included.

*Also listed under: physics.*

### [The Missing Semester of Your CS Education (MIT)](https://missing.csail.mit.edu/)

`Free` · beginner 4/5 · research tooling and command line

Nine-lecture MIT course on the tools nobody teaches: shell and command-line environment, editors, version control with Git, debugging and profiling, code shipping and quality, and — in the 2026 edition — agentic coding. Lecture videos and full written notes are both published.

**Access.** Web notes at missing.csail.mit.edu plus YouTube videos; exercises at the end of each lecture are done in your own terminal.

**Caveats.** CC BY-NC-SA. Community translations exist in 19+ languages. Earlier iterations (2019, 2020) remain archived on the site if you want the pre-AI version of the curriculum. Assumes a Unix-like shell; Windows users need WSL.

### [The Stacks Project](https://stacks.math.columbia.edu/)

`Free` · beginner 1/5 · reference work (algebraic geometry)

An open-source textbook and reference on algebraic geometry, currently 7,654 pages across 116 chapters, 3,298 sections and 21,446 individually tagged results — every lemma, theorem and definition has a permanent tag you can cite even as the text is rewritten around it.

**Access.** Browse online, download the full PDF, or clone the LaTeX source from GitHub; cite by tag (e.g. Tag 01AB) rather than by page.

**Caveats.** Research-level and self-contained from commutative algebra upward — extraordinary as a reference, brutal as a first textbook. The permanent-tag system is the reason it is cited in papers; use it rather than page numbers.

*Also listed under: mathematics.*

### [The Turing Way](https://book.the-turing-way.org/)

`Free` · beginner 5/5 · reproducible research handbook

Community-written handbook in six guides — Reproducible Research, Project Design, Communication, Collaboration, Ethical Research and a Community Handbook — covering version control, testing, licensing, data management, reproducible environments, open-source project running and research ethics.

**Access.** Read the online book at book.the-turing-way.org; source and contribution workflow on GitHub, where you can open an issue or PR against any chapter.

**Caveats.** Prose CC BY 4.0, code MIT. The single best answer to 'how should I actually organise a computational project' for someone with no local mentor. Written by contributors from many countries and disciplines, so depth varies chapter to chapter.

*Also listed under: social, literature-access, workflow-tools.*

## Community

### [Cross Validated (Stack Exchange)](https://stats.stackexchange.com/)

`Free, email` · beginner 4/5 · Q&A — statistics and machine learning

The Stack Exchange site where working statisticians, methodologists and ML practitioners answer questions on study design, model choice, inference and data analysis; a large archive of answered method questions makes it as useful for searching as for asking.

**Access.** Read without an account; a free account is needed to ask, answer, comment or vote. Content is CC BY-SA.

**Caveats.** Moderation is strict: vague 'which test should I use' questions and undisguised coursework get closed quickly. Post a minimal reproducible description — data structure, what you tried, what you expected — and you will usually get a substantive answer within a day. Search the archive first; most standard questions are already answered well.

*Also listed under: social, workflow-tools.*

### [MathOverflow](https://mathoverflow.net/)

`Free, email` · beginner 2/5 · Q&A — research-level mathematics

Question-and-answer site for research-level mathematics, used by professional mathematicians and graduate students to ask about the current literature, counterexamples, and the status of specific results — the venue where an isolated researcher can reach specialists directly.

**Access.** Read without an account; free account required to ask or answer. Content is CC BY-SA.

**Caveats.** Strictly research-level: textbook, undergraduate and general study questions belong on math.stackexchange.com and are closed on sight here. Questions are expected to show you have searched the literature first. Answers frequently come from the people who wrote the relevant papers, which is the entire point.

*Also listed under: mathematics.*
