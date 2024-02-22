#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.


"""


def add_integer(a, b=98):
    """
    Add two integers or floats.
    """
   
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    elif not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
