#!/usr/bin/python3
"""
4-inherits_from: inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    Function to check if an object belongs to a class or superclass
    Args:
        obj (object): The object to compare
        a_class (class): The class to be compared to
    Returns: True or False
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
