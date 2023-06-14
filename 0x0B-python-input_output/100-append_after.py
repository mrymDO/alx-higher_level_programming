#!/usr/bin/python3

""" Module 100-append_after """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of a text to a file
    after each line containing a specific string
    """

    with open(filename, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i]

            if search_string.lower() in line:
                lines.insert(i + 1, new_string)
        file.seek(0)

        file.writelines(lines)

        file.truncate()
