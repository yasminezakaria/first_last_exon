# first_last_exon
Computational Modeling in Systems Genetics project
## Motivation
Detection of aberrant expression and aberrant splicing has been used in diagnostics of rare disorders as it can reveal loss-of-function variants missed or not prioritized by DNA analyses, and provide functional validation for candidate variants. Specialized statistical methods to detect aberrant expression (OUTRIDER [https://github.com/gagneurlab/outrider]). OUTRIDER works at the gene level and FRASER on introns, thus possibly not being able to capture aberrations in the first and last exons. Transcript differences are predominantly driven by alternative first, internal, and last exons. Standard genomic annotations tend to be rather inclusive and contain exons that are not necessarily expressed. A novel pipeline called HIT (hybrid-internal-terminal) [https://github.com/thepailab/HITindex] was recently developed to classify exons depending on their isoform-specific usage, thus providing reliable annotations for the first and last expressed exons. The main goal of this project is to identify those exons in the GEUVADIS dataset and find the aberrantly expressed ones. One possibility would be to run OUTRIDER and another to use the HIT index. Follow-up analyses include determining whether there is an added value with respect to gene-level annotations and computing the enrichment of rare loss of function variants among the outliers.

## Goals
1. obtain an annotation of the first and last exons for each gene from RNA-seq data
2. detect aberrant usage of first and last exons by applying OUTRIDER

## Data
1. GEUVADIS dataset

## Content
This repo contains the processing scripts used to run the experiment
1. hitindex_annotate.ipynb -> contains functions used to run the firt step of HITindex pipline, which annotates metaexons from a gtf file by collapsing overlapping consituent exons.
2. hitindex_classify.py -> contains functions used to run the last step of HITindex pipline, which calculates HIT index metrics and classify metaexons into one of 5 exon-types: first, first-internal, internal, internal-last, and last exons.
3. merge_multiprocessing.py -> contains merging logic of the output of HITindex for all samples which creates a gtf annotation file (multi-processing was used for faster performance as the output of HITindex is a bit large for all samples)
4. Visualization.ipynb -> contains some plotting functions
5. create_sample_annot.ipynb -> contains script used to create `sample annotations` table which is provided as input to run DROP

## Results
Results can be found in the project report [https://drive.google.com/file/d/1k_b-WpeVq29PX1420Qi7_qoKFTrNKp3R/view?usp=share_link]

