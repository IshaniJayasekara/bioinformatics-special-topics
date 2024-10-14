'''
Retrieve genbank record for an input accession number from nucleotide database
Input - accession number from the user
Output - fasta file with the genebank record

Author - Ishani Jayasekara
Date - 2/4/2023
'''

from Bio import Entrez

# get the accession from the user
input_id = input("Please enter the accession number :", )

# retrieve genbank record
genbank_record = Entrez.efetch(db="nucleotide", id=input_id, rettype="fasta")

# output file with genbank record
with open("cds_seq.fasta", "w")as file:
    file.write(genbank_record.read())
genbank_record.close()