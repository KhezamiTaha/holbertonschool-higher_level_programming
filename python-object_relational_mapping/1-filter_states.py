#!/usr/bin/python3
'''
 a script that lists all states with a name starting with N from the database
'''


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL database and retrieves data from the states table.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE \
                    BINARY 'N%' ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
