#!/usr/bin/python3
"""
    2-rectangle: Rectangle class
"""


class Rectangle:
    """
        class Rectangle.
        Attributes:
            width (int): Value for width of rectangle
            height (int): value for Height of rectangle
    """
    def __init__(self, width=0, height=0):
        """
            Initializes The class; Rectangle.
            Args:
                width (int): Value for width
                height (int): value for Height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

    @property
    def width(self):
        """
            Gets attribute of width
            Returns: Width
        """
        return self.__width

    @property
    def height(self):
        """
            Gets attribute of height
            Returns: Height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
            Sets attribute of width
            Args:
                value (int): New width value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
            Sets attribute of height
            Args:
                value (int): New height value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Area of Rectangle.
            Returns: area i.e (height * width)
        """
        return self.height * self.width

    def perimeter(self):
        """
            Perimeter of Rectangle.
            Returns: Perimeter i.e (2*(height + width))
        """
        solution = 0
        if self.width == 0 or self.height == 0:
            return solution
        solution = (2 * (self.height + self.width))
        return solution
