'''
Transcribe coding sequence and store in a separate fasta file
Input - Coding sequence fasta file
Output - Transcribed sequence in fasta file

Author - Ishani Jayasekara
Date - 2/4/2023
'''

from Bio import SeqIO

input_file = "cds_seq.fasta"

# read the cds fasta file using SeqIO
cds_seq_record = SeqIO.read(input_file, "fasta")

# transcribe the sequence
transcribed_seq = cds_seq_record.seq.transcribe()

# create sequence record object for transcribed object
transcribed_seq_record = SeqIO.SeqRecord(transcribed_seq,id= cds_seq_record.id, description= cds_seq_record.description+ "_transcribed")

# output fasta file with transcribed sequence
with open("mRNA_seq.fasta", "w")as file:
    SeqIO.write(transcribed_seq_record, file, "fasta")