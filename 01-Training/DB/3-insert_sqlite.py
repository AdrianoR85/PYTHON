import sqlite3

# Creating a connection
connection = sqlite3.connect("title.db")

# Creating a cursor
cursor = connection.cursor()

# Inserting information into the database
cursor.execute(
  """
  INSERT INTO movies (name, year, score) VALUES ('Matrix', 1999, 10)
  """
)
cursor.execute(
  """
  INSERT INTO movies (name, year, score) VALUES ('Super Mario Bros', 2023, 9.5)
  """
)
cursor.execute(
  """
  INSERT INTO movies (name, year, score) VALUES ('Avatar', 2023, 8)
  """
)

# Saving 
connection.commit()

# Closing connection
connection.close()