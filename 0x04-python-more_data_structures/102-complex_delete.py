#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = dict(a_dictionary)
    for k, v in new_dict.items():
        if v == value:
            a_dictionary.pop(k)
    return a_dictionary
