#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string:
        return 0
    conv = 0
    length = len(roman_string)
    for i in range(length):
        if i < length-1 and my_dic[roman_string[i]] < my_dic[roman_string[i+1]]:
            conv -= my_dic[roman_string[i]]
        else:
            conv += my_dic[roman_string[i]]
    return conv
