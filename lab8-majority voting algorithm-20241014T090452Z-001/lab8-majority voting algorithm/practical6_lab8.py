'''
Implentation of majority voting algotihm to predict new protein functions
Input - tsv file with ppi network, function annotated protein file
Output - text file with majority voting scores

Auhtor - Ishani Jayasekara
Date - 02/04/2023
'''

import networkx as nx
import collections

G = nx.Graph()

# create ppi network
with open("string_interactions_short_pr8.tsv", "r")as file:
    for line in file:
        if not line.startswith("#") or line == "\n":
            line = line.strip().split("\t")
            G.add_edges_from([[line[0].upper(), line[1].upper()]])

# get the known protein list
AT_stress_proteins = set()
with open("AT_stress_proteins.txt", "r")as file:
    for line in file:
        if not line == "\n":
            protein = line.strip().split("\t")[1].upper()
            AT_stress_proteins.add(protein)

# majority voting algorithm
all_network_proteins = set(G.nodes)
unknown_proteins = all_network_proteins.difference(AT_stress_proteins)

voting_score_dic = {}
for protein in unknown_proteins:
    neighbors = set(G.neighbors(protein))
    known_neighbors = neighbors.intersection(AT_stress_proteins)
    majority_voting_score = len(known_neighbors)
    voting_score_dic[protein] = majority_voting_score

# sort the dictionary in ascending order
voting_score_dic_sorted = collections.OrderedDict(sorted(voting_score_dic.items(), key=lambda item: item[1], reverse=True))

# write voting scores into output text file
with open("voting-scores.txt", "w")as file:
    file.write("#protein\tvoting_score\n")
    for key, value in voting_score_dic_sorted.items():
        file.write("{}\t{}\n".format(key, value))



