'''
Algorithm to get the length of a given DNA sequence in fasta format
Input - DNA sequence in fasta file
Ouput – length of the sequence

Author - Ishani Jayasekara
Date - 5/3/2023
'''


sequence = ""

# open the file and read line by line
with open("brca1.fasta") as file:
    for line in file:
        # select the lines except empty line and header line
        if (line != "\n") and (line[0] != ">"):
            # remove unknown characters add line into the sequence string
            sequence += line.strip()

    # print the count as length
    length = len(sequence)
    print(length)

