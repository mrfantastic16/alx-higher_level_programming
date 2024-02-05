#!/usr/bin/python3
''' A square module. '''


class Square:
    ''' Class with a private instance size which
    cannot be negative or not be a number. It is also optional

    Args:
    size: param 1
    '''

    def __init__(self, size=0):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
