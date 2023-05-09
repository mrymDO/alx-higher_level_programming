#!/usr/bin/python3
def remove_char_at(str, n):
    str_c = str[:]
    while (n >= 0):
        for i in range(len(str_c)):
            if i == n:
                continue
            return str_c[:n] + str_c[n+1:]
    else:
        return str
