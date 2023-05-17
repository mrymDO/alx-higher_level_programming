#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary)
    for k in sorted_dic:
        print("{} : {}".format(k, a_dictionary[k]))
