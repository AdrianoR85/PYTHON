from connection_post import conn
from show_data import show

cursor = conn.cursor()

sql = """
  DELETE FROM game
  WHERE id = %s 
"""

cursor.execute(sql, (7,))
conn.commit()
show()

conn.close()