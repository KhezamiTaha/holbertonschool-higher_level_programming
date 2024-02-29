#!/usr/bin/python3
"""
Checks if the given object is a subclass of
the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is a subclass of
    the specified class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
