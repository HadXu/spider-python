#coding:utf-8
'''
Created on 2015年10月29日

@author: HadXu
'''
import urllib
import re
import pickle
def downloadURL(urls):
    """
    urls: 需要下载的url列表
    dirpath: 下载的本地路径
    """
    i = 0
    for url in urls:
        print i
        if len(url)>0:
            #print "current process id is ",os.getpid()
            urllib.urlretrieve(url,'%s.jpg' % i)
            i += 1
def parseTarget(url):
    content=urllib.urlopen(url).read()
    #pattern = r'data-original="(.*?\.jpg)" src'
    pattern = r'src="(.*?\.jpg)" title'
    imglist = re.findall(pattern,content)

    return imglist
    
#html = "http://www.meizitu.com/a/1.html"

#print parseTarget(html)

urls = []

"""for i in range(1,500):
    http_url = "http://www.meizitu.com/a/%s" % str(i)+".html"
    try:
        urls.extend(parseTarget(http_url))
        print i 
    except:
        break"""
#with open('meizi_url.pkl','wb') as f:
   # pickle.dump(urls, f)
#downloadURL(urls)

with open('meizi_url.pkl','r') as f:
    urls = pickle.load(f)
#print len(urls)
downloadURL(urls)
