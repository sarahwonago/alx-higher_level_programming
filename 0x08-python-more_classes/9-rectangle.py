#!/usr/bin/python3

"""Module 9-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with values.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += str(self.print_symbol)
            rec_str += '\n'
        return rec_str[:-1]        

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        """Retrieves the width of a Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle

        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle

        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

       """Computes the area of a Rectangle.
       Returns:
           int: The area of a Rectangle.
       """

       return self.__width * self.__height

    def perimeter(self):

       """ Computes the perimeter of a Rectangle.
       Returns:
           int: The perimeter of a Rectangle.
       """

       if self.__width == 0 or self.__height == 0:
           return 0

       return self.__width * 2 + self.__height * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the biggest or equal area value between two Rectangles
        Args:
            rect_1 (Rectangle): The first Rectangle to compare
            rect_2 (Rectangle): The second Rectangle to compare
        Returns:
            Rectangle: The biggest Rectangle, or `rect_1` if the
            two Rectangles have the same area value.
        Raises:
            TypeError: If `rect_1` or `rect_2` aren't an instance
            of the Rectangle class.
        """

        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        rct1_area = rect_1.area()
        rct2_area = rect_2.area()

        if rct1_area >= rct2_area:
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size.
        Args:
            size: size of the square
        Returns:
            Rectangle: A new Rectangle instance representing a square.
        """
        return cls(size, size)
