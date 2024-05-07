#!/usr/bin/python3
"""

Module contains the print_square function that prints square

"""


def print_square(size):
    """Prints a square of height and width `size`

    Args:
        size: height and width of the square to be printed

    Returns: None

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
