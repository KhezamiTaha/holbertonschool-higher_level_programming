#!/usr/bin/python3
"""
Module: 10-square
Description: Defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    This class inherits from Rectangle and provides functionality to validate
    and set the size of the square.
    """

    def __init__(self, size):
        """
        Initialize a new Square object.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
