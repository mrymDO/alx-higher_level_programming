#!/usr/bin/python3

"""
Print a square with the character #.
"""


def print_square(size):
    """
    Returns a square printed with the character #,
    or raises errors if size is not an int or less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
