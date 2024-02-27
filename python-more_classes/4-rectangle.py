#!/usr/bin/python3

"""
This script defines a Rectangle class with properties for width and height,
"""


class Rectangle:

    """
    Constructor for the Rectangle class, initializing a rectangle with the
    given width and height values. Defaults to zero if no values are provided.
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """
    int: The width of the rectangle.
    """

    @property
    def width(self):
        return self.__width

    """
    Set the width of the rectangle.

    Args:
        value (int): The new width of the rectangle.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """
    int: The height of the rectangle.
    """

    @property
    def height(self):

        return self.__height

    """
    Set the height of the rectangle.

    Args:
        value (int): The new height of the rectangle.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height * self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """
        str doc
        """
        if self.__height * self.__width == 0:
            return ""
        return ((("#" * self.__width) + "\n") * (self.__height - 1)) + (
            "#" * self.__width
        )

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(
            self.__height) + ")"
