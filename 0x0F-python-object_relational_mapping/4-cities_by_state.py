#!/usr/bin/python3

"""module that displays cities by states"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    cursor = connection.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            ORDER BY id")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    connection.close()
