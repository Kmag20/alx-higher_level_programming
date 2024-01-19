#!/usr/bin/python3
""" Module for Base class"""
import json


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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_dictionary(list_dictionaries):
        """ returns json representation of list dicts """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
