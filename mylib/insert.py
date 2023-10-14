'''Insert data'''
import sqlite3
from mylib.query import query

def insert(dbname: str, tab: str, new_data: dict):
    '''Insert new row of data into database'''
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"PRAGMA table_info({tab})")
    columns_info = c.fetchall()
    num_columns = len(columns_info)
    payload = format_data(new_data, columns_info)
    placeholders = ", ".join(["?"] * num_columns)
    c.execute(f"INSERT INTO {tab} VALUES ({placeholders})", payload)
    conn.commit()
    query(dbname = "kenpom.db",
          tab = 'kenpom_data',
          cond = "Year = '2018'")

def format_data(data: dict, columns_info: list):
    # Cycle through the db columns, determine if there's any new data. 
    # Save new data/NULL values in new_data
    payload = ()
    for item in columns_info:
        _, col_name, _, _, _, _ = item
        payload += (data.get(str(col_name)),)
    
    return payload