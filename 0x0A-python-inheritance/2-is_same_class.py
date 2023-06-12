#!/usr/bin/python3
"""
Module : 2-is_same_class
check if an object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """returns True if object is an instance other wise False"""
    return type(obj) == a_class
