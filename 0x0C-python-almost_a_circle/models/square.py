#!/usr/bin/python3
"""Defines square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): size of new Square.
            x (int): x coordinate of Square.
            y (int): y coordinate of Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square.
        Args:
            *args (int): New attribute values.
                - first argument represent the id attribute
                - second argument represents size attribute
                - third argument represents x attribute
                - forth argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
  
    def __str__(self):
        """Return a string representation of the Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
