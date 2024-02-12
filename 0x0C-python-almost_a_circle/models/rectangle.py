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

    def area(self):
        """Calculate and return the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Display the Rectangle with # characters"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (int): New attribute values.
                - first argument represents id attribute
                - second argument represents width attribute
                - third argument represent height attribute
                - forth argument represents x attribute
                - fifth argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """Return a string representation of the Rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
