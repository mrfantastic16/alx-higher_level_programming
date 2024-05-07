#!/usr/bin/python3
"""

This module provides the say_my_name function

"""


def say_my_name(first_name, last_name=""):
    """Prints received parameters in the format
    `My name is {first_name} {last_name}`

    Args:
        first_name: param1 to be printed
        last_name: optional param2

    Returns: None

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
