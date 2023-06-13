#!/usr/bin/python3

""" Module: 9-student"""


class Student():
    """defines a student by first_name, last_name, age"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""

        return {
            "first_name":  self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
