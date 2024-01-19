#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the rectangle.
        __y (int): Y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle (default is 0).
            y (int, optional): Y-coordinate of the rectangle (default is 0).
            id (int, optional): Unique identifier (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, positive=True):
        """Method for validating all setter methods and instantiation"""

        if not isinstance(value, (int, bool)):
            raise TypeError("{} must be an integer".format(name))
        if positive and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not positive and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ Area of rectangle
        Area = width x height
        """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle instance using #(hashes) inclusive of x a
        nd y cartisian planes"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print("".join(" " for _ in range(self.__x)), end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ return informat string representation of an instance """
        return "[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__,
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute in the *args """

        i = 0
        attribute = ["id", "width", "height", "x", "y"]
        if args:
            for arg in args:
                setattr(self, attribute[i], arg)
                i += 1
        else:
            if kwargs:
                for arg, value in kwargs.items():
                    setattr(self, arg, value)

    def to_dictionary(self):
        """ returns the dictionary representaion of a Rectangle """
        attributes = ["x", "y", "id", "height", "width"]
        dict = {}

        for key in attributes:
            dict[key] = getattr(self, key)

        return dict
