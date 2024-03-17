#!/usr/bin/python3
""" Takes an argument and displays values in the table
    where name matches the argument """

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM\
                   states WHERE name = '{}'".format(sys.argv[4]))
    query = cursor.fetchall()
    [print(row) for row in query]
