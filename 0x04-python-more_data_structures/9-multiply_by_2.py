#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {}
    for key, val in a_dictionary.items():
        newDict[key] = val * 2
    return newDict
