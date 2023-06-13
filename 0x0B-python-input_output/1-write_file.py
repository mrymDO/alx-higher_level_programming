#!/usr/bin/python3

"""Module: 1-write_file that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    a function that swrite a string to a text file
    Returns number of characters
    """

    with open(filename, 'w', encoding='utf-8') as a_file:
        num_char = a_file.write(text)
        return num_char
