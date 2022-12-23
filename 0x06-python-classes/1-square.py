#!/usr/bin/python3
""" Module contains: class Square """


class Square():
    """
        Square: defines a square.
        Attributes:
            size (no type or value identification): size of square.
        Method:
            __init__ : init of square class with each attribute.
    """

    def __init__(self, size):
        """
            Initialization of attributes to instances.
            Args:
                size (no type): size of square.
        """
        self.__size = size
