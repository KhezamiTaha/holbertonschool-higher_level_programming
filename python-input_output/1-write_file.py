#!/usr/bin/python3
"""
Module: file_writer
Description: Provides a function to write
"""


def write_file(filename="", text=""):
    """
    Write text to a file.

    Args:
        filename (str): The name of the file to write to. Default
        text (str): The text to write to the file. D

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as filee:
        return filee.write(text)
