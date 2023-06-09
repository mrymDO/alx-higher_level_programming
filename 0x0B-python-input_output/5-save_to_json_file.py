#!/usr/bin/python3

"""
Module: 5-save_to_json_file that writes an OBject to a text file
using JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """writes object to a text file"""

    with open(filename, 'w') as a_file:
        json_string = json.dumps(my_obj)
        a_file.write(json_string)
