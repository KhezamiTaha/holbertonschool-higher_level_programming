#!/usr/bin/python3
"""
Module: student
Description: Defines a Student class representing a student.
"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the Student object to a JSON serializable dictionary.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        if not isinstance(attrs, list) or \
                not all(isinstance(elem, str) for elem in attrs):
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    new_dict[key] = getattr(self, key)
            return new_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
