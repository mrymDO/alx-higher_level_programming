#!/usr/bin/python3
"""
Multiplies two matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using numpy
    Returns new matrix, the result of multiplication of m_a and m_b
    """
    result = np.matmul(m_a, m_b)
    return result.tolist()
