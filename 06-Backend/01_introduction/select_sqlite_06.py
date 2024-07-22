from connection_sqlite_01 import cursor

def get_all_clients(cursor):
  cursor.execute("SELECT * FROM client")
  return cursor.fetchall()

def get_one_client(cursor, name):
  cursor.execute("SELECT * FROM client WHERE fname=?", (name,))
  return cursor.fetchone()

all_client = get_all_clients(cursor)

for client in all_client:
  print(client)

one_client = get_one_client(cursor, 'Lara')
print(one_client if one_client != None else 'Client not found')