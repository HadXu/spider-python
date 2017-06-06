# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class UserItem(scrapy.Item):
    url_token = Field()
    name = Field()
    gender = Field()
    location = Field()
    avatar_url = Field()
    business = Field()
    company = Field()
    job = Field()
    headline = Field()
    school = Field()
    voteup_count = Field()
    follower_count = Field()
