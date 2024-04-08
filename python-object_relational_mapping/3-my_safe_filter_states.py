#!/usr/bin/python3
'''
write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument. 
But this time, write one that is safe from MySQL injections!
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"

    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
