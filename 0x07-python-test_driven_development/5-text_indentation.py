#!/usr/bin/python3

"""
Print a text with 2 new lines after the charachters: '.', '?', ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after eaach occurrence of '.', '?'and ':'.
    Or raises error if test is not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ".?:"
    for char in punctuations:
        lines = text.split(char)
        for i in range(len(lines)):
            lines[i] = lines[i].strip(" ")
        text = (char + "\n" * 2).join(lines)
    print("{}".format(text), end="")
