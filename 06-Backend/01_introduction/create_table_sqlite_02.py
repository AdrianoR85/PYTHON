from connection_sqlite_01 import cursor

def create_client():
  cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS client (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      fname TEXT NOT NULL,
      lname TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL
    )
  """
  )

def create_address():
  cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS address (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      client_id INTEGER,
      street VARCHAR(30) NOT NULL,
      city VARCHAR(30) NOT NULL,
      FOREIGN KEY (client_id) REFERENCES client(id)
    )
  """
  )

create_address()

