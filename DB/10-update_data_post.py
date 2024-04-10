from connection_post import conn
from show_data import show

cursor = conn.cursor()

sql = """
  UPDATE game
  SET score = %s
  WHERE id = %s 
"""

cursor.execute(sql, (9, 9))
conn.commit()
show()

conn.close()