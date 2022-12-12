#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    score = 0
    name = None
    for key in a_dictionary.keys():
        if score == 0 or a_dictionary[key] > score:
            score = a_dictionary[key]
            name = key
    return name
