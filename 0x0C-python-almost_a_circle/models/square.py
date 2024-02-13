#!/usr/bin/python3
""" module for square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns an informal representation of the Square instance """

        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__,
                self.id,
                self.x,
                self.y,
                self.width)

    @property
    def size(self):
        """ size of square (width and height) """
        return self.width

    @size.setter
    def size(self, value):
        """ set size of the square """
        self.width = value
        self.height = value

    def to_dictionary(self):
        """ dictionary representaion of Square class """
        attributes = ["id", "x", "size", "y"]
        dict = {}

        for key in attributes:
            if key == 'size':
                dict[key] = getattr(self, 'width')
            else:
                dict[key] = getattr(self, key)

        return dict
