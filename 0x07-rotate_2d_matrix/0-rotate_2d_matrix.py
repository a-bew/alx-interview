#!/usr/bin/python3
"""
Solution to the 0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix in-place
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse the order of the columns in-place
    for row in matrix:
        row.reverse()
