# coding=utf-8
import scrapy
from scrapy import Request
import json
from zhihuuser.items import UserItem
from .helper import help


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&amp;offset={offset}&amp;limit={limit}'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    start_user = 'hi-id'
    start_user_list = [
        'feifeimao', 'xiepanda', 'magasa', 'cheng-yi-nan', 'fu-er', 'lawrencelry', 'zombie', 'binka',
        'xiaodaoren', 'su-fei-17', 'bo-cai-28-7', 'commando', 'guo-zi-501', 'yu-yi-duo', 'chenqin',
        'wangnuonuo', 'rio', 'lisongwei', 'xia-chu-fang', 'zhen-shi-gu-shi-ji-hua', 'sunlau']
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        for self.start_user in self.start_user_list:
            yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
            yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, limit=20, offset=0),
                          self.parse_follows)
            yield Request(
                    self.followers_url.format(user=self.start_user, include=self.followers_query, limit=20, offset=0),
                    self.parse_followers)

    def parse_user(self, response):
        if response.status == 200:
            result = json.loads(response.text)
            item = UserItem()
            item['url_token'] = result.get('url_token')
            item['name'] = result.get('name')
            # location
            try:
                item['location'] = result.get('locations')[0].get('name')
            except:
                item['location'] = ''

            item['gender'] = result.get('gender')

            item['avatar_url'] = result.get('avatar_url').replace('is', 'xl')

            # business
            try:
                item['business'] = result.get('business').get('name')
            except:
                item['business'] = ''

            # company and job
            try:
                item['company'] = result.get('employments')[0].get('company').get('name')
                item['job'] = result.get('employments')[0].get('job').get('name')
            except:
                item['company'] = ''
                item['job'] = ''

            item['headline'] = result.get('headline', '')

            # school
            try:
                item['school'] = result.get('educations')[0].get('school').get('name')
            except:
                item['school'] = ''

            item['voteup_count'] = result.get('voteup_count')
            item['follower_count'] = result.get('follower_count')

            yield item

    def parse_follows(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_follows)

    def parse_followers(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_followers)
