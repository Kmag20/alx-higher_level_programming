#!/usr/bin/python3
""" Displays all values in the states table of the database """

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in cursor.fetchall() if state[1] == sys.argv[4]]
