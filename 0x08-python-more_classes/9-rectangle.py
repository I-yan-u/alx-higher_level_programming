#!/usr/bin/python3
"""
    9-rectangle: Rectangle class
"""


class Rectangle:
    """
        class Rectangle.
        Attributes:
            width (int): Value for width of rectangle
            height (int): value for Height of rectangle
            number_of_instances (int): number of instance
    """
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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

    def __str__(self):
        """
            String representation of Rectangle
            Returns:
                Default: '#' grid format of rectangle
        """
        output = ''
        if self.width == 0 or self.height == 0:
            return output
        for high in range(self.height - 1):
            for wide in range(self.width):
                output += str(self.print_symbol)
            output += '\n'
        output += str(self.print_symbol) * self.width
        return output

    def __repr__(self):
        """
           String representation of rectangle object
        """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """ Delete a Rectangle instance """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    def bigger_or_equal(rect_1, rect_2):
        """Comparison method.
            Args:
                rect_1 (Rectangle): Fisrt rectangle for comparison
                rect_2 (Rectangle): second rectangle for comparison
            Return: larger rectangle, rect_1 if both are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Class Method; converts Rectangle to square.
            Args:
                size (int): New Square size.
            Return:
                Returns a Square.
        """
        return cls(size, size)
