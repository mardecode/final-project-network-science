import os 
import json
import pickle
import glob
from helper import *



def checkUnicode(var):
  characters = "'!? _*"
  for x in range(len(characters)):
    var = var.replace(characters[x],"")

  var = var.replace('á','a')
  var = var.replace('é','e')
  var = var.replace('í','i')
  var = var.replace('ó','o')
  var = var.replace('ú','u')

  return var.encode('ascii', 'ignore').decode("utf-8")


files = glob.glob('data/**/*.json', recursive=True) #get path of files

#print path of files
'''
for filex in files:
  print(filex)
'''

def getVideos():
  dic_videos = {}
  for filex in files:
    dic = readFile(filex)
    try:
      print('reading '+filex)
      if('#' in filex):
        dic = dic["itemList"]
        # continue
      for item in dic:
        if item['createTime'] >=1619067600:
          dic_videos[item['id']] = {
            'createTime':item['createTime'],
            'idUser':item['author']['id'],
            'nickname': item['author']['nickname'],
            'stats':item['stats'],
            'hashtags':[ { 'id': itemcha['id'], 'title': checkUnicode(itemcha['title'])}   for itemcha in item['challenges']],
            'followers':item['authorStats']['followerCount'],
            'videolikes':item['stats']['diggCount'],
            'date':item['createTime'],
          }
    except:
      print('Error reading file !',filex)
  return dic_videos

dic_videos = getVideos()  
createPickle('dic_videos2.pk',dic_videos)


# print(checkUnicode("elecciones2021perú!!!____\ud83c\uddf5\ud83c\uddea"))
