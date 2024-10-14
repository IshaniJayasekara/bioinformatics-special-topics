'''
Implementation of object creating using Sequence and its subclasses
Input - multi-fasta file
Output - sequence objects

Author - Ishani Jayasekara
Date - 8/2/2023
'''

# import classes
from practical3_lab4_Q2 import Sequence
from practical4_lab5_Q1 import DNAseq, MRNAseq, ProteinSeq

# create sequence dictionary
fasta_file = "OSDREB_sequences.fasta"
seq_dict = Sequence.fasta_split(fasta_file)
print(seq_dict)

# object creation
values = seq_dict['DREB1A_P']
DREB1A_P = ProteinSeq(values[-1], values[1], values[0], values[2], values[3], values[-2], values[-3])

values = seq_dict['DREB1A_CDS']
DREB1A_CDS = DNAseq(values[-1], values[1], values[0], values[2], values[3])

values = seq_dict['DREB1B_P']
DREB1B_P = ProteinSeq(values[-1], values[1], values[0], values[2], values[3], values[-2], values[-3])

values = seq_dict['DREB1B_CDS']
DREB1B_CDS = DNAseq(values[-1], values[1], values[0], values[2], values[3])

values = seq_dict['DREB2A_P']
DREB2A_P = ProteinSeq(values[-1], values[1], values[0], values[2], values[3], values[-2], values[-3])

values = seq_dict['DREB2A_CDS']
DREB2A_CDS = DNAseq(values[-1], values[1], values[0], values[2], values[3])

values = seq_dict['DREB2B_P']
DREB2B_P = ProteinSeq(values[-1], values[1], values[0], values[2], values[3], values[-2], values[-3])

values = seq_dict['DREB2B_CDS']
DREB2B_CDS = DNAseq(values[-1], values[1], values[0], values[2], values[3])

# DREB1A DNA sequence details
DREB1A_CDS.sequence_length = len(DREB1A_CDS.sequence)
DREB1A_CDS.get_seq_type()
DREB1A_CDS.get_AT_content()
print("Gene id :", DREB1A_CDS.gene_id, "\nSequence length :", DREB1A_CDS.sequence_length,
      "\nSequence type :", DREB1A_CDS.sequence_type, "\nAT_content :", DREB1A_CDS.AT_content)

# transcribe DREB2B coding sequence
DREB2B_CDS.transcribed_seq = DREB2B_CDS.transcribe_sequence()

# create mRNA object
DREB2B_mRNA = MRNAseq(DREB2B_CDS.transcribed_seq, DREB2B_CDS.gene_id, DREB2B_CDS.gene_name, DREB2B_CDS.species_name,
                      DREB2B_CDS.subspecies_name)
DREB2B_mRNA.sequence_length = len(DREB2B_mRNA.sequence)
DREB2B_mRNA.get_seq_type()
DREB2B_mRNA.get_AT_content()
print("Sequence length : ", DREB2B_mRNA.sequence_length, "\nSequence type : ",DREB2B_mRNA.sequence_type,
      "\nSequence : ",DREB2B_mRNA.sequence, "\nAT content : ",DREB2B_mRNA.AT_content)

# translate mRNA sequence
text_file = "codon_table.txt"
codon_dict = MRNAseq.upload_codons(text_file)
DREB2B_mRNA.translated_seq = DREB2B_mRNA.translate_sequence()
print("Translated_sequence : ",DREB2B_mRNA.translated_seq, "\nLength : ",len(DREB2B_mRNA.translated_seq))

# DREB2A protein details
DREB2A_P.get_seq_type()
DREB2A_P.get_hydrophibicity()
Amino_acid_composition = DREB2A_P.get_character_count()
print("Uniprot id :", DREB2A_P.uniprot_id,"\nReviewed status :", DREB2A_P.reviewed_status,
      "\nSequence type : ", DREB2A_P.sequence_type, "\nHydrophobicity : ",DREB2A_P.hydrophobicity)

print(Sequence.Sequence_count)

fasta_file = "OSDREB_sequences.fasta"
seq_dic = Sequence.fasta_split(fasta_file)
print(seq_dic)


objects_dic = {}
for key, value in seq_dic.items():
    amino_acid_list = ["K", "N", "R", "S", "I", "M", "Q", "H", "P", "L", "E", "D", "V", "Y", "W", "F"]
    if any(aa in value[-1] for aa in amino_acid_list):
        objects_dic[key] = ProteinSeq(value[-1], value[1], value[0], value[2], value[3], value[5], value[4])
    elif "T" in value[-1]:
        objects_dic[key] = DNAseq(value[-1], value[1], value[0], value[2], value[3])
    elif "U" in value[-1]:
        objects_dic[key] = MRNAseq(value[-1], value[1], value[0], value[2], value[3])


print(objects_dic)

for gene_name, object in objects_dic.items():
    globals()[gene_name] = object

print(DREB1A_CDS.get_seq_type())
print(DREB1A_CDS.sequence_length)
print(DREB1A_CDS.get_AT_content())

# transcribe DREB2B coding sequence
DREB2B_CDS.transcribed_sequence = DREB2B_CDS.transcribe_sequence()

print(Sequence.Sequence_count)