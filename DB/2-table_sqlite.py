import sqlite3

# Creating a connection
connection = sqlite3.connect("title.db")

# Creating a cursor
cursor = connection.cursor()

# Creating a table
cursor.execute("""
  CREATE TABLE if not exists movies (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    year INTEGER NOT NULL,
    score INTEGER NOT NULL 
  )                 
               """)

# Closing the connection
connection.close()