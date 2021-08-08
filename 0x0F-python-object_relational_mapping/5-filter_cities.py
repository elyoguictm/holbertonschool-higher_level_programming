#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]
    STATE = argv[4]
    db = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD,
                         db=DATABASE, port=PORT)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN " +
                   "states ON cities.state_id = states.id WHERE " +
                   "states.name = %s ORDER BY cities.id ASC", (STATE,))
    querry = cursor.fetchall()
    print(", ".join(city[0] for city in querry))
    cursor.close()
    db.close()
