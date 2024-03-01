#!/usr/bin/python3
"""
Module: BaseGeometry
Description: Defines a base class for geometric shapes.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
