'''
Algorithm to get AT content for each sequence in the multi-fasta file
Input - multi-fasta file with protein and DNA sequences
Output - dictionary of AT content

Author - Ishani Jayseakara
Date - 8/2/2023
'''

# method to calculate AT_content
def get_AT_content(sequence):
    AT_count = 0
    for base in sequence:
        if (base == "A") or (base == "T"):
            AT_count += 1
    seq_len = len(sequence)
    AT_content = (AT_count/seq_len)*100
    return AT_content

# method to create sequence dictionary using multi-fasta file
def create_seq_dict(fasta_file):
    seq_dict = {}
    sequence = ""
    with open(fasta_file,"r") as file:
        for line in file:
            if line[0] == ">":
                header = line.strip()
                sequence = ""
            elif line != "\n":
                sequence += line.strip()
            seq_dict[header] = sequence
    return seq_dict

# method to get the sequence type
def get_sequence_type(sequence):
    Amino_acid_list = ["K", "N", "R","S", "I", "M", "Q", "H", "P", "L", "E", "D","V", "Y", "W","F"]
    if any(aa in sequence for aa in Amino_acid_list):
        sequence_type = "Protein"
    elif "T" in sequence:
        sequence_type = "DNA"
    else:
        sequence_type = "RNA"
    return sequence_type

# implementation
# get the dictionary of sequences using multi-fasta file
fasta_file = "OSDREB_sequences.fasta"
seq_dict = create_seq_dict(fasta_file)

# get AT content for each sequence in the multi fasta file
AT_content_dict = {}
for key, value in seq_dict.items():
    # check the sequence type
    seq_type = get_sequence_type(value)

    if seq_type == "DNA":
        AT_content = get_AT_content(value)
        AT_content_dict[key] = AT_content

print(AT_content_dict)