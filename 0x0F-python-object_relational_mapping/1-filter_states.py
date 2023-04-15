#!/usr/bin/python3
# Lists all states with a name starting with N from the database hbtn_0e_0_usa.
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == '__main__':
    # read command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to mysql server
    try:
        db = MySQLdb.connect(host='localhost',
                             user=mysql_user,
                             passwd=mysql_password,
                             db=db_name,
                             port=3306)
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Server: {e}")
        sys.exit(1)

    # execute sql query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # print results
    for row in cursor.fetchall():
        print(row)

    # close connection
    db.close()
