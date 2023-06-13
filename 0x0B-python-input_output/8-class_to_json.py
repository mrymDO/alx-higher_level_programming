#!/usr/bin/python3
"""Module : 8-class_to_json"""


def class_to_json(obj):
    """
    Takes an object instance as input
    Returns dictionary representation of that object
    """

    result = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, bool, str, int, dict)):
            result[key] = value
    return result
