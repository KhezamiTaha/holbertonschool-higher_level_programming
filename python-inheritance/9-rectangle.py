#!/usr/bin/python3
"""
Module: 8-rectangle
Description: Defines a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    This class inherits from BaseGeometry and provides functionality
    and set the width and height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
