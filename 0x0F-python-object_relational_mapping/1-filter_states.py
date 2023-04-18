#!/usr/bin/python3
"""
This script lists all states with a name starting with N from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


def main():
    """Main function"""

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
