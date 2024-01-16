#!/usr/bin/python3

def weight_average(my_list=[]):
    total_value = 0
    total_weight = 0

    for tup in my_list:
        total_value += (tup[0] * tup[1])
        total_weight += tup[1]

    return (total_value / total_weight if total_weight != 0 else 0)
