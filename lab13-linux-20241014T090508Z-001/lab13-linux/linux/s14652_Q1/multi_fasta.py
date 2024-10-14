'''
Retrieve multiple sequence records as separate fasta files
Input - list of accession numbers
Output - separate fasta files each one having single fasta record

Author - Ishani Jayasekara
Date - 2/4/2023
'''

from Bio import Entrez

# input id list
id_list = ["AAK43967", "AED90870", "NP_567720", "AAK59861"]

# get genbank record for each accession
for id in id_list:

    result = Entrez.efetch(db="protein", id=id, rettype="fasta")

    # output the fasta file of each genbank record
    file_name = str(id) + ".fasta"
    with open(file_name, "w") as file:
        file.write(result.read())
    result.close()
