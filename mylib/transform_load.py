"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="/mjh140-sqlite-lab/kenpom.csv",
         database = "kenpom.db",
         target_table = "kenpom_data"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    column_names, num_columns = extract_column_names(payload)
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(f"DROP TABLE IF EXISTS GroceryDB")
    c.execute(f"DROP TABLE IF EXISTS {target_table}")
    c.execute(f"CREATE TABLE {target_table} ({column_names})")
    #insert
    placeholders = ", ".join(["?"] * num_columns)
    c.executemany(f"INSERT INTO {target_table} VALUES ({placeholders})", payload)
    conn.commit()
    conn.close()
    return database

def extract_column_names(csv_text):
    # Read the header row from the CSV reader
    header_row = next(csv_text)
    # Number of columns
    num_columns = len(header_row)
    # Join the column names into a string (comma-separated, no spaces)
    column_names = ','.join(header_row)
    column_names = column_names.replace(' ', '_')
    return column_names, num_columns