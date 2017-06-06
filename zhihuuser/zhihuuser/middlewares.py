# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
import base64


class ZhihuuserSpiderMiddleware(UserAgentMiddleware):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RotateUserAgentMiddleware(object):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.USER_AGENTS)
        if ua:
            # print('*****current User_agent:%s*******' % ua)
            request.headers.setdefault('User-Agent', ua)

    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]


class IPPOOLS(HttpProxyMiddleware):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        ip = random.choice(self.ip_pools)
        print('当前使用的IP是' + ip['ip'])
        try:
            request.meta["proxy"] = "http://" + ip['ip']
        except Exception:
            pass

    ip_pools = [{'ip': '182.90.42.158:80'}, {'ip': '115.202.160.114:808'}, {'ip': '111.183.94.79:808'},
                {'ip': '218.64.92.137:808'}, {'ip': '115.213.202.75:808'}, {'ip': '182.32.151.45:808'},
                {'ip': '115.213.203.121:808'}, {'ip': '121.226.171.69:808'}, {'ip': '175.155.142.93:808'},
                {'ip': '121.40.40.182:80'}, {'ip': '117.43.0.136:808'}, {'ip': '123.169.87.212:808'},
                {'ip': '36.99.206.41:808'}, {'ip': '113.219.103.235:8998'}, {'ip': '221.229.46.6:808'},
                {'ip': '222.95.23.226:808'}, {'ip': '115.215.70.230:808'}, {'ip': '123.55.95.17:808'},
                {'ip': '221.7.167.214:8123'}, {'ip': '122.235.163.159:808'}, {'ip': '218.64.93.150:808'},
                {'ip': '123.55.187.38:808'}, {'ip': '114.239.3.236:808'}, {'ip': '218.64.93.28:808'},
                {'ip': '115.213.202.219:808'}, {'ip': '114.239.2.192:808'}, {'ip': '182.38.41.49:808'},
                {'ip': '60.167.20.153:808'}, {'ip': '36.99.206.152:808'}, {'ip': '153.36.57.4:808'},
                {'ip': '120.83.122.158:808'}, {'ip': '119.5.0.58:808'}, {'ip': '119.5.1.67:808'},
                {'ip': '123.169.85.27:808'}, {'ip': '27.18.136.99:8998'}, {'ip': '221.229.44.156:808'},
                {'ip': '121.237.136.221:808'}, {'ip': '60.178.86.23:808'}, {'ip': '114.239.149.255:808'},
                {'ip': '119.5.0.185:808'}, {'ip': '175.155.25.55:808'}, {'ip': '222.85.50.99:808'},
                {'ip': '113.121.147.10:80'}, {'ip': '183.153.23.190:808'}, {'ip': '183.153.54.159:808'},
                {'ip': '123.169.91.165:808'}, {'ip': '121.226.169.186:808'}, {'ip': '121.233.16.88:808'},
                {'ip': '110.73.54.38:8123'}, {'ip': '114.239.150.228:808'}, {'ip': '221.229.45.203:808'},
                {'ip': '123.169.87.5:808'}, {'ip': '59.62.127.9:808'}, {'ip': '123.169.85.208:808'},
                {'ip': '122.96.59.105:82'}, {'ip': '123.169.87.70:808'}, {'ip': '202.108.2.42:80'},
                {'ip': '144.255.48.113:808'}, {'ip': '114.99.7.48:808'}, {'ip': '60.167.133.211:808'},
                {'ip': '175.155.24.28:808'}, {'ip': '140.224.76.43:808'}, {'ip': '123.163.166.102:808'},
                {'ip': '175.155.142.158:808'}, {'ip': '123.55.186.97:808'}, {'ip': '222.94.148.112:808'},
                {'ip': '218.64.93.147:808'}, {'ip': '119.5.0.8:808'}, {'ip': '182.38.15.237:808'},
                {'ip': '110.87.5.129:45188'}, {'ip': '121.226.172.216:808'}, {'ip': '121.226.163.119:808'},
                {'ip': '113.121.162.186:808'}, {'ip': '123.169.89.113:808'}, {'ip': '117.43.1.191:808'},
                {'ip': '60.167.21.6:808'}, {'ip': '113.121.187.213:808'}, {'ip': '123.163.166.97:808'},
                {'ip': '114.230.104.123:808'}, {'ip': '180.110.134.121:808'}, {'ip': '153.36.54.104:808'},
                {'ip': '175.155.25.80:808'}, {'ip': '115.213.201.59:808'}, {'ip': '153.36.55.34:808'},
                {'ip': '183.157.181.88:80'}, {'ip': '123.55.188.62:808'}, {'ip': '115.192.248.162:808'},
                {'ip': '220.160.10.117:808'}, {'ip': '123.55.95.233:808'}, {'ip': '171.37.161.225:8123'},
                {'ip': '59.62.126.235:808'}]
