#!/usr/bin/python3
"""
Module: is_same_class
Description: Provides a function to check if an object inherits from a specific class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is a subclass of
    the specified class.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
