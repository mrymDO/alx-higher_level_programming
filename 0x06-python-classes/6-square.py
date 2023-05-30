#!/usr/bin/python3
"""Define class Square"""


class Square:
    """
    This class defines a square by its size
    Attributes:
           size (int): The size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with the given size
        args:
             size (int): the size of the square.
        Raises:
             TypeError: If size is not an integer
             ValueError: If size is less than 0
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter methid for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position"""
        if isinstance(value, tuple) and len(value) == 2 and \
                isinstance(value[0], int) and isinstance(value[1], int):
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise ValueError("position values must be >= 0")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
