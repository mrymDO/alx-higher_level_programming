#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        res = 0
        total_weight = 0
        average = 0
        for tuples in my_list:
            score = tuples[0]
            weight = tuples[1]
            res += score * weight
        for tuples in my_list:
            total_weight += tuples[1]
        average = res / total_weight
        return average
    else:
        return 0
