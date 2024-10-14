'''
Drug-target prediction in a PPI network using Common Neighbor Algorithm
Input - DTI network in tsv file
Output - CN scores of newly predicted drug-target interactions

Author - Ishani Jayasekara
Date - 2/4/2023
'''

import networkx as nx
import collections

G = nx.Graph()

# create bipartite graph for DTI network
drug_set = set()
protein_set = set()
interactions = list()
with open("DTIsubset.tsv", "r")as file:
    for line in file.readlines()[1:]:
        line = line.strip().split("\t")
        drug_set.add(line[0])
        protein_set.add(line[1])
        interactions.append([line[0], line[1]])

G.add_nodes_from(drug_set, bipartite=0)
G.add_nodes_from(protein_set, bipartite=1)
G.add_edges_from(interactions)

# predict new drug-protein interactions
predicted_interactions = {}

for drug in drug_set:
    neighbors_of_drug = set(G[drug]) # set of proteins

    for protein in protein_set:
        # find new interactions by filtering non-neighbor proteins of the drug
        if not protein in neighbors_of_drug:

            new_interaction = (drug, protein)

            complementary_neighbors_of_proteins = [] # set of proteins
            for drug_neighbor in set(G[protein]):
                complementary_neighbors_of_proteins += G[drug_neighbor]

            # common neighbor algorithm
            common_neighbors = set(complementary_neighbors_of_proteins).intersection(neighbors_of_drug)
            cn_score = len(common_neighbors)

            if not cn_score == 0:
                predicted_interactions[new_interaction] = cn_score

# sorted cn_scores in ascending order
predicted_interactions_sorted = collections.OrderedDict(sorted(predicted_interactions.items(), key= lambda item:item[1], reverse=True))

# output the newly predicted drug-target interactions
with open("new_predicions", "w")as file:
    file.write("#drug\tprotein\tcn_score\n")
    for key, value in predicted_interactions_sorted.items():
        file.write("{}\t{}\t{}\n".format(key[0], key[1], value))
