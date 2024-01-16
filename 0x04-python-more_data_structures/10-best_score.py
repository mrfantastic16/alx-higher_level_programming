#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    key_lst = list(a_dictionary.keys())
    value_lst = list(a_dictionary)

    max_val = max(value_lst)
    indx_max_val = value_lst.index(max_val)

    return key_lst[indx_max_val]