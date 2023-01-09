#!/usr/bin/python3


def lookup(obj):
    """returns the list of available attributes and method in an object
    Args:
        obj (object): An object
    """
    return dir(obj)
