# 为了断点爬虫，获得最后的爬虫的记录
import pymongo


class help:
    @classmethod
    def get_last_url_token(cls):
        try:
            client = pymongo.MongoClient()
            db = client['zhihu']
            users = db['users'].find({}).sort('follower_count', pymongo.DESCENDING).limit(50)
            return [user.get('url_token') for user in users]
        except:
            return ''


if __name__ == '__main__':
    res = help().get_last_url_token()
    print(res)
