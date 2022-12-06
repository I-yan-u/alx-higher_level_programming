#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    while l:
        print("{:d}".format(my_list[l-1]))
        l -= 1
