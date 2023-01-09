#!/usr/bin/python3
"""
3-is_kind_of_class: is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if an object belongs to a class or superclass
    Args:
        obj (object): The object to compare
        a_class (class): The class to be compared to
    Returns: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
