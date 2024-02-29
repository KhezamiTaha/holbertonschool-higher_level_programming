#!/usr/bin/python3
"""
Module: is_same_class
Description: Provides a function to check if an object
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
