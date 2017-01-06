import time
from bs4 import BeautifulSoup
import requests
import pymongo
from multiprocessing import Pool

client = pymongo.MongoClient('localhost', 27017)
meinv = client['meinv']
every_meizi_link = meinv['every_meizi_link']
img_link = meinv['img_link']

urls = []
for url in every_meizi_link.find():
    urls.append(url['url'])


def get_imgLink(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    img = soup.select('div.main-image > p > a > img')[0]
    imgLink = img.get('src')
    img_link.insert_one({'img_link': imgLink})
    print(imgLink)


# get_imgLink('http://www.mzitu.com/6733/8')

if __name__ == '__main__':
    pool = Pool(processes=6)
    pool.map(get_imgLink, urls)
