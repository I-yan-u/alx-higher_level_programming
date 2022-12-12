#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
        key_list = sorted(a_dictionary)
        for key in key_list:
            print("{}: {}".format(key, a_dictionary[key]))
