#!/usr/bin/python3
"""
Docstring
"""


def inherits_from(obj, a_class):
    """
    Docstring
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
