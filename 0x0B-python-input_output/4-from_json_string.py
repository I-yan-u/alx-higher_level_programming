#!/usr/bin/python3
"""
    4-from_json_string: from_json_string()
"""
import json


def from_json_string(my_str):
    """
        Converts JSON string format python obj.
    """
    return json.loads(my_str)
