import pymysql 
import dotenv
import os
dotenv.load_dotenv()

conn = pymysql.Connection(
  host=os.environ['HOST'],
  user=os.environ['MYSQL_USER'],
  password=os.environ['MYSQL_PASSWORD'],
  database=os.environ['MYSQL_DATABASE']
)

with conn:
  with conn.cursor() as cursor:
    cursor.execute(
      'CREATE TABLE IF NOT EXISTS customers ( '
      'id INTEGER PRIMARY KEY AUTO_INCREMENT, '
      'name VARCHAR(255) NOT NULL, '
      'age INTEGER NOT NULL'
      ' ) '
    )