#coding:utf-8

import requests
from bs4 import BeautifulSoup
import csv

Baseurl = 'http://cslg.91job.gov.cn/contest/learn?page='

f = open('answer.csv','w')
for page in range(1,736):
	url = Baseurl+str(page)
	print url
	soup = BeautifulSoup(requests.get(url).text,'html5lib')
	content = soup('div','all')
	title = content[0].find('div','title').b.text.replace('\n','')
	title = title.replace(',','')
	right = content[0].find('div','right').p.font.b.text.split(':')[-1]
	
	#这里还有一个方法，使用extract
	#title = content[0].find('div','title').b.text
	#title.font.extract() 就可以将font标签除去

	f.write(title.encode('utf8')+','+right.encode('utf8'))
	f.write('\n')
	print '爬完了第%d页' % page

f.close()
