#!/usr/bin/python3

"""a module that lists all cities of state that is an input arg"""

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

    cursor.execute("SELECT cities.name FROM cities JOIN states ON \
            cities.state_id = states.id WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id", (sys.argv[4],))

    cities = cursor.fetchall()

    print(', '.join([city[0] for city in cities]))

    cursor.close()
    connection.close()
