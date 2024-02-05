#!/usr/bin/python3
''' Define a Square Class '''


class Square:
    ''' A square template to
    Args:
        size (int): size of sqauere sizes
    '''

    def __init__(self, size=0):
        '''Intializing a new square. '''
        self.size = size

    @property
    def size(self):
        '''Get the current size of square. '''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''Return the area of the sqaure'''
        return (self.__size * self.__size)
