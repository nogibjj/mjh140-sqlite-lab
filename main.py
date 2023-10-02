"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

# Extract
print("Extracting data...")
extract(url="https://raw.githubusercontent.com/jfinocchiaro/marchmadness/master/kenpom.csv", 
        file_path = "kenpom.csv")

# Transform and load
print("Transforming data...")
load(dataset="kenpom.csv",
     database="kenpom.db",
     target_table = "kenpom_data")

# Query
print("Querying data...")
query(dbname = "kenpom.db",
      table = 'kenpom_data')
