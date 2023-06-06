#!/usr/bin/python3

"""
A Module that print first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Returns My name is <first name> <last name>,
    or raises errors if first_name and last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name and last_name:
        print("My name is {} {}".format(first_name, last_name))
    elif first_name or last_name:
        print("My name is {}{}".format(first_name, " " +
              last_name if last_name else ""))
    else:
        print("My name is")
