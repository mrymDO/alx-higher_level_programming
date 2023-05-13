#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [elem % 2 == 0 for elem in my_list]
    return new_list
