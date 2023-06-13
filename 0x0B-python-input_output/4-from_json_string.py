#!/usr/bin/python3

"""Module: 4-from_json_string convert JSON string into Python data"""

import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""

    return json.loads(my_str)
