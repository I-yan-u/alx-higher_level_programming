#!/usr/bin/python3
from sys.stderr import write

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as Err:
        write("Exception: " + str(Err) + "\n")
        return False
