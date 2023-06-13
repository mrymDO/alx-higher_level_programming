#!/usr/bin/python3

"""Module: 0-read_file that defines a function that reads a text file"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, 'r', encoding='utf-8') as a_file:
        content = a_file.read()
        print(content, end="")
