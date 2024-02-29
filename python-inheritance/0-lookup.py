#!/usr/bin/python3
"""
Module: mylookup
Description: Defines a function to inspect attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns the list of attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings containing the names of the attributes and methods
        of the given object.
    """
    return dir(obj)
