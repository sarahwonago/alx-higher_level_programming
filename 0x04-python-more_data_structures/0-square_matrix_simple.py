#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_list = [row[:] for row in matrix]
    for i, row in enumerate(squared_list):
        for i2, col in enumerate(squared_list):
            squared_list[i][i2] = row[i2] ** 2
    return squared_list
