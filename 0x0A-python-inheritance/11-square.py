#!/usr/bin/python3
"""
Module: 11-square.py
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """compute the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
