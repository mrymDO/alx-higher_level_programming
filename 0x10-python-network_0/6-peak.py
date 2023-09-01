#!/usr/bin/python3
""" module to find a peadk in a list of unsorted integers """


def find_peak(list_of_integers):
    """ find a peak in a list """
    n = len(list_of_integers)
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)

    mid = n // 2
    if (list_of_integers[mid] >= list_of_integers[mid + 1] and
            list_of_integers[mid] >= list_of_integers[mid - 1]):
        return list_of_integers[mid]
    elif list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
