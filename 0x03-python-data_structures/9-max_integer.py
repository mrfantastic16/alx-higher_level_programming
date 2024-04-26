#!/usr/bin/python3

def highest(arr):
    max_int = arr[0]

    for ar in arr:
        if ar > max_int:
            max_int = ar

    return max_int


def max_integer(my_list=[]):
    return None if len(my_list) <= 0 else highest(my_list)
