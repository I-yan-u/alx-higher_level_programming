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
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
            getter function for private attribute size.
            Returns:
                size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            setter function for private attribute size.
            Args:
                value: value to be set.
            Returns:
                nothing.
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
