#!/usr/bin/python3
"""
Module: 4-inherits_from
Checks if an object is an instance of a class that inherited
from a specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """return True or False"""
    return isinstance(obj, a_class) and type(obj) != a_class
