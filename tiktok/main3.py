from TikTokAPI import TikTokAPI
import os 
import json


def toJson(var):
  return json.dumps(var,indent=4)

cookie = {
  "s_v_web_id": "verify_ko1w5v2d_Bkht79Md_JAtu_4X5R_BQXi_0yI3nQj4IKYN",
  "tt_webid": "6903243350104901126"
}

api = TikTokAPI(cookie=cookie)
resp = api.getVideosByHashTag("#NoAKeiko",1)
resp = toJson(resp["itemList"][0]["desc"])

save_path = '/home/margarcuae/Documents/UNICAMP/MO412/final-project/hashtagsInfo'
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

# getNumberHastag("noakeiko")

hashtag_data["noakeiko"]=getNumberHastag("noakeiko")
hashtag_data["noacastillo"]=getNumberHastag("noacastillo")
hashtag_data["eleccionesperu2021"]=getNumberHastag("eleccionesperu2021")



hashtag_data = toJson(hashtag_data)

file_name2 = "hashtagsData.json"
f = open(file_name2, "a")
f.write(hashtag_data)
f.close()