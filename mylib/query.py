"""Query the database"""

import sqlite3
from tabulate import tabulate

def query(dbname: str, tab: str, cond = None):
    """Query the database for the top 5 rows of the specified table"""
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    columns = 'Year, Rank, Team, Conference, Wins, Losses'
    if cond == None:
        print(f"Top 5 rows of the {tab} table:")
        query = f"SELECT {columns} FROM {tab} LIMIT 5"
    else:
        print(f"Top 5 rows of the {tab} table where {cond}:")
        query = f"SELECT {columns} FROM {tab} WHERE {cond} LIMIT 5"
    cursor.execute(query)
    results = cursor.fetchall()
    print(
        tabulate(
            results,
            headers = [
                'Year',
                'Rank',
                'Team',
                'Conference',
                'Wins',
                'Losses',
            ],
            tablefmt="grid",
        )
    )
    conn.close()
    return "Success"

if __name__ == "__main__":
    query(dbname = "kenpom.db",
          tab = 'kenpom_data',
          cond = "Year = '2018'")

