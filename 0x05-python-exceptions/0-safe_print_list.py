#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for num in my_list[:x]:
            count += 1
            print("{}".format(num), end="")
    except IndexError:
        pass
    print()
    return count
