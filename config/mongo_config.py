import pymongo

# Create the client
client = pymongo.MongoClient('localhost', 27017)
db = client['poks_bot_db']
users = db['gks_users']
themes = db['themes']
records = db['records']