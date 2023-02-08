# This scripts implements multi-processing for merging.ipynb logic

import os
import numpy as np
import pandas as pd
from multiprocessing import Process
from multiprocessing import Pool




def add_entry(dic, gene, exon, strand, exon_id, exon_type):
#     Add exon record
    chrom = exon.split(":")[0]
    print("chrom: ", chrom)
    dic["seqname"].append(chrom)
    dic["source"].append("hitindex")
    dic["feature"].append("exon")
    start, end = exon.split(":")[1].split("-")
    dic["start"].append(start)
    dic["end"].append(end)
    dic["score"].append(".")
    dic["strand"].append(strand)
    dic["frame"].append(".")
    dic["attribute"].append("gene_id "+ gene + "_" + str(exon_id) + "_" + exon_type + "; transcript_id " + gene + "_" + str(exon_id))
    
#     Add Gene record
    dic["seqname"].append(chrom)
    dic["source"].append("hitindex")
    dic["feature"].append("gene")
    start, end = exon.split(":")[1].split("-")
    dic["start"].append(start)
    dic["end"].append(end)
    dic["score"].append(".")
    dic["strand"].append(strand)
    dic["frame"].append(".")
    dic["attribute"].append("gene_id "+ gene + "_" + str(exon_id) + "_" + exon_type)
    
#     Add Transcript record
    dic["seqname"].append(chrom)
    dic["source"].append("hitindex")
    dic["feature"].append("transcript")
    start, end = exon.split(":")[1].split("-")
    dic["start"].append(start)
    dic["end"].append(end)
    dic["score"].append(".")
    dic["strand"].append(strand)
    dic["frame"].append(".")
    dic["attribute"].append("gene_id "+ gene + "_" + str(exon_id) + "_" + exon_type + "; transcript_id " + gene + "_" + str(exon_id))
            
def merge_gene_exons(gene):
#     function merges exons of a gene and saves the output to a gtf file
# adds 3 records per exons of 3 types [gene, exon, transcipt]
    gene_rows = merged_df[merged_df["gene"] == gene]    
    first_last_exons_merge_output = {
                "seqname": [],
               "source": [],
                "feature": [],
                "start": [],
                "end": [],
                "score": [],
                "strand": [],
                "frame": [],
                "attribute": []
    }
        
    strand = np.array(gene_rows["strand"])[0]
    exons_set = gene_rows["exon"].unique()
    for exon_id, exon in enumerate(exons_set):
        labels_set = gene_rows[gene_rows["exon"] == exon]["ID_position"].unique()
        first = False
        last = False
        for l in labels_set:
            if "first" in l.lower():
                first = True
            elif "last" in l.lower():
                last = True
        if first:
            add_entry(first_last_exons_merge_output, gene, exon, strand, exon_id, "first")
        if last:
            add_entry(first_last_exons_merge_output, gene, exon, strand, exon_id, "last")
    first_last_exons_merge_output_df = pd.DataFrame(first_last_exons_merge_output)
    first_last_exons_merge_output_df.to_csv("/data/nasif12/home_if12/afi/computationl_modeling/first_last_exon/gtfs/"+ gene + ".gtf", index=False, sep='\t', header=False)

if __name__ == "__main__":
    
    exon_files_dir = "/s/project/first_last_exon/Data/output_data/HITindex/rna_seq/step_2/whole_sample_files/" 
    exon_files = [f for f in os.listdir(exon_files_dir) if f.endswith(".exon") and not "reduced" in f]
    print("We have {} different .exon files".format(len(exon_files)))

    dataframes_ls = []
    for idx, f in enumerate(exon_files):
        df = pd.read_csv(os.path.join(exon_files_dir, f),  sep='\t')
        dataframes_ls.append(df)

    merged_df = pd.concat(dataframes_ls, sort=False)
    merged_df.head()


    genes_set = merged_df["gene"].unique()
    classes_labels_set = ["first", "FirstInternal_medium", "FirstInternal_high", "last", "InternalLast_medium", "InternalLast_high", "internal"]

    print("Total number of unique genes = {}".format(len(genes_set)))
    
    genes_np_list = np.array(genes_set)

#     check for unprocessed genes
    processed_genes = [f.split(".gtf")[0] for f in os.listdir("gtfs") if f.endswith(".gtf")]
    unprocessed_genes = [gene for gene in genes_np_list if not gene in processed_genes]
    print(len(processed_genes))
    print("unprocessed genes: ",len(unprocessed_genes))

#     Apply multi-processing for faster performance
    num_threads = 16

    p = Pool(num_threads)
    p.map(merge_gene_exons, unprocessed_genes)
    p.close()
    p.join()
    
    
    # Finally put all gtf records into one gtf file
    # Merge gtf files

    gtf_files_dir = "gtfs"
    gtf_files = [f for f in os.listdir(gtf_files_dir)  if f.endswith(".gtf")]
    print(len(gtf_files))
    with open("./whole_samples_first_last_exons_merge_output.gtf", 'w') as f:
        for gtf_file in gtf_files:
            with open(os.path.join(gtf_files_dir, gtf_file), "r") as gf:
                f.write("".join(gf.readlines()))