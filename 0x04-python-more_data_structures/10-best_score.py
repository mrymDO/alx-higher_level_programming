#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        values = list(a_dictionary)
        max = values[0]
        for i in range(len(values)):
            if values[i] > max:
                max = values[i]
        return max
