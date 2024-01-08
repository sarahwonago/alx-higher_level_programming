#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for num in i:
            print("{:d}".format(num), end=" " if num != i[-1] else "$")
        print()
