#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """ square class """
    def __init__(self, size=0):
        """ Initialize the square class """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
