#!/usr/bin/python3
"""Define class Square"""


class Square:
    """
    This class defines a square by its size
    Attributes:
           size (int): The size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with the given size
        args:
             size (int): the size of the square.
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
                print(size)
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
