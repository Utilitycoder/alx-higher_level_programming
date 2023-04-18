#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument, safe from MySQL injections
"""

import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database_name)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
