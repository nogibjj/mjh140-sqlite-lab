"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="/mjh140-sqlite-lab/kenpom.csv",
         database = "kenpom.db"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS kenpomDB")
    c.execute("DROP TABLE IF EXISTS kenpom_data")
    c.execute("CREATE TABLE kenpom_data (Year,Rank,Team,Conference,Wins,Losses,Seed,Pyth,AdjustO,AdjustO_Rank,AdjustD,AdjustD_Rank,AdjustT,AdjustT_Rank,Luck,Luck_Rank,SOS_Pyth,SOS_Pyth_Rank,SOS_OppO,SOS_OppO_Rank,SOS_OppD,SOS_OppD_Rank,NCSOS_Pyth,NCSOS_Pyth_Rank)")
    #insert
    c.executemany("INSERT INTO kenpom_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "kenpom.db"

