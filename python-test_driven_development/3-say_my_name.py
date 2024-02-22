#!/usr/bin/python3
"""
code module


"""
def say_my_name(first_name, last_name=""):
    """
    Print the name with the given first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Default is "".

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is", first_name)
