#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches matches an argument passed as a parameter
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]
    STATE = argv[4]
    db = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD,
                         db=DATABASE, port=PORT)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE \
    name = '{}' ORDER BY id".format(STATE))
    querry = cursor.fetchall()
    for data in querry:
        print(data)
    cursor.close()
    db.close()
