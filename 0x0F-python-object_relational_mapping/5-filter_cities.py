#!/usr/bin/python3
"""Script displays cities in database by ascending id order
   from states table
   Script should take 4 arguments:
   mysql username, mysql password and database name
"""


import MySQLdb
import sys

if len(sys.argv) > 3:
    link = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = link.cursor()
    query = "SELECT c.name, c.state_id, states.name FROM cities AS c \
        INNER JOIN states ON c.state_id = states.id \
        ORDER BY c.state_id ASC;"

    query_list = []
    cur.execute(query)
    for row in cur.fetchall():
        if row[2] == sys.argv[4]:
            query_list.append(row[0])
    out = ', '.join(query_list)
    print(out)

    cur.close()
    link.close()
