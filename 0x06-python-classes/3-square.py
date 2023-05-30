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
        Raises:
             TypeError: If size is not an integer
             ValueError: If size is less than 0
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size
