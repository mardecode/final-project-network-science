# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 23:37:15 2021

@author: W10
"""

import tweepy
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from tweepy import StreamListener
import time
import json
import sys

class SListener(StreamListener):
    def __init__(self, api = None, fprefix = 'streamer', time_limit=60):
        self.api = api 
        self.counter = 0
        self.counterT= 0
        self.start_time = time.time()
        self.limit_time = time_limit
    
        self.fprefix = fprefix
        self.output  = open(fprefix + '_0.json', 'w')
        self.delout  = open(fprefix + '_delete.txt', 'a')
        self.error   = open(fprefix + '_error.txt', 'w')

    def on_data(self, data):
        if  'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print (warning['message'])
            return False

    def on_status(self, status):
      if self.counter == 0:
        self.output.write("{ \"data\" : [ " + "\n")
        self.output.write(status)
        self.counter += 1
        return
      
      self.output.write("," + "\n" + status)
      self.counter += 1
      
      if self.counter >= 150:
        self.output.write("] }" + "\n")
        self.output.close()
        self.output = open(self.fprefix + "_" + str(self.counterT+1) + '.json', 'w')
        self.counter = 0
        self.counterT += 1
        print(self.counterT)
        return

    def on_delete(self, status_id, user_id):
        self.delout.write( str(status_id) + "\n")
        return

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        self.error.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        self.error.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout \n")
        self.error.write("Timeout \n")
        time.sleep(60)
        return 

consumer_key = "1dAGo5lZyl8J6AHEL5IYg"
consumer_secret = "tVJfogDCRJdOpo0aK19fI6TugEfnaLPYipzrjqz6X0"

access_key = "84490435-dNltopbXXLTTckUKtAKP8Wt6xafkA4CDp5MswcIqX"
access_secret = "s7bTXavUus6p70AkvWEvaLE8y71O2tZOL92mHx7gg"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def Crawlear(file, track):
    languages = ['en', 'es']

    filename= file + time.strftime("%Y_%m_%d_%H")
    
    listen = SListener(api, filename)
    stream = tweepy.Stream(auth, listen)

    print ("Streaming started...")

    try:
        stream.filter(track = track, languages=languages)
    except:
        print ("error!")
        stream.disconnect()

filePeru = 'TwitterData/Peru/'
trackPeru = ['Elecciones Peru 2021', '2021 Peruvian Election', 'Perú libre', 'Fuerza Popular',
             '#fujiratas', '#eleccionebicentenario', '#Castillonomerepresenta', '#PedroCastilloNiCagando',
             '#CastilloNoVa','#PedroCastillo', '#PedroCastilloComunista', '#KeikoFujimori', '#FujiTrol',
             '#unvotoporlapatria', '#fujimorismo', "#votoviciado", "#nulo", "#noacastillo", "#noakeiko"]

fileMexico = 'TwitterData/Mexico/'
trackMexico = ['Elecciones Mexico 2021', '2021 Mexican Election', 'MRN Mexico', 'PAN Mexico', 'PRI Mexico', 'PRD Mexico', 'PT Mexico', 'PVEM Mexico']

fileChile = 'TwitterData/Chile/'
trackChile = ['Elecciones Chile 2021', '2021 Chilean Election']
Crawlear(filePeru, trackPeru)