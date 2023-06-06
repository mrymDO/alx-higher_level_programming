#!/usr/bin/python3
"""module that prevent creating instance attributes"""


class LockedClass:
    """a class with no class or object attribute"""
    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        """initialize first_name"""
        self.first_name = first_name
