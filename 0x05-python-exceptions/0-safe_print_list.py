#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    new_list = []

    for i in range(0, x):
        try:
            new_list.append(my_list[i])
        except IndexError:
            pass

    i = 0
    for el in new_list:
        print(f"{el}", end="")
        i += 1

    print()
    return (i)
