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

    def __init__(self, size=0):
        """
            Initialization of attributes to instances.
            Args:
                size (no type): size of square.
        """
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size
