#!/usr/bin/python3
"""
Module: json_converter
Description: Provides a function to convert Python objects to JSON strings.
"""


import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string.

    Args:
        my_obj: The Python object to convert.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
