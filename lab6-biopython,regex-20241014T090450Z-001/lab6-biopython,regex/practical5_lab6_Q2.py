'''
Use Biopython module for biological sequence analysis

Author - Ishani Jayasekara
Date - 15/03/2023
'''

# read fasta file and create seq_record object
from Bio import SeqIO

seq_record = SeqIO.read("ATderb2a.fasta", "fasta")
print(seq_record.id)
print(seq_record.description)
print(seq_record.seq)
print(len(seq_record.seq))

# run web-based blast
from Bio.Blast import NCBIWWW
#
# result = NCBIWWW.qblast("blastn", "nt", seq_record.seq)
#
# # store blast output
# with open("ATdreb2_blast.xml", "w") as output:
#     output.write(result.read())
# result.close()

# parse blast output
from Bio.Blast import NCBIXML

result = open("ATdreb2_blast.xml")
blast_records = NCBIXML.read(result)

# filter the blast hits using e values
e_value_threshold = 0.05

for alignment in blast_records.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < e_value_threshold:
            print(alignment.title)
            print(alignment.length)
            print(hsp.expect)
            print(hsp.query)
            print(hsp.sbjct)
            print(hsp)

# search ABRE elements in blast hits using regular expression
import re

search_pattern = "[CT]ACGT[GT]C"
count = 0
for alignment in blast_records.alignments:
    for hsp in alignment.hsps:
        match = re.search(search_pattern, hsp.sbjct)
        if match:
            print(match.group())
            print(match.span())
            count += 1

print(count)
