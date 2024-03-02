#!/usr/bin/python3
"""
Module: json_file_writer
Description: Provides a function to save a Python object to a JSON file.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file.

    Args:
        my_obj: The Python object to save.
        filename (str): The name of the JSON file to save to.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
