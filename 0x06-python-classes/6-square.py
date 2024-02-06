#!/usr/bin/python3
''' A square class '''


class Square:
    ''' Template for a square. '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialize the square.

        Parameters:
        - size (int): The size of the square (default is 0).
        - position (tuple): The position of the square (default is (0, 0)).
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        ''' Get the size of the square. '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Set the size of the square.

        Parameters:
        - value (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' Get the position of the square. '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Set the position of the square.

        Parameters:
        - value (tuple): The position of the square.

        Raises:
        - TypeError: If position is not a tuple of 2 positive integers.
        '''
        if (isinstance(value, tuple)
                and len(value) == 2
                and all(isinstance(i, int) and i >= 0 for i in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        ''' Calculate the area of the square. '''
        return self.__size ** 2

    def my_print(self):
        ''' Print a graphical representation of the square. '''
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__position[1]):
            print("")

        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end='')

            for k in range(0, self.__size):
                print("#", end='')

            print()
