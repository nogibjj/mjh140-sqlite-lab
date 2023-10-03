import sqlite3

def delete(dbname: str, table:str, conditional_column:str, conditional_value:str):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"DELETE FROM {table} WHERE {conditional_column} = '{conditional_value}'")
    conn.commit()