# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:57:32 2021

@author: W10
"""

import networkx as nx
from networkx.algorithms import bipartite
import re
import matplotlib.pyplot as plt
import numpy as np
import collections
import math
from sklearn.linear_model import LinearRegression


nameFile = ['twitterData/twitterEdgesWeek1.txt']
nameFile2= 'data_week.txt'
nameFigDegree = "images/Bipartite_DegreeDistributionWeek.png"
nameFigDegree1= "images/Hashtag_DegreeDistributionWeek.png"
nameFigDegree2= "images/User_DegreeDistributionWeek.png"
nameGEX = "gephi/Bipartite_graphWeek.gexf"
nameGEX1= "gephi/Hashtag_graphWeek.gexf"
nameGEX2= "gephi/User_graphWeek.gexf"

saveData = open(nameFile2, 'w')

edgesFinal = []
for i in range(len(nameFile)):
    EdgesFile = open(nameFile[i], 'r', encoding='utf-8')
    
    
    edges = [sub.replace('\n', '') for sub in list(EdgesFile)]
    
    for ed in edges:
        edgesFinal.append(re.split(r'\t+', ed.rstrip('\t')))

edgesFinal = np.array(edgesFinal)

B = nx.Graph()
# Add nodes with the node attribute "bipartite"
nodes_hash = list(edgesFinal[:,0])
nodes_user = list(edgesFinal[:,1])
B.add_nodes_from(list(edgesFinal[:,0]), bipartite='hashtags')
B.add_nodes_from(list(edgesFinal[:,1]), bipartite='users')


for nodes in edgesFinal:
    B.add_edge(nodes[0], nodes[1], weight=nodes[2])


top_nodes = set(n for n,d in B.nodes(data=True) if d['bipartite']=='users')
bottom_nodes = set(B) - top_nodes


B1_hash = bipartite.projected_graph(B, nodes_hash)
#B2_user = bipartite.projected_graph(B, nodes_user)


N = B.number_of_nodes()
L = B.number_of_edges()
print("Number of nodes: ", N)
print("Number of edges: ", L)

saveData.write("Number of Nodes: " + str(N) + "\n")

print("Number of nodes Project Hash: ", B1_hash.number_of_nodes())
saveData.write("Number of Nodes Hash: " + str(B1_hash.number_of_nodes()) + "\n")
#saveData.write("Number of Nodes User: " + str(B2_user.number_of_nodes()))

saveData.write("Number of Edges: " + str(L) + "\n")
print("Number of edges Project Hash: ", B1_hash.number_of_edges())
saveData.write("Number of Edges Hash: " + str(B1_hash.number_of_edges()) + "\n")
#saveData.write("Number of Edges User: " + str(B2_user.number_of_edges()))



nx.write_gexf(B, nameGEX)
nx.write_gexf(B1_hash, nameGEX1)
#nx.write_gexf(B2_user, nameGEX2)


##############################################################
#                  DEGREE DISTRIBUTION                       #
##############################################################

degP, degH = bipartite.degrees(B, nodes_hash)
degree_sequenceP = sorted([d for n, d in degP], reverse=True)  # degree sequence
degree_sequenceH = sorted([d for n, d in degH], reverse=True)  # degree sequence

degreeCountP = collections.Counter(degree_sequenceP)
degP, cntP = zip(*degreeCountP.items())

degreeCountH = collections.Counter(degree_sequenceH)
degH, cntH = zip(*degreeCountH.items())

degree_sequence = []
degree_seq = []
degree_sequence.append(degree_sequenceP)
degree_sequence.append(degree_sequenceH)
for i in range(len(degree_sequence)):
  for j in range(len(degree_sequence[i])):
    degree_seq.append(degree_sequence[i][j])
degree_sequence = sorted(degree_seq, reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig = plt.figure(figsize=(16,6))

ax = fig.add_subplot(1, 3, 1)
ax.plot(deg, np.array(list(cnt))/len(B.nodes), 'bo')
#ax.bar(deg, np.array(list(cnt))/len(B.nodes), width=0.80, color="b")
ax.set_title("Degree Distribution of Graph Bipartite")
ax.set_ylabel("Pk")
ax.set_xlabel("k")
ax.set_yscale('log')
ax.set_xscale('log')

ax = fig.add_subplot(1, 3, 2)
ax.plot(degP, np.array(list(cntP))/len(nodes_hash), 'bo')
#ax.bar(degP, np.array(list(cntP))/len(nodes_hash), width=0.80, color="b")
ax.set_title("Degree Distribution of Graph Bipartite Hash_tags")
ax.set_ylabel("Pk")
ax.set_xlabel("k")
ax.set_yscale('log')
ax.set_xscale('log')

ax = fig.add_subplot(1, 3, 3)
ax.plot(degH, np.array(list(cntH))/len(nodes_user), 'bo')
#ax.bar(degH, np.array(list(cntH))/len(nodes_user), width=0.80, color="b")
ax.set_title("Degree Distribution of Graph Bipartite User")
ax.set_ylabel("Pk")
ax.set_xlabel("k")
ax.set_yscale('log')
ax.set_xscale('log')

plt.savefig(nameFigDegree)

##############################################################
#                   AVERAGE DEGREE                           #
##############################################################

degP, degH = bipartite.degrees(B, nodes_hash)
degree_sequenceP = sorted([d for n, d in degP], reverse=True)  # degree sequence
average = np.sum(np.array(degree_sequenceP)) / len(nodes_hash)
print("Average Degree: ", average)
saveData.write("Gamma: " + str(average) + "\n")


##############################################################
#                         GAMMA                              #
##############################################################

Pk = np.array(list(cnt))/len(B.nodes)
domain = range(len(Pk))

#Complementary accumulative distribution function (CCDF)
CCDF = [sum(Pk[k:]) for k in domain]
logkdata = []
logFdata = []
prevF = CCDF[0]
for k in domain:
  F = CCDF[k]
  if F != prevF:
    logkdata.append(math.log(k))
    logFdata.append(math.log(F))
    prevF = F
    
#Regression Linear with sklearn
regressor = LinearRegression()
logkdata = np.array(logkdata)
regressor.fit(logkdata.reshape(len(logkdata), 1), logFdata)
slope = regressor.coef_[0]
intercept = regressor.intercept_
gamma = -(slope-1)
print("gamma: ", gamma)
saveData.write("Gamma: " + str(gamma) + "\n")



##############################################################
#                   NUMBER COMPONENTS                        #
##############################################################

nx.is_connected(B)
components = [len(c) for c in sorted(nx.connected_components(B), key=len, reverse=True)]

largest_cc = max(nx.connected_components(B), key=len)
print("Number of components: ", nx.number_connected_components(B))
saveData.write("Number of Components: " + str(nx.number_connected_components(B)) + "\n")


from networkx.algorithms import bipartite
coeff_clustering = bipartite.average_clustering(B)
print("Average Coefficient Clustering: ", coeff_clustering)
saveData.write("Average Coefficient Clustering: " + str(coeff_clustering) + "\n")


from networkx.algorithms import community
partition = list(community.asyn_lpa_communities(B))
print("Number of Communities: ", len(partition))
saveData.write("Number of Communities: " + str(len(partition)) )

assorciativyCoeff  = nx.degree_assortativity_coefficient(B)
print("Assorciativity Coefficient: ", assorciativyCoeff)
saveData.write("Assorciativity Coefficient: " + str(assorciativyCoeff) )