"""
ETL-Query script
"""
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

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


