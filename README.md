Final project Network Science MO412 UNICAMP
====================================================================================

This is the base repository for final project of netwrok science using the 
tiktok and twitter data. 

This project is elaborated by Maria Fernanda and Margarita 


Introduction
------------------------------------------------------------------------------------
This work arises from the question about how much social networks influence 
the voters' decision. Therefore, we focus on the second round of the election 
in Perú 2021, in which we begin to obtain information from April 22 to June 5. 
Voting was held on June 6. These votes have been one of the most polarized 
votes in Perú.

We chose to work with a bipartite network which is composed of two types of 
nodes: user and hashtag. TO hide the user's information, only the IDs and 
number of followers were used. IN addition, the wieghts of our edges is the
combination between of number of favorites and the number of followers of the 
user. 

At the end of this work, we are goint to make a comparison of what indicated
to us that he/she was goint to win in the voting vs the real candidate who came
out as president. 

Social Netwoks
-------------------------------------------------------------------------------------
# tiktok
To run the folder tiktok please follow this steps 
https://github.com/avilash/TikTokAPI-Python#get-videos-by-hashtag
python3 main3.py 

# twitter
A crawler that is inside the twitter paste was used, curranelty to obtain
the key to do this type of work, a request must be sent to twitter to release
the key. 

THe information obtainesd was crawled for all those days, obtaining at least
40 to 120 files per day. IN each file containing 150 tweets. It was divided
in this way so that the information management is better. We obtained 3.87GB 
of raw information. 

So, in the same paste there is a python file to clean the data and obtain the 
information that you wat to divide into 3 files: two of them are the nodes, and
the last one is the one that save the links. These files will be loaded to obtain
our graph through the networkx library.

-------------------------------------------------------------------------------------
# Language of programming
Python 3

# Libraries
- json
- tweepy
- networkx

# Graphic Software
- Gephi
