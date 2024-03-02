#!/usr/bin/python3
"""
Script: add_to_json_file
Description: Appends command-line arguments to a JSON file.
"""


import sys
from os.path import exists

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def main():
    """
    Append command-line arguments to a JSON file.

    If the JSON file exists, it loads its content into a list,
    then appends the command-line arguments to the list.
    Finally, it saves the combined list back to the JSON file.

    If the JSON file does not exist, it creates a new list
    containing only the command-line arguments and saves it
    to the JSON file.

    Args:
        None

    Returns:
        None
    """
    listy = sys.argv[1:]
    filename = "add_item.json"

    if exists(filename):
        try:
            list2 = load_from_json_file(filename)
            list_final = list2 + listy
        except Exception as e:
            print(f"Error loading data from '{filename}': {e}")
            list_final = listy
    else:
        list_final = listy

    save_to_json_file(list_final, filename)


if __name__ == "__main__":
    main()
