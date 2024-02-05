#!/usr/bin/python3
''' Defines a class Module, Square with private instance '''


class Square:
    ''' Defines a square with a private instance
    Arg:
        size: size of the square
    '''

    def __init__(self, size):
        self.__size = size
