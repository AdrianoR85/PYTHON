from connection_sqlite_01 import cursor

def create_table():
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
