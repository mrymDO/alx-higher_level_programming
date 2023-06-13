#!/usr/bin/python3

""" Module: 9-student"""


class Student():
    """defines a student by first_name, last_name, age"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""

        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__
