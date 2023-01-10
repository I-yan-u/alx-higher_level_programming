#!/usr/bin/python3
"""
7-base_geometry: class Basegeometry
"""


class BaseGeometry:
    """
    Basegeometry
    Attribute: None
    Method:
        area(): The area of an (BaseGeometry)Object
        integer_validator(): checks if value is allowed.
    """
    def area(self):
        """
        Area of a shape
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value as parseable
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
