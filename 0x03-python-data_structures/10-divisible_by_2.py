#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bool_lst = []

    for lst in my_list:
        bool_lst.append(True) if lst % 2 == 0 else bool_lst.append(False)

    return bool_lst
