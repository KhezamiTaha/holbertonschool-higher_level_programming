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

    # Initialize an empty string to store the formatted text
    formatted_text = ""

    # Iterate through each character in the text
    for char in text:
        # Append the current character to the formatted text
        formatted_text += char

        # If the current character is '.', '?', or ':', add 2 new lines
        if char in (".", "?", ":"):
            formatted_text += "\n\n"

    # Print the formatted text without leading or trailing spaces
    print("\n".join(line.strip() for line in formatted_text.split("\n")))
