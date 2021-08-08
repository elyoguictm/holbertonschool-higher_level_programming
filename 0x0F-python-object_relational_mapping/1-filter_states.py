#!/usr/bin/python3
"""script that lists all states with a name starting with N"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]
    db = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD,
                         db=DATABASE, port=PORT)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    for data in cursor.fetchall():
        if data[1][0] == 'N':
            print(data)
    cursor.close()
    db.close()
