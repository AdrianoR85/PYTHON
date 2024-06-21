from connection_post import conn
from show_data import show

def show_data():
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM game")
  for row in cursor.fetchall():
    print(row)
    
show_data()