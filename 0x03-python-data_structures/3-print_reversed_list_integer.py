#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    j = len(my_list) - 1

    while j >= 0:
        print("{:d}".format(my_list[j]))
        j -= 1
