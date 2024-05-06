#!/usr/bin/python3
"""

This module has one function - add_integer(a, b=98): -
that returns the addition of two number

"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b. Floats are
    typecast to ints before addition

    Args:
        a: param 1
        b: param 2

    Returns:
        int(param1) + int(param2)

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
