import json
import pickle
import glob
import os


def getPickle(filename):
  infile = open(filename,'rb')
  data = pickle.load(infile)
  infile.close()
  return data

def createPickle(filename,filevalue):
  outfile = open(filename,'wb')
  pickle.dump(filevalue,outfile)
  outfile.close() 

def readFile(filename):
  if os.path.getsize(filename) == 0:
    print('File is empty :/ '+filename)
    return {}
  f = open(filename, "r")
  return json.loads(f.read())

def toJson(var):
  return json.dumps(var,indent=4)

