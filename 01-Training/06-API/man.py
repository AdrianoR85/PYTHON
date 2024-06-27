import requests
import pandas as pd
from sqlalchemy import create_engine 

url = 'https://api.coincap.io/v2/assets'

header = {
  'Content-Type': 'application/json',
  'Accept-Encoding': 'deflate'
}

response = requests.get(url, headers=header)

if response.status_code == 200:
  response_data = response.json()
  df = pd.json_normalize(response_data, 'data')
  df = df[['id','symbol','name', 'priceUsd' ]]
  engine = create_engine('mysql+pymysql://root:root@localhost:3306/python_test')
  df.to_sql('crypto_data', engine, if_exists='replace', index=False)
else:
  print('Failed to get data')