#!/usr/bin/python3
''' Square module with attribute and method '''


class Square:
    ''' Used to intialize a new square
    Args:
        size (int): size of the new square
    '''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("ize must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        ''' Returns current area of the square '''
        return (self.__size * self.__size)
