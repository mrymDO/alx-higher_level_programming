#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    def sqr(n):
        return n ** 2

    for row in matrix:
        new_row = list(map(sqr, row))
        new_matrix.append(new_row)
    return new_matrix
