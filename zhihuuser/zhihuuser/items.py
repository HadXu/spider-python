# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	id = Field()
	name = Field()
	headline = Field()
	url_token = Field()
	url = Field()
	gender = Field()
	answer_count = Field()
	articles_count = Field()
	follower_count = Field()