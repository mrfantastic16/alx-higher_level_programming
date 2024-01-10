#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    add_0 = (0, 0)

    a = tuple_a + add_0
    b = tuple_b + add_0

    return a[0] + b[0], a[1] + b[1]
