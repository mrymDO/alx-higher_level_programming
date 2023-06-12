#!/usr/bin/python3
"""
Module: 7-base_geometry.py
"""


class BaseGeometry:
    """
    Base class for geometry operations
    """
    def area(self):
        """
        Raises an exception indicating that area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it is an integer
        and greater than 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
