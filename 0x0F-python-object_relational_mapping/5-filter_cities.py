#!/usr/bin/python3
"""
This module lists all cities of a state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    """
    Lists all cities of a state from the database hbtn_0e_4_usa
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
                 cities.state_id=states.id WHERE states.name=%s \
                 ORDER BY cities.id ASC", (state_name,))
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: {} username password database state_name".format(sys.argv[0]))

