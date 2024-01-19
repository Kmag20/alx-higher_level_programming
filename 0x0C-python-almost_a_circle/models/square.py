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
