import time
import pymongo
client = pymongo.MongoClient('localhost', 27017)
meinv = client['meinv']
mzitu = meinv['mzitu']
every_meizi_link = meinv['every_meizi_link']
img_link = meinv['img_link']
downloaded_Link = meinv['downloaded_Link']
while True:
    print(downloaded_Link.count())
    time.sleep(2)