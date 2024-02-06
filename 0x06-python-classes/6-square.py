#!/usr/bin/python3
''' A square class '''


class Square:
    ''' Template for a square. '''
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        if (type(value) == tuple and len(value) == 2 and
            all(isinstance(i, int) and i >= 0 for i in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            print('\n'.join(' ' * self.__position[0] + '#' * self.__size for _ in
                range(self.__size)))
