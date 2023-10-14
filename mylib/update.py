'''Update data'''

import sqlite3
from mylib.query import query

def update(dbname, tab, col, n_val, cond_col, cond_val):
    '''Update existing data in database.'''
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"UPDATE {tab} SET {col} = ? WHERE {cond_col} = ?", (n_val, cond_val))
    conn.commit()
    query(dbname = "kenpom.db",
          tab = 'kenpom_data',
          cond = "Year = '2018'")