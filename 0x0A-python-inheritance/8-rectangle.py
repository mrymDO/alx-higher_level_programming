#!/usr/bin/python3
"""
Module: 8-rectangle.py
Creates Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    subclass of BaseGeometry representing a rectangle
    represente a rectangle with width and height as private attributes
    """

    def __init__(self, width, height):
        """instantiate an instance"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
