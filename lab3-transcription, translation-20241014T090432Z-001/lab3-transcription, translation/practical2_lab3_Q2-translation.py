'''
Algorithm to translate given mRNA sequence
Input - mRNA in fasta file
Ouput- translated amino acid sequence in fasta file

Author - Ishani Jayasekara
Date - 7/2/2023
'''

# create the codon table dictionary
codon_table = {}
with open("codon_table.txt","r") as file:
    for line in file:
        if (line[0] != "#") and (line != "\n"):
            codon = line.strip().split("\t")[0]
            codon_table[codon] = line.strip().split("\t")[2]

# read the mRNA file
sequence = ""
translated = ""
trans_dict = {}
with open("OSDREB1A_transcribed.fasta","r") as mRNA_file:
    for line in mRNA_file:
        if line[0] == ">":
            header = line.strip()

        elif line != "\n":
            sequence += line.strip()

    # translate mRNA sequence while reading codon by codon
    stop_codons = ["UAG", "UAA", "UGA"]
    count = 0
    while count < len(sequence):
        codon = sequence[count:count+3]
        # stop the translation when stop codon is encountered
        if codon in stop_codons:
            break
        translated += codon_table[codon]
        trans_dict[header] = translated
        count += 3

# write translated amino acid into a new fasta file
with open("OSDREB1A_protein", "w") as new_file:
    new_file.writelines([header, "\n", trans_dict[header]])

# print the length of resulted amino acid sequence
print(len(translated))
