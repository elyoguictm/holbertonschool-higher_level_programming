#!/usr/bin/python3
""" Lazy matrix multiplication module """

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices
    Args:
        m_a (list): first matrice
        m_b (list): second matrice
    Return:
        m_c (list): the result matrice
    """
    m_c = np.matmul(m_a, m_b)
    return m_c
