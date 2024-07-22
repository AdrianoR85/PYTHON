from connection_sqlite_01 import cursor
from connection_sqlite_01 import conn

def delete(id):
  cursor.execute("DELETE FROM client WHERE id=?", (id,))
  conn.commit()
  conn.close()

def delete_address(id):
  cursor.execute("DELETE FROM address WHERE id=?", (id,))
  conn.commit()
  conn.close()

# delete_address(3)
# delete(3)

