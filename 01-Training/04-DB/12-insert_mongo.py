from pymongo import MongoClient

client = MongoClient()
mydb = client.obcblog
mycol = mydb.posts

post1 = {
  "id": 2,
  "title": "FastApi",
  "content": "Backend",
  "author": {
    "name": "Ciri",
    "email": "ciri@gmail.com"
  }
}

try:
  result = mycol.insert_one(post1)
  print("Success")
except:
  print(ValueError("Failed to insert"))
