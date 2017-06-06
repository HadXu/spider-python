# 为了断点爬虫，获得最后的爬虫的记录
import pymongo


class help:
    @classmethod
    def get_last_url_token(cls):
        try:
            client = pymongo.MongoClient()
            db = client['zhihu']
            users = db['users'].find().sort('_id',pymongo.DESCENDING).limit(1)
            return users[0].get('url_token')
        except:
            return ''


if __name__ == '__main__':
    res = help().get_last_url_token()
    print(res)
