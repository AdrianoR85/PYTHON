from connection_sqlite_01 import cursor
from connection_sqlite_01 import conn


def update(data, cursor, conn):
    cursor.execute(
        """
    UPDATE client
    SET fname=?, lname=?, email=?
    WHERE id=?
    """,
        data,
    )
    conn.commit()


# Example usage:
update(
    ("John", "Doe", "john.doe@example.com", 1), cursor, conn
)  # Update the first client record
