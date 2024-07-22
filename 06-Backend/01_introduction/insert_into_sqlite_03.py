from connection_sqlite_01 import cursor
from connection_sqlite_01 import conn


def get_last_id():
    cursor.execute("SELECT id FROM client ORDER BY id DESC LIMIT 1;")
    return cursor.fetchone()[0]

def insert_register(fname, lname, email):
    cursor.execute(
        "INSERT INTO client (fname, lname, email) VALUES (?,?,?);",
        (fname, lname, email),
    )

def insert_address(client_id, street, city):
    cursor.execute(
        "INSERT INTO address (client_id, street, city) VALUES (?,?,?);",
        (client_id, street, city),
    )

first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email: ')
street = input('Street: ')
city = input('City: ')

try:
    insert_register(first_name, last_name, email)
    last_id = get_last_id()
    insert_address(4, last_id, street, city)
    conn.commit()
except Exception as exc:
    print(f"An error occurred: {exc}")
    conn.rollback()