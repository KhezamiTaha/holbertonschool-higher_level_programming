#!/usr/bin/python3
"""
Module: file_reader
Description: Provides a function to read and
"""


def read_file(filename=""):
    """
    Read the contents of a file and print them to the console.

    Args:
        filename (str): The name of the file to read. Default

    Raises:
        FileNotFoundError: If the specified file is not found.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as filee:
        print(filee.read(), end="")
