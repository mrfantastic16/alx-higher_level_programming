#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_lst = my_list[:]

    if 0 <= idx < len(new_lst):
        new_lst[idx] = element

    return new_lst
