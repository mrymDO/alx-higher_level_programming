#!/usr/bin/python3

def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='UTF8') as a_file:
        content = a_file.read()
        print(content)
