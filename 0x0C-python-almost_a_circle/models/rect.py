#!/usr/bin/python3
""" Rectangle class inherits from Base Class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width setter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
        Args:
            w(int) -> width of the rectangle
        Raises:
            TypeError -> if value is not an integer
            ValueError -> if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Height setter """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter
        Args:
            h(int) -> Height of the rectangle
        Raises:
            TypeError -> if value is not an integer
            ValueError -> if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter
        Args:
            x(int) -> value of x
        Raises:
            TypeError -> if x is not an int
            ValueError -> if x < 0
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter
        Args:
            y(int) -> value of y
        Raises:
            TypeError -> if y is not an integer
            ValueError -> if y < 0
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif x < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
