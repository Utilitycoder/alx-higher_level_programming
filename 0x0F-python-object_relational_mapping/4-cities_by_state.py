#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def list_all_cities(username: str, password: str, db_name: str):
    """
    Lists all cities from the database hbtn_0e_4_usa

    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): database name

    Returns:
        None
    """
    try:
        conn = MySQLdb.connect(host="localhost",
                               user=username,
                               passwd=password,
                               db=db_name,
                               port=3306,
                               charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM cities ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print(f"MySQL Error {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password db_name".format(sys.argv[0]))
        sys.exit(1)
    list_all_cities(sys.argv[1], sys.argv[2], sys.argv[3])


