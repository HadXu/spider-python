# 妹子图爬虫 全站爬取以及并行爬取
## 该项目基于python的爬虫，将妹子图上所有的图片全部爬取下来，总共耗时3个小时。


----------
采用mongodb存放链接，通过

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

在这里使用了一个技巧，可以实现断点爬取，思想就是每爬取一个图片，就将该地址放在数据库中，等爬取出现问题的时候，将需要爬的地址与已经爬到的地址集合相减就ok。

    # 需要下载的地址
    img_links = [link['img_link'] for link in img_link.find()]
    # 已下载的地址
    downloaded_link = [link['img_link'] for link in downloaded_Link.find()]
    # 未下载的地址
    undownload_link = set(img_links) - set(downloaded_link)
