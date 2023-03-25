#!/usr/bin/python3
"""Script displays cities in database by ascending id order
   based on states table
   Script should take 3 arguments:
   mysql username, mysql password and database name
"""


import MySQLdb
import sys

if len(sys.argv) > 3:
    link = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3])

    cur = link.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
    INNER JOIN states ON cities.state_id = states.id ORDER BY id ASC;"
    cur.execute(query)
    for row in cur.fetchall():
        print(row)

    cur.close()
    link.close()