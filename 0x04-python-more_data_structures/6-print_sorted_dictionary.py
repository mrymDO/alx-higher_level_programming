#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    items = a_dictionary.items()
    sorted_items = sorted(items)
    for k, v in sorted_items:
        print("{}: {}".format(k, v))
