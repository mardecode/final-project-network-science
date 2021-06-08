# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:57:32 2021

@author: W10
"""

import networkx as nx
from networkx.algorithms import bipartite
import re
import matplotlib.pyplot as plt


EdgesFile = open('twitterData/twitterEdges.txt', 'r', encoding='utf-8')
NodesHashTagFile = open('twitterData/twitterNodesHashTag.txt', 'r', encoding='utf-8')
NodesUsersFile = open('twitterData/twitterNodesUser.txt', 'r', encoding='utf-8')

hashTags = [sub.replace('\n', '') for sub in list(NodesHashTagFile)]
users = [sub.replace('\n', '') for sub in list(NodesUsersFile)]
edges = [sub.replace('\n', '') for sub in list(EdgesFile)]

edgesFinal = []
for ed in edges:
    edgesFinal.append(re.split(r'\t+', ed.rstrip('\t')))

#print([re.split(r'\t+', p.rstrip('\t')) for p in [sub.replaces('\n', '') for sub in list(EdgesFile)]])

B = nx.Graph()
# Add nodes with the node attribute "bipartite"
B.add_nodes_from(hashTags, bipartite='hashtags')
B.add_nodes_from(users, bipartite='users')


for nodes in edgesFinal:
    B.add_edge(nodes[0], nodes[1])


#print(B.nodes(data=True)) 

N = B.number_of_nodes()
L = B.number_of_edges()
print("Number of nodes: ", N)
print("Number of edges: ", L)

top_nodes = set(n for n,d in B.nodes(data=True) if d['bipartite']=='users')
bottom_nodes = set(B) - top_nodes

#nx.write_gexf(B, "twitterData/Tgraph.gexf")
#my_matching = bipartite.matching.hopcroft_karp_matching(B, users)

nodeColor = []

for i in range(len(bottom_nodes)):
    nodeColor.append('blue')

for i in range(len(top_nodes)):
    nodeColor.append('green')
    
   
#top = top_nodes
#pos = nx.bipartite_layout(B, top)
#nx.draw(B, pos=pos, font_size=8, alpha=0.8, with_labels=True, node_color=nodeColor)
#plt.show()