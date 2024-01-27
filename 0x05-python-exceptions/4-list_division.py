#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_lst = []

    for i in range(0, list_length):
        try:
            if all(isinstance(x, (int, float)) for x in (my_list_1[i], my_list_2[i])):
                res_lst.append(my_list_1[i] / my_list_2[i])
            else:
                print("wrong type")
                res_lst.append(0)
        except ZeroDivisionError:
            print("division by 0")
            res_lst.append(0)
        except IndexError:
            print("out of range")
            res_lst.append(0)

    return res_lst
