#!/usr/bin/python3
"""Defines class: Base"""


class Base:
    """ Base class
    The  class Base  will be the “base” of all other classes in this project.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Base objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """Initializing a new Base.
        Args:
            id (int): New Base Id.
        """

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
