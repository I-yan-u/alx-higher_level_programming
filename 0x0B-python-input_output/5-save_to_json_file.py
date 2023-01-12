#!/usr/bin/python3
"""
    5-save_t0_json_file: save_to_json_file()
"""
import json


def save_to_json_file(my_obj, filename):
    """
        saves JSON string to file.
    """
    with open(filename, "w") as json_file:
        json_str = json.dumps(my_obj)
        json_file.write(json_str)
