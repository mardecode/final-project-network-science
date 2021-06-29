from TikTokApi import TikTokApi
import random
import string
import json
import argparse

verifyFp = "".join(random.choice(string.digits) for num in range(19))
api = TikTokApi.get_instance()


def toJson(var):
  return json.dumps(var,indent=4)



data=['castillonomerepresenta',
'castillonova',
'eleccionesbicentenario',
'eleccionesperu2021',
'fuerzapopular',
'fujimorinuncamas',
'fujirata',
'fujitroll',
'keikofujimori',
'keikonova',
'keikopresidenta2021',
'noacastillo',
'noakeiko',
'nulo',
'pedrocastillo',
'pedrocastillocomunista',
'pedrocastillonicagando',
'pedrocastillopresidente2021',
'perulibre',
'petercastle',
'politicaperuana',
'votonulo',
'votoviciado',
'peruvotainformado',
'politicaperu',
'votoenblanco',
'voto2021',
'nokeiko',
'nocastillo',
'noalcomunismo',
'segundavuelta',
'votoblanco',
'despiertaperu',
'nikeikonipedro',
'nipedronikeiko',
'perulibredecorruptos',
'tuvotoespoder',
'veronikamendoza',
'castillopresidente',
'debatepresidencial2021',
'kenyi',
'keikopresidenta',
'castillnoesterrorista',
'keikocorrupta',
'segundavuelta2021',
'castillopresidente2021',
'peruzuela',
'mivotoesporcastillo',
'fueracomunistas',
'larutadekeiko',
'pontelacamisetaperu',
'willaxtv',
'miedoqueganecastillo',
'vamoskeikopresidenta2021',
'vivalademocraciaenperu',
'comunismonuncamas'

]

parser = argparse.ArgumentParser()
parser.add_argument('cursor')
parser.add_argument('hashtag')
args = parser.parse_args()

cursor = int(args.cursor)
hashtag = args.hashtag

resp = api.by_hashtag(hashtag,count=50,offset=cursor)
resp = toJson(resp)
print(resp)
    

