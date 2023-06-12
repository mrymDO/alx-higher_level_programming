#!/usr/bin/python3
"""
Module: 5-base_geometry.py
"""


class BaseGeometry():
    def area(self):
        """returns error if area() is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
