#!/usr/bin/python3
"""
Module: 100-my_int.py
"""


class MyInt(int):
    """subclass of int which inverse equality and inequality"""

    def __eq__(self, other):
        """Override the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator"""
        return super().__eq__(other)
