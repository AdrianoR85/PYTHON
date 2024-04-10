from connection_post import conn

def show():
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM game")
  for row in cursor.fetchall():
    print(row)

if __name__ == "__main__":
  show()