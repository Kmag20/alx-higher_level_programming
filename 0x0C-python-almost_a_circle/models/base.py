#!/usr/bin/python3

class Base:
    """" Represent the base model.

    Represents the "base" for all other clasess in 0x0c*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0;

    def __init__(self, id=None):
        """ Initialize a new base.

        Args:
            id(int): The identitiy of the new Base.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else if id is not None:
            self.id = id
        else:
            if self is None:
                

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
