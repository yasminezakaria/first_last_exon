# first_last_exon
Computational Modeling in Systems Genetics project
## Motivation
Detection of aberrant expression and aberrant splicing has been used in diagnostics of rare disorders as it can reveal loss-of-function variants missed or not prioritized by DNA analyses, and provide functional validation for candidate variants [1,2]. Specialized statistical methods to detect aberrant expression (OUTRIDER [3]) and splicing (FRASER [4]) have been developed. OUTRIDER works at the gene level and FRASER on introns, thus possibly not being able to capture aberrations in the first and last exons. Transcript differences are predominantly driven by alternative first, internal, and last exons. Standard genomic annotations tend to be rather inclusive and contain exons that are not necessarily expressed. A novel pipeline called HIT (hybrid-internal-terminal) [5] was recently developed to classify exons depending on their isoform-specific usage, thus providing reliable annotations for the first and last expressed exons. The main goal of this project is to identify those exons in the GEUVADIS dataset and find the aberrantly expressed ones. One possibility would be to run OUTRIDER and another to use the HIT index. Follow-up analyses include determining whether there is an added value with respect to gene-level annotations and computing the enrichment of rare loss of function variants among the outliers.
## Goals
1. obtain an annotation of the first and last exons for each gene from RNA-seq data
2. detect aberrant usage of first and last exons by either applying OUTRIDER or fitting the HIT index
3. conclude whether there is an added value in focusing on those exons instead of using the whole gene
## Data
1. RNA-seq data of unaffected controls
2. Genomic data of the same samples to benchmark
## Work steps
1. download 1 bam file from: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-GEUV-1 
2. apply the HIT index pipeline [5] to the RNA-seq data to define the first, internal and last exons
3. verify a handful of called exons by visualizing them in IGV
4. Generate 2 gtf files, one containing the first and one containing the last exons
5. apply OUTRIDER [3] to detect expression outliers in the RNA-seq data on the first and last exons, and on the full gene body. Alternatively, decide whether fitting the HIT index itself would be a better metric.
6. follow up on results, e.g., compare the detected outliers at the exonic level with the gene level.
7. [optional depending on the time] benchmark your approach by computing the recall of rare loss-of-function variants against simply taking the first and last exon from a standard annotation file (e.g. from GENCODE [7])

## Available code
1. OUTRIDER: https://github.com/gagneurlab/outrider
2. HIT index: https://github.com/thepailab/HITindex
## References
1. Kremer et al. Genetic diagnosis of Mendelian disorders via RNA sequencing. Nat Commun 8, 15824. (2017)
2. Yepez et al. Clinical implementation of RNA sequencing for Mendelian disease diagnostics. Genome Med 14, 38. (2022)
3. Brechtmann et al. OUTRIDER: A Statistical Method for Detecting Aberrantly Expressed Genes in RNA Sequencing Data. The American Journal of Human Genetics, doi: 10.1016/j.ajhg.2018.10.025 (2018)
4. Mertes et al. (2021). Detection of aberrant splicing events in RNA-seq data using FRASER. Nat Commun, 12, 529 (2021)
5. Fiszbein et al., Widespread occurrence of hybrid internal-terminal exons in human transcriptomes. Sci. Adv. 8, eabk1752 (2022)
6. Lappalainen et al, Transcriptome and genome sequencing uncover functional variation in humans. Nature 501 (2013)
7. https://www.gencodegenes.org/human/release_42.html

