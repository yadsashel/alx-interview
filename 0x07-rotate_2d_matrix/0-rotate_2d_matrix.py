#!/usr/bin/python3
"""
Rotate 2D Matrix: Rotate a given n x n matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix in place by 90 degrees clockwise.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.

    Returns:
        None: The matrix is modified in place.
    """
    # Step 1: Transpose the matrix (swap rows with columns)
    n = len(matrix)  # Get the size of the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
