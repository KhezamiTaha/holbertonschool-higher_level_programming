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
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string representation"""
        return json.dumps(list_dictionaries)
