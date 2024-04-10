import sqlite3

# Create a connection
connection = sqlite3.connect("title.db")

# Create a cursor
cursor = connection.cursor()

# Get data from the user
id = int(input("Enter movie ID for update: "))
new_name = input("Enter new name for update: ")

# Update the database

cursor.execute("""
  UPDATE movies
  SET name = ?
  WHERE id = ?""", (new_name, id))

connection.commit()
# Close the connection
connection.close()