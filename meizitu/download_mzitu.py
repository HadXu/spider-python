from urllib.request import urlretrieve
import time
from multiprocessing import Pool
import pymongo

client = pymongo.MongoClient('localhost', 27017)
meinv = client['meinv']
every_meizi_link = meinv['every_meizi_link']
img_link = meinv['img_link']
downloaded_Link = meinv['downloaded_Link']

# 需要下载的地址
img_links = [link['img_link'] for link in img_link.find()]
# 已下载的地址
downloaded_link = [link['img_link'] for link in downloaded_Link.find()]
# 未下载的地址
undownload_link = set(img_links) - set(downloaded_link)


def download(url):
    urlretrieve(url, 'images/%s.jpg' % time.time())
    time.sleep(0.2)
    downloaded_Link.insert_one({'img_link': url})
    print("已下载完" + url)


if __name__ == '__main__':
    pool = Pool()
    pool.map(download, undownload_link)
