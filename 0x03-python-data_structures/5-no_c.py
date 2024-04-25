#!/usr/bin/python3


def no_c(my_string):
    string_lst = list(my_string)

    for key, val in enumerate(string_lst):
        if val in ['c', 'C']:
            string_lst.pop(key)

    return "".join(string_lst)
