#!/usr/bin/python3

"""Module: 6-load_from_json_file creates an object from a "JSON file" """

import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""

    with open(filename, 'r') as a_file:
        json_data = a_file.read()
        return json.loads(json_data)
