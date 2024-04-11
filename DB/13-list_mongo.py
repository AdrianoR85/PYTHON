from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

# Return just one document
# result = mycol.find()

# Return all documents
result = mycol.find()

for row in result:
  pprint(row)