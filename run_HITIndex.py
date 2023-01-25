import sys
sys.path.append('../HITindex/hitindex')
import os
import subprocess
import HITindex_classify_mainfn as hitmain


class args:
    def __init__(self, junctionReads, bam, juncbam, readstrand, HITindex, bed, classify, calculatePSI, outname):
        self.junctionReads = junctionReads
        self.bam = bam
        self.juncbam = juncbam
        self.readstrand = readstrand
        self.HITindex = HITindex
        self.bed = bed
        self.classify = classify
        self.calculatePSI = calculatePSI
        self.outname = outname
        self.readtype = 'paired'
        self.overlap = 10
        self.readnum = 2
        self.parameters = "HIT_identity_parameters.txt"
        self.bootstrap = 1000
        self.edge  = False
        
        
        
        
datafolder_path = "/s/project/first_last_exon/Data/input_data/rna-seq/"
output_folder_path = "/s/project/first_last_exon/Data/output_data/HITindex/rna_seq/step_2/chr_files"
computed_files = [f for f in os.listdir(output_folder_path) if f.endswith(".exon")]
bed_file_path = "/s/project/first_last_exon/Data/output_data/HITindex/rna_seq/step_1/metaexons.bed_ss3-50ss5-20.buffer"
bam_files_list = [f for f in os.listdir(datafolder_path) if f.endswith("_chr1.bam")]
print(len(bam_files_list), "files detected")

print("Number of computed files: ", len(computed_files))

for i, f in enumerate(bam_files_list):
    sample_name = f.split("_chr1.bam")[0]
    if not sample_name + "_HITindex.exon" in computed_files:
        junctionReads = True
        bam = os.path.join(datafolder_path, f)
        juncbam = os.path.join(output_folder_path, sample_name + ".junctions.bam") 
        readstrand = "fr-unstrand"
        HITindex = True
        bed = bed_file_path 
        classify = True
        calculatePSI = True
        outname = os.path.join(output_folder_path, sample_name + "_HITindex")
        arguments = args(junctionReads, bam, juncbam, readstrand, HITindex, bed, classify, calculatePSI, outname)
        print("Computing sample: {}, {}/{}".format(sample_name, i+1, len(bam_files_list)))
        hitmain.main(arguments)
        print("Sample {} is done!".format(sample_name))