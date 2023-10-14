## Mini Project 5: SQLite Lab

[![CI](https://github.com/nogibjj/mjh140-sqlite-lab/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mjh140-sqlite-lab/actions/workflows/cicd.yml)


### Summary:

This project introduced sql commands using a SQLite database stored directly in this repository. The data chosen for this project was 2002 - 2017 college basketball stats taken from the KenPOMS database. The following commands were executed in order on this data set:

* `Extract`: Extract a url to a file path
* `Transform`: Transform and load data into the local SQLite3 database
* `Query`: Query the database for the top 5 rows of the specified table
* `Insert`: Insert a new row of data into database
* `Update`: Update existing data in database
* `Delete`: Delete data from database

SQL commands were separated into individual `.py` files and saved within the `/mylib` folder. The main script, `/src/main.py` executed all SQL commands sequentially. 

#### Results:

After converting the data into a SQLite database, the first 5 rows were printed using the `tabulate` package. Because of the size of the database, only the first 6 columns were printed. The table is shown below.
![image](https://github.com/nogibjj/mjh140-sqlite-lab/assets/114833075/29fa7122-7dea-44b8-9bab-b4af78418ad8)

This database includes data between 2002 and 2017 as shown by this query of data under the condition `Year = '2018'`:
![image](https://github.com/nogibjj/mjh140-sqlite-lab/assets/114833075/ff0ca09b-7f54-457f-9ae9-edf1f000e9bb)

For the purposes of utilizing CRUD operations on a SQLite database, a new row of data from 2018 will be `Inserted`, `Updated`, and `Deleted`. After executing the `Insert` command, the query returned one result where `Year = '2018'`:
![image](https://github.com/nogibjj/mjh140-sqlite-lab/assets/114833075/04ff5ecd-7caf-493a-913f-99d2a8bba0ce)

The new row of data was successfully inserted, but the Conference column is missing. The `Update` script was executed and the results of the conditional query `Year = '2018'` are shown below. 
![image](https://github.com/nogibjj/mjh140-sqlite-lab/assets/114833075/797ddf26-9134-49fd-8390-d53a202caffd)

The conference was successfully updated to "BE" (Big East). The final command will delete this new row of data. The conditional query shows there is no longer data where `Year = '2018'`:
![image](https://github.com/nogibjj/mjh140-sqlite-lab/assets/114833075/5fa6ecac-848c-43e0-8aca-435e1bee54f3)



