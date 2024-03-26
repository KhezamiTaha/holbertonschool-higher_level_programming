#!/usr/bin/python3
'''
A script that filter cities and print output
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
    query = "SELECT cities.name FROM cities \
             JOIN states ON cities.state_id = states.id WHERE \
             states.name = %s ORDER BY cities.id ASC"

    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        if rows.index(row) == len(rows) - 1:
            print(f"{row[0]}")
        else:
            print(f"{row[0]}, ", end="")
    cursor.close()
    db.close()
