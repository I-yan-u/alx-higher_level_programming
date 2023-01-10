#!/usr/bin/python3
"""
10-square.py: class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Rectangle subclass of BaseGeometry
    Attribute:
        size (int): size of the square
    Method:
        __init__ = initializes the square
    """
    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Calculates the area of the square obj
        """
        return self.__size * self.__size

    def __str__(self):
        """String representation of the object
        """
        return "[{}] \
{}/{}".format(type(self).__name__, self.__size)
