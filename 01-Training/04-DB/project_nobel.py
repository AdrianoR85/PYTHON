import requests
from pymongo import MongoClient

URL= 'https://api.nobelprize.org/v1'
# 1. Establishes connection with MongoDB and the Database
client = MongoClient()
db = client['nobel']

# 2. Import Data into Documents
for collection_name in ["prizes", "laureates"]:
  response = requests.get(f'{URL}/{collection_name[:-1]}.json')
  documents = response.json()[collection_name]
  
  db[collection_name].insert_many(documents)

# 3. Accessing Collections / Counting Documents in the collection
prizes = db["prizes"]
laureates = db["laureates"]

len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})

print(len_prizes)
print(len_laureates)