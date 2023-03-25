#!/usr/bin/python3
"""Script displays states in database by ascending id order
   Where state == arg[4]
   Script should take 4 arguments:
   mysql username, mysql password and database name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) > 3:
        link = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])

        curs = link.cursor()
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
        curs.execute(query.format(sys.argv[4]))
        for row in curs.fetchall():
            if row[1] == sys.argv[4]:
                print(row)
        curs.close()
        link.close()
