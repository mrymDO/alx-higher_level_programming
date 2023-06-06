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

    punctuations = ['.', '?', ':']
    lines = text.splitlines()

    for line in lines:
        line = line.strip(" ")
        if line:
            for char in punctuations:
                line = line.replace(char, char + '\n\n')
            print(line, end="")
        else:
            print()
