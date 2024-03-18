#!/usr/bin/python3
""" List all cities from a database """

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    cursor = conn.cursor()
    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities \
                   JOIN states ON states.id = cities.state_id;')
    query = cursor.fetchall()
    [print(row) for row in query]
