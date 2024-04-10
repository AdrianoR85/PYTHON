import sqlite3

# Creating a connection
connection = sqlite3.connect("title.db")

# Creating a cursor
cursor = connection.cursor()

## Reading data from the database
# data = cursor.execute("SELECT * FROM movies")
# print(data.fetchall())

for row in cursor.execute("SELECT * FROM movies ORDER BY score"):
  print(row)

# Closing the connection
connection.close()
