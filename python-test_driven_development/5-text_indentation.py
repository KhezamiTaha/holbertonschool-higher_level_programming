#!/usr/bin/python3
"""
a function that prints  after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    code

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in [".", "?", ":"]:
            print(i)
            print()
        else:
            print("{}".format(i), end="")
