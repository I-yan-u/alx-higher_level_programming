#!/usr/bin/python3
"""
    6-load_from_json_file: load_from_json_file()
"""
import json


def load_from_json_file(filename):
    """
        saves JSON string to file.
    """
    with open(filename, "r") as json_file:
        my_obj = json_file.read()
        py_obj = json.loads(my_obj)
        return py_obj
