'''
Algorithm to get the degree of a given protein using graph data structure
Input - tsv file with data
Output - degree of protein

Author - Ishani Jayasekara
Date - 2/3/2023
'''

# load the package
import networkx as nx

# create an empty graph
G = nx.Graph()

target_protein = "ERF24"
counter = 0

# using tsv file add interactions to the empty graphs
with open("string_interactions_short .tsv", "r") as file:
    for line in file.readlines()[2:]:
        line = line.strip().split("\t")
        combined_score = line[-1]
        G.add_weighted_edges_from([(line[0], line[1], combined_score)])

        # check the weighted scores more than 0.7 for neighbors of target protein
        if (float(line[-1]) > 0.7) and (line[0] == target_protein or line[1] == target_protein):
            counter += 1

print("The degree of the target protein :", G.degree(target_protein))
print("The number of neighbors with more than 0.7 combined score :", counter)

# get the neighbors of the target protein
neighbors_dic = G[target_protein]
neighbors = []
for key, values in neighbors_dic.items():
    neighbors += [key]

# get the degree of the target protein
degree_of_protein = len(neighbors) # using hard code
print(degree_of_protein)
print(G.degree(target_protein)) # using built-in function

# get neighbors with weighted scores more than 0.7
filtered_neighbors = []
for key, value in neighbors_dic.items():
    for head, score in value.items():
        if float(score) > 0.7:
            filtered_neighbors += [key]

# print(filtered_neighbors)
degree_of_filtered_neighbors = len(filtered_neighbors)
print(degree_of_filtered_neighbors)
