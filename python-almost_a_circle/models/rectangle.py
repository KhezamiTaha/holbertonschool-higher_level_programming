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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        elif isinstance(value, bool):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """int: Height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        elif isinstance(value, bool):
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def x(self):
        """int: X-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: Y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area ofthe rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the rectanglr in #"""
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            print(f'{" " * self.__x}{self.__width * "#"}')

    def __str__(self):
        """str for the print function"""
        return ("[Rectangle] (" + str(self.id) + ") " +
                str(self.__x) + "/" + str(self.__y) + " - " +
                str(self.__width) + "/" + str(self.__height))

    def update(self, *args, **kwargs):
        """update for the print function"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return the dict representation"""
        return {'id': self.id, 'width': self.__width,
                "height": self.__height, 'x': self.__x, 'y': self.__y}
