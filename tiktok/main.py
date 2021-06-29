from typing import Tuple
from TikTokAPI import TikTokAPI
import os 
import json
import pickle

def toJson(var):
  return json.dumps(var,indent=4)

cookie = {
  "s_v_web_id": "verify_kpesr1fz_iAc046WF_wgy1_4B7k_BSKv_WoCGvcZd0hvS",
  "tt_webid": "6952944401862936069",
  "tt_webid_v2":"6952944401862936069",
  "ttwid": "1%7C32IUy325K74JuSpVqW8SAVf5sdZ3zNDYbXsICOkalng%7C1622600731%7Cd135e137c0793402d5d233ad2cdc56918f6dc5a82a78ed2541d9ad824c78bc95"
}


api = TikTokAPI(cookie=cookie)
save_path = '/home/margarcuae/Documents/github/final-project-network-science/tiktok/hashtagsInfo'
hashtag_data ={}

def getNumberHastag(hashtag):
  resp = api.getHashTag(hashtag)
  resp_stats = resp['challengeInfo']['stats']


  resp = toJson(resp)

  file_name = hashtag+'.json'
  completeName = os.path.join(save_path, file_name)
  f = open(completeName, "w")
  f.write(resp)
  f.close()
  return resp_stats


# hashtag_data["noakeiko"]=getNumberHastag("noakeiko")
# hashtag_data["noacastillo"]=getNumberHastag("noacastillo")
# hashtag_data["eleccionesperu2021"]=getNumberHastag("eleccionesperu2021")
# hashtag_data["fujimorinuncamas"]=getNumberHastag("fujimorinuncamas")

# hashtag_data = toJson(hashtag_data)


# file_name2 = "hashtagsData.json"
# f = open(file_name2, "a")
# f.write(hashtag_data)
# f.close()

# def test(hashtag_file):

#   cont = 30
#   cursor = 0
#   while(cursor < 61):
#     resp = api.getVideosByHashTag("#fujimorinuncamas", count=30, cursor=cursor )
#     resp = resp["itemList"]
#     print(cursor)
#     cursor += 30
#     for j in range(len(resp)):
#       video = resp[j]["challenges"]
#       for i in range(len(video)):
#         hashtag_title = video[i]['title']
#         verdad = hashtag_title in hashtag_file
#         if(verdad == False):
#           hashtag_file.append(hashtag_title)
      

#   return hashtag_file

#hashatgs = []
#hashatgs = test(hashatgs)
# print(hashatgs)

# variable1 = test()

# print(variable1)
# info = toJson(api.getUserByName("fcbarcelona"))

# file_name = "infouser.json"
# completeName = os.path.join(save_path, file_name)
# f = open(completeName, "w")
# f.write(info)
# f.close()





def getData(hashtag,cursor=0):
  resp = api.getVideosByHashTag(hashtag, count=30, cursor=cursor)
  # print(resp)
  print(toJson(resp))
  # tienemas = resp['hasMore']
  
  resp = toJson(resp)
  file_name = hashtag+'-'+str(cursor)+".json"
  save_path = '/home/margarcuae/Documents/github/final-project-network-science/tiktok/data/'+hashtag[1:]
  completeName = os.path.join(save_path, file_name)
  f = open(completeName, "w")
  f.write(resp)
  f.close()
  return [cursor+30,tienemas]




name_hashtag = 'fujimorinuncamas'
filename = name_hashtag+'.pk'

count = 0

tienemas = True
new_cursor = 0.0
while(tienemas):
  # infile = open(filename,'rb')
  # new_cursor = pickle.load(infile)
  
  # infile.close()
  # new_cursor = 1530
  cursor = getData('#'+name_hashtag,new_cursor)
  # new_cursor += 30
  tienemas =False
  # tienemas = cursor[1]
  # outfile = open(filename,'wb')
  # pickle.dump(cursor[0],outfile)
  # outfile.close()
  # print(str(cursor[0]) +" - "+str(cursor[1]))
  

  
  # if(count==0):
  #   tienemas=False


# resp = api.getHashTag("#fcbarcelona")
# resp = toJson(resp)
# print(resp)
# print(api.getTrending(count=5))
