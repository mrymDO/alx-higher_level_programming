#!/usr/bin/python3
"""
Module: 9-rectangle.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    subclass of BaseGeometry representing a rectangle
    represents a rectangle with width and height as private attributes
    """

    def __init__(self, width, height):
        """instantiate an instance"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of a rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """     """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
