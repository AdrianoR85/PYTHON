import sqlite3

connection = sqlite3.connect("title.db")
cursor = connection.cursor()

id = int(input("Enter movie ID for delete: "))

cursor.execute("""
  DELETE FROM movies WHERE id = ?
""", (id,))

connection.commit()
connection.close()