# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:08:00 2021

@author: W10
"""

import json
import os
from unidecode import unidecode

def finddataTest(pathDir):
    dataTest = []
    dataTest1= []
    for _, _, arquivo in os.walk(pathDir):
        dataTest += arquivo 
    
    for data in dataTest:
        if data.find('.txt') == -1:
            dataTest1.append(pathDir + "/" + data)
    
    return dataTest1


NodesHashTagFile = open('twitterData/twitterNodesHashTag1.txt', 'w', encoding='utf-8')
NodesUsersFile = open('twitterData/twitterNodesUser1.txt', 'w', encoding='utf-8')

def addNodesEdges(dict_, dicUser_, path):    
    with open(path) as data_file:
        #print(data_file)
        data = json.load(data_file)
        
    for i in range(len(data["data"])):
        #u1 = data["data"][i]["user"]["id"];
        u1 = data["data"][i]["user"]["id"];
        u2 = data["data"][i]["user"]["followers_count"]
        u3 = data["data"][i]["entities"]["hashtags"]
        #u4 = data["data"][i]["favorite_count"]
        #u5 = data["data"][i]["created_at"]
        
        for j in range(len(u3)):
            uu3 = unidecode(u3[j]["text"].casefold())
            
            if not( uu3 in dict_):
                NodesHashTagFile.write(uu3 + "\n")
                dict_[uu3] = []
                
            if not( u1 in dicUser_):
                NodesUsersFile.write(str(u1) + "\n")
        
            dict_[uu3].append(u1)
            dicUser_[u1] = u2
            
            

paths = finddataTest('twitterData/Peru/Semana1/')

dictHashTagUser = {}
dictUserFollower = {}

minPaths = 0
maxPaths = len(paths)

for i in range(minPaths, maxPaths):
    addNodesEdges(dictHashTagUser, dictUserFollower, paths[i])


print("Users:", len(dictUserFollower))
print("HashTags: ", len(dictHashTagUser))

number_Items = 0

EdgesFile = open('twitterData/twitterEdges1.txt', 'w', encoding='utf-8')

for k, v in dictHashTagUser.items():
    if isinstance(v, list):
        number_Items += len(v)
        for j in range(len(v)):
            EdgesFile.write(k + "\t" + str(v[j]) + "\t" + str(dictUserFollower[v[j]]) + "\n")


print("Number of Nodes: ", len(dictHashTagUser) + len(dictUserFollower))
print("Number of Edges: ", number_Items)

NodesHashTagFile.close()
NodesUsersFile.close()
EdgesFile.close()    
   
