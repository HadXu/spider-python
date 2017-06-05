import pymongo

client = pymongo.MongoClient()
db = client.zhihu
users = db.users
users = users.find()
