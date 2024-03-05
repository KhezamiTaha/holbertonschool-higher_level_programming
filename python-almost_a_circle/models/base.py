#!/usr/bin/python3
"""
Module: base
Desc: Defines Base class with identifier.
"""
import json


class Base:
    """
    Base class for objects with an identifier.

    Attrs:
        __nb_objects (int): Number of objects created.

    Methods:
        __init__(self, id=None): Initializes object with optional id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int): Optional identifier. If not provided,
                      assigns incremented object count.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances.

        Notes:
            - If list_objs is None, an empty list will be saved.
            - The filename is <Class name>.json.
            - The file will be overwritten if it already exists.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dictonary_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(dictonary_list))
