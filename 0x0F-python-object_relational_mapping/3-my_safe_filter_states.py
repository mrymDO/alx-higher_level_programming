#!/usr/bin/python3

"""
a module that filter states by user input that is safe from MySQL injection
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    cursor = connection.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id", (sys.argv[4],))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
