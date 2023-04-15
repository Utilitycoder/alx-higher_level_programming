#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

# Make a connection to the database using the provided arguments
connection = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

# Create cursor to interact with the database
cursor = connection.cursor()

# Execute the query to fetch all the states from the hbtn_0e_0_usa table
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows from the table
rows = cursor.fetchall()

# Iterate through each row and print the id and name in the required format
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
