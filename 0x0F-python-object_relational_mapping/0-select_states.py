#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM `states`')
    query = cursor.fetchall()
    [print(row) for row in query]
