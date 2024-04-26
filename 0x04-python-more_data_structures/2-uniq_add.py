#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set(my_list)
    uniq_sum = 0

    for it in uniq:
        uniq_sum += it

    return uniq_sum
