#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    my_list[idx] = element if len(my_list) - 1 > idx >= 0 else my_list
    return my_list
