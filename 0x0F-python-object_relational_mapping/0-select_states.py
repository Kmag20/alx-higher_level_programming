#!/usr/bin/python3
""" Lists all states form the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM states')
    query = cursor.fetchall()
    [print(row) for row in query]
