#!/usr/bin/python3
"""
Defines a custom list class that extends the built-in list class.
"""


class MyList(list):

    """
    A custom list class that extends the built-in list class.

    This class provides additional functionality to print the list sorted.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.
        """
        print(sorted(self))
