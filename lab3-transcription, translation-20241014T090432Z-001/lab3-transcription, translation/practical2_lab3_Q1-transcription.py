'''
Algorithm to differentiate mRNA and protein sequence followed by transcription of mRNA
Input - multi-fasta file with protein and mRNA sequences
Ouput - separate fasta file of transcribed mRNA

Author - Ishani Jayasekara
Date - 7/2/2023
'''

# define the dictionary
seq_dict = {}

# define the sequence string
sequence = ""

# open the file and read line by line
with open("OSDREB1A.fasta", "r") as file:
    for line in file:
        # assign header line
        if line[0]==">":
            header = line.strip()
            sequence = ""

        # assign sequence as value of header in seq dict
        elif line != "\n":
            sequence += line.strip()
            seq_dict[header] = sequence

# amino acid list
amino_acid_list = ["K", "N", "R","S", "I", "M", "Q", "H", "P", "L", "E", "D","V", "Y", "W","F"]

# transcribed dict
trans_dict = {}

# get dictionary items and check the amino acid or mRNA
for key, value in seq_dict.items():
    # check if at least one aa is not present in the sequence to differentiate mRNA
    if all(aa not in value for aa in amino_acid_list):
        transcribed = value.replace("T", "U")
        new_head = str(key+"_transcribed")
        trans_dict[new_head] = transcribed

        # write the transcribed sequence in a different file
        with open("OSDREB1A_transcribed.fasta", "w") as new_file:
            new_file.writelines([new_head,"\n", trans_dict[new_head]])
