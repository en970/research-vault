# Mathematics

Part of [research-vault](../README.md). 86 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (13) · [Software](#software) (20) · [Literature](#literature) (9) · [Compute](#compute) (8) · [Publishing](#publishing) (15) · [Funding](#funding) (5) · [Learning](#learning) (11) · [Community](#community) (5)

## Data

### [ATLAS of Finite Group Representations (Version 3)](https://brauer.maths.qmul.ac.uk/Atlas/v3/)

`Free` · beginner 2/5 · finite group representations

Version 3.004 of the ATLAS holds 5,215 explicit representations of about 716 groups - sporadic, alternating, linear, classical, exceptional Lie type and miscellaneous - as permutation and matrix representations. For M11, for instance, it gives permutation representations on 11, 12, 55, 66 and 165 points and matrices over Z, Z[i2], GF(2), GF(3), GF(4), GF(5), GF(11) and GF(25).

**Access.** Browse by family at brauer.maths.qmul.ac.uk/Atlas/v3/; each representation has a details page with standard generators and downloadable generator files. Programmatic route: in GAP, LoadPackage("atlasrep") (package 2.1.12, 19 August 2026) then AtlasGenerators("M11", 1), which fetches the same data over the network.

**Caveats.** Maintained by Robert Wilson and collaborators at Queen Mary University of London. Versions 2 and 3 of the site coexist and old links point at v2. Data is supplied as is, with provenance sometimes only implicit, and the standard generators must be used exactly as specified or results are not comparable with the literature. Assumes real familiarity with computational group theory.

### [Catalogue of Lattices](https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/)

`Free` · beginner 2/5 · lattices and sphere packings

Nebe-Sloane catalogue of about 160,000 lattices covering dimensions 1 to 40 with selected examples up to dimension 248: root, laminated, unimodular, modular, extremal and perfect lattices, the Leech, Niemeier and Barnes-Wall families, with Gram matrices, minima, kissing numbers, densities and theta-series data.

**Access.** Direct download per lattice in standard .std format, plus a gzipped archive (about 1 MB) of all .std files; conversion scripts are provided to read the data into GAP, MAGMA, MAPLE, MACSYMA and PARI.

**Caveats.** A static hand-built HTML catalogue: no search, no API, no versioning, and navigation is by index page. Some sections are pointers into the literature rather than downloadable data, and MAGMA - one of the supported output formats - is commercial. Cite the catalogue and the original papers, as the maintainers ask.

### [DLMF - NIST Digital Library of Mathematical Functions](https://dlmf.nist.gov/)

`Free` · beginner 4/5 · special-functions reference

36 chapters of vetted formulas, asymptotics, numerical methods and software pointers for special functions; the online companion to the NIST Handbook of Mathematical Functions. Version 1.2.7, released 2026-06-15, with a public errata list.

**Access.** Web interface; every equation has a permanent number and can be copied as LaTeX; chapters include 'Computation' sections and a software index pointing at free implementations (mpmath, GSL, Boost).

**Caveats.** A US government work, so effectively free to use, but NIST asks for citation and the site carries no blanket open licence for wholesale republication. It is a reference, not a computation engine - pair it with mpmath or Arb for actual evaluation.

### [FindStat](https://www.findstat.org/)

`Free` · beginner 3/5 · combinatorial statistics database

A database of 1,996 combinatorial statistics, 336 maps and 24 combinatorial collections (permutations, partitions, tableaux, posets, Dyck paths, ...), with a search engine that identifies your data as a composition of known maps and statistics.

**Access.** Web search: paste a list of (object, value) pairs and it returns candidate statistics; SageMath interface built in - 'from sage.databases.findstat import findstat' then findstat(your_data).

**Caveats.** Search and browsing are open; submitting new statistics or maps needs a free account and editorial review. Coverage is deep for classical enumerative combinatorics and thin outside it.

### [GroupNames](https://people.maths.bris.ac.uk/~matyd/GroupNames/)

`Free` · beginner 4/5 · finite group tables

Browsable tables of the finite groups of order at most 500, giving standard names, presentations, extension structure (direct, semidirect, central and wreath decompositions), properties (abelian, soluble, supersoluble, monomial, metacyclic, metabelian, p-group, perfect, simple, almost simple, quasisimple, rational) and character tables, each cross-linked to its GAP SmallGroup ID.

**Access.** Web interface: browse the lists for orders up to 60, 120, 250 or 500, filter by property, or jump to a family (C_n, D_n, S_n, A_n); each group page shows the GAP ID so results transfer straight into GAP or SageMath.

**Caveats.** A single-maintainer academic page rather than a versioned database - cite it with an access date. Orders with more than 300 groups (128, 192, 256, 288, 320, 384, 432, 448, 480) are split into separate listings and are the least convenient to browse; for anything past order 500 use GAP's SmallGroups library directly.

### [House of Graphs](https://houseofgraphs.org/)

`Free` · beginner 3/5 · graph database

A searchable database of 29,224 'interesting' graphs (totalElements reported by its own API on 2026-08-28) with computed invariants, plus a meta-directory pointing at complete generated lists (cubic graphs, snarks, fullerenes, hypohamiltonian graphs and so on).

**Access.** Web search by invariant ranges or by graph6 string; REST API, e.g. https://houseofgraphs.org/api/graphs?size=1 returns paged JSON; individual graphs download as graph6/adjacency lists that feed directly into nauty, SageMath or networkx.

**Caveats.** The front end is a JavaScript app, so scripted access should go through the API rather than scraping HTML. Submitting a graph as 'interesting' requires a free account.

### [ISGCI - Information System on Graph Classes and their Inclusions](https://www.graphclasses.org/)

`Free` · beginner 3/5 · graph classes and complexity

An encyclopaedia of graph classes holding 1,691 classes, 242,656 inclusions, 28,919 problem-complexity results and 51,902 bounds (site figures, last updated 2026-05-10), recording inclusions with witnesses and references, forbidden-subgraph characterisations, and the complexity of problems such as colourability, independent set, domination and recognition on each class.

**Access.** Web browsing by class or by problem; a downloadable Java application draws and colours inclusion diagrams and exports PostScript/GraphML/SVG; the underlying data is available as an XML file.

**Caveats.** The interactive diagram tool needs a local Java runtime. Bibliographic references are given, but conclusions should be checked against the cited papers before being used in print.

### [KnotInfo and LinkInfo](https://knotinfo.org/)

`Free` · beginner 3/5 · knot tables and invariants

Tables of knots up to 13 crossings (and links, in LinkInfo) with dozens of invariants per knot: braid and DT notation, Seifert matrices, Alexander/Jones/HOMFLY polynomials, signatures, geometric type, boundary slopes, sliceness data and more.

**Access.** Web table builder (tick the invariants, submit) with CSV/Excel export; SageMath ships an interface: 'from sage.knots.knotinfo import KnotInfo' then KnotInfo.K5_2.homfly_polynomial().

**Caveats.** Some invariant columns are incomplete or conditional on unproved conjectures; the site marks these, and the marks matter. Cite the database, not just the website, as the maintainers request.

### [LMFDB - L-functions and Modular Forms Database](https://www.lmfdb.org/)

`Free` · beginner 4/5 · number-theory data

Tables of L-functions, classical/Maass/Hilbert/Bianchi modular forms, elliptic curves, genus 2 curves, abelian varieties over finite fields, number fields, p-adic fields, Dirichlet characters, Artin representations, Galois and Sato-Tate groups, and abstract groups. The elliptic-curves-over-Q table alone holds 3,824,372 curves in 2,917,287 isogeny classes, with conductor up to 299,996,953.

**Access.** Web interface with searchable tables and 'knowls' (inline definitions); REST API, e.g. https://www.lmfdb.org/api/ec_curvedata/?conductor=i389&_format=json (type-prefixed values: i=int, s=string); source code and data-loading scripts on GitHub.

**Caveats.** API returns at most 100 rows per request and roughly 10,000 rows overall per query, so large-scale work means many paginated calls or building from the GitHub sources; there is no one-click full dump. Completeness varies sharply by table - read the per-section 'Completeness of the data' pages before drawing statistical conclusions.

### [Mathematics Genealogy Project](https://www.mathgenealogy.org/)

`Free` · beginner 5/5 · academic genealogy database

Database of doctoral advisor-student lineages in the mathematical sciences: 341,501 records as stated on its homepage on 28 August 2026, each giving the degree-granting institution, year, dissertation title and advisor(s). Hosted by the Department of Mathematics at North Dakota State University in association with the American Mathematical Society.

**Access.** Web interface: quick search by name or advanced search by institution, year and country; each record links up to advisors and down to students, and corrections or new entries go through the site's 'submit data' form.

**Caveats.** Volunteer-run and badly backlogged: the site states that submissions received after 1 October 2025 (new entries) and 18 August 2025 (updates) were still unprocessed as of August 2026, and asks people not to chase them. Coverage is thinner outside Europe and North America, older records can be wrong or conflated, and there is no API or bulk download.

### [MathRepo (MPI MiS mathematical research data repository)](https://mathrepo.mis.mpg.de/)

`Free` · beginner 3/5 · supplementary code and data for papers

A repository of research data attached to papers - scripts, certificates, computed examples - indexed by year (2017-2025), by author, and by the software used (Macaulay2, OSCAR, SageMath, Singular, polymake, HomotopyContinuation.jl, Julia, Python and others). Documentation build dated 2026-06-16.

**Access.** Browse by software or year and download files directly from the project page; each page states the paper it belongs to.

**Caveats.** Hosted by the Max Planck Institute for Mathematics in the Sciences (Leipzig), so coverage skews to nonlinear algebra, algebraic statistics and applied algebraic geometry rather than mathematics at large. Some entries depend on Magma or Maple, which are not free.

### [MIPLIB 2017](https://miplib.zib.de/)

`Free` · beginner 3/5 · mixed-integer programming instances

Sixth edition of the mixed-integer programming library curated at Zuse Institute Berlin with academic and industrial partners (the library dates to 1992). The collection set holds 1,065 real-world MIP instances and the benchmark set 240 of them, each tagged easy, hard or open with best known solutions and structural metadata.

**Access.** Direct download, no account: per-instance `.mps.gz` files and `.sol.gz` solutions from the instance pages, or whole-set ZIP archives from the download page (benchmark set 317.3 MB, collection set 3.5 GB, solutions 209.2 MB), plus model data, precomputed instance features, decomposition files and test scripts for solver runs.

**Caveats.** The site states no explicit licence for the instances; the maintainers ask that you cite the MIPLIB 2017 paper in Mathematical Programming Computation. Instance classifications and incumbent solutions are revised periodically, so record which version you benchmarked against. The instances are input data only - you still need a solver, and many collection instances are unsolved by design, so they will exhaust any time limit you set.

### [The On-Line Encyclopedia of Integer Sequences (OEIS)](https://oeis.org/)

`Free` · beginner 5/5 · integer sequence database

Contains 398,735 sequences as of 27 August 2026, each with terms, formulas, references, cross-references and often generating code. Content is licensed CC BY-SA 4.0.

**Access.** Web search at oeis.org; JSON API: https://oeis.org/search?q=1,1,2,5,14&fmt=json ; bulk files stripped.gz (all terms) and names.gz; per-sequence b-files give thousands of terms; in SageMath: oeis([1,1,2,5,14]).

**Caveats.** Reading and API use need no account; contributing a sequence or an edit requires a (free) registered account and passes through volunteer editors, which can take days to weeks. Be polite with the API - it is a small server run on donations.

## Software

### [FLINT (Fast Library for Number Theory)](https://flintlib.org/)

`Free` · beginner 2/5 · arbitrary-precision arithmetic library

LGPL v3+ C library providing arithmetic over the integers, rationals, algebraic, real, complex and p-adic numbers, finite fields and number fields, plus polynomials, power series, matrices, LLL, factorisation and special functions. Since 3.0 it absorbed Arb (ball arithmetic), Antic (algebraic numbers) and Calcium (exact reals/complexes); the project describes about 8,000 documented functions, 3,500 test programs and 900,000 lines of code. Latest release 3.6.0 (29 June 2026).

**Access.** Distribution packages or conda-forge; Python bindings: pip install python-flint (0.9.0, 3 July 2026; wheels for CPython 3.10-3.14 on Windows, macOS, Linux and WebAssembly), then 'from flint import arb; arb.pi()'. It is also the arithmetic backend inside SageMath, OSCAR/Nemo, Singular and Macaulay2, so many users get it indirectly.

**Caveats.** A library, not an interactive system - expect C or Python glue rather than a REPL. Ball arithmetic returns certified enclosures only if you actually read the radius; ignoring it turns a rigorous computation into a plausible-looking number. Source builds need GMP and MPFR.

### [GAP](https://www.gap-system.org/)

`Free` · beginner 3/5 · computational group theory

System for computational discrete algebra with emphasis on group theory: permutation, matrix, finitely presented and polycyclic groups, representations, characters, plus large data libraries (small groups, transitive groups, character tables). Version 4.16.1 released 23 August 2026; free including source.

**Access.** apt/dnf/Homebrew or conda-forge 'gap'; run 'gap' for the REPL, LoadPackage("ctbllib"); also reachable from SageMath (libgap) and from OSCAR.

**Caveats.** The GAP language is idiosyncratic and error messages are terse; expect a real learning curve. Some contributed packages need extra compilation or external programs.

### [GNU Octave](https://octave.org/)

`Free` · beginner 5/5 · numerical computing environment

GPL-licensed numerical computing language and environment whose syntax is largely MATLAB compatible, with dense and sparse linear algebra, ODE/DAE solvers, optimization, statistics and plotting, usable from a GUI or the command line. Version 11.3.0 was released on 1 June 2026.

**Access.** `brew install octave`, `apt install octave`, `conda install -c conda-forge octave`, or the Windows installer from octave.org/download; add-on packages with `pkg install -forge <name>`; run scripts headlessly with `octave file.m`.

**Caveats.** Compatibility with MATLAB is good for the core language and many library functions but is not complete: there is no Simulink equivalent, MathWorks toolboxes have only partial Octave Forge counterparts, and nontrivial MATLAB code usually needs edits. Performance on large problems generally trails MATLAB. Its main value is as the exit route when you lose an institutional MATLAB licence and still have .m files to run.

### [Isabelle and the Archive of Formal Proofs](https://www.isa-afp.org/)

`Free` · beginner 2/5 · proof assistant library

The AFP is a refereed collection of Isabelle formalisations: 1,024 entries by 607 authors, about 325,400 lemmas and 5,421,600 lines of code. Entries are citable, versioned with each Isabelle release, and cover algebra, analysis, number theory, logic and verified algorithms.

**Access.** Download the Isabelle bundle from isabelle.in.tum.de (includes the jEdit-based IDE), then add the AFP as a component; every entry is browsable as HTML theory text and downloadable as a tarball; submissions go through the AFP editors.

**Caveats.** Isabelle/HOL's logic (simply typed higher-order) differs from Lean's and Rocq's dependent type theory, so libraries are not interchangeable. Building large AFP entries locally can take hours of CPU.

### [Lean 4 and mathlib](https://leanprover-community.github.io/)

`Free` · beginner 2/5 · proof assistant and formal library

Lean 4 with mathlib, the community-built unified library of formalised mathematics: 135,940 definitions, 286,121 theorems and 772 contributors on the project's live statistics page as of 2026-08-28. Covers analysis, algebra, topology, category theory, number theory and more, all machine-checked.

**Access.** Install the 'elan' toolchain manager, then 'lake new myproject math' pulls mathlib; VS Code extension gives an interactive goal view; browse the API docs and the library overview online; run experiments in the browser at live.lean-lang.org with no install.

**Caveats.** Building mathlib from source is heavy; use the cached oleans that lake downloads. mathlib moves fast and breaks user code between versions - pin a toolchain. Contributing means a public GitHub PR and review, which is welcoming but slow.

### [Macaulay2](https://macaulay2.com/)

`Free` · beginner 2/5 · commutative algebra and algebraic geometry

Open-source system for computations in commutative algebra and algebraic geometry - Groebner bases, free resolutions, sheaf cohomology, primary decomposition - with a large ecosystem of user-contributed packages. NSF-funded since 1992.

**Access.** Distribution packages (Debian/Ubuntu, Fedora), Homebrew tap 'brew install macaulay2/tap/M2', or build from source; run 'M2', then loadPackage "..."; also usable from SageMath and inside MathRepo/OSCAR workflows.

**Caveats.** Windows support is via WSL. Groebner-basis computations can exhaust memory on a laptop with no warning; start small and use finite characteristic to test.

### [Maxima](https://maxima.sourceforge.io/)

`Free` · beginner 4/5 · general-purpose computer algebra system

GPL computer algebra system descended from Macsyma: symbolic differentiation and integration, Taylor series, Laplace transforms, ODEs, systems of linear equations, polynomials, sets, lists, vectors, matrices and tensors, with exact rationals, arbitrary-precision integers and variable-precision floats plus 2D/3D plotting. Released under the GPL in 1998 by William Schelter and updated frequently since.

**Access.** Distribution packages or the installers on maxima.sourceforge.io; three interfaces ship together - the 'maxima' command line, the wxMaxima notebook GUI and XMaxima. Also callable from SageMath (maxima_calculus) and from a SageMathCell in the browser.

**Caveats.** Its own Lisp-flavoured language, and its integration and simplification are weaker than commercial systems on hard inputs. The documentation is a reference manual rather than a tutorial; wxMaxima is the realistic entry point. For research-scale algebra, Singular/PARI/OSCAR are the better tools - Maxima's niche is fast, dependency-light symbolic calculus.

### [mpmath](https://mpmath.org/)

`Free` · beginner 4/5 · arbitrary-precision special functions

BSD-licensed pure-Python library for real and complex floating-point arithmetic at arbitrary precision: elementary and special functions (gamma, Riemann zeta with the Riemann-Siegel expansion, Bessel, elliptic, hypergeometric, Meijer G, Jacobi theta), numerical quadrature, differentiation, root finding, linear algebra and ODEs. Version 1.4.0, released 23 February 2026; no dependencies beyond Python 3.

**Access.** pip install mpmath; then 'from mpmath import mp, zeta, mpc; mp.dps = 50; zeta(mpc(0.5, 14.134725))'. It is SymPy's numerical backend and ships inside SageMath, so it is often already installed.

**Caveats.** Pure Python, so it is slow next to FLINT/Arb on heavy work, and results are heuristically accurate rather than rigorously bounded - use FLINT ball arithmetic when you need a proof-grade enclosure. This is the natural companion for actually evaluating the functions that DLMF only documents.

### [nauty and Traces](https://users.cecs.anu.edu.au/~bdm/nauty/)

`Free` · beginner 2/5 · graph isomorphism and generation

The standard programs for graph automorphism groups and canonical labelling, plus the gtools suite - geng generates all non-isomorphic graphs on n vertices very quickly, with generators for bipartite graphs, digraphs and multigraphs. Current version 2.9.3 (1 January 2026).

**Access.** Download and build the C source (portable, no dependencies); run e.g. 'geng -c 8' to generate connected 8-vertex graphs in graph6 format, 'dreadnaut' for interactive use; Python wrapper: pip install pynauty; also called internally by SageMath.

**Caveats.** Licence is free for research use but is nauty's own licence, not a standard OSI one - check it before redistributing inside your own package. Traces does not accept digraphs. Exhaustive generation grows explosively: 10-vertex graphs are fine, 12-vertex graphs are a project.

### [Normaliz](https://www.normaliz.uni-osnabrueck.de/)

`Free` · beginner 2/5 · affine monoids and lattice points

Open-source tool for affine monoids, rational cones and lattice polytopes: Hilbert bases, lattice-point enumeration, triangulations and Stanley decompositions, volumes, Hilbert/Ehrhart series and quasi-polynomials, and automorphism groups; also handles polyhedra over real algebraic number fields. Current release 3.11.1.

**Access.** GitHub releases or conda-forge; command line 'normaliz file.in', C++ API libnormaliz, Python bindings via pip install PyNormaliz; interfaces exist from SageMath, Macaulay2, Singular and OSCAR; a ready-made Binder notebook is linked from the front page.

**Caveats.** Input format is terse and documented mainly in the PDF manual. Ehrhart and Hilbert-series computations blow up quickly in dimension; parallel builds need OpenMP.

### [OSCAR](https://www.oscar-system.org/)

`Free` · beginner 3/5 · Julia-based computer algebra

Open-source computer algebra research system written in Julia that combines GAP, Singular, polymake and ANTIC/Nemo-Hecke in one language for group theory, commutative algebra, polyhedral and tropical geometry, and number theory. Version 1.8.1 released 10 August 2026.

**Access.** In Julia: using Pkg; Pkg.add("Oscar"); then 'using Oscar'. Tutorials, an online 'Try Online' service and the free OSCAR Book (covering version 1.0) are on the site; support runs through a public Slack channel.

**Caveats.** The API is still moving between minor versions, so pin the version in papers and re-check scripts after upgrades. First installation compiles a lot of Julia code and needs several GB of disk.

### [PARI/GP](https://pari.math.u-bordeaux.fr/)

`Free` · beginner 3/5 · number theory computation

A fast GPL system for number theory: arbitrary-precision arithmetic, number fields, elliptic curves, modular forms, L-functions, factorisation. Ships as the 'gp' calculator, the libpari C library and the gp2c compiler.

**Access.** apt/dnf/Homebrew 'pari-gp' or conda-forge; run 'gp' then e.g. ellinit([0,-1,1,-10,-20]); Python binding: pip install cypari2; browser demo linked from the front page ('Try GP in your browser'); also embedded in SageMath.

**Caveats.** The GP scripting language is small and quirky compared with Python; large computations need explicit precision management (\p) and stack sizing (parisizemax).

### [polymake](https://polymake.org/)

`Free` · beginner 2/5 · polyhedral geometry

Open-source system for polytopes, polyhedra and fans, and also simplicial complexes, matroids, graphs and tropical hypersurfaces. Latest stable release 4.15 (download page, revised 28 July 2026).

**Access.** Prebuilt tarballs (which bundle a suitable perl) from the site, or via OSCAR/SageMath interfaces; 'polymake' REPL, e.g. $p = cube(3); print $p->F_VECTOR; a browser 'try it online' service is linked from the wiki.

**Caveats.** Several install routes are offered today: a source tarball (41 MB, or a 7 MB minimal version), prebuilt tarballs for Linux and macOS that bundle a suitable perl, Debian/Fedora/Gentoo/Ubuntu packages, Homebrew, nightly Docker images, the Polymake.jl Julia interface and a browser 'try online' version (with restrictions, including missing visualisation). The prebuilt tarball remains the safest route when a distribution's perl version is awkward.

### [Regina](https://regina-normal.github.io/)

`Free` · beginner 3/5 · low-dimensional topology

Software for 3-manifold and 4-manifold topology and normal surface theory: triangulation censuses, normal/almost normal surfaces, angle structures, knot and link invariants, homology and recognition. Latest version 7.4.1 (November 2025).

**Access.** Packages for Linux distributions, macOS (download or App Store) and 64-bit Windows, or build from source; use the GUI, the command-line tools, or the Python module. Quickest route for scripting: pip install regina - self-contained wheels, version 7.4.1 of 23 December 2025, macOS 10.15+ and Linux only, Python interface without GUI - then 'import regina; t = regina.Example3.figureEight()'.

**Caveats.** Normal surface enumeration is exponential - even modest triangulations can run for hours or exhaust RAM. Some parts of the documentation lag the current release (the site's own documentation date is older than the binary).

### [SageMath](https://www.sagemath.org/)

`Free` · beginner 4/5 · general-purpose computer algebra system

A GPL-licensed mathematics system with a Python interface that bundles and unifies GAP, PARI/GP, Singular, FLINT, Maxima, NetworkX, NumPy/SciPy and around a hundred other components. Version 10.9 is the current stable release.

**Access.** conda install -c conda-forge sage is the recommended route on Linux and macOS; distribution packages or a source build also work. Linux binaries have been discontinued, and macOS binaries are published through the 3-manifolds GitHub releases page linked from sagemath.org/download.html. Then 'sage' for the REPL or the Sage Jupyter kernel. Windows users go through WSL. Zero-install options: SageMathCell and CoCalc.

**Caveats.** A source build is slow and disk-hungry (hours, several GB); use conda-forge or a distribution package on a modest laptop. Some optional interfaces target non-free systems (Magma, Maple, Mathematica) and simply do nothing without them.

### [Singular](https://www.singular.uni-kl.de/)

`Free` · beginner 2/5 · polynomial computation

GPL computer algebra system for polynomial computations with emphasis on commutative and non-commutative algebra, algebraic geometry and singularity theory; more than 90 libraries covering primary decomposition, normalisation, resolution of singularities, D-modules, invariant theory and classification of singularities.

**Access.** Distribution packages or conda-forge; run 'Singular'; a Jupyter interface and an online 'Try Online' service are linked from the site; Singular is also the commutative-algebra engine inside SageMath and OSCAR.

**Caveats.** The C-like scripting language is separate from Python/Julia, so most newcomers meet Singular indirectly through SageMath or OSCAR. Development continues at RPTU Kaiserslautern after the death of core author Hans Schoenemann in December 2025.

### [SnapPy](https://snappy.computop.org/)

`Free` · beginner 3/5 · hyperbolic 3-manifolds

Program and Python module for the topology and geometry of 3-manifolds, built on the SnapPea kernel: hyperbolic structures, verified computations, length spectra, cusp areas, link invariants and slice obstructions. Version 3.3.2 (March 2026); GPL v2 or later. The OrientableCuspedCensus was extended to 10 ideal tetrahedra, adding about 150,000 manifolds.

**Access.** pip install snappy; then 'from snappy import Manifold; M = Manifold("m004"); M.volume()'; standalone GUI applications for macOS/Linux/Windows; runs inside SageMath (10.8 and later; current Sage is 10.9) for verified and number-theoretic computations.

**Caveats.** Verified (interval-arithmetic) results require SageMath; without it results are numerical and should not be used as proof. Bundled censuses are large downloads on their own.

### [SymPy](https://www.sympy.org/)

`Free` · beginner 5/5 · symbolic computation in Python

BSD-licensed pure-Python computer algebra system covering symbolic algebra, calculus, equation and ODE solving, linear algebra, number theory, combinatorics, geometry and LaTeX/code output. Current release 1.14.0 (27 April 2025); its only hard dependency is mpmath, which supplies the arbitrary-precision floating point.

**Access.** pip install sympy (or conda install -c conda-forge sympy); then 'from sympy import symbols, integrate; x = symbols("x"); integrate(1/(x**2+1), x)'. Also bundled inside SageMath and available in any Jupyter kernel, including Binder and Colab.

**Caveats.** Being pure Python, it is far slower than the FLINT/Singular-backed systems on large Groebner bases, factorisation or high-precision work - move to SageMath or OSCAR when objects get big. simplify() is heuristic and not canonical, so symbolic equality needs care (use simplify(a-b) == 0 patterns, not a == b). The sympy.org front page still advertises 1.12 from 2023, so check PyPI or GitHub for the current release.

### [TeX Live](https://www.tug.org/texlive/)

`Free` · beginner 3/5 · typesetting

The comprehensive free TeX distribution: pdfTeX, LuaTeX, XeTeX, BibTeX/Biber, AMS packages, TikZ and essentially every CTAN package a mathematician needs for papers, theses and arXiv submissions. Released annually and maintained by the TeX Users Group.

**Access.** Run the install-tl network installer for the full current distribution, or install your distribution's texlive packages; then 'pdflatex paper.tex'; 'tlmgr install <pkg>' adds packages later.

**Caveats.** A full install is several GB; on a constrained laptop install the 'basic' or 'small' scheme and add packages with tlmgr. Distribution-packaged TeX Live is often a year or two behind, which matters when a journal class file needs a recent package.

### [The Rocq Prover (formerly Coq)](https://rocq-prover.org/)

`Free` · beginner 2/5 · proof assistant

Interactive theorem prover and dependently-typed programming language with over 40 years of development behind its core type theory; current release 9.2.0 (27 March 2026) and Rocq Platform 2026.07.0 (30 July 2026). Home of the Mathematical Components library and the formal proofs of the Four Colour and Feit-Thompson theorems.

**Access.** Install the Rocq Platform bundle (Windows/macOS/Linux) or 'opam install rocq-prover'; edit with VS Code, Emacs/Proof General or CoqIDE; there is a browser playground and a package index on the site.

**Caveats.** The rename from Coq is recent, so most tutorials, StackOverflow answers and package names you find still say 'Coq'. For mainstream research mathematics, Lean/mathlib now has the larger library; Rocq is stronger in program verification and in the SSReflect/MathComp style.

## Literature

### [AMS Open Math Notes](https://www.ams.org/open-math-notes)

`Free` · beginner 5/5 · lecture notes and draft textbooks

Repository of freely downloadable mathematical works hosted by the American Mathematical Society: draft course notes, textbooks and research expositions that have not been published elsewhere, plus short notes and JIBLM refereed inquiry-based course notes, spanning undergraduate to research level.

**Access.** Browse or search at ams.org/open-math-notes by subject, level and note type, sort by most downloaded, and take the PDF directly; no AMS membership needed. An optional free 'My Notes' account only saves items for later.

**Caveats.** Everything except the JIBLM course notes is explicitly draft material, unrefereed and subject to revision, so cite it as you would a preprint and expect items to change or disappear when an author publishes. Authors keep copyright and terms differ per item, so check before reusing notes in your own teaching. There is no API or bulk export, and the search is basic - browsing by subject is usually faster.

### [arXiv (mathematics archive)](https://arxiv.org/archive/math)

`Free, email` · beginner 5/5 · preprint server

The mathematics section of arXiv has run since February 1992 and is where essentially all research mathematics appears first, across subject classes from math.AG to math.ST. Full texts are free to read and download with no account.

**Access.** Browse https://arxiv.org/list/math.AG/recent, subscribe to daily mailings, or query the API: https://export.arxiv.org/api/query?search_query=cat:math.NT&max_results=20 ; submissions upload LaTeX source through the web interface.

**Caveats.** Reading needs nothing; submitting does. First-time submitters must be endorsed by an established arXiv author in that archive, and the automatic route is narrower than it sounds: per info.arxiv.org/help/endorsement.html your account may be endorsed automatically only if you have claimed ownership of a paper a co-author already submitted AND your email meets arXiv's institutional-email criteria - an institutional address by itself does not do it. This is the single biggest practical obstacle for unaffiliated researchers, so line up an endorser before you finish the paper (HAL has no endorsement requirement if you need a fallback archive). arXiv is not peer reviewed and moderators can reclassify or reject submissions.

### [EuDML - The European Digital Mathematics Library](https://eudml.org/)

`Free` · beginner 4/5 · digitised mathematics literature

Aggregator indexing 271,792 items across 14 collections of European mathematical literature - journal back-runs, seminar proceedings and books - with full text freely available for most items.

**Access.** Web search and browse by subject or journal; a reference-lookup tool matches citations to indexed items; links resolve to the hosting library (Numdam, GDZ, DML-CZ, etc.).

**Caveats.** It is an index, not a host: a minority of items sit behind a publisher's moving wall at the destination. Metadata quality varies by contributing collection and the interface is dated.

### [HAL (Hyper Articles en Ligne)](https://hal.science/)

`Free, email` · beginner 4/5 · open archive and preprint server

France's national open archive, run by the CNRS's CCSD: about 4.64 million records in total (4,644,610 returned by its search API on 2026-08-28), of which roughly 53,000 carry the mathematics domain code. Deposits are permanent, get a stable HAL identifier, and are the deposit route feeding the Episciences overlay journals (EPIGA, Annals of Formalized Mathematics).

**Access.** Search or query the API without an account: https://api.archives-ouvertes.fr/search/?q=domainAllCode_s:math&rows=20&wt=json . Depositing needs a free hal.science account; the form takes the PDF plus metadata, can forward the deposit to arXiv, and returns a citable identifier.

**Caveats.** Unlike arXiv there is no endorsement system, which makes HAL a realistic first-deposit route for unaffiliated researchers; deposits are still moderated for form, scope and rights and can take several days. The interface and most documentation are French-first, and the public web front end sits behind a bot check (Anubis), so scripted access must go through the API. Mathematicians still look on arXiv, so cross-deposit rather than substituting.

### [Numdam](https://www.numdam.org/)

`Free` · beginner 4/5 · French mathematics digital library

Full text of French research mathematics: about 75,719 articles from 120 journals and seminars, 706 books in 8 collections and 416 theses - over 1.4 million pages - including the Bourbaki, Cartan and Chevalley seminars, conference proceedings, lecture notes and doctoral theses, mostly digitised from first issues and extended with newer material supplied by publishers.

**Access.** Free PDF download from the article page; browse by journal, seminar or author; Centre Mersenne journals appear here one year after publication.

**Caveats.** Recent content can sit behind a moving wall of 2 to 10 years depending on the collection. The interface is bilingual but mostly French, and the search engine is occasionally offline.

### [OpenAlex](https://openalex.org/)

`Free` · beginner 3/5 · bibliographic metadata and citation graph

Open catalogue of scholarly works run by OurResearch: 322,147,582 works, 126,053,818 authors, 255,810 sources and 136,136 institutions on 2026-08-28, including about 3.65 million works classified in the mathematics field, with citation links, open-access status and topic labels. Data is CC0.

**Access.** REST API needing no key: https://api.openalex.org/works?filter=primary_topic.field.id:fields/26&per-page=25 (append '&mailto=you@example.org' for the polite pool); full monthly snapshot on AWS S3; Python client: pip install pyalex.

**Caveats.** Metadata is assembled automatically, so author disambiguation and mathematics classification are visibly weaker than zbMATH's - verify before putting counts in a paper. Per-second and per-day rate limits apply, and heavy analyses are expected to use the snapshot rather than hammering the API.

### [Project Euclid](https://projecteuclid.org/)

`Freemium` · beginner 4/5 · journal hosting platform

Platform for independent and society publishers in mathematics and statistics, created by Cornell University Library in 2000 and now managed by Duke University Press: over 100 journals and book series and roughly 2.5 million pages, mixing fully open-access titles with subscription ones.

**Access.** Search or browse at projecteuclid.org and use the open-access marker/filter; open articles are direct PDF downloads with no account, and many subscription titles have free back-runs.

**Caveats.** A large part of the platform is subscription-only - 'Euclid Prime' alone is a 27-title paid bundle - so check the open-access icon before assuming access. Some journals hosted here are fully open access with no author charges; others sit behind a moving wall. No bulk download, and its search is weaker than zbMATH for literature discovery.

### [zbMATH Open](https://zbmath.org/)

`Free` · beginner 4/5 · abstracting and reviewing database

More than 4.8 million bibliographic records with reviews or abstracts covering the mathematical literature continuously since 1868 (through the integrated Jahrbuch data), written by a network of over 8,000 reviewers, plus author disambiguation, formula search, software links and integrated arXiv math preprints. Free of charge to everyone since the start of 2021.

**Access.** Web search at zbmath.org; REST API at https://api.zbmath.org/v1/ (accept the terms once; no paid key) and OAI-PMH harvesting at https://oai.zbmath.org for bulk metadata.

**Caveats.** This is the realistic free substitute for MathSciNet, which remains subscription-only; coverage and review depth are comparable but not identical, and some reviews are abstracts rather than signed reviews. Published jointly by FIZ Karlsruhe, the EMS and the Heidelberg Academy of Sciences. The site sits behind a bot-protection layer, so scripted access should use the API rather than the HTML.

### [Zotero](https://www.zotero.org/)

`Freemium, email` · beginner 5/5 · reference manager

Reference manager whose source code is released under the GNU AGPL v3: a browser connector captures metadata and PDFs from arXiv, zbMATH, journal and library pages, and the desktop app exports BibTeX/BibLaTeX for LaTeX and drives Word/LibreOffice citation plugins. Accounts include 300 MB of hosted storage.

**Access.** Install the desktop app (Windows/macOS/Linux) plus the browser connector; use it entirely offline, or create a free account to sync; 'File > Export Library > BibTeX' (or the Better BibTeX plugin) feeds a LaTeX bibliography directly.

**Caveats.** The software is free and open source, the hosted storage is not: beyond the 300 MB free quota the tiers are 2 GB at $20/year, 6 GB at $60/year and unlimited at $120/year. Running Zotero purely locally with no account avoids that entirely, at the cost of cross-device sync.

## Compute

### [Binder (mybinder.org)](https://mybinder.org/)

`Free` · beginner 3/5 · reproducible notebooks from a repository

Turns a public Git repository containing an environment specification into a live Jupyter session in the browser, free and with no account - the standard way to let readers of a paper run its notebooks (Normaliz, for instance, publishes a ready-made Binder link).

**Access.** Point mybinder.org at a repo URL, or add a badge to your README; the environment comes from environment.yml, requirements.txt or a Dockerfile in the repo.

**Caveats.** Public service run on donated capacity: sessions are ephemeral (nothing you write is saved), memory is capped around a couple of GB, the session dies after roughly 10 minutes idle, and first builds can take many minutes or fail when the federation is loaded. Never put private data in a Binder session.

### [CoCalc](https://cocalc.ai/)

`Free tier, email` · beginner 4/5 · browser computation environment

Collaborative browser environment with SageMath, Jupyter (Python, R, Julia, Octave), a full LaTeX editor with SageTeX, and a Linux terminal - the whole software stack is present in the free trial project, including time-travel history and real-time collaboration.

**Access.** Sign up with an email address and open a free trial project; pick a Sage image for the SageMath kernel, or use the LaTeX editor to compile papers.

**Caveats.** Trial limits confirmed at doc.cocalc.com/trial.html on 2026-08-28: 'You do not have direct Internet access' (no git clone, no pip install from PyPI - uploads from your own machine only), hardware 'enough to run a basic Jupyter notebook' but not serious computation, a small idle timeout and limited overall session duration. On the other hand 'trial projects do not expire at the moment', so occasional small computations genuinely are free; sustained work needs a paid licence or pay-as-you-go credits. Note the domain move to cocalc.ai.

### [Google Colab](https://colab.research.google.com/)

`Free tier, email` · beginner 5/5 · hosted Jupyter notebooks

Hosted Jupyter notebooks on Google VMs with notebooks stored in Google Drive. The FAQ states free-tier notebooks 'can run for at most 12 hours, depending on availability and your usage patterns', that GPU and TPU types 'available in Colab vary over time', and that priority, memory and longer runtimes are what the paid tiers buy.

**Access.** Sign in with a Google account and open a new notebook; root-level installs work, so '!pip install snappy python-flint sympy' and '!apt-get install -y pari-gp' give a working mathematics stack on a machine you do not own.

**Caveats.** Runtimes are pre-emptible and recycled when idle - anything not written back to Drive or a repo is lost. GPU/TPU allocation on the free tier is unpredictable and can be refused for hours. No SageMath kernel out of the box (installing Sage in a session is slow and fragile - use CoCalc or SageMathCell instead). Needs a Google account, and the terms make it unsuitable for confidential or embargoed data.

### [Lean 4 Web](https://live.lean-lang.org/)

`Free` · beginner 4/5 · proof assistant in the browser

Runs Lean 4 with mathlib preloaded in the browser, with the full interactive goal view, so you can check a proof or follow a tutorial without installing a toolchain.

**Access.** Open the page and type; sessions are shareable by URL and the site is the target of most 'try this' links in Lean tutorials.

**Caveats.** Shared public server: compilation is slower than a local install, sessions are not persistent, and you cannot add dependencies beyond what is preloaded. Fine for learning and small experiments, not for a formalisation project.

### [Magma Calculator](https://magma.maths.usyd.edu.au/calc/)

`Free tier` · beginner 3/5 · browser access to a closed-source CAS

Free browser interface to Magma, the system behind a large share of the number theory and algebraic geometry literature; it was running Magma V2.29-9 on 2026-08-28. The page states calculations are restricted to 60 seconds and input is limited to 50,000 bytes.

**Access.** Open the page, paste Magma code into the box, press Submit; output comes back in the browser. No account and no install.

**Caveats.** Magma itself is commercial and expensive; only this capped calculator is free. There is no state between submissions and no file persistence, so it suits re-running a short computation from a paper or checking a construction, not research runs. Anything longer than a minute has to move to a licensed Magma or to a free system (PARI/GP, SageMath, OSCAR).

### [NEOS Server](https://neos-server.org/neos/)

`Free, email` · beginner 4/5 · hosted optimization solvers

Free internet service hosted by the Wisconsin Institute for Discovery that runs your optimization model on someone else's machines: more than 60 solvers in more than a dozen categories (LP, MILP, nonlinear, mixed-integer nonlinear, semidefinite, complementarity, stochastic), including commercial codes such as CPLEX, Gurobi, Xpress, MOSEK, Knitro and BARON alongside open ones like SCIP, Cbc and Ipopt. Jobs are distributed with HTCondor at Wisconsin plus remote solvers at Arizona State, Klagenfurt and Minho.

**Access.** Upload a model through the web form in AMPL, GAMS, MPS, LP or the solver's own format and get results in the browser or by email; or submit programmatically over the XML-RPC API (Python client provided), or straight from AMPL/GAMS with the Kestrel client.

**Caveats.** Hard limits: 8 hours CPU for standard jobs (5 minutes on the short queues), 3 GB RAM, at most 4 threads per job, input files no larger than 16 MB, and solver output truncated at 100 MB. An email address must accompany each submission and users are asked not to queue more than about 10-15 jobs at once. The commercial solvers are usable through the service only - you get results, not a local licence - and everything runs on shared academic machines, so do not send models you need to keep confidential.

### [Overleaf](https://www.overleaf.com/)

`Freemium, email` · beginner 5/5 · collaborative LaTeX

Browser LaTeX editor with journal and arXiv-ready templates. The free plan gives unlimited projects, one collaborator per project, a basic compile timeout, and 5 AI uses per day.

**Access.** Sign up with an email address and start a project, or upload an existing .tex tree; git and Dropbox sync are paid features.

**Caveats.** The free compile timeout is the binding constraint: long documents, big TikZ pictures or heavy bibliographies can fail to compile until you pay (paid tiers advertise 24x the basic timeout) - a local TeX Live install has no such limit. The free plan also keeps only the previous 24 hours of document history and excludes track changes, Git/GitHub/Dropbox sync and advanced reference search. Many universities buy site licences, which unaffiliated researchers cannot use.

### [SageMathCell](https://sagecell.sagemath.org/)

`Free` · beginner 5/5 · one-shot Sage evaluation

A public server that evaluates a single SageMath (or Python, GAP, GP, Maxima, Singular, R, Octave) cell in the browser and returns output, plots and interacts, with a permalink for sharing.

**Access.** Open the page, paste code, press Evaluate; the cell can be embedded in any web page with a short script tag, which is how many free textbooks add live computation.

**Caveats.** Stateless and time-limited: no persistent files, no long computations, no installing packages. It is for demonstrations, quick checks and teaching, not for research runs.

## Publishing

### [Algebraic Combinatorics](https://alco.centre-mersenne.org/)

`Free, email` · beginner 4/5 · diamond OA journal

Journal owned by its editorial board (founded in 2018 after the editors of a commercial journal resigned), publishing work where algebra and combinatorics interact. Adheres to the Fair Open Access principles: no author charges, no reader charges; indexed in Web of Science, Scopus, MathSciNet, zbMATH and DOAJ (e-ISSN 2589-5486).

**Access.** Submit via the journal website on the Centre Mersenne platform; free PDFs of all issues; mirrored into Numdam after a year.

**Caveats.** One of the clearest working examples of a board that walked away from a paywalled publisher - useful precedent if you are arguing the case at your own institution.

### [Annales Henri Lebesgue](https://ahl.centre-mersenne.org/)

`Free, email` · beginner 4/5 · diamond OA generalist journal

Generalist mathematics journal, fully open access and free of author charges, published on the Centre Mersenne platform by a non-profit backed by French public institutions; publishing since 2018 (e-ISSN 2644-9463).

**Access.** Submit through the journal website; articles are free PDF/HTML immediately and are mirrored into Numdam after one year.

**Caveats.** Standards are those of a strong generalist journal, so expect a low acceptance rate and long refereeing times typical of mathematics.

### [Annals of Formalized Mathematics](https://afm.episciences.org/)

`Free, email` · beginner 3/5 · diamond OA journal, formalised mathematics

Journal founded in 2024, supported by MathOA and hosted on Episciences (eISSN 3117-4604), publishing original articles on formalised mathematics and mathematical applications of proof assistants; papers are typically accompanied by a code artifact. Single-blind peer review, no charges.

**Access.** Deposit the paper in an open archive (arXiv/HAL), then submit the identifier through Episciences together with the accompanying formalisation.

**Caveats.** Very young, so its indexing footprint is still small - check how your evaluation committee treats it before sending your only paper of the year. Natural venue for Lean/Rocq/Isabelle work that would otherwise land in a computer science conference.

### [Ars Inveniendi Analytica](https://ars-ojs-utexas.tdl.org/ars)

`Free, email` · beginner 3/5 · diamond OA journal, analysis

Peer-reviewed journal for mathematical analysis with volumes running from 2021 to 2026, hosted on the University of Texas Digital Library's OJS instance and describing itself as 'completely free for authors and readers'.

**Access.** All articles are free PDFs from the journal site; submit through the OJS system after creating a free account.

**Caveats.** Not listed in DOAJ as of 2026-08-28 and small in volume (a handful of long papers per year), so check how your evaluation committee treats it before sending your only paper of the year. Scope is nonlinear analysis, PDE and calculus of variations rather than analysis at large. The old ars-inveniendi-analytica.com address now 301-redirects to the UT Digital Library host - update stored links and bibliographies.

### [Combinatorial Theory](https://escholarship.org/uc/combinatorial_theory)

`Free, email` · beginner 4/5 · diamond OA journal, combinatorics

Diamond open-access journal (eISSN 2766-1334) open access since 2021, founded after the editorial board of Journal of Combinatorial Theory Series A resigned from its commercial publisher; published on the University of California's eScholarship platform under CC BY with no article processing charges (confirmed in DOAJ on 2026-08-28).

**Access.** Read and download every article from eScholarship with no account; submissions go through the journal's editorial system, linked from the eScholarship journal page.

**Caveats.** The journal's own domain combinatorialtheory.org did not serve content to standard clients on 2026-08-28, so navigate via eScholarship. Like the Algebraic Combinatorics case, this is a usable precedent when arguing for a board to leave a paywalled publisher.

### [Discrete Analysis](https://discreteanalysisjournal.com/)

`Free, email` · beginner 4/5 · diamond OA arXiv overlay journal

Arxiv overlay journal for additive combinatorics, harmonic analysis, ergodic theory and related areas, founded in 2016 by Timothy Gowers. No charges to authors or readers; articles are CC BY and are hosted on arXiv, with the journal publishing peer review plus an editorial 'summary' of each accepted paper.

**Access.** Post the paper to arXiv, then submit its arXiv identifier through the journal's website; accepted papers stay on arXiv with a journal-issued DOI.

**Caveats.** Confirmed by DOAJ as having no article processing charges. Narrow scope and a high acceptance bar; running costs are covered by Scholastica fees paid by the editorial board, not by authors.

### [Documenta Mathematica](https://ems.press/journals/dm)

`Free, email` · beginner 4/5 · diamond OA generalist journal

Refereed generalist mathematics journal, open access since 1996 with no article processing charges and CC BY licensing (as recorded in DOAJ); now published through EMS Press. Also publishes the Extra Volumes, including the ICM proceedings volumes it has hosted.

**Access.** Submit through the journal's editorial contacts listed on the EMS Press page; all volumes are free PDF downloads.

**Caveats.** Proof that a diamond journal can be old, general and highly selective; acceptance is hard. The historical bielefeld.de address now redirects into the EMS Press platform, so update old bookmarks and bibliography URLs.

### [Epijournal de Geometrie Algebrique (EPIGA)](https://epiga.episciences.org/)

`Free, email` · beginner 4/5 · diamond OA overlay journal

Peer-reviewed overlay journal founded in 2016 covering algebraic geometry broadly, including complex and arithmetic geometry and algebraic groups/representations; runs on the public Episciences platform, with no charges to authors or readers. Articles appear in English or French with an English abstract.

**Access.** Deposit the preprint on arXiv or HAL, then submit the identifier via Episciences; refereeing is the classical editorial process.

**Caveats.** Submission requires an Episciences account and a preprint already deposited in an open archive - the deposit is a prerequisite, not an afterthought. Site navigation defaults to French.

### [Episciences](https://www.episciences.org/)

`Free, email` · beginner 3/5 · overlay-journal platform

Public overlay-journal platform developed by the CCSD (CNRS/Inria/INRAE) that lets a community run a peer-reviewed journal on top of preprints deposited in arXiv or HAL, with no cost to authors or readers. Hosts the mathematics journals EPIGA and Annals of Formalized Mathematics among others.

**Access.** As an author, deposit in arXiv/HAL and submit the identifier to the chosen journal; as an editorial board, apply to have a journal hosted - the platform provides submission, review workflow, DOIs and long-term hosting.

**Caveats.** This is the realistic route if your community wants to start a journal without a publisher or a budget. It is publicly funded infrastructure, not a service you control; editorial policies must satisfy the platform's requirements, and the interface is French-first.

### [Free Journal Network](https://freejournals.org/)

`Free` · beginner 4/5 · directory of diamond OA journals

Non-profit membership organisation (registered in Massachusetts) promoting Fair Open Access - journals controlled by the scholarly community with no financial barrier to readers or authors. It maintains acceptance criteria, lists member journals, shares best practice and provides small grants to member journals.

**Access.** Browse the member-journal list from the site's Journals menu to find no-APC venues in your area; journals apply for membership against the published criteria; there is no fee for membership.

**Caveats.** Website upkeep is patchy - some navigation links 404 and the blog has not been updated since 2022 - but the member list is the fastest way to find legitimate diamond journals in mathematics and neighbouring fields. Membership is not a quality ranking; check each journal's editorial board yourself.

### [New York Journal of Mathematics](https://nyjm.albany.edu/)

`Free, email` · beginner 4/5 · diamond OA generalist journal

Generalist mathematics journal established in 1993 as the first electronic general mathematics journal; free to readers and, in its own words, 'completely free to the author'. DOAJ records no APCs and eISSN 1076-9803; since 2022 papers carry CC BY 4.0 with authors retaining copyright, and refereeing is single-blind. Hosted by the University at Albany, with mirror sites and an NYJM Monographs series.

**Access.** Every volume is a free download from the journal site or its mirrors; submission instructions are on the 'For Authors' page.

**Caveats.** Run on university infrastructure by a small volunteer staff: the site is plain HTML and editorial handling is by direct correspondence rather than a modern submission portal, which some authors find off-putting. Standards are those of a solid generalist journal - a paper must be 'new, correct, significant, and interesting to a broad audience' - and visibility depends heavily on also posting to arXiv.

### [SIGMA (Symmetry, Integrability and Geometry: Methods and Applications)](https://www.emis.de/journals/SIGMA/)

`Free, email` · beginner 4/5 · diamond OA journal, mathematical physics

Refereed electronic journal (ISSN 1815-0659) for integrable systems, symmetry methods, special functions, representation theory and geometry in mathematical physics. Free for authors and free for readers, operating as an arXiv overlay and a member of the Free Journal Network.

**Access.** Post to arXiv and submit through the journal site; published papers are free PDFs and remain on arXiv; special issues are a regular feature.

**Caveats.** The canonical site is hosted on the EMIS mirror network, which looks dated but is the real thing. Scope is genuinely at the mathematics/physics boundary - a pure algebraic geometry paper is out of scope.

### [The Electronic Journal of Combinatorics](https://www.combinatorics.org/)

`Free, email` · beginner 5/5 · diamond OA journal

Fully refereed electronic journal for all branches of discrete mathematics, founded in 1994 by Herbert Wilf and Neil Calkin; completely free for both authors and readers, authors retain copyright, all papers get DOIs and are indexed in zbMATH, MathSciNet and Web of Science. Currently at Volume 33 (2026).

**Access.** Submit through the journal's OJS site; PDFs of every issue since 1994 are free to download; the journal also publishes long-lived Dynamic Surveys.

**Caveats.** A founding member of the Free Journal Network. Volunteer-run, so refereeing times vary a lot between editors.

### [Theory and Applications of Categories (TAC)](https://tac.mta.ca/tac/)

`Free, email` · beginner 3/5 · diamond OA journal, category theory

Refereed electronic journal for category theory and its applications, publishing since Volume 1 in 1995 and at Volume 45 in 2026. The journal states plainly that 'The journal is free'; authors retain copyright to their articles and full texts are free PDFs. It also runs the TAC Reprints series, which republishes classic out-of-print categorical texts.

**Access.** Submission requirements at tac.mta.ca/tac/authinfo.html; all volumes download free from the home site at Mount Allison University, with mirrors including EMIS and Library and Archives Canada.

**Caveats.** Use https://tac.mta.ca/ - the www. host presents a certificate that does not cover that name, so www.tac.mta.ca fails TLS validation. Mirrors can lag the home site, which the journal itself warns about. Scope is strictly categorical, and it is volunteer-run, so refereeing times vary.

### [Zenodo](https://zenodo.org/)

`Free (registration), email` · beginner 4/5 · data and code repository with DOIs

CERN-operated general-purpose repository that mints a DOI for datasets, code snapshots, notes and slides. Each record accepts up to 100 files and 50 GB (50,000,000,000 bytes) by default, with up to 200 GB available on request.

**Access.** Upload through the web interface, or automate via the REST API with a personal access token; GitHub integration archives a release and issues a DOI automatically - the standard way to make the computations behind a paper citable.

**Caveats.** Records are permanent: files can be replaced only by publishing a new version, and DOIs cannot be withdrawn. Zenodo does no peer review or curation, so a Zenodo DOI carries no quality signal by itself.

## Funding

### [American Institute of Mathematics: SQuaREs, workshops and problem lists](https://aimath.org/research/squares/)

`Free, application` · beginner 2/5 · funded small-group research

AIM's SQuaREs programme supports a group of four to six mathematicians to spend a week at AIM's Pasadena facility working on a specific problem, with AIM providing facilities and financial support and groups eligible for up to three meetings over three consecutive years. AIM also runs topic workshops and publishes the resulting problem lists.

**Access.** Proposals are short (typically two or three pages: participants plus a description of the project) and are submitted through the SQuaRE proposal form; the annual deadline is 1 November.

**Caveats.** At least half the participants must be from North America, with at least one from the US - a real limit for internationally based groups. AIM is NSF-funded, so programme continuity depends on US federal funding decisions.

### [CIMPA](https://www.cimpa.info/en)

`Free, application` · beginner 2/5 · research schools and fellowships

The International Centre for Pure and Applied Mathematics has for almost 50 years funded and organised research schools in developing countries, plus CIMPA fellowships, CIMPA-ICTP Research in Pairs, and (announced August 2026) a mentoring programme pairing researchers with experienced mathematicians.

**Access.** Two routes: apply as a participant to an announced school (travel and local costs often covered), or propose a school as a local organiser roughly 18 months ahead through the 'I organise' pages.

**Caveats.** Schools are geographically targeted - participation calls usually prioritise applicants from the region hosting the school. Proposing a school requires a committed local host institution.

### [ICTP mathematics programmes (Trieste)](https://www.ictp.it/)

`Free, application` · beginner 2/5 · fellowships and funded visits

The Abdus Salam International Centre for Theoretical Physics runs mathematics-specific opportunities aimed at researchers from developing countries: the one-year Postgraduate Diploma Programme (a bridge to a PhD), PhD and sandwich programmes, postdoctoral positions, and the Associates Programme, which funds repeated research visits to Trieste over several years.

**Access.** Apply online per programme through the ICTP opportunities pages; ICTP also runs schools and workshops throughout the year with travel and living support for participants from developing countries.

**Caveats.** Competitive and calendar-driven - Diploma and Associates calls have fixed annual deadlines. Most schemes require nationality of, or a position in, a developing country; the Associates scheme additionally requires an academic position to return to.

### [IMU Commission for Developing Countries (CDC) grants](https://www.mathunion.org/cdc)

`Free, application` · beginner 2/5 · grants for developing-country mathematicians

The International Mathematical Union's grant programmes for mathematicians in developing countries, as listed on the CDC pages in August 2026: the Abel Visiting Scholar Program for Graduate Students (month-long research visits abroad; deadline 15 September 2026), the IMU-Simons Research Fellowship Program (collaborative research visits, funded by the Simons Foundation), the IMU Breakout Graduate Fellowship Program, the Conference Support Program (partial support for conferences in developing countries, including participant travel), and the Volunteer Lecturer Program, which sends lecturers to run intensive courses of 10 days to several weeks at universities that request them.

**Access.** Application forms and deadlines per programme on the CDC pages; enquiries to cdc.grants@mathunion.org; most programmes require a host institution's invitation letter.

**Caveats.** Eligibility is tied to the IMU's own published list of developing countries and usually to holding a position (or a PhD place) at an institution there - fully unaffiliated researchers generally do not qualify. Award sizes are modest travel/subsistence grants, not salaries.

### [Mathematisches Forschungsinstitut Oberwolfach](https://www.mfo.de/scientific-program)

`Free, application` · beginner 2/5 · funded research stays in Germany

Oberwolfach runs six programmes: Workshops, Mini-Workshops, Oberwolfach Seminars, Arbeitsgemeinschaft, Oberwolfach Research Fellows (small groups of 2-4 who apply to work together at the institute for two to three weeks) and Oberwolfach Leibniz Fellows for early-career researchers. Board and lodging at the institute are provided.

**Access.** Check which programmes you can actually enter: the weekly Workshops (45-48 participants) are by personal invitation from the Director on the organisers' recommendation, and Mini-Workshops are decided about six months ahead from proposals. The self-application routes are the Oberwolfach Seminars (applications to the Director; roughly 24 PhD students and postdocs per seminar), the Arbeitsgemeinschaft (application to the organisers, who select participants to give the talks), and the Research Fellows / Leibniz Fellows schemes, where researchers apply directly. All participants in the scientific programme receive full board and lodging, and several programmes have grants covering travel costs.

**Caveats.** Stays are funded in kind (accommodation and meals); travel is only partly covered, and the institute has publicly flagged uncertainty around the US NSF grant that supports some participation costs. Visa processing for Germany has been slow, so apply for appointments immediately after an invitation.

## Learning

### [AIM Open Textbook Initiative](https://aimath.org/textbooks/)

`Free` · beginner 5/5 · vetted free textbooks

The American Institute of Mathematics maintains an editorial board that evaluates open-source and open-access mathematics textbooks against published criteria and publishes a list of Approved Textbooks, organised by course from pre-calculus to upper-division analysis and algebra, each with a description and how to obtain it.

**Access.** Browse the Approved Textbooks list and download from the linked source; the Evaluation Criteria and Guide for Authors pages are useful if you plan to write one.

**Caveats.** Scope is undergraduate and early graduate teaching material - it will not cover a research seminar. Approval means suitability for a traditional course, not that the book is the best in its subject.

### [Allen Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html)

`Free` · beginner 4/5 · free graduate textbook

The standard first-year graduate algebraic topology text (Cambridge University Press, 2002), roughly 550 pages, available as a free PDF by arrangement with the publisher and kept up to date with corrections. The author's other books and notes (3-manifolds, vector bundles and K-theory, spectral sequences) are on the same site.

**Access.** Direct PDF download - whole book, or individual chapters plus an expanded appendix; a cumulative errata list is maintained alongside.

**Caveats.** Free to download and read under the author's copyright notice, not an open licence - do not redistribute or remix. Two versions are posted: one with a clickable table of contents that lags the corrections, one plain version that is current.

### [Carmin.tv](https://www.carmin.tv/en)

`Free` · beginner 4/5 · mathematics lecture video archive

Video platform of the French mathematics institutes - founded by CIMPA, CIRM, IHES and IHP with Institut Fourier, LMR and SMF as partners - holding roughly 9,922 videos totalling about 9,037 hours from 5,565 speakers: conference talks, mini-courses and research-school lectures.

**Access.** Browse or search by institution, event, speaker or topic and stream in the browser; watching needs no account (registration only adds bookmarks, a watch-later list and comments).

**Caveats.** Coverage mirrors what those institutes recorded, so it is strong on European programmes and thin elsewhere, and talks are a mixture of French and English. Streaming assumes reasonable bandwidth; reuse terms differ per video, so check the individual page before redistributing.

### [Encyclopedia of Mathematics](https://encyclopediaofmath.org/)

`Free` · beginner 4/5 · reference encyclopedia

Wiki edition of the Springer/Kluwer Encyclopaedia of Mathematics: more than 8,000 entries illuminating close to 50,000 notions, now hosted by EMS Press with an editorial board appointed by the European Mathematical Society overseeing changes.

**Access.** Read and search freely at encyclopediaofmath.org (MediaWiki with MathJax); registered contributors can correct or extend articles under editorial oversight.

**Caveats.** Licensing is split: original Springer articles remain under Springer copyright, while new articles and edits made on the site are CC BY-SA - check an article's history before reusing text. Many entries are 1990s translations, excellent for definitions and orientation but dated on anything post-2000. Availability is patchy: repeated requests to the site returned HTTP 502 on 2026-08-28, so keep a local copy of anything you rely on.

### [J.S. Milne's course notes and books](https://www.jmilne.org/math/)

`Free` · beginner 4/5 · free course notes, algebra and number theory

Complete free course notes and books on group theory, fields and Galois theory, algebraic geometry, algebraic number theory, modular functions and modular forms, elliptic curves, abelian varieties, etale cohomology, class field theory, complex multiplication and algebraic groups, maintained since 1996 and still revised (Tannakian Categories updated July 2026).

**Access.** Direct PDF download per title; errata and addenda are posted per book.

**Caveats.** Terse and demanding in the way research-level notes are; some titles also exist as inexpensive paperbacks. Not CC-licensed: the author asks that you link to the top level of the site rather than repost his files elsewhere, and that you cite the published versions where they exist. Revision dates differ sharply per item (Tannakian Categories July 2026, the Algebraic Geometry notes November 2024), so record the version you actually used.

### [Keith Conrad's expository papers ('blurbs')](https://kconrad.math.uconn.edu/blurbs/)

`Free` · beginner 5/5 · short expository notes

A large collection of short, self-contained expository notes covering proof technique, group theory, linear and multilinear algebra, Galois theory, algebraic number theory, p-adic analysis and more - the notes practising number theorists routinely send to students when a standard text is too heavy.

**Access.** Direct PDF download, organised by topic; each note is typically 5-30 pages and readable on its own.

**Caveats.** Files are revised in place with no version marker, so a link may point at slightly different text later; save a copy if you cite a specific page.

### [Kerodon](https://kerodon.net/)

`Free` · beginner 2/5 · open reference, higher category theory

Jacob Lurie's online, Stacks-style reference for homotopy-coherent mathematics: foundations of infinity-categories (the language, examples, Kan complexes, homotopy theory of infinity-categories, fibrations) and higher category theory (adjoints, limits and colimits, the Yoneda embedding, large infinity-categories, exactness and animation).

**Access.** Read online at kerodon.net and navigate by permanent tag (the Gerby interface, the same software the Stacks Project uses); every tag has a stable URL of the form kerodon.net/tag/XXXX and is the correct way to cite a result. Comments are open on every section. Currently 10 chapters in two parts (Foundations; Higher Category Theory).

**Caveats.** Written for people who already know ordinary category theory and algebraic topology; it is still growing, so some referenced material is not yet written. Cite by tag.

### [MIT OpenCourseWare - Mathematics](https://ocw.mit.edu/courses/?d=Mathematics)

`Free` · beginner 5/5 · full course materials

Complete materials for MIT's 18.xxx mathematics courses - lecture notes, problem sets with solutions, exams, and full video lectures for many courses (linear algebra, analysis, algebraic topology, probability, algorithms-adjacent topics), published under CC BY-NC-SA.

**Access.** Browse or search by course number/topic and download materials directly; videos are also mirrored on the MIT OpenCourseWare YouTube channel for low-bandwidth or offline use.

**Caveats.** The NC clause blocks commercial reuse. Coverage is uneven: some courses have full video, others only a syllabus and problem sets, and some pages date from a decade or more ago.

### [nLab](https://ncatlab.org/nlab/show/HomePage)

`Free` · beginner 3/5 · research wiki, category theory and higher structures

A collaboratively written research wiki covering category theory, higher category theory, homotopy theory, topos theory, foundations and mathematical physics from a structural perspective, with dense cross-linking and literature pointers on almost every page.

**Access.** Read and search freely; editing is open to anyone who registers, and discussion happens on the associated nForum.

**Caveats.** Written by and for specialists: pages assume the ambient viewpoint and are not always self-contained or uniformly reliable, since anyone can edit. Excellent for orientation and references, not a citable source of proofs.

### [The Stacks Project](https://stacks.math.columbia.edu/)

`Free` · beginner 3/5 · open textbook and reference, algebraic geometry

Open-source, collaboratively maintained textbook and reference on algebraic geometry and algebraic stacks: 7,654 pages, 767,328 lines of LaTeX, 21,446 stable tags and 116 chapters as of August 2026, with a comment system attached to every result.

**Access.** Read online by tag, download the full PDF, or clone the LaTeX source from GitHub; each result has a permanent four-character tag (e.g. Tag 01WC) that is the standard way to cite it in papers.

**Caveats.** It is a reference, not a course: it starts from set theory and proves everything, which makes it exhaustive but unsuitable as a first pass through the subject. Tags are stable, but chapter and section numbers are not - always cite tags.

### [Wolfram MathWorld](https://mathworld.wolfram.com/)

`Free` · beginner 5/5 · online mathematics encyclopaedia

Free online mathematics encyclopaedia with 14,353 entries, assembled over more than 25 years by Eric W. Weisstein with thousands of contributors; strongest on formulas, special functions, named constants, integer sequences and the cross-references between them.

**Access.** Web interface, free to read with no account; each entry has a stable URL and a citation block, and many carry Wolfram Language input for the objects described.

**Caveats.** Copyright Wolfram Research (c) 1999-2026 under their terms of use, not an open licence: free to read, not free to republish or mine wholesale. Not peer reviewed - it has a long-known tail of errors and idiosyncratic conventions, so verify anything load-bearing against DLMF or a textbook. Many entries route you toward Mathematica or Wolfram Alpha, which are not free.

## Community

### [AIM problem lists](https://aimath.org/problemlists/)

`Free` · beginner 3/5 · curated open problems

Curated lists of open problems produced by AIM workshops across algebraic geometry, number theory, analysis, combinatorics, topology and more - each list records what a room of specialists considered the tractable open questions in the area at the time.

**Access.** Browse the index by field and open each list as a PDF or as an interactive AimPL page, where problems can be discussed and updated.

**Caveats.** The interactive lists live on the separate aimpl.org host, whose TLS certificate has expired (checked 2026-08-28: the connection fails with 'certificate has expired'), so browsers interpose a warning and scripted fetches fail outright - use the PDF versions from the aimath.org index instead. Lists are dated snapshots: check whether a problem has since been solved before investing in it.

### [Lean Zulip chat](https://leanprover.zulipchat.com/)

`Free, email` · beginner 3/5 · working research chat, formalisation

The main gathering place of the Lean and mathlib community, where formalisation projects are planned, reviewed and debugged in public, and where mathematicians new to Lean can get concrete help in hours. Archives are publicly readable.

**Access.** Join free with an email or GitHub account; the '#new members' stream is the standard place to introduce yourself and ask beginner questions, with topic streams for maths areas and mathlib review.

**Caveats.** This is a working venue, not a help desk: search the archive first, post code that actually compiles, and expect answers in the language of the library. Volume is high enough that threads move fast.

### [Mathematics Stack Exchange](https://math.stackexchange.com/)

`Free, email` · beginner 5/5 · general mathematics Q&A

The high-volume companion to MathOverflow, covering everything from undergraduate exercises to early graduate material, with a very large archive of answered questions about standard techniques, definitions and worked examples.

**Access.** Search the archive without an account (most questions are already answered); register with an email address to ask or answer; LaTeX renders in posts via MathJax.

**Caveats.** Answer quality varies far more than on MathOverflow, and the volume means good questions can be buried. Research-level questions belong on MathOverflow instead.

### [MathOverflow](https://mathoverflow.net/)

`Free, email` · beginner 4/5 · research-level Q&A

Question-and-answer site for research-level mathematics, holding 168,133 questions on 2026-08-28, where working mathematicians (including many well-known ones) routinely answer questions about the state of the literature, counterexamples and technical obstructions.

**Access.** Read without an account; register with an email or a linked account to ask, answer, comment or vote; reputation unlocks further privileges.

**Caveats.** Strictly for research-level questions - homework, textbook exercises and 'please explain this concept' get closed fast and pushed to Math StackExchange. Read a few closed questions before posting your first one. Content is CC BY-SA; the site is run by Stack Overflow's network.

### [researchseminars.org](https://researchseminars.org/)

`Free` · beginner 5/5 · online seminar and conference listings

Community-maintained listing of online and hybrid research seminars, series and conferences, built by people from the LMFDB project and open source at github.com/roed314/seminars. On 2026-08-28 it carried 285 series tagged Mathematics (against 85 physics and 65 computer science), each with time-zone-adjusted schedules, speakers, abstracts and joining details.

**Access.** Browse or filter by topic, language, institution and date without an account; organisers create a free account to list and manage a series.

**Caveats.** Running since April 2020 and still labelled beta. Listings are only as current as the organisers keep them - series go stale after a term, coverage is dense in some communities (number theory, category theory, combinatorics) and empty in others, and some joining links are given out on request rather than published. The single best route into research talks for someone with no seminar culture locally.

*Also listed under: physics.*
