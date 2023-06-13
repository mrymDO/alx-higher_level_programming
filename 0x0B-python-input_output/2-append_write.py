#!/usr/bin/python3

"""Module: 2-append_write that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    appends a string at end of text file
    returns number of character added
    """

    with open(filename, 'a', encoding='utf-8') as a_file:
        nb_char = a_file.write(text)
        return nb_char
