#!/usr/bin/python3
"""A module to multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(sublist_a, list) for sublist_a in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(sublist_b, list) for sublist_b in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or any(sublist_a == [] for sublist_a in m_a):
        raise ValueError("m_a can't be empty")
    if m_b == [] or any(sublist_b == [] for sublist_b in m_b):
        raise ValueError("m_b can't be empty")
    for sublist_a in m_a:
        if len(sublist_a) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for i in sublist_a:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for sublist_b in m_b:
        if len(sublist_b) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for j in sublist_b:
            if not isinstance(j, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)
    return result
