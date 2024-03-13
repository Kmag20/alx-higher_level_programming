#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """ class Square """
    def __init__(self, size=0):
        """ Initialize a square class """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ Returns the area of the square """
        return self.__size ** 2

    @property
    def size(self):
        """ Getter method for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for size """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
