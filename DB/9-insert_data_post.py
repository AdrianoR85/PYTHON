from connection_post import conn
from show_data import show

cursor = conn.cursor()

games = [
  ('Luigis Mansion 3', 2019, 9)
]

for game in games:
  cursor.execute("""
    INSERT INTO game(name, year, score)
    VALUES(%s, %s, %s)
  """, game)

conn.commit()
show()

conn.close()