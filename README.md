## Mini Project 5: SQLite Lab

[![CI](https://github.com/nogibjj/mjh140-sqlite-lab/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mjh140-sqlite-lab/actions/workflows/cicd.yml)


### Summary:

This project introduced sql commands using a SQLite database stored directly in this repository. The data chosen for this project was 2002 - 2017 college basketball stats taken from the KenPOMS database. THe following commands were executed in order on this data set:

* `Extract`: Extract a url to a file path
* `Transform`: Transform and load data into the local SQLite3 database
* `Query`: Query the database for the top 5 rows of the specified table
* `Insert`: Insert new new row of data into database
* `Update`: Update existing data in database
* `Delete`: Delete data from database

SQL commands were separated into individual `.py` files and saved within the `mylib` folder. The main script, `main.py` executed all SQL commands sequentially. 

#### Tasks:

* Fork this project and get it to run
* Make the query more useful and not a giant mess that prints to screen
* Convert the main.py into a command-line tool that lets you run each step independantly
* Fork this project and do the same thing for a new dataset you choose
* Make sure your project passes lint/tests and has a built badge
* Include an architectural diagram showing how the project works

#### Reflection Questions

* What challenges did you face when extracting, transforming, and loading the data? How did you overcome them?
* What insights or new knowledge did you gain from querying the SQLite database?
* How can SQLite and SQL help make data analysis more efficient? What are the limitations?
* What AI assistant did you use and how did it compare to others you've tried? What are its strengths and weaknesses?
* If you could enhance this lab, what would you add or change? What other data would be interesting to load and query?

##### Challenge Exercises

* Add more transformations to the data before loading it into SQLite. Ideas: join with another dataset, aggregate by categories, normalize columns.
* Write a query to find correlated fields in the data. Print the query results nicely formatted.
* Create a second table in the SQLite database and write a join query with the two tables.
* Build a simple Flask web app that runs queries on demand and displays results.
* Containerize the application using Docker so the database and queries can be portable


