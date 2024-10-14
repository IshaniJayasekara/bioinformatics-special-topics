'''
Analyse protein sequence and record the statistics in a separate fasta file
Input - Protein sequence in fasta format
Output - Protetin statistics in text file

Author - Ishani Jayasekara
Date - 2/4/2023
'''

from Bio import SeqIO
from Bio.SeqUtils import ProtParam

input_file = "aa_seq.fasta"

# read and create amino acid sequence record
aa_seq_record = SeqIO.read(input_file, "fasta")
aa_seq = aa_seq_record.seq.replace("*", "")

aa_seq_length = len(aa_seq)

# create protein analysis object
protein_parameters = ProtParam.ProteinAnalysis(aa_seq)

# analyze protein sequence
alanine_percentage = protein_parameters.get_amino_acids_percent()["A"]*100
glycine_percentage = protein_parameters.get_amino_acids_percent()["G"]*100
aa_molecular_weight = protein_parameters.molecular_weight()

# store the statistical details in a separate text file
with open("aa_stats.txt", "w") as file:
 file.write("Sequence Length : " + str(aa_seq_length) + "\nMolecular Weight : " +
str(aa_molecular_weight) +
 "\nAlanine Percemtage : " + str(alanine_percentage) + "\nGlycine Percentage : " + str(glycine_percentage))