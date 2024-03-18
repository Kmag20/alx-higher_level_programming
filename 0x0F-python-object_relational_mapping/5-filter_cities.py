#!/usr/bin/python3
""" A script that takes in a name of a state as an argument and lists
    all cities of the state """

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    cursor = conn.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                   JOIN states ON cities.state_id = \
                   states.id WHERE states.name = '{}';".format(sys.argv[4]))
    states = cursor.fetchall()
    print(", ".join([state[0] for state in states]))
