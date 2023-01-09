#!/usr/bin/python3
"""
2-is_same_class: is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    Function to check if an object belongs to a class
    Args:
        obj (object): The object to compare
        a_class (class): The class to be compared to
    Returns: True or False
    """
    if type(obj).__name__ == a_class.__name__:
        return True
    else:
        return False
