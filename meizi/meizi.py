#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import multiprocessing
import time

def crawl():
	j = 298
	for i in range(5300,5364):
		url = 'http://www.meizitu.com/a/%d.html' % (i)
		soup = BeautifulSoup(requests.get(url).text,'html5lib')
		content = soup('div',id='picture')[0]
		content = soup('div','postContent')[0]
		img =  content.findAll('img')
		imgsrc = [c.get('src') for c in img]
		for photo in imgsrc:
			try:
				r = requests.get(photo,stream=True,timeout=10)
			except Exception, e:
				continue
			else:
				with open('meizi/'+str(j)+'.jpg','wb') as fd:
					for chunk in r.iter_content():
						fd.write(chunk)
				j += 1
			print (u'进行到第%d页' % (i)).encode('gbk')


def process_link_crawler():
	num_cpus = multiprocessing.cpu_count()
	process = []
	for i in range(num_cpus):
		p = multiprocessing.Process(target=crawl)
		p.start()
		process.append(p)
	for p in process:
		p.join()

if __name__ == '__main__':
	start = time.clock()
	process_link_crawler()
	end = time.clock()
	print end - start
