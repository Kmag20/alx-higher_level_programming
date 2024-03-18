#!/usr/bin/python3
""" Lists all states with a name starting with N """

import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    cursor = conn.cursor()
    cursor.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS \
    LIKE 'N%';")
    query = cursor.fetchall()
    [print(row) for row in query]
