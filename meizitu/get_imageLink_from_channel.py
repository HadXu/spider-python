from bs4 import BeautifulSoup
import requests
import pymongo
from multiprocessing import Pool

url = 'http://www.mzitu.com/83048/'

client = pymongo.MongoClient('localhost', 27017)
meinv = client['meinv']
mzitu = meinv['mzitu']

every_meizi_link = meinv['every_meizi_link']


def get_every_page(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    num_of_this_URL = soup.select('div.pagenavi > a > span')
    num_of_this_URL = [n.text for n in num_of_this_URL][-2]

    url = [url + '/' + str(i) for i in range(1, int(num_of_this_URL) + 1)]
    for l in url:
        every_meizi_link.insert_one({'url': l})
        print(l)


link = []
for i in mzitu.find():
    link.append(i['url'])

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(get_every_page, link)
