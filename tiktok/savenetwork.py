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
'''
En caso requiera ver como es la data descomentar el print 
correr el archivo de la siguiente manera: 
python3 savenetwork.py > dic_network.json
'''
# print(toJson(dic_network)) 


G = nx.DiGraph()

stop = 0
stopp = 20
users = []
for id_user,dic_user in dic_network.items():
  print(id_user)
  users.append(id_user)
  if(stop==stopp):
    break
  for hashtag,rep in dic_user.items():
    G.add_edge(id_user,hashtag,weight=rep)
  # stop +=1
  

# # G.add_edge(1, 2,weight=0)
# # G.add_edge(1, 3,weight=1)
# # G.add_edge(1, 4,weight=2)
# # G.add_edge(1, 5,weight=3)
# # G.add_edge(1, 6,weight=4)


# # nx.draw(G, with_labels=True)

# print(G.nodes)

 
# pos = nx.bipartite_layout(G,nodes=users)
# # c = bipartite.color(G)

# # weights = [G[u][v]['weight'] for u,v in G.edges()]
# print("nodos",len(G.nodes))
# print('links',len(G.edges))


# nx.draw(G,pos=pos,with_labels=True,width=0.5)

# # nx.draw_networkx_nodes(G,pos=pos)
# # nx.draw_networkx_edges(G,pos=pos,width=weights)
# # nx.draw_networkx_labels(G, pos=pos)

# plt.show()