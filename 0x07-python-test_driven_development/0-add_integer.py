#!usr/bin/python3
"""
Module add-integer
Adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers together.
    Returns the sum of a and b or raises an error
    if a and b are not integers or floats
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a+b
