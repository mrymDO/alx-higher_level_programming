#!/usr/bin/python3
"""
Module: 101-add_attribute.py
"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object"""
    if not hasattr(obj, attr):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
