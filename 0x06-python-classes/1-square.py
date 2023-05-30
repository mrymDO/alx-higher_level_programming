#!/usr/bin/python3
"""Define class Square"""


class Square:
    """
    This class defines a square by its size
    Attributes:
           size (int): The size of the square
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size
        args:
             size (int): the size of the square.
        """
        self.__size = size
