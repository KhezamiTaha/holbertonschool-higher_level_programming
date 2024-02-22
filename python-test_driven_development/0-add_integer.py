#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.


"""


def add_integer(a, b=98):
    """
    Add two integers or floats.

    Args:
        a: The first number to add.
        b: The second number to add. Default is 98.

    Returns:
        The sum of a and b, cast to an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    elif not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
