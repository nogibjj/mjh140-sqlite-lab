import sqlite3

def update(dbname, table, column_name, new_value, conditional_column, conditional_value):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"UPDATE {table} SET {column_name} = ? WHERE {conditional_column} = ?", (new_value, conditional_value))
    conn.commit()