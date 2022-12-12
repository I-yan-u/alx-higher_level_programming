#!/usr/bin/python3
def search_replace(my_list, search, replace):
    index = 0
    new_list = []
    for num in my_list:
        index += 1
        if num != search:
            new_list.append(num)
        else:
            new_list.append(replace)
    return new_list
