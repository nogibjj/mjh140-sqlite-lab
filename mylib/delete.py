import sqlite3
from mylib.query import query

def delete(dbname: str, tab:str, cond_col:str, cond_val:str):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"DELETE FROM {tab} WHERE {cond_col} = '{cond_val}'")
    conn.commit()
    query(dbname = "kenpom.db",
          tab = 'kenpom_data',
          cond = "Year = '2018'")