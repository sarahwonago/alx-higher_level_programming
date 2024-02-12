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

    def __str__(self):
        """Return a string representation of the Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

