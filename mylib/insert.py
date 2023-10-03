import sqlite3

def insert(dbname: str, table: str, new_data: dict):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute(f"PRAGMA table_info({table})")
    # Fetch all rows (each row represents a column)
    columns_info = c.fetchall()
    # Count the number of columns
    num_columns = len(columns_info)
    payload = format_data(new_data, columns_info)
    placeholders = ", ".join(["?"] * num_columns)
    c.execute(f"INSERT INTO {table} VALUES ({placeholders})", payload)
    conn.commit()

def format_data(data: dict, columns_info: list):
    new_data = ()
    for item in columns_info:
        _, col_name, _, _, _, _ = item
        new_data += (data.get(str(col_name)),)
    print(new_data)
    
    return new_data