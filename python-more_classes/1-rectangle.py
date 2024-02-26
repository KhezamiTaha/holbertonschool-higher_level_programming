#!/usr/bin/python3

"""
Rectangle height and weight
"""


class Rectangle:

    """
    A class representing a rectangle.

    This class provides a blueprint for creating rectangle objects.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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
