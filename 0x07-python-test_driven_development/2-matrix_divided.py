#!/usr/bin/python3

"""
Module matrix_divided
Divides elements of a matrix of numbers by a number
"""


def matrix_divided(matrix, div):
    """Divides matrix with div.
    Returns a new matrix (list of list)
    with the result of the division of matrix by div
    rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for x in i:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    rows = []
    for i in matrix:
        rows.append(len(i))
    if not all(elem == rows[0] for elem in rows):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
