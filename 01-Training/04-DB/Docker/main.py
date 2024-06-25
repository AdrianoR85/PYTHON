import pymysql 
import dotenv
import os
dotenv.load_dotenv()

TABLE_NAME = 'customers'

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
    cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  
  conn.commit()
  
  with conn.cursor() as cursor:
    sql =(
      f'INSERT INTO {TABLE_NAME} '
      '(name, age) VALUES (%(name)s, %(age)s) '
    )
    
    data = (
        {"name":'Lara', "age":30},
        {"name":'Triss', "age":35},
        {"name":'Ciri', "age":25}
      )
    result = cursor.executemany(sql, data)
  conn.commit()
  
  with conn.cursor() as cursor:
    sql = (
      f'SELECT * FROM {TABLE_NAME} '
    )
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
      str_row = map(str,row)
      print(' - '.join(str_row))