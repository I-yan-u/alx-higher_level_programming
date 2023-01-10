#!/usr/bin/python3
"""
9-rectangle.py: class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle subclass of BaseGeometry
    Attribute:
        width (int): Width of the rectangle
        height (int): height of the rectangle
    Method:
        __init__ = initializes the Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle obj
        """
        return self.__width * self.__height

    def __str__(self):
        """String representation of the object
        """
        return "[{}] \
{}/{}".format(type(self).__name__, self.__width, self.__height)
