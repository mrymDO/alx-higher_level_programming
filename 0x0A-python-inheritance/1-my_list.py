#!/usr/bin/python3
"""
Module: 1-my_list
A class that inherits form list
"""


class MyList(list):
    """print a list in a sorted ascending order"""
    def print_sorted(self):
        print(sorted(self))
