# Biology & life sciences

Part of [research-vault](../README.md). 60 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (20) · [Software](#software) (13) · [Literature](#literature) (4) · [Compute](#compute) (3) · [Publishing](#publishing) (5) · [Funding](#funding) (5) · [Learning](#learning) (6) · [Community](#community) (4)

## Data

### [Alliance of Genome Resources](https://www.alliancegenome.org/)

`Free` · beginner 4/5 · model organism databases

Unified portal and data warehouse across the major model organism databases - WormBase, FlyBase, SGD (yeast), ZFIN (zebrafish), MGI (mouse), RGD (rat), PomBase and Xenbase - plus human, giving cross-species orthology, expression, disease association, allele and phenotype data in one schema.

**Access.** Cross-species web search at alliancegenome.org; REST API at https://www.alliancegenome.org/api/ (e.g. /api/gene/HGNC:5). Bulk TSV/JSON files on the Downloads page. Member databases keep their own APIs - for example `curl 'https://api.flybase.org/api/v1.0/gene/summaries/auto/FBgn0000490'` returns FlyBase FB2026_02 data.

**Caveats.** The Alliance harmonises a subset of what each member database curates; for deep organism-specific work (WormBase phenotype ontologies, FlyBase stock records, SGD literature curation) go to the member site directly. Gene nomenclature conventions differ across organisms, so orthology mapping needs care.

### [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/)

`Free` · beginner 4/5 · predicted protein structures

241,070,489 AlphaFold2-predicted protein structures (v6 release dated 2025-09-15, aligned to UniProt 2025_03), including 40,054 isoform sequences and, new in this release, the input multiple sequence alignments in A3M format plus per-entry MSA depths.

**Access.** Per-entry files by UniProt accession: `curl -O https://alphafold.ebi.ac.uk/files/AF-P00520-F1-model_v4.cif`. Bulk: per-proteome tar files and the full 110 GB sequences.fasta at https://ftp.ebi.ac.uk/pub/databases/alphafold/; the complete dataset is also a Google Cloud public dataset. Current API documented at https://alphafold.ebi.ac.uk/api-docs.

**Caveats.** CC BY 4.0. The legacy API is retiring in June 2026 - check that any inherited script uses the new endpoints. These are predictions, not measurements: read per-residue pLDDT and PAE before trusting a region, and note that low-pLDDT stretches often indicate genuine disorder. No complexes, no ligands, no alternative conformations; use ColabFold for those.

### [BOLD (Barcode of Life Data System)](https://www.boldsystems.org/)

`Free` · beginner 3/5 · DNA barcode reference library

Reference library of DNA barcodes (chiefly COI for animals, rbcL/matK for plants, ITS for fungi) linked to vouchered specimens: over 20.7 million public records representing 1.6 million species, organised into Barcode Index Numbers (BINs) that approximate species clusters.

**Access.** Data Portal search and versioned, citable Data Packages at boldsystems.org; the Barcode ID Engine identifies an unknown sequence from a pasted FASTA in the browser. Public API at https://v4.boldsystems.org/index.php/API_Public/ for combined specimen+sequence records; R client `BOLDconnectR`. A free Workbench account is needed to upload and manage your own project data.

**Caveats.** BOLD v5 restructured the site and APIs; v4 remains reachable at v4.boldsystems.org and older scripts often still target it. A large share of total records are not public (awaiting validation or release). Taxonomic labels are only as good as the original specimen identification - BINs, not names, are the more stable unit.

### [CZ CELLxGENE Discover](https://cellxgene.cziscience.com/)

`Free` · beginner 4/5 · single-cell transcriptomics

Standardised, ontology-annotated single-cell RNA-seq corpus: 388 public collections spanning 2,216 datasets as of August 2026, plus the Census API for querying arbitrary slices of the whole corpus and a browser-based Explorer for interactive visualisation with no local install.

**Access.** `pip install cellxgene-census` then `import cellxgene_census; census = cellxgene_census.open_soma()` (R: `cellxgene.census`) to pull a filtered AnnData/Seurat object directly. Per-dataset .h5ad and .rds files download from each collection page. REST curation API at https://api.cellxgene.cziscience.com/curation/v1/collections.

**Caveats.** Census slices are memory-hungry - filter by tissue, assay and cell type before materialising, or a broad query will exhaust a 16 GB laptop. Datasets are reprocessed to a common schema, so counts and metadata may differ from the original publication's matrices. The Human Cell Atlas Data Portal (https://data.humancellatlas.org, 532 projects and 70.9M cells) holds the raw-data counterpart.

### [eBird and the Macaulay Library](https://science.ebird.org/en/use-ebird-data)

`Free (registration), application` · beginner 2/5 · bird occurrence and media archive

The largest biodiversity citizen-science dataset in the world: complete checklists with effort covariates (duration, distance, observer count) from every country, released as the eBird Basic Dataset (EBD) on a monthly cycle, plus the Macaulay Library archive of bird photos, audio and video linked to those checklists.

**Access.** Create a free eBird account, then submit a data request for the EBD; on approval you download a large tab-delimited file and filter it with the R package `auk` (`install.packages('auk')`, which wraps AWK for out-of-memory filtering). For live queries of recent sightings, the eBird API 2.0 uses a free API key. Modelled abundance surfaces come via the `ebirdst` package, which needs its own access key.

**Caveats.** The EBD is a single multi-gigabyte file that will not open in a spreadsheet - `auk` filtering before import is effectively mandatory. Data requests are reviewed and must state a research or education purpose; approval is routine but not instant, and terms restrict commercial redistribution. Sampling is unstructured, so effort covariates and the sampling-event file are needed for any occupancy or abundance modelling.

### [Ensembl](https://www.ensembl.org/)

`Free` · beginner 3/5 · genome annotation and comparative genomics

Release 116 (August 2026) provides annotated genomes, gene models, variation, regulation and comparative alignments for 356 vertebrate species through the main site, with Ensembl Genomes covering bacteria, protists, fungi, plants and metazoa separately.

**Access.** REST: `curl 'https://rest.ensembl.org/lookup/symbol/homo_sapiens/BRCA2?content-type=application/json'`. In R: `BiocManager::install('biomaRt')` then `useEnsembl(biomart='genes', dataset='hsapiens_gene_ensembl')`. Bulk GTF/FASTA at https://ftp.ensembl.org/pub/. The Variant Effect Predictor (VEP) runs online, as a Perl CLI, or offline from cache files.

**Caveats.** Apache 2.0 code, no restrictions on data. REST is rate-limited with retry headers - use the FTP dumps or the offline VEP cache for anything batch. Gene IDs change between releases, so pin the release number in methods; archive sites (e.g. jul2023.archive.ensembl.org) keep old versions queryable.

### [European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena/browser/home)

`Free` · beginner 4/5 · nucleotide sequence and read archive

EMBL-EBI's node of the International Nucleotide Sequence Database Collaboration, holding 44,308,969 raw read runs, 5,895,330 genome assemblies, 316,220,701 nucleotide sequences and 59,345,791 samples as of 27 August 2026. Data are synchronised daily with NCBI and DDBJ, so the same records are reachable from either side.

**Access.** Portal API returns TSV/JSON without a key: `curl 'https://www.ebi.ac.uk/ena/portal/api/search?result=read_run&query=tax_eq(9606)&fields=run_accession,fastq_ftp&format=tsv'`. FASTQ files are served directly over FTP/HTTPS, which is often faster and simpler than SRA toolkit conversion. Browser at ena/browser for interactive search.

**Caveats.** ENA serves submitter-supplied FASTQ, which may differ subtly from NCBI's regenerated files. Submitting data requires a free Webin account. For assembled metagenomes and MAG catalogues, the sibling MGnify resource (https://www.ebi.ac.uk/metagenomics) reuses the same accessions and API style.

### [GBIF (Global Biodiversity Information Facility)](https://www.gbif.org/)

`Free, email` · beginner 4/5 · biodiversity occurrence records

3,929,851,607 species occurrence records from 123,816 datasets as of August 2026, aggregating museum specimens, citizen-science observations, survey data and eDNA-derived records under a single taxonomic backbone. Licence split across records is roughly 2.79 billion CC BY 4.0, 662 million CC BY-NC 4.0 and 474 million CC0.

**Access.** `pip install pygbif` (`from pygbif import occurrences; occurrences.search(scientificName='Panthera onca')`) or R `install.packages('rgbif')` then `occ_download(...)`. Open REST API at https://api.gbif.org/v1/occurrence/search - no key needed for search. Large downloads are queued asynchronously, require a free account, and each gets a citable DOI.

**Caveats.** Search and small API pulls are anonymous; DOI-minted bulk downloads need a free account. Records carry heavy sampling bias (Europe, North America and birds are massively over-represented) and coordinate quality varies - filter on hasCoordinate, hasGeospatialIssue and coordinateUncertaintyInMeters. The CC BY-NC fraction cannot be used in commercial products.

### [gnomAD (Genome Aggregation Database)](https://gnomad.broadinstitute.org/)

`Free` · beginner 4/5 · human population genetic variation

Aggregated allele frequencies from harmonised human exomes and genomes; the browser's current dataset family is gnomAD v4, giving per-variant frequencies by genetic ancestry group, per-gene constraint metrics (pLI, LOEUF, missense Z), and separate structural-variant and copy-number releases.

**Access.** Browser search by gene, region, variant or rsID. Public GraphQL API at https://gnomad.broadinstitute.org/api (POST a query; no key). Bulk VCFs and Hail Tables are hosted as open cloud datasets on Google Cloud Storage, AWS and Azure - exact bucket paths are on the Downloads page.

**Caveats.** Free with no restrictions on use, but the full genome VCFs run to terabytes; per-gene or per-region slices via the browser or API are the realistic route on a laptop. Frequencies are summary statistics only - individual genotypes are not released. For open genotypes and actual sequence data, use IGSR/1000 Genomes (https://www.internationalgenome.org/), which is fully open including CRAMs.

### [Human Protein Atlas](https://www.proteinatlas.org/)

`Free` · beginner 5/5 · protein expression and localisation atlas

Open atlas of human protein expression across nine sections (Tissue, Brain, Single Cell, Subcellular, Cancer, Blood, Cell Line, Structure, Interaction), with antibody-based tissue profiling for 15,312 genes, subcellular localisation for 13,603 genes, RNA-seq across 51 tissue types, and millions of immunohistochemistry images.

**Access.** Web interface at proteinatlas.org - searching a gene symbol goes straight to the summary page. Bulk TSV/XML/JSON downloads at https://www.proteinatlas.org/about/download, including normal-tissue, pathology, subcellular-location and single-cell expression tables. Individual entries are also available as XML, e.g. proteinatlas.org/ENSG00000134057.xml.

**Caveats.** CC BY-SA 3.0 for images and data - the share-alike clause matters if you redistribute. Antibody-based data carry a validation score; unvalidated or 'uncertain' antibody results are common and should not be treated as definitive evidence of localisation. Human only.

### [iNaturalist](https://www.inaturalist.org/)

`Free` · beginner 5/5 · citizen-science species observations

381,040,626 observations as of August 2026, of which 215,599,402 carry Research Grade status (community-verified identification with date and coordinates). Each observation bundles photos or audio, location, timestamp and a full identification history.

**Access.** Open REST API at https://api.inaturalist.org/v1/observations (no key for read access), R package `rinat`, Python `pyinaturalist`. Research Grade records with open licences flow into GBIF as the iNaturalist Research-grade Observations dataset. Monthly open-data exports (metadata plus photo URLs) are hosted in an open AWS S3 bucket under the AWS Open Data programme.

**Caveats.** Licences are per-observation and per-photo, chosen by the observer: CC0, CC BY and CC BY-NC are all common, and a photo frequently carries a different licence from its observation record. Locations of threatened taxa are automatically obscured to a coarse grid cell. Identification accuracy depends on the community - filter on Research Grade and check identifier counts for anything consequential.

### [InterPro](https://www.ebi.ac.uk/interpro/)

`Free` · beginner 3/5 · protein families, domains and functional sites

Integrates member databases into 54,190 InterPro entries, including the 30,134 Pfam families that InterPro now hosts directly. Provides domain architectures, GO term mappings and precomputed matches for all UniProtKB sequences.

**Access.** Web search plus a paginated JSON API with no key: `curl 'https://www.ebi.ac.uk/interpro/api/entry/pfam/?page_size=20'`. To annotate your own sequences, submit to InterProScan via the EBI REST service, or install InterProScan 5 locally (Linux, Java; the full data package is tens of gigabytes).

**Caveats.** CC0 for InterPro entries; member databases carry their own terms. Local InterProScan needs substantial disk and RAM - for a handful of sequences the EBI web service is the pragmatic route. Pfam's standalone website was retired and redirects here, so old bookmarks and scripts pointing at pfam.xfam.org will fail.

### [Movebank](https://www.movebank.org/)

`Free (registration), email` · beginner 3/5 · animal tracking / biologging data

Free animal movement database hosted by the Max Planck Institute of Animal Behavior: 11.3 billion location records and 9.4 billion additional sensor measurements across 10,095 studies, 1,963 species and 5,263 data contributors. Includes the Env-DATA service that annotates tracks with matched environmental covariates.

**Access.** Free account, then browse or download studies through the web interface. Programmatic access via the Movebank REST API (https://www.movebank.org/movebank/service/direct-read) or the R packages `move2`/`move`, which authenticate with your Movebank credentials. Archived, permanently citable datasets live in the Movebank Data Repository with DOIs.

**Caveats.** Availability is set per study by the data owner: many studies are fully open, many require you to request permission from the owner, and some expose metadata only. Env-DATA annotation jobs are queued and can take hours for large tracks. Deployment metadata (tag type, attachment, duty cycle) is essential context and is not always complete.

### [NCBI GenBank and RefSeq](https://www.ncbi.nlm.nih.gov/genbank/)

`Free` · beginner 4/5 · nucleotide and protein sequence archive

GenBank release 273 (August 2026) holds 267,383,895 annotated sequences totalling 8.24 trillion bases, plus a Whole Genome Shotgun division of 5.13 billion sequences and 50.8 trillion bases. The curated RefSeq companion (release 236, 6 July 2026) contains 629,953,391 accessions of non-redundant genomic, transcript and protein records.

**Access.** Programmatic: E-utilities REST, e.g. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nuccore&term=BRCA1 ; in Python `pip install biopython` then `from Bio import Entrez; Entrez.email='you@example.com'`. Bulk: FTP/HTTPS at https://ftp.ncbi.nlm.nih.gov/genbank/ and /refseq/. CLI: NCBI `datasets` tool (`conda install -c conda-forge ncbi-datasets-cli`) for genomes and annotations.

**Caveats.** E-utilities are capped at 3 requests/second without an API key and 10/s with a free key; NCBI asks that large jobs run outside US peak hours and that an email be supplied. GenBank records are author-submitted and not curated, so annotation quality varies - RefSeq is the curated view. Bulk FTP of a full release is hundreds of gigabytes.

### [NCBI Gene Expression Omnibus (GEO)](https://www.ncbi.nlm.nih.gov/geo/)

`Free` · beginner 4/5 · functional genomics / expression data

Public archive of processed functional-genomics experiments: 294,373 GEO Series (GSE) as of August 2026, covering microarray, RNA-seq, ChIP-seq, methylation and single-cell studies, most with author-supplied processed matrices alongside links to raw reads in SRA.

**Access.** Web search at the GEO site, or in R: `BiocManager::install('GEOquery')` then `gse <- getGEO('GSE12345')`. Supplementary files download over FTP from https://ftp.ncbi.nlm.nih.gov/geo/series/. GEO2R gives browser-based differential expression on many series with no local install.

**Caveats.** Metadata quality is entirely down to the submitter; sample annotation is often free text and needs manual curation before reuse. Processed-value normalisation differs between series, so cross-study comparison usually means going back to the raw data in SRA.

### [NCBI Sequence Read Archive (SRA)](https://www.ncbi.nlm.nih.gov/sra)

`Free` · beginner 3/5 · raw sequencing reads

The world's largest public repository of raw high-throughput sequencing data, with 46,228,773 SRA records indexed in Entrez as of August 2026; NCBI's own growth statistics recorded over 53 petabases of open-access sequence by early 2024. Covers genomes, transcriptomes, metagenomes and single-cell libraries across all taxa.

**Access.** `conda install -c bioconda sra-tools`, then `prefetch SRR390728 && fasterq-dump SRR390728`. Cloud mirrors avoid the download entirely: the same runs sit in open S3 (`s3://sra-pub-run-odp/`) and Google Cloud buckets, and the SRA Toolkit can stream from them. Metadata search via Entrez `db=sra` or the SRA Run Selector web interface.

**Caveats.** Individual runs are commonly 1-50 GB, so disk and bandwidth, not permission, is the real barrier; `fasterq-dump` needs roughly 10x the final FASTQ size in scratch space. Human-subject data under dbGaP controlled access is NOT free - it requires institutional sponsorship and a Data Access Request, which unaffiliated researchers generally cannot obtain.

### [PRIDE Archive](https://www.ebi.ac.uk/pride/)

`Free` · beginner 2/5 · mass-spectrometry proteomics data

The largest public proteomics repository and the main ProteomeXchange deposition site, holding 40,947 projects as of August 2026 - raw spectra, search results and, for 'complete submission' projects, standardised mzIdentML/mzTab identifications.

**Access.** Web search at ebi.ac.uk/pride/archive; REST v3 API, e.g. `curl 'https://www.ebi.ac.uk/pride/ws/archive/v3/projects?pageSize=20'`. Files download over FTP from ftp.pride.ebi.ac.uk/pride/data/archive/, and via Aspera for large transfers. R client: `BiocManager::install('rpx')`.

**Caveats.** Reading and downloading need no account; submitting does (free ProteomeXchange/PRIDE account). Vendor raw files are large (often 0.5-5 GB per run) and many need conversion with ThermoRawFileParser or msconvert before open-source tools can read them. 'Partial' submissions may lack usable identification files.

### [RCSB Protein Data Bank](https://www.rcsb.org/)

`Free` · beginner 5/5 · experimental macromolecular structures

The single global archive of experimentally determined biomolecular structures: 258,735 experimental entries, 394 integrative structures and 1,062,058 linked computed structure models as of August 2026, including 82,979 human-sequence structures and 22,249 nucleic-acid-containing structures.

**Access.** Direct download: `curl -O https://files.rcsb.org/download/1CBS.cif`. Search and Data APIs are open JSON endpoints (https://search.rcsb.org, https://data.rcsb.org); Python wrapper `pip install rcsbsearchapi`. Whole-archive rsync from rsync.rcsb.org. Mirrors with different tooling: PDBe (https://www.ebi.ac.uk/pdbe/) and PDBj.

**Caveats.** Public domain, no licence restrictions. Legacy PDB-format files are unavailable for very large structures - use mmCIF/BinaryCIF, which is now the primary format. Resolution and validation metrics vary widely; check the wwPDB validation report before treating coordinates as ground truth.

### [UCSC Genome Browser](https://genome.ucsc.edu/)

`Free` · beginner 5/5 · genome browser and annotation tracks

Interactive browser and annotation warehouse for human (hg38, hg19, T2T-CHM13/hs1), mouse and, via the GenArk hub system, thousands of additional assemblies. Bundles BLAT, In-Silico PCR, LiftOver coordinate conversion and the Table Browser for filtered bulk export.

**Access.** Web browser at genome.ucsc.edu; Table Browser for filtered downloads; REST API at https://api.genome.ucsc.edu/getData/track?genome=hg38;track=knownGene;chrom=chr1. Bulk annotation files via rsync from rsync://hgdownload.soe.ucsc.edu/goldenPath/. Command-line utilities (bigWigSummary, liftOver, faToTwoBit) at hgdownload.soe.ucsc.edu/admin/exe/.

**Caveats.** Data are free; the Genome Browser software itself requires a paid licence for commercial use (academic and non-profit use is free). Public LiftOver and BLAT servers are rate-limited - heavy users are asked to install locally or use a mirror. For read-level BAM inspection on a laptop, IGV (https://igv.org) is the usual desktop companion.

### [UniProt](https://www.uniprot.org/)

`Free` · beginner 4/5 · protein sequence and function knowledgebase

Release 2026_02 (10 June 2026) contains 149,810,139 UniProtKB entries, of which 575,503 are manually reviewed Swiss-Prot records with literature-based annotation of function, domains, PTMs, variants and cross-references. Includes UniRef clusters and UniParc archival sequences.

**Access.** REST with content negotiation and no key: `curl 'https://rest.uniprot.org/uniprotkb/search?query=gene:TP53+AND+organism_id:9606&format=tsv&fields=accession,protein_name,length'`. Whole-proteome FASTA at https://ftp.uniprot.org/pub/databases/uniprot/. ID mapping runs as an async REST job; the website ID-mapping tool wraps the same endpoint.

**Caveats.** CC BY 4.0. The reviewed/unreviewed distinction matters enormously: TrEMBL entries are computationally annotated and roughly 260x more numerous than Swiss-Prot, so always filter on `reviewed:true` for curated work. GO annotations are propagated here and can be pulled in the same query.

## Software

### [Bioconda](https://bioconda.github.io/)

`Free` · beginner 4/5 · package manager channel for bioinformatics

Conda channel distributing thousands of prebuilt bioinformatics packages with their dependencies, so tools like samtools, BWA, STAR, salmon and Kraken2 install without a compiler, root access or a system package manager. Underpins most reproducible pipeline environments in the field.

**Access.** With pixi: `pixi config set default-channels '["conda-forge","bioconda"]'` then `pixi global install samtools`. With conda/mamba: `conda config --add channels bioconda --add channels conda-forge --set channel_priority strict`, then `mamba create -n bio samtools bcftools minimap2`. Every package also gets an auto-built Docker/Singularity image via BioContainers.

**Caveats.** Supports Linux (x86_64, aarch64) and macOS (x86_64, arm64) only - no native Windows, so Windows users need WSL2. Channel priority must be strict or dependency resolution can silently produce broken mixtures. Some packages lag upstream releases by weeks.

### [Bioconductor](https://bioconductor.org/)

`Free` · beginner 3/5 · R analysis ecosystem for genomics

Release 3.23 (29 April 2026, for R 4.6) provides 2,418 peer-reviewed software packages plus annotation and experiment-data packages, covering RNA-seq (DESeq2, edgeR, limma), single-cell (SingleCellExperiment, scran, scater), ChIP-seq, methylation, flow cytometry, mass spectrometry and imaging.

**Access.** `install.packages('BiocManager'); BiocManager::install(c('DESeq2','SummarizedExperiment'))`. Every package ships an executable vignette (`browseVignettes('DESeq2')`), which is usually the fastest path to a working analysis. Two releases a year, in spring and autumn.

**Caveats.** Package versions are pinned to an R version - mixing a Bioconductor release with the wrong R is the most common install failure for newcomers. Packages must pass build checks to stay in a release, so abandonware is pruned, but that also means version bumps can break older scripts. Record `BiocManager::version()` in your methods.

### [Biopython](https://biopython.org/)

`Free` · beginner 4/5 · Python bioinformatics library

The standard Python toolkit for sequence handling, file-format parsing (FASTA, GenBank, FASTQ, PDB, Clustal and dozens more), NCBI Entrez access, pairwise alignment, phylogenetics and population genetics. Version 1.88 as of August 2026.

**Access.** `pip install biopython` or `conda install -c conda-forge biopython`. One-liner: `from Bio import SeqIO; [print(r.id, len(r)) for r in SeqIO.parse('x.fasta','fasta')]`. The Biopython Tutorial and Cookbook is the canonical free reference.

**Caveats.** Uses the permissive Biopython Licence (BSD-like) rather than a standard SPDX identifier - worth knowing if a legal review expects a named licence. Several wrapper modules for external command-line aligners were deprecated and removed; call the tools directly with `subprocess` instead of following old tutorials.

### [CellProfiler](https://cellprofiler.org/)

`Free` · beginner 4/5 · high-throughput image cytometry

Modular pipeline software (v4.2.8) for measuring phenotypes from biological images without writing code: illumination correction, object identification, per-object morphology, intensity and texture measurement, and export to CSV or a database, designed for batches of thousands of images.

**Access.** Download the installer for Windows/macOS from cellprofiler.org, or `pip install cellprofiler` for the headless route. Build a pipeline in the GUI on a few images, then run the whole plate headless: `cellprofiler -c -r -p pipeline.cppipe -i images/ -o output/`. Example pipelines are published on the site and in the Broad Bioimage Benchmark Collection.

**Caveats.** BSD licensed. The GUI is comfortable on a laptop but a full plate is best run headless in batches. Segmentation parameters do not transfer between microscopes or stains - expect to retune. CellProfiler Analyst (interactive classification) is a separate download.

### [Fiji / ImageJ](https://fiji.sc/)

`Free` · beginner 4/5 · scientific image analysis

Fiji is a batteries-included distribution of ImageJ bundling thousands of scientific image-analysis plugins with an automatic updater and dependency management: segmentation, registration, deconvolution, particle tracking (TrackMate), stitching, 3D rendering and the Bio-Formats reader for over a hundred microscope file formats.

**Access.** Download the one-click bundle for Windows/macOS/Linux from fiji.sc - it runs from the extracted folder with no installer and no admin rights. Automate with the Script Editor (Groovy, Jython, JavaScript, Beanshell, ImageJ macro), or use Plugins > Macros > Record to turn clicks into a reproducible script.

**Caveats.** Open source (GPL/BSD depending on component), and one of the few genuinely heavy-duty analysis platforms that works well on an old laptop. Java heap must be raised manually (Edit > Options > Memory) for large stacks. Plugin quality is uneven and some update sites are unmaintained - cite the specific plugin and version, not just 'ImageJ'.

### [IQ-TREE](https://iqtree.github.io/)

`Free` · beginner 3/5 · phylogenetic inference

Maximum-likelihood phylogenetics (v2.4.0) with ModelFinder automatic substitution-model selection, ultrafast bootstrap approximation, SH-aLRT branch support, partitioned and mixture models, and topology tests - fast enough for genome-scale alignments on a desktop.

**Access.** `conda install -c bioconda iqtree`, or download a dependency-free static binary for Windows/macOS/Linux. Standard run: `iqtree2 -s alignment.fa -m MFP -B 1000 -alrt 1000 -T AUTO`, which picks a model, runs 1000 ultrafast bootstraps and chooses a thread count. Also available as a free web server at iqtree.org.

**Caveats.** GPL-2. Ultrafast bootstrap values are not on the same scale as standard bootstrap - 95% is the usual threshold, and mixing the two in one figure legend is a common error. Alignment quality dominates the result; pair with MAFFT and a trimming step. Large partitioned analyses can still take days.

### [Nextflow and nf-core](https://nf-co.re/)

`Free` · beginner 3/5 · workflow engine and curated pipelines

Nextflow (v26.04.6, July 2026) is a dataflow workflow engine with built-in container support and resume; nf-core is the community collection of 156 peer-reviewed, versioned, test-covered pipelines built on it, including rnaseq, sarek, mag, ampliseq, chipseq and scrnaseq.

**Access.** `curl -s https://get.nextflow.io | bash` (needs Java 17+), then `nextflow run nf-core/rnaseq -profile test,docker --outdir results` to verify the whole stack on a tiny dataset. Each pipeline documents its parameters and samplesheet format; `-resume` restarts from the last successful step.

**Caveats.** Apache 2.0 and fully runnable locally with Docker or Apptainer, but realistic genome-scale runs of pipelines like sarek need tens of gigabytes of RAM - plan on a shared cluster or cloud. Reference genome assets (iGenomes) are large; specify only what you need. Free training with a ready-made Codespaces environment is at https://training.nextflow.io/.

### [QIIME 2](https://qiime2.org/)

`Free` · beginner 3/5 · microbiome / amplicon analysis platform

Plugin-based microbiome multi-omics platform covering amplicon (16S/18S/ITS) and shotgun metagenome analysis, with automatic decentralised provenance recorded inside every artifact so any result can be traced back to the exact commands and parameters that made it. Cited over 65,000 times.

**Access.** Install a distribution (amplicon, metagenome or tiny) from the environment files at docs.qiime2.org via conda/mamba, then run e.g. `qiime dada2 denoise-paired ...`. Also usable through Galaxy with no install, and through the Python API (`import qiime2`) inside Jupyter. Visualisations (.qzv) open in the browser at https://view.qiime2.org without installing anything.

**Caveats.** BSD-3. Releases are dated (e.g. 2025.x) and the distributions were split apart in 2024, so instructions referring to a single monolithic `qiime2` environment are obsolete. DADA2 denoising is the memory bottleneck - a few hundred samples can exceed 16 GB. Reference classifiers (SILVA, GREENGENES2) are multi-gigabyte downloads.

### [SAMtools, BCFtools and HTSlib](https://www.htslib.org/)

`Free` · beginner 3/5 · alignment and variant file toolkit

The reference implementation for SAM/BAM/CRAM alignment files and VCF/BCF variant files, and the de facto standard for sorting, indexing, filtering, pileup, consensus calling and variant calling on the command line. SAMtools 1.24 released July 2026.

**Access.** `conda install -c bioconda samtools bcftools htslib`. Typical use: `samtools sort -@4 -o sorted.bam in.bam && samtools index sorted.bam`; `bcftools mpileup -f ref.fa sorted.bam | bcftools call -mv -Oz -o calls.vcf.gz`. C library plus Python bindings (`pip install pysam`) for programmatic access.

**Caveats.** MIT/Expat licensed. Keep samtools, bcftools and htslib at matching versions - mixed versions cause obscure index and header errors. CRAM saves 30-60% of disk versus BAM but requires the exact reference FASTA to decode, so archive the reference alongside the data.

### [Scanpy and the scverse ecosystem](https://scverse.org/)

`Free` · beginner 3/5 · single-cell analysis in Python

Scanpy 1.12.4 with AnnData 0.13.3 is the Python standard for single-cell RNA-seq: QC, normalisation, HVG selection, PCA, neighbour graphs, UMAP, Leiden clustering and differential expression, scaling to millions of cells. The scverse organisation also maintains muon (multimodal), squidpy (spatial) and scvi-tools (probabilistic models).

**Access.** `pip install scanpy` (add `scanpy[leiden]` for clustering). Standard opening: `import scanpy as sc; adata = sc.read_10x_h5('filtered.h5'); sc.pp.filter_cells(adata, min_genes=200)`. Tutorials at scanpy.readthedocs.io follow one AnnData object through the whole pipeline.

**Caveats.** BSD-3. Memory is the practical constraint: a dense 100k cells x 30k genes matrix will not fit in 16 GB, so keep `.X` sparse and use backed mode or the on-disk dask/zarr paths for atlas-scale data. API deprecations are frequent between minor versions - pin versions in any published analysis.

### [Seurat](https://satijalab.org/seurat/)

`Free` · beginner 4/5 · single-cell analysis in R

The most widely used R toolkit for single-cell genomics (v5.5.1 on CRAN, published 26 June 2026), covering QC, normalisation including SCTransform, anchor-based integration across datasets, clustering, DE testing, and multimodal and spatial assays via the v5 Assay5 and BPCells on-disk backends.

**Access.** `install.packages('Seurat')`; then `obj <- CreateSeuratObject(Read10X('filtered_feature_bc_matrix/'))` and follow the PBMC3K guided clustering vignette, which is the field's standard first tutorial. Reference-mapping and integration vignettes are on the same site.

**Caveats.** MIT + file LICENSE. The v4 to v5 object change broke many downstream packages and older scripts; `options(Seurat.object.assay.version='v3')` and `UpdateSeuratObject()` exist for compatibility. Some companion tools live on GitHub rather than CRAN and need `remotes::install_github`.

### [Snakemake](https://snakemake.readthedocs.io/)

`Free` · beginner 3/5 · workflow engine (Python/Make style)

Python-based workflow manager (v9.26.0, August 2026) using rules with input/output file patterns, with automatic dependency resolution, per-rule conda environments and containers, checkpointing, and executor plugins for SLURM, cloud and Kubernetes.

**Access.** `pip install snakemake` or `conda install -c bioconda snakemake`. Write a `Snakefile` of rules, then `snakemake --cores 4 --software-deployment-method conda`. The Snakemake Workflow Catalog (https://snakemake.github.io/snakemake-workflow-catalog/) lists reusable published workflows.

**Caveats.** MIT licensed. The CLI changed substantially at v8 (executor plugins replaced `--cluster`, `--use-conda` became `--software-deployment-method conda`), so pre-v8 tutorials will not run as written - check the version before copying commands. Python familiarity helps; Nextflow suits people who prefer channels over file-pattern rules.

### [UCSF ChimeraX](https://www.cgl.ucsf.edu/chimerax/)

`Free (registration), email` · beginner 3/5 · molecular structure visualisation and analysis

Successor to Chimera for visualising and analysing molecular structures, cryo-EM density maps, AlphaFold predictions (with built-in pLDDT and PAE colouring), sequence-structure alignment and publication-quality rendering, driven by a command language and a Python API.

**Access.** Download builds for Windows/macOS/Linux after accepting the non-commercial licence agreement. Fetch structures by accession without leaving the app: `open 1cbs` for the PDB, `open P00520 from alphafold` for AlphaFold DB. Script with ChimeraX commands in a .cxc file or Python via `runscript`.

**Caveats.** Free of charge for non-commercial use only - you must agree to the UCSF ChimeraX Non-Commercial Licence before downloading, and commercial use requires a separate paid licence priced by user count. Rendering large cryo-EM maps benefits from a discrete GPU. Open-source PyMOL is the main alternative where a non-commercial restriction is a problem.

## Literature

### [bioRxiv](https://www.biorxiv.org/)

`Free` · beginner 5/5 · preprint server

The preprint server for biology, covering all biological subject areas and receiving on the order of ten million views a month; roughly a hundred new preprints appear on a typical weekday. Since 11 March 2025 it has been operated by openRxiv, a purpose-built non-profit that also runs medRxiv.

**Access.** Read and download PDFs and full text with no account. Public metadata API: `curl 'https://api.biorxiv.org/details/biorxiv/2026-08-01/2026-08-02'` returns titles, authors, DOIs and categories. Posting needs a free account and passes a basic screen, not peer review. Full-text and supplementary bulk corpora sit in an AWS S3 requester-pays bucket.

**Caveats.** Reading is entirely free; the S3 text-and-data-mining corpus is requester-pays, so bulk downloads incur AWS charges you pay. Author-chosen licences vary (CC BY, CC BY-NC-ND, or 'no reuse' by default), which constrains text mining. Preprints are screened, not reviewed. openRxiv Labs began running interactive-reading experiments in 2026, so the reading interface may change.

*Also listed under: neuro-psych.*

### [Europe PMC](https://europepmc.org/)

`Free` · beginner 4/5 · life-science literature search and text mining

48,779,933 indexed records as of August 2026, combining PubMed/PMC content with preprints, patents, clinical guidelines and grant records, plus mined annotations that link papers to accession numbers, gene names, organisms and chemicals.

**Access.** Open REST API with no key: `curl 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:%22crispr%22&format=json&pageSize=25'`. Full-text XML for OA articles via the /fullTextXML endpoints; mined annotations via the Annotations API. R client: `install.packages('europepmc')`. SciLite overlays annotations on the article view.

**Caveats.** The preprint index and the cross-links from papers to ENA/UniProt/PDB accessions are what PubMed does not do, and the main reason to use it. Full text is available only for OA articles; abstract-only records dominate for subscription journals. Mined annotations are automated and carry false positives.

### [protocols.io](https://www.protocols.io/)

`Free tier, email` · beginner 5/5 · methods repository

Platform for writing, versioning, running and citing step-by-step experimental and computational methods. The free 'Open Research' plan gives unlimited public protocols with DOIs, version history, forking, and long-term preservation through CLOCKSS plus mirroring to the Internet Archive and GitHub.

**Access.** Free account at protocols.io, then write or fork a protocol and publish it to mint a DOI; run mode turns a protocol into an interactive checklist at the bench. Public protocols are searchable and readable without an account, and a REST API exposes protocol content as JSON.

**Caveats.** Free forever for published (public) protocols, but the free tier allows only 2 private protocols; unlimited private protocols, 10 GB storage, SSO, HIPAA support and 21 CFR Part 11 features are Enterprise-only and priced on request. Owned by Springer Nature since 2023. Not the tool if you need private electronic-lab-notebook privacy at no cost.

### [PubMed and PubMed Central](https://pubmed.ncbi.nlm.nih.gov/)

`Free` · beginner 5/5 · bibliographic database and full-text archive

PubMed indexes 41,074,375 citations in biomedicine and the life sciences; PubMed Central holds 12,559,759 records, of which 8,183,037 are flagged open access. PMC also archives NIH-funded author manuscripts and preprints from the NIH Preprint Pilot.

**Access.** Free web search with MeSH terms and field tags, e.g. `crispr[tiab] AND 2025:2026[dp]`. Programmatic via E-utilities: `esearch.fcgi?db=pubmed&term=...` then `efetch.fcgi?db=pubmed&id=...&retmode=xml`. The PMC Open Access Subset downloads in bulk from ftp.ncbi.nlm.nih.gov/pub/pmc/ or through the OA Web Service for text mining.

**Caveats.** Indexing is free, but only the OA subset (about two thirds of PMC) is legally reusable in bulk; the rest is readable on the site and not redistributable. PubMed indexes metadata only - a PubMed hit is not a full text. E-utilities are capped at 3 requests/second without a free API key, 10/s with one.

## Compute

### [ColabFold](https://github.com/sokrypton/ColabFold)

`Free tier, email` · beginner 4/5 · free protein structure prediction

Runs AlphaFold2, ESMFold and newer models (OpenFold3/AlphaFold3, Boltz, RoseTTAFold2, BioEmu, OmegaFold) in a Google Colab notebook, using a fast MMseqs2 API server for MSA generation instead of the multi-terabyte AlphaFold genetic databases. MIT licensed.

**Access.** Open the AlphaFold2_mmseqs2 notebook from the repository in Colab, paste a sequence (use a colon to separate chains for complexes), and run - no install, no local databases. For local or batch use, `pip install colabfold` and run `colabfold_batch input.fasta out/`, which still calls the public MSA server unless you host your own.

**Caveats.** Depends on whatever GPU Colab allocates that day; Colab's own FAQ states resources are 'not guaranteed and not unlimited'. Practical sequence-length ceiling is around 2000 residues on a ~16 GB GPU. The MMseqs2 API server is a shared community resource - the authors ask that queries be serial from a single IP and not spread across machines. A Google account is required.

### [EMBL-EBI Job Dispatcher web services](https://www.ebi.ac.uk/jdispatcher/)

`Free, email` · beginner 3/5 · free hosted sequence analysis jobs

Free hosted execution of the standard sequence-analysis tools - NCBI BLAST+, InterProScan 5, HMMER, Clustal Omega, MAFFT, MUSCLE, T-Coffee and EMBOSS among others - against EBI's reference databases, through both a web interface and a plain REST API. Removes the need to install multi-gigabyte databases locally.

**Access.** REST in three calls: POST to https://www.ebi.ac.uk/Tools/services/rest/ncbiblast/run with `email`, `sequence`, `program` and `database`; poll /status/<jobid>; GET /result/<jobid>/out. Same pattern for `iprscan5`, `clustalo`, `hmmer3_phmmer` and the rest; parameter lists are self-describing at /parameters. EBI publishes Python and Perl client scripts.

**Caveats.** No API key, but a valid email address is a required parameter and is used to contact heavy users. EMBL-EBI's terms state that usage which degrades service for others will be blocked - batch politely with delays, and switch to local installs for thousands of sequences. Jobs and results are retained only for about a week.

### [Galaxy public servers (usegalaxy.org / .eu / .org.au)](https://galaxyproject.org/use/)

`Free tier, email` · beginner 5/5 · free hosted bioinformatics compute

Free browser-based analysis platform with thousands of preinstalled tools and no local software or command line required. usegalaxy.org gives registered users 250 GB of storage and up to 6 concurrent jobs (5 GB and 1 job unregistered), dispatching work to national HPC resources; usegalaxy.eu also gives 250 GB, rising to 500 GB for ELIXIR members.

**Access.** Create a free account at usegalaxy.org, usegalaxy.eu or usegalaxy.org.au, upload FASTQ or fetch directly by SRA accession, and run tools from the tool panel. Histories and workflows can be shared by URL or published, and exported for reproducibility. The same servers run Jupyter and RStudio interactive tools in-browser.

**Caveats.** The single most practical free compute route for a bioinformatician without a cluster, but quotas are real - a couple of human WGS samples will fill 250 GB. Jobs queue behind other users and can wait hours at busy times. Not a compliance-grade private environment: do not upload identifiable human data. Quotas and tool availability differ between the three main servers and change over time.

## Publishing

### [eLife](https://elifesciences.org/)

`Freemium, email` · beginner 4/5 · reviewed preprints / open access journal

eLife no longer accepts or rejects: every reviewed paper is published as a Reviewed Preprint carrying public reviews and an eLife assessment that rates significance (landmark down to useful) and strength of evidence (exceptional down to inadequate). Authors may then publish a Version of Record to satisfy funder requirements.

**Access.** Submit an existing preprint at elifesciences.org; editors decide whether to send it for review. All content is free to read, and full text plus assessments are machine-readable through the eLife API and mirrored into PMC and Europe PMC.

**Caveats.** Reading is free; publishing carries a $3,750 fee charged at the review stage - but eLife states the fee is waived for anyone who cannot afford to pay, and a waiver request does not affect editorial decisions. Real cost of the model: because nothing is rejected, a Reviewed Preprint with a weak assessment is still permanently public. Clarivate removed eLife's impact factor over this model, which may matter to some assessment committees.

### [microPublication Biology](https://www.micropublication.org/)

`Freemium, email` · beginner 4/5 · single-figure peer-reviewed reports

Peer-reviewed open-access journal for brief reports built around a single multi-panel figure, explicitly publishing negative results, successful replications (including being scooped) and failed replications alongside novel findings. Indexed in PubMed, PMC and Europe PMC, and curated directly into WormBase, FlyBase, PomBase, ZFIN and the Alliance of Genome Resources.

**Access.** Submit at portal.micropublication.org; authors complete structured data forms using community controlled vocabularies, so results flow into the model organism databases on publication. Review assesses data quality and rigour rather than perceived impact.

**Caveats.** $350 APC for submissions received from 1 January 2025 (up from $250), but the journal states no article is refused for inability to pay. Best fit for a self-contained result - a validated reagent, a failed replication, a strain phenotype - that would otherwise never be published. The single-figure format is a hard constraint, not a suggestion.

### [Peer Community In and Peer Community Journal](https://peercommunityin.org/)

`Free, email` · beginner 4/5 · diamond open access / preprint peer review

Non-profit network of 21 thematic communities - including PCI Ecology, PCI Evolutionary Biology, PCI Genomics, PCI Microbiology, PCI Neuroscience, PCI Zoology, PCI Animal Science and PCI Plants - that peer-review and recommend preprints; 1,051 preprints recommended to date. Peer Community Journal publishes recommended preprints as citable, indexed diamond open-access articles, 532 so far.

**Access.** Post a preprint (bioRxiv, EcoEvoRxiv, Zenodo and others are accepted), then submit its DOI to the relevant PCI through the PCI website. If recommended, the recommendation is published with a DOI alongside the reviews; you may then publish in Peer Community Journal at no charge, or take the reviews to any other journal.

**Caveats.** Genuinely free for authors and readers with no APC at any stage - the strongest publishing route in this catalogue for an unfunded or unaffiliated researcher. Trade-offs: lower name recognition than established journals, no impact factor for Peer Community Journal, and review can be slow because recommenders are volunteers. Not every biology subfield has an active community.

### [PLOS journals](https://plos.org/publish/fees/)

`Freemium, email` · beginner 4/5 · open access journals with equity waivers

Non-profit publisher of PLOS Biology, PLOS Genetics, PLOS Pathogens, PLOS Computational Biology, PLOS ONE and others, all CC BY. Publication is free for authors at institutions in Research4Life Group A countries who have no external funding; Group B authors publish free in PLOS Biology, Medicine and Sustainability and Transformation, and pay a reduced $940 elsewhere.

**Access.** Submit through each journal's Editorial Manager site and declare fee-assistance need at submission, not later. Check country eligibility with the Research4Life country checker. Separately, the discretionary PLOS Publication Fee Assistance programme takes case-by-case hardship applications, decided within about 10 business days and kept hidden from editors and reviewers.

**Caveats.** Reading is always free. Standard fees without a waiver are substantial ($3,400-$6,460 for the Community Action Publishing titles), so the waiver route is the entire point for this audience - and it must be requested at submission, which authors routinely miss. 'No external funding' is a real condition: grant-funded authors in eligible countries may not qualify.

### [Review Commons](https://www.reviewcommons.org/)

`Free, email` · beginner 3/5 · journal-independent peer review

Platform launched by ASAPbio and EMBO that peer-reviews preprints before any journal submission, producing a refereed preprint with reviews and author response that can be taken to roughly twenty affiliate journals - including eLife, EMBO Journal, PLOS Biology, PLOS Genetics, Molecular Biology of the Cell, Development and Journal of Cell Science - without a fresh round of review.

**Access.** Recommended route is to post to bioRxiv or medRxiv first and transfer directly from their submission system; direct submission at https://reviewcommons.msubmit.net also works and posts the preprint to bioRxiv for you. Since 1 July 2023 a public preprint is mandatory. Authors control whether and when the reviews are posted publicly.

**Caveats.** No charge to authors. Editorial pre-screening means not every submission is sent for review, and scope is limited to the listed life-science areas. The submission system is live, but the platform's own blog has not been updated since April 2024 - confirm current affiliate participation before planning a route to a specific journal.

## Funding

### [Idea Wild](https://ideawild.org/)

`Free, application` · beginner 4/5 · equipment grants for conservation researchers

US non-profit that awards equipment rather than cash to biodiversity conservation researchers - camera traps, GPS units, binoculars, field laptops, lab consumables - for people who have the project but not the kit. Currently accepting applications from all countries.

**Access.** Single online application at https://ideawild.org/apply describing the project and the specific equipment needed; awards are purchased on the recipient's behalf or shipped. Past funded projects are mapped on the site.

**Caveats.** Awards are modest and in kind, not money, so they cannot cover salaries, travel or bench fees - this is a way to unblock a project missing one piece of hardware. The maximum award value is not published on the application page; ask before planning around a figure. Focus is biodiversity conservation, so molecular or biomedical work is generally out of scope.

### [Mohamed bin Zayed Species Conservation Fund](https://www.speciesconservation.org/grants/)

`Free, application` · beginner 3/5 · species-focused conservation grants

Grants targeted at individual species conservation initiatives for any plant, animal or fungus anywhere in the world, with emphasis on critically endangered, endangered and data-deficient species. 3,274 grants awarded since 2009 across mammals, birds, reptiles, amphibians, fish, invertebrates, plants and fungi.

**Access.** Apply online during one of three annual windows: 1-31 January (decision by late April), 1-31 May (decision by end September), and mid-September to mid-October (decision by late December). Application criteria, FAQs and a glossary are published on the grants pages, and past awards are browsable in the Grant Explorer.

**Caveats.** Windows are short and firmly enforced - check the current dates on the site, which lists them a year ahead. The fund is species-focused: habitat, education or broad ecosystem projects without a clear target species tend not to fit. Award sizes are not stated on the criteria page; browse the Grant Explorer for realistic figures in your taxon.

### [National Geographic Society grants](https://www.nationalgeographic.org/society/grants-and-investments/)

`Free, application` · beginner 3/5 · field research and exploration grants

Funds conservation, ecology, exploration, science and storytelling projects worldwide. As of 2026 the Society has replaced its former Level I / Level II tiered grants with a Request-for-Proposals model: time-bound calls, each with its own scope, eligibility and deadline, announced on the Society's funding pages.

**Access.** Applications go through the National Geographic Funding Portal against a currently open RFP. Applicants must be 18 or over, project start dates must be at least six months after submission, and a person may lead only one funded project at a time.

**Caveats.** The move away from open Level I/II calls is significant: there is no longer a permanently open general application, so success depends on an RFP matching your topic and region. Institutional affiliation is not stated as a requirement - the Explorer community explicitly includes people outside academia - but strong local context and partnerships are weighted heavily.

### [The Company of Biologists grants](https://www.biologists.com/grants/)

`Free, application` · beginner 4/5 · travel, meeting and training grants

Not-for-profit publisher offering small grants aimed at early-career biologists: Travelling Fellowships of up to £3,000 for graduate students and postdocs to make collaborative lab visits, with no nationality restriction; Scientific Meeting Grants up to £3,000; Sustainable Conferencing Grants up to £2,500; and Biology Open conference travel grants of up to £3,000 for early-career researchers based in the Global South.

**Access.** All schemes are applied for through the grants portal at cob.smartsimpleuk.com after free registration; deadlines and eligibility differ per scheme and are listed at biologists.com/grants. Journal of Cell Science also funds microscopy course attendance up to £1,000, and Disease Models & Mechanisms funds meeting travel up to £500.

**Caveats.** Travelling Fellowships require both a home lab and a host lab, which in practice means holding a current research position - they do not fit fully unaffiliated researchers. Amounts are small and intended as top-ups, not project funding. The Global South conference travel grants are the most accessible route for researchers at poorly resourced institutions.

### [The Rufford Foundation](https://www.rufford.org/)

`Free, application` · beginner 3/5 · small grants for nature conservation

UK charity funding nature conservation and pilot projects led by early-career conservationists in developing and emerging-economy countries; 6,841 projects funded across 152 countries. Four sequential grant levels (1st RSG, 2nd RSG, Booster, Completion) ranging from £7,000 to £18,000.

**Access.** Apply through the online portal at https://apply.ruffordsmallgrants.org - applications are accepted year-round with no deadlines, and a guidance webinar is published on the Rufford site. The application is written by the individual, not routed through an institutional grants office.

**Caveats.** Eligibility is genuinely narrow: nature conservation focus, threatened species, project located in an eligible (developing or emerging economy) country, and the applicant must be a current or recent master's/doctoral student or equivalent early-career conservationist. Undergraduates are not supported. Unsuccessful applicants must wait 12 months to reapply. Not a route for lab-based or biomedical work.

*Also listed under: earth.*

## Learning

### [EMBL-EBI Training](https://www.ebi.ac.uk/training/)

`Free` · beginner 5/5 · on-demand courses on public data resources

Free on-demand courses, quick tours and webinars written by the teams that build the resources: how to search and interpret UniProt, Ensembl, PDBe, BioStudies/ArrayExpress, InterPro, AlphaFold and the ENA, alongside broader topics such as data management plans, FAIR principles and statistics for biologists.

**Access.** Browse https://www.ebi.ac.uk/training/on-demand and start any course in the browser - most need no account and no software installed. Live virtual and on-site courses are listed separately with their own applications; recordings of past webinars are published free.

**Caveats.** The on-demand material is genuinely free and self-paced; residential and some live virtual courses are competitive and may charge a fee. Content is resource-focused - excellent for learning what is inside a database and how to query it, much less useful for learning to program. Some older courses reference retired interfaces.

### [Galaxy Training Network](https://training.galaxyproject.org/)

`Free` · beginner 5/5 · hands-on bioinformatics tutorials

Community-maintained curriculum of 536 tutorials across 35 topics, with 28 learning paths, 549 FAQs, 361 ready-to-run workflows and 222 videos totalling 155 hours, contributed by 539 people over more than 11 years. Topics span genome assembly, variant calling, RNA-seq, single-cell, proteomics, microbiome, ecology and machine learning.

**Access.** Read at training.galaxyproject.org and run every step in a free public Galaxy account - tutorials include buttons that import the exact history and workflow into a Galaxy server. Many tutorials also carry command-line and Jupyter variants for people not using Galaxy.

**Caveats.** CC BY. The closest thing in biology to a complete, free, no-install practical curriculum, and it stays current - new tutorials were added on 28 August 2026. Tutorial datasets are deliberately small, so timings and resource estimates do not transfer to real data. Some tutorials assume tools installed only on a particular public server (usegalaxy.eu vs .org), so check the recommended server.

### [iBiology](https://www.ibiology.org/)

`Free` · beginner 5/5 · research talks and skills courses

Free library of over 600 biology talks by working scientists, plus structured courses including a full Microscopy Series (and a 14-lecture short version), Bioimage Analysis, Next Generation Sequencing, and professional-development courses on scientific writing, presenting and career planning. Produced by the non-profit Science Communication Lab.

**Access.** Watch on ibiology.org or the associated YouTube channels with no account. A free educator account unlocks lesson plans, learning objectives and discussion questions for classroom use. Courses are organised as ordered playlists.

**Caveats.** These are lectures, not interactive courses - no exercises, no certificates. Some talks are several years old and describe methods that have since moved on, which matters most in the sequencing and imaging series. The Microscopy Series remains the strongest free introduction to optical microscopy available anywhere.

### [Orchestrating Single-Cell Analysis with Bioconductor (OSCA)](https://bioconductor.org/books/release/OSCA/)

`Free` · beginner 3/5 · open textbook, single-cell analysis

The field's reference open textbook for single-cell RNA-seq in R, covering QC, normalisation, feature selection, dimensionality reduction, clustering, marker detection, cell type annotation, doublet handling, trajectory analysis, multi-sample designs and complete worked workflows. Compiled 29 April 2026 against Bioconductor 3.23 and R 4.6.

**Access.** Read free online at the URL above; the book is split into Introduction, Basics, Advanced, Multi-sample and Workflows volumes. All code is executable and the book rebuilds with each Bioconductor release, so printed output matches the current package versions. Source on GitHub.

**Caveats.** CC BY 4.0. Assumes working R and some statistics - it is a reference text, not a first programming course. Bioconductor-centric, so if your lab standardises on Seurat or Scanpy the concepts transfer but the code does not. Bioconductor hosts a shelf of similar free books at bioconductor.org/books/.

### [Rosalind](https://rosalind.info/)

`Free (registration), email` · beginner 4/5 · bioinformatics programming exercises

Free problem-solving platform for learning bioinformatics through code, structured as tracks: Python Village for absolute beginners, the Bioinformatics Stronghold for core algorithms (string algorithms, assembly, phylogeny, population genetics), and a Textbook Track keyed to the Bioinformatics Algorithms textbook.

**Access.** Free account at rosalind.info, then solve problems in any language and paste the output, which is checked against a dataset randomised per user. Problems unlock progressively, and each links to the relevant biological background.

**Caveats.** Requires JavaScript. Teaches algorithms in isolation rather than the real toolchain - you will not learn BAM files, workflow managers or cluster jobs here. Difficulty rises steeply after the first dozen Stronghold problems. Best used alongside a practical course, not instead of one.

### [The Carpentries (Data Carpentry Genomics)](https://datacarpentry.github.io/genomics-workshop/)

`Free` · beginner 5/5 · foundational computing skills workshops

Two-day openly licensed curriculum teaching project organisation for bioinformatics, the Unix shell, sequence quality control and variant calling on real data, plus connecting to and using cloud computing. Part of the wider Carpentries family (Software Carpentry: shell, Git, Python/R; Data Carpentry: domain data lessons).

**Access.** All lessons are free to read and self-study at the URL above, with a Setup page listing exactly what to install and downloadable example data. Instructor notes and an onboarding video let anyone teach the material; contact team@carpentries.org to be recorded as an onboarded instructor.

**Caveats.** CC BY licensed, so lessons can be reused and translated freely. Self-study loses the main benefit, which is live helpers who unstick installation problems. Attending an official workshop usually carries a registration fee set by the host, though many are free or subsidised. Lessons assume a Unix-like environment; Windows users need Git Bash or WSL.

## Community

### [Bioconductor Support Site](https://support.bioconductor.org/)

`Free, email` · beginner 4/5 · R/Bioconductor package support

Official support forum for Bioconductor packages, where package maintainers are expected to answer questions about their own software. The canonical place to ask about DESeq2 design formulas, limma contrasts, SummarizedExperiment handling and installation failures across R and Bioconductor versions.

**Access.** Read without an account; free registration to post. Tag your post with the package name so its maintainer is notified, and include the output of `sessionInfo()`. The separate bioc-devel mailing list is for package development, not usage.

**Caveats.** Posting guidelines are enforced: questions without a reproducible example and sessionInfo() often receive only a request for those. Maintainers answer voluntarily, so response time ranges from hours to a week. Questions about non-Bioconductor R packages will be redirected elsewhere.

### [Biostars](https://www.biostars.org/)

`Free, email` · beginner 4/5 · bioinformatics Q&A forum

The long-running Q&A site for practical bioinformatics: file formats, aligner behaviour, tool errors, pipeline design, statistics of differential expression, and 'which tool should I use' questions. Answers frequently come from the authors of the tools being discussed, and the archive is deep enough that most beginner questions are already answered.

**Access.** Read and search without an account at biostars.org; a free account (email or OAuth) is needed to post or vote. Tag-based browsing and a job board are on the same site. Search the archive before posting - duplicates are closed quickly.

**Caveats.** Culture rewards a minimal reproducible example with exact commands, versions and error text; vague questions are often ignored or downvoted. Activity has thinned somewhat as discussion moved to tool-specific Slack and Discourse forums, so niche questions can go unanswered. Old accepted answers may reference deprecated tool versions.

### [Image.sc Forum](https://forum.image.sc/)

`Free, email` · beginner 4/5 · scientific imaging and image analysis

Shared Discourse forum for the open-source bioimage analysis ecosystem - ImageJ/Fiji, napari, CellProfiler, QuPath, Icy, ilastik, Bio-Formats and OMERO. 48,866 topics and 363,626 posts from 33,864 registered users, running roughly 120 new topics and 790 posts a month as of August 2026.

**Access.** Read without an account at forum.image.sc; free registration to post. Tag your topic with the software you are using so the right developers see it, and attach a sample image or screenshot - image analysis questions are close to unanswerable without one.

**Caveats.** Developers of the major tools read and answer here directly, which makes it unusually high-signal. Traffic skews toward the biggest tools, so questions about rarely used plugins can go unanswered. Uploading images makes them public - check permissions for unpublished or patient-derived data first.

### [nf-core community (Slack and Bytesize)](https://nf-co.re/join)

`Free, email` · beginner 3/5 · workflow and pipeline community

Open community behind the 156 nf-core pipelines, with a public Slack workspace containing per-pipeline channels where maintainers answer questions directly, plus the free weekly 'Bytesize' talk series, regular hackathons, mentorship programmes and special interest groups.

**Access.** Self-serve invite to the Slack workspace at nf-co.re/join, then join #help and the channel for your pipeline (e.g. #rnaseq). Bytesize talks are livestreamed and archived free on the nf-core site and YouTube. Bugs and feature requests go to each pipeline's GitHub repository.

**Caveats.** Slack's free tier hides older messages, so answers are not durably searchable the way a forum is - check the pipeline docs and GitHub issues first. The community assumes you can read a Nextflow error trace; complete beginners should work through the free training at training.nextflow.io before asking. Activity skews to European time zones.
