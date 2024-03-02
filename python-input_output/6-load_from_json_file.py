#!/usr/bin/python3
"""
Module: json_file_loader
Description: Provides a function to load JSON data from a
file into a Python object.
"""

import json


def load_from_json_file(filename):
    """
    Load JSON data from a file into a Python object.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        obj: The Python object representing the JSON data.
    """
    with open(filename, "r") as file:
        return json.load(file)
