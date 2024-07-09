#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """Prevents user from instantiating a new class"""

    __slots__ = ["first_name"]

