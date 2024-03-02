#!/usr/bin/python3
"""
Module: file_appender
Description: Provides a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Append text to a file.

    Args:
        filename (str): The name of the file to append to.
            Default is an empty string.
        text (str): The text to append to the file.
            Default is an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf-8") as filee:
        return filee.write(text)
