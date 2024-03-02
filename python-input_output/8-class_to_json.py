#!/usr/bin/python3
"""object to JSON string representation."""


def class_to_json(obj):
    """Converts a class object to JSON string representation."""

    return obj.__dict__
