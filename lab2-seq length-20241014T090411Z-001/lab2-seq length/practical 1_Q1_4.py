'''
Algorithm to get the length of a given DNA sequence in fasta format
Input - DNA sequence in fasta file
Ouput – length of the sequence

Author - Ishani Jayasekara
Date - 5/3/2023
'''


counter = 0
sequence = ""

# open the file and read line by line
with open("brca1.fasta") as file:
    for line in file:
        # select the lines except header and empty lines
        if (line != "\n") and (line[0] != ">"):
            # remove unknown characters add line into the sequence string
            sequence += line.strip()

    # get the length of the sequence
    for base in sequence:
        counter += 1

print(counter)


