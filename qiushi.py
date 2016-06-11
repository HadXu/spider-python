#-*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import requests
from bs4 import BeautifulSoup



for i in range(1,10):
	url = 'http://www.qiushibaike.com/8hr/page/%d/?s=4872223' % (i)
	soup = BeautifulSoup(requests.get(url).text,'html5lib')
	content = soup('div','content')

	text = [c.text for c in content]

	for t in text:
		with open('1.txt','a') as f:
			f.write(t)
