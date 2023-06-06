#!/usr/bin/python3

"""
This module provides a function for adding two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the addition of a and b
    Or Error if a or b are not int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
