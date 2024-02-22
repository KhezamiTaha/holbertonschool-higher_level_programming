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

    dlm = [".", "?", ":"]
    modified_text = ""
    line = ""

    for ch in text:
        line += ch
        if ch in dlm:
            print(line.strip(" ") + "\n")
            line = ""

    if line:
        print(line.strip(" "))

    print(modified_text, end="")
