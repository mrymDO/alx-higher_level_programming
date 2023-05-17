#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    new_list = [replace if i == search else i for i in new_list]
    return new_list
