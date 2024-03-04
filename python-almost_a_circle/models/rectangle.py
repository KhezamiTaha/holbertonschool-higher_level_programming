#!/usr/bin/python3
"""
Module: rectangle
Desc: Defines Rectangle class.
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle's position.
        y (int): Y-coordinate of the rectangle's position.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a Rectangle object with optional id.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle's position. Default is 0.
            y (int): Y-coordinate of the rectangle's position. Default is 0.
            id (int): Optional identifier for the Rectangle object.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """int: Width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """int: Height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """int: X-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """int: Y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
