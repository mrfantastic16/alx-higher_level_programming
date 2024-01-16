#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = next(iter(a_dictionary))
    max_val = a_dictionary[max_key]

    for key, val in a_dictionary.items():
        if val > max_val:
            max_val = val
            max_key = key

    return (max_key)
