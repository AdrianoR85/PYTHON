from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

old_value = { "content": "Data Analysis" }
new_value = { "$set":{ "content": "Backend" }}

try:
  mycol.update_one(old_value, new_value)
  print('Updated successfully')
  
  for doc in mycol.find():
    pprint(doc)
except Exception:
  print('Update failed')
  print(Exception)