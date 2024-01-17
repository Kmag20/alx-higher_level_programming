#!/usr/bin/python3

from base import Base

class Rectangle(Base):
    def __init__(self, width, height, x, y, id):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")

            self.__width = width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("Height must be an integer")
            if value < 0:
                raise ValueError("height must be > 0")

            self.__height = height
           
        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
        


