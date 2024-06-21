import sqlite3

# Creating a connection
connection = sqlite3.connect("title.db")
# Creating a cursor
cursor = connection.cursor()

name = input("Movie name: ")
year = int(input("Year: "))
score = float(input("Score: "))

cursor.execute("""
  INSERT INTO movies (name, year, score)
  VALUES (?,?,?)""", (name, year, score))

# Saving 
connection.commit()

# Closing connection
connection.close()