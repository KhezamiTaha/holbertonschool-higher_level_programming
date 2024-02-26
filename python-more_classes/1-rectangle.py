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
        """
        initiantion
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
