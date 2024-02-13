#!/usr/bin/python3
"""Defines the base model class."""


class Base:
    """ Base model class
    The  class will be the “base” of all other classes in this project.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Base objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """Initializing a new Base.
        Args:
            id (int): New Base Id representing identity of object.
        """

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
