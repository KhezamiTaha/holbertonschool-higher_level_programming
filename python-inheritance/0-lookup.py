#!/usr/bin/python3
"""
Provides a function to inspect the attributes and methods of an object.
"""


def lookup(obj):
    """
    Return the list of attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings containing the names
        of the given object.
    """
    return dir(obj)
