# Biology & life sciences

Part of [research-vault](../README.md). 87 entries, verified 2026-08-28. Free status and limits change; check the source before you build on it.

Beginner ratings run 1–5: 5 means a newcomer gets something useful out of it in ten minutes, 1 means a specialist toolchain and patience.

**Contents:** [Data](#data) (38) · [Software](#software) (20) · [Literature](#literature) (5) · [Compute](#compute) (4) · [Publishing](#publishing) (5) · [Funding](#funding) (5) · [Learning](#learning) (6) · [Community](#community) (4)

## Data

### [Addgene](https://www.addgene.org/)

`Freemium, email` · beginner 5/5 · plasmid repository and sequence database

Non-profit plasmid repository distributing 176,441 plasmids deposited by 7,029 laboratories, plus 1,091 ready-to-use viral preps and 304 recombinant antibodies; materials have been requested over 2.4 million times across 113 countries. Catalogue entries carry maps, sequence data, the depositing publication and quality-control information.

**Access.** Search by gene, vector element, technique or paper at addgene.org - catalogue entries, plasmid maps, and the protocol, eBook and molecular-biology reference library are readable with no account; full sequence downloads sit behind a free login. Ordering requires a free account plus a signed institutional MTA; material ships as a bacterial stab, purified DNA or viral prep.

**Caveats.** The knowledge layer is free; the material is not. Each plasmid carries a per-item fee plus shipping, priced higher for industry than for non-profits (current prices are on Addgene's help site). The institutional MTA is a hard barrier for genuinely unaffiliated researchers, since someone with signing authority must execute it. Deposited constructs inherit the depositor's own terms and some are restricted to non-commercial use - check the entry before building a product on one.

### [Alliance of Genome Resources](https://www.alliancegenome.org/)

`Free` · beginner 4/5 · model organism databases

Unified portal and data warehouse across the major model organism databases - WormBase, FlyBase, SGD (yeast), ZFIN (zebrafish), MGI (mouse), RGD (rat), PomBase and Xenbase - plus human, giving cross-species orthology, expression, disease association, allele and phenotype data in one schema.

**Access.** Cross-species web search at alliancegenome.org; REST API at https://www.alliancegenome.org/api/ (e.g. /api/gene/HGNC:5). Bulk TSV/JSON files on the Downloads page. Member databases keep their own APIs - for example `curl 'https://api.flybase.org/api/v1.0/gene/summaries/auto/FBgn0000490'` returns FlyBase FB2026_02 data.

**Caveats.** The Alliance harmonises a subset of what each member database curates; for deep organism-specific work (WormBase phenotype ontologies, FlyBase stock records, SGD literature curation) go to the member site directly. Gene nomenclature conventions differ across organisms, so orthology mapping needs care.

### [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/)

`Free` · beginner 4/5 · predicted protein structures

241,070,489 AlphaFold2-predicted protein structures (v6 release dated 2025-09-15, aligned to UniProt 2025_03), including 40,054 isoform sequences and, new in this release, the input multiple sequence alignments in A3M format plus per-entry MSA depths.

**Access.** Per-entry files by UniProt accession: `curl -O https://alphafold.ebi.ac.uk/files/AF-P00520-F1-model_v6.cif`. Bulk: per-proteome tar files and the full 110 GB sequences.fasta at https://ftp.ebi.ac.uk/pub/databases/alphafold/; the complete dataset is also a Google Cloud public dataset. Per-accession JSON metadata from https://alphafold.ebi.ac.uk/api/prediction/P00520; current API documented at https://alphafold.ebi.ac.uk/api-docs.

**Caveats.** CC BY 4.0. The legacy API's announced retirement date (June 2026) has now passed, so check that any inherited script uses the current endpoint (https://alphafold.ebi.ac.uk/api/prediction/<accession>), and note that older model_v4/v5 file URLs no longer resolve. These are predictions, not measurements: read per-residue pLDDT and PAE before trusting a region, and low-pLDDT stretches often indicate genuine disorder. No complexes, no ligands, no alternative conformations; use ColabFold for those.

### [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/)

`Free` · beginner 3/5 · biological imaging data archive

EMBL-EBI's open archive for biological imaging data of any modality - light and electron microscopy, high-content screens, whole-slide histology, tomography, correlative imaging - holding 1,594 studies as of August 2026. It is the recommended deposition route for images underlying a publication and the storage layer beneath the Image Data Resource.

**Access.** Search and browse at ebi.ac.uk/bioimage-archive. Every study has an open FTP/HTTPS directory and a REST endpoint through the BioStudies API: `curl 'https://www.ebi.ac.uk/biostudies/api/v1/search?collection=bioimages&query=cryoEM'` and `/api/v1/studies/S-BIAD###`. Submission is free through the BioStudies submission tool, with Aspera/FTP drop for terabyte-scale datasets.

**Caveats.** Free to read and free to deposit, but studies routinely run to hundreds of gigabytes or terabytes, so plan transfers and prefer streaming from OME-Zarr copies where they exist. Metadata quality varies hugely by submitter; REMBI-compliant studies are far more reusable than minimal ones. This is an archive, not a browsing or analysis environment - use IDR when you want curated, annotated, viewable collections. Submitters must self-certify rights to release the data publicly.

### [BOLD (Barcode of Life Data System)](https://www.boldsystems.org/)

`Free` · beginner 3/5 · DNA barcode reference library

Reference library of DNA barcodes (chiefly COI for animals, rbcL/matK for plants, ITS for fungi) linked to vouchered specimens: over 20.7 million public records representing 1.6 million species, organised into Barcode Index Numbers (BINs) that approximate species clusters.

**Access.** Data Portal search and versioned, citable Data Packages at boldsystems.org; the Barcode ID Engine identifies an unknown sequence from a pasted FASTA in the browser. Public API at https://v4.boldsystems.org/index.php/API_Public/ for combined specimen+sequence records; R client `BOLDconnectR`. A free Workbench account is needed to upload and manage your own project data.

**Caveats.** BOLD v5 restructured the site and APIs; v4 remains reachable at v4.boldsystems.org and older scripts often still target it. A large share of total records are not public (awaiting validation or release). Taxonomic labels are only as good as the original specimen identification - BINs, not names, are the more stable unit.

### [BV-BRC (Bacterial and Viral Bioinformatics Resource Center)](https://www.bv-brc.org/)

`Free` · beginner 4/5 · bacterial and viral genomes plus free hosted analysis

NIAID-funded merger of PATRIC and IRD/ViPR holding 16,935,541 consistently annotated genomes (1,380,120 bacterial, 15,510,758 viral) with AMR phenotypes, protein families and comparative-genomics views, alongside free hosted analysis services: assembly, RASTtk annotation, variant calling, phylogenetic trees, metagenomic binning, RNA-seq and AMR prediction.

**Access.** Browse and download without an account at bv-brc.org. Data API returns JSON/TSV with no key: `curl 'https://www.bv-brc.org/api/genome/?eq(species,Mycobacterium%20tuberculosis)&limit(10)&http_accept=application/json'` (total count comes back in the Content-Range header). To run analysis services, register a free account and submit jobs from the web workspace or with the `bv-brc-cli` command-line tools.

**Caveats.** Data access needs nothing; running the compute services needs a free account, and jobs queue behind other users so large assemblies or trees can wait hours. The genome count is dominated by SARS-CoV-2 and influenza submissions, so unfiltered totals are misleading. Annotation shown is BV-BRC's own (RASTtk for bacteria, VIGOR for viruses) and can differ from the GenBank record for the same accession.

### [cBioPortal for Cancer Genomics](https://www.cbioportal.org/)

`Free` · beginner 5/5 · cancer genomics portal

Browser and API over 542 public cancer genomics studies totalling 400,281 samples as of August 2026 - TCGA, TARGET, MSK-IMPACT, ICGC and hundreds of single-paper cohorts - with harmonised mutation, copy-number, fusion, mRNA and protein expression and clinical/survival annotation.

**Access.** Query genes across one or many studies at cbioportal.org; OncoPrint, mutation lollipop, co-expression, mutual-exclusivity and Kaplan-Meier views are built in and need no code. Open REST API with no key: `curl 'https://www.cbioportal.org/api/studies?projection=SUMMARY'`, `/api/molecular-profiles`, `/api/studies/{studyId}/samples`; interactive docs at /api/swagger-ui. R: `BiocManager::install('cBioPortalData')`.

**Caveats.** Public studies need no login; a small number of consortium studies are access-restricted and a few (for example TARGET) carry publication-embargo conditions. Data are reprocessed by cBioPortal's own pipelines, so mutation calls and discrete copy-number thresholds can differ from the source paper - go to the NCI Genomic Data Commons for raw or controlled-access files. Pooling studies mixes whole-exome with targeted panels of different gene content, which quietly biases mutation-frequency comparisons.

### [CZ CELLxGENE Discover](https://cellxgene.cziscience.com/)

`Free` · beginner 4/5 · single-cell transcriptomics

Standardised, ontology-annotated single-cell RNA-seq corpus: 388 public collections spanning 2,216 datasets as of August 2026, plus the Census API for querying arbitrary slices of the whole corpus and a browser-based Explorer for interactive visualisation with no local install.

**Access.** `pip install cellxgene-census` then `import cellxgene_census; census = cellxgene_census.open_soma()` (R: `cellxgene.census`) to pull a filtered AnnData/Seurat object directly. Per-dataset .h5ad and .rds files download from each collection page. REST curation API at https://api.cellxgene.cziscience.com/curation/v1/collections.

**Caveats.** Census slices are memory-hungry - filter by tissue, assay and cell type before materialising, or a broad query will exhaust a 16 GB laptop. Datasets are reprocessed to a common schema, so counts and metadata may differ from the original publication's matrices. The Human Cell Atlas Data Portal (https://data.humancellatlas.org, 532 projects and 70.9M cells) holds the raw-data counterpart.

### [DepMap Portal](https://depmap.org/portal/)

`Free` · beginner 4/5 · cancer cell line dependencies and omics

Broad Institute portal for genome-wide CRISPR knockout and RNAi viability screens across cancer cell lines, released twice a year (26Q1 is current), with matched omics for the same models: mutations, copy number, expression, fusions, methylation, proteomics (including Olink profiling of 161 lines across 24 lineages) and drug sensitivity.

**Access.** Search a gene or cell line at depmap.org/portal for its dependency profile, co-dependency correlations and expression; Data Explorer plots any two features against each other in the browser. Full release matrices (CRISPRGeneEffect.csv, OmicsExpressionProteinCodingGenesTPMLogp1.csv, Model.csv and the rest) download from the Downloads page, with each release also archived on figshare with a DOI.

**Caveats.** Chronos gene-effect scores are relative, not absolute: roughly 0 means no effect and -1 is about the median of common essential genes, and scores are only comparable within one release, so never mix quarters in a single analysis. Cell lines are not tumours - an in vitro dependency may not survive in vivo. Check each release's terms page before redistributing derived files, since some contributed datasets carry their own conditions.

### [eBird and the Macaulay Library](https://science.ebird.org/en/use-ebird-data)

`Free (registration), application` · beginner 2/5 · bird occurrence and media archive

The largest biodiversity citizen-science dataset in the world: complete checklists with effort covariates (duration, distance, observer count) from every country, released as the eBird Basic Dataset (EBD) on a monthly cycle, plus the Macaulay Library archive of bird photos, audio and video linked to those checklists.

**Access.** Create a free eBird account, then submit a data request for the EBD; on approval you download a large tab-delimited file and filter it with the R package `auk` (`install.packages('auk')`, which wraps AWK for out-of-memory filtering). For live queries of recent sightings, the eBird API 2.0 uses a free API key. Modelled abundance surfaces come via the `ebirdst` package, which needs its own access key.

**Caveats.** The EBD is a single multi-gigabyte file that will not open in a spreadsheet - `auk` filtering before import is effectively mandatory. Data requests are reviewed and must state a research or education purpose; approval is routine but not instant, and terms restrict commercial redistribution. Sampling is unstructured, so effort covariates and the sampling-event file are needed for any occupancy or abundance modelling.

### [ENCODE Portal](https://www.encodeproject.org/)

`Free` · beginner 3/5 · regulatory and functional genomics

Uniformly processed functional-genomics data: 28,642 experiments as of August 2026 spanning ChIP-seq, ATAC-seq, DNase-seq, total and polyA RNA-seq, WGBS, Hi-C, CRISPR screens and more across human and mouse cell lines, primary cells and tissues, each with released FASTQ, BAM, peak and bigWig files, full metadata and automated audit flags.

**Access.** Faceted search at encodeproject.org; append `&format=json` to any search or object URL for the same data as JSON (`https://www.encodeproject.org/search/?type=Experiment&assay_title=ChIP-seq&status=released&format=json`). 'Download' on a search produces a files.txt of URLs to feed `xargs -n1 curl -O -L`. Processed signal and peak files load straight into the UCSC Genome Browser and IGV as tracks.

**Caveats.** No account, no restrictions on use - the barrier is the metadata model. Experiment > replicate > file with audit categories and 'preferred default' flags takes real time to learn, and using a file without reading its audits (low read depth, missing controls, non-compliant replicates) is the usual beginner mistake. The full archive is petabyte-scale; filter on assembly, output type and released status before downloading anything.

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

### [Gene Ontology (GO) Consortium](https://geneontology.org/)

`Free` · beginner 4/5 · functional annotation ontology

The controlled vocabulary underpinning nearly all functional interpretation in biology. The 2026-08-05 release defines 38,092 non-obsolete terms (23,974 biological process, 10,041 molecular function, 4,077 cellular component) and 15,129,348 gene-product annotations, of which 1,086,714 carry experimental evidence codes and 9,458,635 are electronic (IEA).

**Access.** Ontology (go-basic.obo, go.owl) and GAF/GPAD annotation files at https://current.geneontology.org/; browse and search annotations at AmiGO (https://amigo.geneontology.org/); run enrichment through the PANTHER-backed GO Enrichment tool on the homepage. In R: `BiocManager::install(c('GO.db','topGO'))`; in Python: `pip install goatools` then `python -m goatools.cli.find_enrichment study.txt pop.txt assoc.txt`.

**Caveats.** CC BY 4.0. Evidence codes matter more than most users realise: only about 7% of annotations are experimental, so an unfiltered enrichment result is largely driven by electronic and phylogenetically inferred annotations. Terms are obsoleted and merged between releases (10,248 obsolete, 2,434 merged currently), so record the release date. GO describes function, not causation - GO-CAM models are the newer, more mechanistic layer.

### [gnomAD (Genome Aggregation Database)](https://gnomad.broadinstitute.org/)

`Free` · beginner 4/5 · human population genetic variation

Aggregated allele frequencies from harmonised human exomes and genomes; the browser's current dataset family is gnomAD v4, giving per-variant frequencies by genetic ancestry group, per-gene constraint metrics (pLI, LOEUF, missense Z), and separate structural-variant and copy-number releases.

**Access.** Browser search by gene, region, variant or rsID. Public GraphQL API at https://gnomad.broadinstitute.org/api (POST a query; no key). Bulk VCFs and Hail Tables are hosted as open cloud datasets on Google Cloud Storage, AWS and Azure - exact bucket paths are on the Downloads page.

**Caveats.** Free with no restrictions on use, but the full genome VCFs run to terabytes; per-gene or per-region slices via the browser or API are the realistic route on a laptop. Frequencies are summary statistics only - individual genotypes are not released. For open genotypes and actual sequence data, use IGSR/1000 Genomes (https://www.internationalgenome.org/), which is fully open including CRAMs.

### [GTEx Portal](https://gtexportal.org/)

`Free` · beginner 5/5 · human tissue expression and eQTLs

Reference resource for normal human tissue gene expression and its genetic regulation. The v8 release, still the portal's current release, catalogues 22,734 samples from 979 post-mortem donors across 54 tissue sites, with gene and transcript TPMs, cis- and trans-eQTLs, sQTLs and structural-variant QTLs.

**Access.** Search a gene at gtexportal.org for per-tissue expression violin plots, eQTL violin plots and the multi-tissue eQTL heatmap. Open REST API v2, no key: `curl 'https://gtexportal.org/api/v2/expression/medianGeneExpression?gencodeId=ENSG00000141510.16'`; summary files (GTEx_Analysis_*_gene_tpm.gct.gz, eQTL result tarballs, sample attributes) from the Datasets page.

**Caveats.** Summary statistics are fully open; individual-level genotypes, RNA-seq reads and detailed phenotypes are protected and require a dbGaP controlled-access application (phs000424) sponsored by an institution, which unaffiliated researchers generally cannot obtain. Donors are post-mortem adults, predominantly of European ancestry and male-skewed, so eQTL portability to other populations is limited, and post-mortem interval affects some tissues' transcriptomes.

### [Human Protein Atlas](https://www.proteinatlas.org/)

`Free` · beginner 5/5 · protein expression and localisation atlas

Open atlas of human protein expression across nine sections (Tissue, Brain, Single Cell, Subcellular, Cancer, Blood, Cell Line, Structure, Interaction). Version 25.1 was released on 25 May 2026, following v25.0 (11 November 2025) which covered over 27,800 antibodies targeting more than 17,400 human genes (~88% of protein-coding genes). Includes antibody-based tissue profiling for 15,312 genes, subcellular localisation for 13,603 genes, RNA-seq across 51 tissue types, and millions of immunohistochemistry images.

**Access.** Web interface at proteinatlas.org - searching a gene symbol goes straight to the summary page. Bulk TSV/XML/JSON downloads at https://www.proteinatlas.org/about/download, including normal-tissue, pathology, subcellular-location and single-cell expression tables. Individual entries are also available as XML, e.g. proteinatlas.org/ENSG00000134057.xml.

**Caveats.** CC BY-SA 3.0 for images and data - the share-alike clause matters if you redistribute. Antibody-based data carry a validation score; unvalidated or 'uncertain' antibody results are common and should not be treated as definitive evidence of localisation. Human only.

### [Image Data Resource (IDR)](https://idr.openmicroscopy.org/)

`Free` · beginner 3/5 · curated public imaging datasets

Curated, OMERO-backed collection of published imaging studies - genome-scale high-content screens, super-resolution, EM volumes, light-sheet and spatially resolved transcriptomics - with harmonised experimental metadata, phenotype annotations and regions of interest, browsable in the viewer and queryable through the OMERO API. Content is licensed CC BY 4.0.

**Access.** Browse at idr.openmicroscopy.org with no account. Programmatic access through the OMERO JSON API (`https://idr.openmicroscopy.org/api/v0/m/screens/`, `/api/v0/m/projects/`) and via `pip install omero-py` or `ezomero`; a public Jupyter environment lets you compute next to the data instead of downloading it. Newer studies are published as OME-Zarr and read directly with `ome-zarr-py`, napari or Fiji.

**Caveats.** Read-only for outside users: new depositions now go to the BioImage Archive, and IDR curates a subset from there. The ongoing migration to OME-Zarr means some older non-Zarr images are currently thumbnail-only in the web viewer. Screens are enormous - subset by screen, plate and well before pulling pixel data, and prefer the API's rendered images over full-resolution planes for browsing.

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

### [JGI Data Portal (Phytozome, MycoCosm, IMG/M)](https://data.jgi.doe.gov/)

`Free (registration), email` · beginner 3/5 · plant, fungal, algal and microbial genomics

US DOE Joint Genome Institute's public data hub and the route into its domain portals: Phytozome for plant genomes and gene families, MycoCosm for fungi, PhycoCosm for algae, and IMG/M for microbial isolate genomes and metagenomes, together with the raw sequencing and analysis project files behind them.

**Access.** Search across projects at data.jgi.doe.gov, or work in the domain portals directly - phytozome-next.jgi.doe.gov, mycocosm.jgi.doe.gov, img.jgi.doe.gov - which add comparative genomics, gene-family and pathway tools in the browser. Downloading files requires a free JGI account (ORCID sign-in), after which the portal issues direct download links or a curl-based bulk download script.

**Caveats.** Genuinely free but login-gated for downloads, and unpublished genomes fall under the JGI Data Utilization Policy, which asks that you contact the sequencing PI before publishing analyses of pre-publication data - a real constraint, not a formality. Annotation is JGI's own and can differ from the RefSeq record for the same organism. The portal interfaces are dated and large IMG/M queries are slow.

### [KEGG](https://www.kegg.jp/)

`Freemium` · beginner 4/5 · pathway, genome and compound database

Release 119.0 (1 July 2026): 587 reference pathway maps, 28,439 KEGG Orthology (KO) groups, 19,626 compounds and 67,775,989 genes across 11,949 organisms, plus BRITE functional hierarchies, KEGG MODULE, and the drug and disease databases.

**Access.** Free web browsing at kegg.jp and genome.jp. REST API needs no key: `curl https://rest.kegg.jp/get/hsa04110` (pathway record), `curl https://rest.kegg.jp/link/pathway/hsa` (gene-to-pathway table), `curl https://rest.kegg.jp/conv/hsa/uniprot:P04637` (ID mapping). Annotate a new genome with BlastKOALA/GhostKOALA (free web submission); map a gene list with KEGG Mapper. R: `BiocManager::install('KEGGREST')`.

**Caveats.** KEGG is privately owned by Kanehisa Laboratories and is explicitly not a public or publicly funded database. Academic web and REST access is free for individual research, but bulk FTP requires a paid academic subscription, offering any KEGG-based service requires an academic service-provider licence, and all non-academic use requires a commercial licence. That rules KEGG out of most redistributable pipelines and of any commercial work - use Reactome (CC0) or MetaCyc where licensing matters.

### [MetaboLights](https://www.ebi.ac.uk/metabolights/)

`Free` · beginner 3/5 · metabolomics repository

EMBL-EBI's open repository for metabolomics experiments, holding raw MS and NMR instrument files alongside ISA-Tab study metadata, protocols and compound annotations. The public study listing returned 3,344 MTBLS accessions in August 2026.

**Access.** Search and browse at ebi.ac.uk/metabolights with no account; each study has a stable MTBLS accession. Bulk download over FTP from https://ftp.ebi.ac.uk/pub/databases/metabolights/studies/public/ (one directory per study), or via the REST API - `curl https://www.ebi.ac.uk/metabolights/ws/studies` lists every public accession and `https://www.ebi.ac.uk/metabolights/ws/studies/MTBLS1` returns a single study. Depositing data needs a free submitter account.

**Caveats.** Datasets submitted from April 2025 are released under CC0; older studies fall under the EBI terms of use, so check the licence per study before redistributing. Raw files are vendor-native formats and a single study can be tens of gigabytes, so plan storage and conversion (msconvert, nmrglue) before downloading. Submitters can hold a study private under embargo, so a dataset cited in a paper is not always downloadable yet, and metadata depth varies a lot between submissions.

### [MGnify](https://www.ebi.ac.uk/metagenomics)

`Free` · beginner 3/5 · metagenomics analysis archive

EMBL-EBI's metagenomics resource: 5,203 studies and 635,107 analyses processed through standardised taxonomic and functional pipelines, plus 19 biome-level genome catalogues holding 56,782 non-redundant prokaryotic genomes (human gut, marine, soil, chicken gut, honeybee gut and others) and the MGnify protein database built from them.

**Access.** Browse and search at ebi.ac.uk/metagenomics. Open REST API, no key: `curl 'https://www.ebi.ac.uk/metagenomics/api/v1/studies?page_size=25'`, `/analyses/{accession}/taxonomy`, `/genome-catalogues`. Genome catalogues, protein sets and per-analysis results also sit on FTP at ftp.ebi.ac.uk/pub/databases/metagenomics/. Free browser-based example notebooks run on the MGnify Notebook Server.

**Caveats.** Reading and downloading are open; submitting raw data goes through ENA with a free Webin account, and analysis requests are queued rather than instant. Analyses are labelled with the pipeline version that produced them - comparing results across pipeline versions is not valid, and taxonomic assignments shift when the reference catalogue is updated. MAG catalogues are dereplicated at 95% ANI, so strain-level questions need the raw reads.

### [Movebank](https://www.movebank.org/)

`Free (registration), email` · beginner 3/5 · animal tracking / biologging data

Free animal movement database hosted by the Max Planck Institute of Animal Behavior: 11.3 billion location records and 9.4 billion additional sensor measurements across 10,095 studies, 1,963 species and 5,263 data contributors. Includes the Env-DATA service that annotates tracks with matched environmental covariates.

**Access.** Free account, then browse or download studies through the web interface. Programmatic access via the Movebank REST API (https://www.movebank.org/movebank/service/direct-read) or the R packages `move2`/`move`, which authenticate with your Movebank credentials. Archived, permanently citable datasets live in the Movebank Data Repository with DOIs.

**Caveats.** Availability is set per study by the data owner: many studies are fully open, many require you to request permission from the owner, and some expose metadata only. Env-DATA annotation jobs are queued and can take hours for large tracks. Deployment metadata (tag type, attachment, duty cycle) is essential context and is not always complete.

### [NCBI ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/)

`Free` · beginner 4/5 · clinical variant interpretation archive

Public archive of submitted relationships between human sequence variants and phenotypes: 4,560,228 variation records indexed in Entrez as of 23 August 2026, each carrying submitter-level clinical significance, a 0-4 star review status, condition terms (MedGen/OMIM/MONDO) and links to the supporting evidence and submitting laboratory.

**Access.** Web search by gene, HGVS expression, rsID or filtered query (`BRCA1[gene] AND "pathogenic"[Clinical significance]`). Programmatic via E-utilities with `db=clinvar`. Bulk: monthly and weekly VCFs for GRCh37 and GRCh38, full ClinVarVCVRelease XML, and the flat `variant_summary.txt.gz` table at https://ftp.ncbi.nlm.nih.gov/pub/clinvar/. Ensembl VEP and ANNOVAR both consume the VCF directly.

**Caveats.** NCBI archives submissions rather than adjudicating them: conflicting interpretations of the same variant are common, so filter on review status and prefer expert-panel or practice-guideline records over single-submitter ones. Absence from ClinVar is not evidence of benignity. Records exist against both GRCh37 and GRCh38 coordinates and silently mixing assemblies is a frequent, serious error. Not a diagnostic resource and not a substitute for clinical genetics.

### [NCBI GenBank and RefSeq](https://www.ncbi.nlm.nih.gov/genbank/)

`Free` · beginner 4/5 · nucleotide and protein sequence archive

GenBank release 273.0 (15 August 2026) holds 267,383,895 traditional annotated sequences totalling 8.24 trillion bases, plus set-based WGS/TSA/TLS divisions of 6,409,108,932 sequences and 51.8 trillion bases. The curated RefSeq companion (release 236, 6 July 2026) contains 629,953,391 accessions of non-redundant genomic, transcript and protein records.

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

### [Open Tree of Life](https://tree.opentreeoflife.org/)

`Free` · beginner 3/5 · synthetic phylogeny and reference taxonomy

A synthetic tree of life assembled from curated published phylogenies grafted onto a reference taxonomy (OTT). The API reports synthesis release opentree16.1, built 2025-12-20, with 2,385,875 tips drawn from 1,931 source studies and 2,064 source trees.

**Access.** Browse and search the tree at tree.opentreeoflife.org. Open REST API at api.opentreeoflife.org with no key - e.g. `curl -X POST https://api.opentreeoflife.org/v3/tree_of_life/about -H 'content-type: application/json' -d '{}'`, plus endpoints for TNRS name matching, induced subtrees, MRCA and the taxonomy. Synthesis and taxonomy releases are archived as downloadable, DOI-citable files linked from the site; R users have `install.packages("rotl")` on CRAN. Curating or adding trees needs a GitHub login.

**Caveats.** The synthesis is only as good as its inputs: large parts of the tree rest on taxonomy rather than a published phylogeny, the synthetic tree carries no branch lengths, and conflict between source trees has to be read from the node annotations rather than assumed away. Name matching through TNRS is the usual failure point - homonyms and unmatched names silently shrink an induced subtree, so check the returned OTT ids. Fine for a backbone or a taxon-sampling scaffold; not a substitute for estimating your own tree when the question is about one clade.

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

### [Reactome](https://reactome.org/)

`Free` · beginner 4/5 · pathway database

Manually curated, peer-reviewed pathway knowledgebase. Release 97 contains 2,883 human pathways and 16,423 human reactions, extended by orthology inference across 96 species to 23,604 pathways and 95,780 reaction-like events in total. All data are CC0.

**Access.** Interactive Pathway Browser at reactome.org; paste a gene, protein or expression table into Analysis Tools for over-representation or expression overlay. REST with no key: `curl https://reactome.org/ContentService/data/query/R-HSA-68886` and the AnalysisService for enrichment. Bulk SBML, BioPAX, SBGN, PSI-MITAB and identifier-mapping files at https://reactome.org/download-data. R: `BiocManager::install('ReactomePA')`.

**Caveats.** The licence is the reason to prefer Reactome over KEGG for anything redistributable: data are CC0 (illustrations CC BY 4.0, code Apache 2.0), so commercial and derivative use is unrestricted. Most non-human pathways are computationally inferred from human curation rather than independently curated - treat them as hypotheses. Coverage is deep for signalling, metabolism and immune processes and thinner elsewhere.

### [STRING](https://string-db.org/)

`Free` · beginner 5/5 · protein-protein interaction networks

Database of known and predicted protein-protein associations covering 59,309,604 proteins from 12,535 organisms (10,756 bacteria, 1,322 eukaryotes, 457 archaea), with each association scored per evidence channel: experiments, curated databases, co-expression, neighbourhood, gene fusion, co-occurrence and text mining.

**Access.** Paste a protein or gene list at string-db.org for an interactive network with built-in functional enrichment. REST with no key: `curl 'https://string-db.org/api/tsv/network?identifiers=TP53%0dMDM2%0dEGFR&species=9606'`; also /api/tsv/enrichment and /api/image/network_image. Per-organism protein.links.v12.txt.gz and protein.info files on the Download page. Cytoscape users install the stringApp.

**Caveats.** CC BY 4.0, free for academic and commercial use. Scores are confidence in a functional association, not evidence of physical binding or of direction - a 0.9 edge can rest entirely on text mining, so inspect the channel breakdown before interpreting. STRING asks that the API be used for occasional queries only; take the flat files for systematic work. Predicted-channel edges are transferred between organisms and inflate networks for poorly studied species.

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

### [VEuPathDB](https://veupathdb.org/)

`Free` · beginner 3/5 · eukaryotic pathogen, vector and host genomics

Umbrella resource for eukaryotic pathogens and their vectors, made up of PlasmoDB, ToxoDB, CryptoDB, TriTrypDB, FungiDB, VectorBase, AmoebaDB, GiardiaDB, MicrosporidiaDB, PiroplasmaDB, TrichDB, SchistoDB, HostDB and OrthoMCL, plus ClinEpiDB and MicrobiomeDB. Each site joins genome sequence and annotation to transcriptomics, proteomics, phenotype, and population-genetic datasets behind one search-strategy interface.

**Access.** Work directly in any component site (plasmodb.org, vectorbase.org, tritrypdb.org and so on). The search-strategy builder lets you intersect queries - for example genes upregulated in a life stage AND carrying a predicted signal peptide - without writing code, and export the resulting gene list. Bulk FASTA, GFF and annotation files come from each site's Download section; JBrowse and OrthoMCL cover browsing and orthology.

**Caveats.** Browsing, searching and file downloads need no account, but the documented web-service endpoints now reject anonymous calls with 'Valid API Key required for this endpoint' - an API key comes from a free VEuPathDB account profile page. Saving or sharing strategies also needs the account. Some datasets are pre-publication and carry data-use restrictions stated on the dataset page. The sites are JavaScript-heavy and slow over poor connections.

## Software

### [antiSMASH](https://antismash.secondarymetabolites.org/)

`Free` · beginner 3/5 · biosynthetic gene cluster detection

Web server and standalone pipeline that scans a genome for secondary-metabolite biosynthetic gene clusters and reports cluster type, core enzymes, domain architecture and predicted chemistry; version 8.0 was published in the 2025 Nucleic Acids Research web-server issue. Separate servers cover bacteria, fungi (fungiSMASH) and plants (plantiSMASH), and precomputed clusters for public genomes sit in the antiSMASH database.

**Access.** Upload a GenBank/EMBL/FASTA genome at antismash.secondarymetabolites.org - no account, results by job URL with optional e-mail notification. Local install through Bioconda: `conda create -n antismash antismash && conda activate antismash && download-antismash-databases`, or the Docker wrapper script from dl.secondarymetabolites.org. Precomputed results: https://antismash-db.secondarymetabolites.org/.

**Caveats.** The site states antiSMASH is free for everyone, including commercial use, but the public server is a shared queue and the FAQ says result files are deleted within about a month - download the output archive. Full runs with the optional comparative analyses (ClusterBlast, KnownClusterBlast, MIBiG comparison) take hours per genome; batch work belongs on a local install, which needs the reference databases (tens of GB) plus HMMER, DIAMOND, BLAST+ and Prodigal. The code is AGPL-3.0, so a derived web service must publish its source. Cluster boundaries and predicted products are hypotheses that still need chemistry to confirm.

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

### [g:Profiler](https://biit.cs.ut.ee/gprofiler/)

`Free` · beginner 5/5 · functional enrichment and ID conversion

Web server and API for gene-list enrichment (g:GOSt) over GO, KEGG, Reactome, WikiPathways, TRANSFAC, miRTarBase, Human Protein Atlas, CORUM and HPO across 400+ species from Ensembl and Ensembl Genomes; current data version e114_eg62_p19, updated 20 March 2026. Also provides ID conversion (g:Convert), orthology mapping (g:Orth) and SNP-to-gene mapping (g:SNPense).

**Access.** Paste a gene list at https://biit.cs.ut.ee/gprofiler/gost. Programmatic with no key: POST JSON to https://biit.cs.ut.ee/gprofiler/api/gost/profile/. R: `install.packages('gprofiler2')` then `gost(query = genes, organism = 'hsapiens')`. Python: `pip install gprofiler-official`.

**Caveats.** Archived data versions stay queryable, which is the honest way to reproduce an older analysis - record the version string in your methods. The default multiple-testing correction is g:SCS rather than Benjamini-Hochberg, so results are not directly comparable with DAVID or Enrichr; state which you used. Leaving the statistical background at the default (all annotated genes) rather than your assayed gene set is the single most common way to get misleading enrichment.

### [IQ-TREE](https://iqtree.github.io/)

`Free` · beginner 3/5 · phylogenetic inference

Maximum-likelihood phylogenetics; IQ-TREE 3 (v3.1.3, released 19 June 2026) is the current line, with ModelFinder automatic substitution-model selection, ultrafast bootstrap approximation, SH-aLRT branch support, partitioned and mixture models, and topology tests - fast enough for genome-scale alignments on a desktop. The IQ-TREE 2 series ended at v2.4.0 (February 2025).

**Access.** `conda install -c bioconda iqtree` (the bioconda package currently resolves to 3.1.3), or download a dependency-free static binary for Windows/macOS/Linux. Standard run: `iqtree3 -s alignment.fa -m MFP -B 1000 -alrt 1000 -T AUTO`, which picks a model, runs 1000 ultrafast bootstraps and chooses a thread count. Also available as a free web server at iqtree.org.

**Caveats.** GPL-2. Ultrafast bootstrap values are not on the same scale as standard bootstrap - 95% is the usual threshold, and mixing the two in one figure legend is a common error. Alignment quality dominates the result; pair with MAFFT and a trimming step. Large partitioned analyses can still take days.

### [MEGA (Molecular Evolutionary Genetics Analysis)](https://www.megasoftware.net/)

`Free, email` · beginner 4/5 · phylogenetics desktop suite

Desktop suite for sequence alignment, distance estimation, phylogenetic tree building (maximum likelihood, neighbour-joining, minimum evolution, parsimony), timetree calibration and tests of selection, built around a point-and-click interface for people who do not work at a shell. MEGA 12 is current and the site reports over 4.3 million lifetime downloads.

**Access.** Installers for Windows, macOS, Ubuntu/Debian and RedHat/Fedora at megasoftware.net/download, in two builds: MEGA-GUI for interactive work and MEGA-CC for scripted, batch and pipeline use. The download page asks for name, institution and how MEGA will be used before giving the file; no account or password is created. Source for the computational core is on GitHub (KumarMEGALab/MEGA-source-code) under the GPL.

**Caveats.** Free for research and education but not open source as a whole: the end-user agreement forbids redistributing the binaries, so every user must download their own copy (only the computational core is GPL). Analyses run on your own desktop, so large ML searches or heavy bootstrapping on hundreds of taxa are better done with IQ-TREE or RAxML on a server. MEGA 12 on Linux requires glibc 2.34 or newer, which rules out older distributions.

### [napari](https://napari.org/)

`Free` · beginner 3/5 · n-dimensional image viewer for Python

Fast multi-dimensional image viewer and annotation tool for Python (v0.9.0, BSD-3-Clause), built directly on NumPy/Dask arrays with layer types for images, labels, points, shapes, surfaces, vectors and tracks, 2D and 3D rendering, and a plugin ecosystem (napari-hub) covering readers, segmentation and registration.

**Access.** `pip install 'napari[all]'` (or `conda install -c conda-forge napari pyqt`), then `import napari; viewer = napari.view_image(arr); napari.run()`, or `napari image.tif` from the shell. A standalone bundled application is also published. Works inside Jupyter, and pairs naturally with scikit-image, cellpose and dask for stacks larger than memory.

**Caveats.** BSD-3-Clause and a NumFOCUS project, but still pre-1.0: the viewer and plugin APIs change between minor versions, so pin the version in any published analysis. It is a viewer and manual-annotation tool, not a batch pipeline - inspect and label here, then run processing in a script. Qt-based, so it needs a real desktop session; running it on a headless cluster over X-forwarding is painful.

### [NCBI BLAST](https://blast.ncbi.nlm.nih.gov/)

`Free` · beginner 5/5 · sequence similarity search

The default first move for any unknown sequence: blastn, blastp, blastx, tblastn, PSI-BLAST and DELTA-BLAST run against NCBI's nr/nt, RefSeq, Swiss-Prot, PDB, 16S rRNA and WGS databases, either on NCBI's own servers through the browser and URL API or locally with the BLAST+ command-line suite and preformatted database volumes.

**Access.** Web at blast.ncbi.nlm.nih.gov. URL API in two calls: POST/GET `https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Put&PROGRAM=blastp&DATABASE=nr&QUERY=<sequence>&email=you@example.com` returns an RID, then `...?CMD=Get&RID=<rid>&FORMAT_TYPE=Text`. Local: `conda install -c bioconda blast`, then `makeblastdb -in ref.fa -dbtype nucl` and `blastn -query q.fa -db ref.fa -outfmt 6 -evalue 1e-5`; fetch preformatted databases with `update_blastdb.pl --decompress nt`.

**Caveats.** NCBI's developer guidance for the URL API is explicit: do not contact the server more often than once every 10 seconds, do not poll a single RID more often than once a minute, and always pass the `email` and `tool` parameters so NCBI can contact you. Scripted bulk searching belongs on a local install - nr and nt are hundreds of gigabytes decompressed. E-value depends on database size, so scores from the web nr and from a small local database are not comparable.

### [Nextflow and nf-core](https://nf-co.re/)

`Free` · beginner 3/5 · workflow engine and curated pipelines

Nextflow (v26.04.6, 9 July 2026) is a dataflow workflow engine with built-in container support and resume; nf-core is the community collection of 156 listed pipelines built on it, of which 101 have at least one tagged release and the remainder are still in development - the released set includes rnaseq, sarek, mag, ampliseq, chipseq and scrnaseq.

**Access.** `curl -s https://get.nextflow.io | bash` (needs Java 17+), then `nextflow run nf-core/rnaseq -profile test,docker --outdir results` to verify the whole stack on a tiny dataset. Each pipeline documents its parameters and samplesheet format; `-resume` restarts from the last successful step.

**Caveats.** Apache 2.0 and fully runnable locally with Docker or Apptainer, but realistic genome-scale runs of pipelines like sarek need tens of gigabytes of RAM - plan on a shared cluster or cloud. Reference genome assets (iGenomes) are large; specify only what you need. Free training with a ready-made Codespaces environment is at https://training.nextflow.io/.

### [Nextstrain](https://nextstrain.org/)

`Free` · beginner 4/5 · genomic epidemiology and pathogen phylodynamics

Open platform for real-time pathogen phylogenetics: continuously rebuilt public analyses for SARS-CoV-2, seasonal and avian influenza (including H5N1), measles, mpox, Ebola, RSV, dengue, Zika, rabies, tuberculosis, Yersinia pestis and HIV, built on Augur (analysis CLI) and Auspice (interactive tree, map and mutation viewer). All code is AGPL-licensed.

**Access.** Explore any build in the browser at nextstrain.org with no account. Drag your own Auspice JSON onto auspice.us to view it locally without uploading. Build your own: `conda install -c bioconda augur auspice` or `pip install nextstrain-cli`, clone a pathogen repo from github.com/nextstrain and run `nextstrain build .`. Nextclade (clade assignment, mutation calling and QC for your own sequences) runs entirely in the browser at https://clades.nextstrain.org.

**Caveats.** The software and the public builds are free, but the underlying sequence data are not always redistributable - GISAID-derived builds can only publish derived data, so reproducing them end to end requires your own GISAID access. A full build on a large pathogen dataset needs tens of gigabytes of RAM and hours of CPU; use the subsampled example configs first. Trees invite over-interpretation of transmission direction; treat inferred ancestral locations as uncertainty-laden.

### [QIIME 2](https://qiime2.org/)

`Free` · beginner 3/5 · microbiome / amplicon analysis platform

Plugin-based microbiome multi-omics platform covering amplicon (16S/18S/ITS) and shotgun metagenome analysis, with automatic decentralised provenance recorded inside every artifact so any result can be traced back to the exact commands and parameters that made it. Cited over 65,000 times.

**Access.** Install a distribution (amplicon, metagenome or tiny) from the environment files at docs.qiime2.org via conda/mamba, then run e.g. `qiime dada2 denoise-paired ...`. Also usable through Galaxy with no install, and through the Python API (`import qiime2`) inside Jupyter. Visualisations (.qzv) open in the browser at https://view.qiime2.org without installing anything.

**Caveats.** BSD-3. Releases are dated (e.g. 2025.x) and the distributions were split apart in 2024, so instructions referring to a single monolithic `qiime2` environment are obsolete. DADA2 denoising is the memory bottleneck - a few hundred samples can exceed 16 GB. Reference classifiers (SILVA, GREENGENES2) are multi-gigabyte downloads.

### [QuPath](https://qupath.github.io/)

`Free` · beginner 4/5 · whole-slide and digital pathology image analysis

Open-source (GPL) desktop application, version 0.7.0, purpose-built for whole-slide and highly multiplexed images: cell and nucleus detection, positive-cell scoring and H-score, tissue and object classification with built-in machine learning, TMA dearraying, stain deconvolution, and Groovy scripting to apply one pipeline across a whole project of slides.

**Access.** Download the installer for Windows, macOS (Intel and Apple silicon) or Linux from qupath.github.io - no account, no licence key. Usual first pass: open a slide, draw an annotation, Analyze > Cell detection, then Classify > Object classification; then Automate > Script editor and 'Run for project' to batch every slide. Reads Bio-Formats and OME-Zarr; extensions wrap StarDist, Cellpose and InstanSeg, and it interoperates with Fiji.

**Caveats.** The project states explicitly that QuPath is not intended for clinical, diagnostic or therapeutic purposes. Whole-slide images are gigabytes each; raise the maximum memory in Edit > Preferences before working with multiplexed stacks or expect out-of-memory errors. Detection and classification parameters are stain-, scanner- and cohort-specific and do not transfer without retuning, so always report the exact parameters and version.

*Also listed under: medicine.*

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

Python-based workflow manager (v9.26.1, August 2026) using rules with input/output file patterns, with automatic dependency resolution, per-rule conda environments and containers, checkpointing, and executor plugins for SLURM, cloud and Kubernetes.

**Access.** `pip install snakemake` or `conda install -c bioconda snakemake`. Write a `Snakefile` of rules, then `snakemake --cores 4 --software-deployment-method conda`. The Snakemake Workflow Catalog (https://snakemake.github.io/snakemake-workflow-catalog/) lists reusable published workflows.

**Caveats.** MIT licensed. The CLI changed substantially at v8 (executor plugins replaced `--cluster`, `--use-conda` became `--software-deployment-method conda`), so pre-v8 tutorials will not run as written - check the version before copying commands. Python familiarity helps; Nextflow suits people who prefer channels over file-pattern rules.

### [UCSF ChimeraX](https://www.cgl.ucsf.edu/chimerax/)

`Free` · beginner 3/5 · molecular structure visualisation and analysis

Successor to Chimera for visualising and analysing molecular structures, cryo-EM density maps, AlphaFold predictions (with built-in pLDDT and PAE colouring), sequence-structure alignment and publication-quality rendering, driven by a command language and a Python API.

**Access.** Download builds for Windows/macOS/Linux after accepting the non-commercial licence agreement. Fetch structures by accession without leaving the app: `open 1cbs` for the PDB, `open P00520 from alphafold` for AlphaFold DB. Script with ChimeraX commands in a .cxc file or Python via `runscript`.

**Caveats.** Free of charge for non-commercial use only - you must agree to the UCSF ChimeraX Non-Commercial Licence before downloading, and commercial use requires a separate paid licence priced by user count. Rendering large cryo-EM maps benefits from a discrete GPU. Open-source PyMOL is the main alternative where a non-commercial restriction is a problem.

## Literature

### [Bio-protocol](https://bio-protocol.org/)

`Free` · beginner 5/5 · peer-reviewed protocols journal

Peer-reviewed open-access protocol journal (Volume 16 in 2026) publishing step-by-step life-science methods with full reagent and equipment tables, timing, troubleshooting and validation notes; articles are indexed in PubMed and PMC, and many are commissioned from the methods sections of recently published papers so the protocol is linked to a real, working result.

**Access.** Read and download any protocol at bio-protocol.org with no account, browsing by subject area, by issue, or from the source publication. Authors submit through the journal's own portal; some protocols are invited by editors from published papers, and the site also hosts Bio-101 introductory methods and preprint-linked protocol collections.

**Caveats.** Free to read, but not automatically free to publish in: the journal lists article processing charges that vary by track, so confirm the current fee and any waiver before submitting. Protocols are validated by peer review, not by independent replication, so treat them as a well-documented starting point rather than a guarantee. Complements protocols.io: Bio-protocol is a citable journal with editorial screening, protocols.io is a versioned, forkable working repository.

### [bioRxiv](https://www.biorxiv.org/)

`Free` · beginner 5/5 · preprint server

The preprint server for biology, covering all biological subject areas and receiving on the order of ten million views a month; roughly a hundred new preprints appear on a typical weekday. Since 11 March 2025 it has been operated by openRxiv, a purpose-built non-profit that also runs medRxiv.

**Access.** Read and download PDFs and full text with no account. Public metadata API: `curl 'https://api.biorxiv.org/details/biorxiv/2026-08-01/2026-08-02'` returns titles, authors, DOIs and categories. Posting needs a free account and passes a basic screen, not peer review. Full-text and supplementary bulk corpora sit in an AWS S3 requester-pays bucket.

**Caveats.** Reading is entirely free; the S3 text-and-data-mining corpus is requester-pays, so bulk downloads incur AWS charges you pay. Author-chosen licences vary (CC BY, CC BY-NC-ND, or 'no reuse' by default), which constrains text mining. Preprints are screened, not reviewed. openRxiv Labs began running interactive-reading experiments in 2026, so the reading interface may change.

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

### [SWISS-MODEL](https://swissmodel.expasy.org/)

`Free` · beginner 4/5 · protein homology modelling server

SIB's free automated template-based (homology) modelling server: submit a sequence, it searches the SWISS-MODEL Template Library, builds models and returns GMQE and per-residue QMEANDisCo quality estimates. The companion Repository holds 3,776,284 precomputed models plus 242,908 mapped PDB structures covering 13 core reference proteomes.

**Access.** Paste a sequence at https://swissmodel.expasy.org/interactive and start a job; an anonymous run returns a project link, and a free account adds a persistent workspace, manual template selection, alignment mode and oligomeric-state modelling. Repository entries are fetchable by UniProt accession, e.g. https://swissmodel.expasy.org/repository/uniprot/P00520.json, and the whole repository is downloadable per proteome.

**Caveats.** Template-based, so it simply fails where no homologous structure exists - AlphaFold DB is the better first stop for a single monomer. SWISS-MODEL still earns its place for homo-oligomers, for models that keep a template's ligands and cofactors, and for modelling a specific conformational state by choosing the template yourself. Read GMQE and QMEANDisCo before using a model; jobs queue, and very long sequences can time out.

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

**Caveats.** Reading is always free. Fees without a waiver are substantial and vary far more than a single range suggests: PLOS ONE $1,852-$2,477, PLOS Climate/Global Public Health/Mental Health/Water $2,596, PLOS Neglected Tropical Diseases $2,670, the standard tier (Computational Biology, Genetics, Pathogens, Digital Health, Ecosystems, Aging and Health, Complex Systems) $3,165, and the Community Action Publishing titles $3,150-$5,500 (Biology), $3,400 (Sustainability and Transformation) and $6,460 (Medicine). The waiver route is the entire point for this audience, and it must be requested at submission, which authors routinely miss. 'No external funding' is a real condition: grant-funded authors in eligible countries may not qualify.

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
