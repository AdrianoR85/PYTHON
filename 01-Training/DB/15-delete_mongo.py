from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

my_query = { "content": "Backend" }

try:
  mycol.delete_one(my_query)
  print('Deleted successfully')
  
  for doc in mycol.find():
    pprint(doc)
except Exception:
  print('Delete failed')
  print(Exception)