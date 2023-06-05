#!/usr/bin/python3
"""
Module that defines a rectangle
"""


class Rectangle:
    """
    a class Rectangle that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with specified width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter methode to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method to set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method to set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
