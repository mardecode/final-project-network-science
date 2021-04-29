# verify_knz7g6p1_Ev3dXcIK_XIE9_47KO_9jJ2_dK0MOuZTuxbc

from TikTokApi import TikTokApi
# import json


verifyFp = "verify_ko1w5v2d_Bkht79Md_JAtu_4X5R_BQXi_0yI3nQj4IKYN"
# api = TikTokApi.get_instance(use_selenium=True, custom_verifyFP=verifyFp, use_test_endpoints=True, count=1)
# api = TikTokApi.get_instance(use_selenium=True, custom_verifyFP=verifyFp)


# tiktoks = api.trending()
# print(tiktoks)


# for tiktok in tiktoks:
#   print(json.dumps(tiktok))
#   print(tiktok)


# tiktoks = api.by_hashtag("NoAKeiko",count=1)

# for tiktok in tiktoks:
#   print(tiktok)



api = TikTokApi.get_instance(use_selenium=True, custom_verifyFP=verifyFp, use_test_endpoints=True)

count = 1

tiktoks = api.byHashtag("funny",count=1)
# tiktoks = api.trending()

for tiktok in tiktoks:
    print(tiktok)