#!/usr/bin/python3


def no_c(my_string):
    string_lst = ""

    for key, val in enumerate(list(my_string)):
        if val not in ['c', 'C']:
            string_lst += val

    return string_lst
