#!/usr/bin/python3
"""Defining class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Representing rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing new Rectangle.
        Args:
            width (int): new Rectangle width.
            height (int): new Rectangle height.
            x (int): x coordinate of Rectangle.
            y (int): y coordinate of Rectangle.
            id (int): identity of new Rectangle.
        Raises:
            TypeError: If neither height nor width is an int.
            ValueError: If neither height nor width <= 0.
            TypeError: If neither of x or y is an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):

        """Setter for width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        
        """Get height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):

        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

