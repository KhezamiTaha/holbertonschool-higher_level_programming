#!/usr/bin/python3
"""
Module: is_same_class
Description: Provides a function to check if an object inherits from a specific class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specific class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if the object inherits from the specified class and is not the same class,
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
