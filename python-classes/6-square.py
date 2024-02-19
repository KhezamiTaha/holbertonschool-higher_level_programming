#!/usr/bin/python3
class Square:
    """
    Represents a square.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square's sides. Defaults to
            position (tuple, optional): The position of the square. Defaults
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square's sides.

        Args:
            value (int): The size of the square's sides.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter for the position"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.

        If the size is 0, it prints an empty line. If the position is greater
        it prints spaces before printing the '#' characters to adjust for the
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
