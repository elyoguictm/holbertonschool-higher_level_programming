#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

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
    cursor.execute("SELECT * FROM states")
    row = cursor.fetchall()
    for data in row:
        print(data)
