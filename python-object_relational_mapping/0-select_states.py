#!/usr/bin/python3
'''
DOcstring MySQLdb
'''


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and retrieves data from the states table.

    Usage:
        $ python3 script.py <username> <password> <database>

    Arguments:
        username (str): MySQL database username.
        password (str): MySQL database password.
        database (str): Name of the MySQL database to connect to.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
