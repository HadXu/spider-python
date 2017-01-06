import pymongo
from bs4 import BeautifulSoup
import requests
import time
from multiprocessing import Pool

urls = ['http://www.mzitu.com/xinggan/page/{}'.format(str(i)) for i in range(1, 76)]
client = pymongo.MongoClient('localhost', 27017)
meinv = client['meinv']
mzitu = meinv['mzitu']


def get_channel_link(url):
    time.sleep(2)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('ul#pins > li > a')
    for link in links:
        url = link.get('href')
        mzitu.insert_one({'url': url})


if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(get_channel_link, urls)
