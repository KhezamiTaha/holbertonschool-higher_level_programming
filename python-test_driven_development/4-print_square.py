#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """
    Print a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if size is a float less than 0.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####
        >>> print_square(10)
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        >>> print_square(0)
        (no output)
        >>> print_square(1)
        #
        >>> print_square(-1)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
        >>> print_square(3.5)
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
