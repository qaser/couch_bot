import pymongo

# Create the client
client = pymongo.MongoClient('localhost', 27017)
db = client['couch_bot_db']
users = db['users']
themes = db['themes']
records = db['records']
