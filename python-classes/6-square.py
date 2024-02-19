#!/usr/bin/python3
"""
This module defines a class called Square.
"""


class Square:
    """
    This class represents a square shape.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object with the given side length and position.

        Args:
            size (int): The length of each side of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 integers.
            ValueError: If size is less than 0.
        """
        self.__position = position
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """int: The length of each side of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """
        Set the size of the square.

        Args:
            size (int): The new length of each side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """tuple: The position of the square."""
        return self.__position

    @position.setter
    def position(self, position):
        """
        Set the position of the square.

        Args:
            position (tuple): The new position of the square as a tuple of 2 integers.

        Raises:
            TypeError: If position is not a tuple of 2 integers.
        """
        if not isinstance(position, tuple) or len(position) != 2 or \
                not isinstance(position[0], int) or not isinstance(position[1], int) or \
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using '#' characters.

        Prints the square represented by '#' characters with each side
        having a length equal to the size of the square, and positioned
        according to the current position attribute.
        """
        for _ in range(self.__position[1]):
            print()
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
