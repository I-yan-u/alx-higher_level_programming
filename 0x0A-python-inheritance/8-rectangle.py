#!/usr/bin/python3
"""
7-base_geometry: class Basegeometry
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
