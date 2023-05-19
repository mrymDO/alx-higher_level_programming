#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, Value in list(a_dictionary.items()):
        if Value == value:
            del a_dictionary[key]
    return a_dictionary
