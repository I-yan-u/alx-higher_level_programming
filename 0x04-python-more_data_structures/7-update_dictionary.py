#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        for key1, value1 in a_dictionary.items():
            if key1 == key:
                a_dictionary[key1] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
