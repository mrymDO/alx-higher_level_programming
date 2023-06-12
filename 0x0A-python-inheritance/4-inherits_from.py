#!/usr/bin/python3
"""Module: 4-inherits_from
Check if the object is an instance from a class
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class inherited from a class
    Returns True ptherwise False
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
