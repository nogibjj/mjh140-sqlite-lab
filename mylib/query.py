"""Query the database"""

import sqlite3


def query(dbname: str):
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kenpom_data")
    print("Top 5 rows of the kenpom_data table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


