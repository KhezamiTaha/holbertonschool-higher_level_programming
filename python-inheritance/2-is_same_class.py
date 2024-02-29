#!/usr/bin/python3
"""
Module: is_same_class
Description: Provides a function to check if an object
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance
    """
    if type(obj) is a_class:
        return True
    else:
        return False
