#Title: SQLite database example
#Author: Paul Grant
#Date: 03/10/2025
#Description: Using databases in python

#Libraries
import sqlite3

#create a connection to the database
#create or open a database called example.db
con = sqlite3.connect("example.db")

#create the cursor
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS people (first_name text, last_name text, age integer)")

#insert a row of data(called a record)
#cur.execute("INSERT INTO people VALUES('Peter', 'Moore', '21')")

#commit (or save) the changes
con.commit()