#!/usr/bin/python3
"""
This module defines a class called Square.
"""


class Square:
    """
    This class represents a square shape.
    """

    def __init__(self, size):
        """
        Initializes a new Square object with the given side length.

        Args:
            size(int): The length of each side of the square.
        """
        self.__size = size
