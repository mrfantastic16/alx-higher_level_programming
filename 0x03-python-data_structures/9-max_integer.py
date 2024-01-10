#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    max_n = my_list[0]

    for lst in my_list:
        if lst > max_n:
            max_n = lst

    return max_n
