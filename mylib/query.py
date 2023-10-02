"""Query the database"""

import sqlite3


def query(dbname: str, table: str):
    """Query the database for the top 5 rows of the specified table"""
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    print(f"Top 5 rows of the {table} table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


