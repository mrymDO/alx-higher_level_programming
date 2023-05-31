#!/usr/bin/python3
"""Create a square class"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """returns current square area"""
        return self.size ** 2

    def my_print(self):
        """prints the square with the qcharacter # """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """string representation of the square"""
        square_str = ""
        if self.size == 0:
            return square_str
        else:
            for _ in range(self.position[1]):
                square_str += "\n"
            for _ in range(self.size):
                square_str += " " * self.position[0] + "#" * self.size + "\n"
        return square_str.rstrip()
