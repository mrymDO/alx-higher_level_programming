#!/usr/bin/python3

"""
A Module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a marix by div.
    Returns the quotient matrix rounded two decimal places,
    or raises errors for invalid inputs.
    """

    if not isinstance(matrix, list) or not\
            all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError(
                   "matrix must be a matrix (list of lists) of integers/floats"
                )

    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]
    return new_matrix
