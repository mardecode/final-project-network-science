import os 
import json
import pickle
import glob
from helper import *

hastags = [
  'castilloterrorista',
  'castillonomerepresenta',
  'castillonova',
  'castillopresidente',
  'castillopresidente2021',
  'comunismonuncamas',
  'debatepresidencial2021',
  'despiertaperu',
  'eleccionesbicentenario',
  'eleccionesperu2021',
  'fueracomunistas',
  'fuerzapopular',
  'fujimorinuncamas',
  'fujirata',
  'fujitroll',
  'keikocorrupta',
  'keikofujimori',
  'keikonova',
  'keikopresidenta',
  'keikopresidenta2021',
  'keikopresidente',
  'kenyi',
  'larutadekeiko',
  'miedoqueganecastillo',
  'mivotoesporcastillo',
  'nikeikonipedro',
  'noacastillo',
  'noakeiko',
  'noalcomunismo',
  'nocastillo',
  'nokeiko',
  'nulo',
  'pedrocastillo',
  'pedrocastillocomunista',
  'pedrocastillonicagando',
  'pedrocastillopresidente2021',
  'perulibre',
  'perulibredecorruptos',
  'peruvotainformado',
  'peruzuela',
  'petercastle',
  'politicaperu',
  'politicaperuana',
  'pontelacamisetaperu',
  'segundavuelta',
  'segundavuelta2021',
  'tuvotoespoder',
  'vamoskeikopresidenta2021',
  'veronikomendoza',
  'vivalademocraciaenperu',
  'voto2021',
  'votoblanco',
  'votoenblanco',
  'votonulo',
  'votoviciado',
  'willaxtv'
]


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
      for item in dic:
        dic_videos[item['id']] = {
          'createTime':item['createTime'],
          'idUser':item['author']['id'],
          'nickname': item['author']['nickname'],
          'stats':item['stats'],
          'hashtags':[ { 'id': itemcha['id'], 'title': itemcha['title']} for itemcha in item['challenges']]
        }
    except:
      print('Error reading file !',filex)
  return dic_videos

dic_videos = getVideos()  
createPickle('dic_videos.pk',dic_videos)

# dic_videos = getPickle('dic_videos.pk')
# print(toJson(dic_videos))


