#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","bazek","ve7128","baza_test_python" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO paragony(TypDok,
         DataSprzed,DataWyst)
         VALUES ('2', '14.04.23','14.04.23')"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()



# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")




# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()
