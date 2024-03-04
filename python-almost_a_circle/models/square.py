#!/usr/bin/python3
"""
Module: square
Desc: Defines Square class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        size (int): Length of each side of the square.
        x (int): X-coordinate of the square's position.
        y (int): Y-coordinate of the square's position.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            Initializes a Square object with optional id.
        __str__(self):
            Returns a string representation of the Square object.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): Length of each side of the square.
            x (int): X-coordinate of the square's position. Default is 0.
            y (int): Y-coordinate of the square's position. Default is 0.
            id (int): Optional identifier for the Square object.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string representation of the Square object.
        """
        return ("[Square] (" + str(self.id) + ") " +
                str(self.x) + "/" + str(self.y) + " - " +
                str(self.width))

    @property
    def size(self):
        """int: Length of each side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value
        self.width = value
        self.height = value
