#!/usr/bin/python3

"""
Module: 7-add_item
adds all arguments to a python list, and save them to a file
"""

import sys
save_json = __import__("5-save_to_json_file")
load_json = __import__("6-load_from_json_file")

a_list = load_json.load_from_json_file("add_item.json")

for arguments in sys.argv[1:]:
    a_list.append(arguments)

save_json.save_to_json_file(a_list, "add_item.json")
