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
        Initializes a new Square object with the given side length.

        Args:
            size (int): The length of each side of the square. Default is 0.
            position : the position of the square

        Raises:
            TypeError: If size is not an integer.
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
        return self.__position

    @position.setter
    def position(self, position):
        boollen = self.__position[0] >= 0 and self.__position[1]
        if len(self.__position) == 0 and boollen:
            self.__position == position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        having a length equal to the size of the square.
        """
        for i in range(self.__position[1]):
            print()
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
