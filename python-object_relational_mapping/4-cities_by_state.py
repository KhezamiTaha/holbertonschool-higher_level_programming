#!/usr/bin/python3
'''
DOcstring MySQLdb
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
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
