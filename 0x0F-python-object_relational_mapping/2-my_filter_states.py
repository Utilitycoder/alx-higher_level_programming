#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Get arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Open database connection
    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to SELECT records from the database.
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    try:
        # Execute the SQL command
        cursor.execute(query)

        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            print(row)

    except:
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()

