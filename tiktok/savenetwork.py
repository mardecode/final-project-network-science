from helper import *
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
from networkx.algorithms import bipartite 


dic_videos = getPickle('dic_videos.pk')
# En caso requiera ver como es la data
# print(toJson(dic_videos))  #python3 savenetwork.py > dic_videos.json


'''
dic_network guarda diccionario de los usuarios con los hashtags que utilizo, cada hashtag tiene un numero dependiendo cuantas veces se repitio. 
Si desea ver dic_network ver el archivo dic_network.json, en caso no se encuentre el archivo descomentar el print despues del for 
'''

def allRepeticiones(dic_videos):
  dic_network = {}
  for key in dic_videos:
    item = dic_videos[key]
    
    id_user = item['nickname'] 
    
    if id_user in dic_network:
      for hashtag in item['hashtags']:
        title = hashtag['title']
        if title in dic_network[id_user]:
          dic_network[id_user][title] += 1
        else:
          dic_network[id_user][title] = 1
          
    else:
      dic_network[id_user] = {}
      for hashtag in item['hashtags']:
        title = hashtag['title']
        if title in dic_network[id_user]:
          dic_network[id_user][title] += 1
        else:
          dic_network[id_user][title] = 1
  return dic_network

def weeks (dic_videos,date1,date2):
  week_network = {}

  for key in dic_videos:
    item = dic_videos[key]
    
    id_user = item['nickname'] 
    if item["date"]>=date1 and item["date"]<=date2:
      if id_user in week_network:
        
        for hashtag in item['hashtags']:
          title = hashtag['title']
          if title in week_network[id_user]:
            week_network[id_user][title] += 1
          else:
            week_network[id_user][title] = 1
            
      else:
        week_network[id_user] = {}
        for hashtag in item['hashtags']:
          title = hashtag['title']
          if title in week_network[id_user]:
            week_network[id_user][title] += 1
          else:
            week_network[id_user][title] = 1
  return week_network

def weeksXfollowers (dic_videos,date1,date2):
  week_network = {}

  for key in dic_videos:
    item = dic_videos[key]
    
    id_user = item['nickname'] 
    if item["date"]>=date1 and item["date"]<=date2:
      if id_user in week_network:
        
        for hashtag in item['hashtags']:
          title = hashtag['title']
          if title in week_network[id_user]:
            week_network[id_user][title] = item["followers"]
          else:
            week_network[id_user][title] = item["followers"]
            
      else:
        week_network[id_user] = {}
        for hashtag in item['hashtags']:
          title = hashtag['title']
          if title in week_network[id_user]:
            week_network[id_user][title] = item["followers"]
          else:
            week_network[id_user][title] = item["followers"]
  return week_network
'''
En caso requiera ver como es la data descomentar el print 
correr el archivo de la siguiente manera: 
python3 savenetwork.py > all_network.json
'''
# dic_network = allRepeticiones(dic_videos)
dic_network = weeksXfollowers(dic_videos,1619067600,1722869200) #all weeks 
# dic_network = weeksXfollowers(dic_videos,1619067600,1619931600) #week 1
# dic_network = weeksXfollowers(dic_videos,1620018000,1620968400) #week 2
# dic_network = weeksXfollowers(dic_videos,1621054800,1622005200) #week 3
# dic_network = weeksXfollowers(dic_videos,1622091600,1622869200) #week 4
# print(toJson(dic_network)) 



G = nx.Graph()

createid = 0
users = []
for id_user,dic_user in dic_network.items():
  createid +=1
  users.append(createid)

  for hashtag,rep in dic_user.items():
    # G.add_edge(createid,hashtag,weight=rep)
    G.add_edge(createid,hashtag)

X, Y = nx.bipartite.sets(G)
pos = dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) ) 
pos.update( (n, (2, i)) for i, n in enumerate(Y) ) 

userG =bipartite.projected_graph(G,X)
hashtagG =bipartite.projected_graph(G,Y)

# nx.write_gexf(G, "graphs/all_x_repeticiones.gexf")
# nx.write_gexf(userG, "graphs/u_x_repeticiones.gexf")
# nx.write_gexf(G, "graphs/week4_x_followers.gexf")
# nx.write_gexf(hashtagG, "graphs/hweek4_x_followers.gexf")

degreeDistribution(G)

# print(len(G.nodes))
# print(len(hashtagG.nodes))
# print(len(hashtagG.edges))



assortativity = round(nx.degree_assortativity_coefficient(G),2)
print("Assortativity coefficient: ", assortativity)