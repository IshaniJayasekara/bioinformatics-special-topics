#!/bin/bash

# create intermediate files and output directories
mkdir intermediate_files output

# Retrieve CDS sequence and create fasta file
python3 cds_seq_retrieve.py

# Transcribe CDS sequence and create fasta file
python3 transcribe.py

# Translate mRNA sequence and create fasta file
python3 translate.py

# Analyze protein sequence and save details in a text file
python3 aa_seq_analyze.py

# move files into intermediate directory
mv cds_seq.fasta mRNA_seq.fasta aa_seq.fasta intermediate_files/

# move final output into output directory
mv aa_stats.txt output/