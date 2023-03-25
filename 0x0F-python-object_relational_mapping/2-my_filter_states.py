#!/usr/bin/python3
"""Script displays states in database by ascending id order
   Where state starts with "N"
   Script should take 3 arguments:
   mysql username, mysql password and database name
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) > 3:
        link = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])

        curs = link.cursor()
        curs.execute("""SELECT * FROM states ORDER BY states.id ASC""")
        for row in curs.fetchall():
            if row[1] == sys.argv[4]:
                print(row)
        curs.close()
        link.close()
