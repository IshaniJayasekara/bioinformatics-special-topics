'''
Translate mRNA sequence and store in a separate fasta file
Input - mRNA sequence in fasta file
Output - Amino acid sequence in fasta file

Author - Ishani Jayasekara
Date - 2/4/2023
'''

from Bio import SeqIO

input_file = "mRNA_seq.fasta"

# read mRNA sequence fasta file
mRNA_seq_record = SeqIO.read(input_file, "fasta")

# translate mRNA sequence
translated_seq = mRNA_seq_record.seq.translate()

# create sequence record for translated sequence
translated_seq_record = SeqIO.SeqRecord(translated_seq, id=mRNA_seq_record.id, description= mRNA_seq_record.description+ "_translated")

# output a separate fasta file with translated sequence
with open("aa_seq.fasta", "w")as file:
    SeqIO.write(translated_seq_record, file, "fasta")