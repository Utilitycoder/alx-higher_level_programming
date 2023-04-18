#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_all_states(username, password, database):
    """
    Lists all states from the database hbtn_0e_0_usa
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: {} username password database".format(sys.argv[0]))
