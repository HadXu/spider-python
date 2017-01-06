from bs4 import BeautifulSoup
import requests
import pymongo
client = pymongo.MongoClient('localhost',27017)
meinv = client['meinv']
mzitu = meinv['mzitu']

for i in mzitu.find().limit(10):
    print(i['url'])