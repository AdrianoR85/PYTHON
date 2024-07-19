from connection_sqlite_01 import cursor
from connection_sqlite_01 import conn

first_name = "Lara"
last_name = "Croft"
email = "lara@example.com"


def insert_register(fname, lname, email, cursor, conn):
    cursor.execute(
        "INSERT INTO client (fname, lname, email) VALUES (?,?,?);",
        (fname, lname, email),
    )
    conn.commit()
    conn.close()

insert_register(first_name, last_name, email, cursor, conn)
