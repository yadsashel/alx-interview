#!/bin/bash/python3
""" 
function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal's triangle of n 
"""

def pascal_triangle(n):
    """
    Function to return Pascal's triangle of n rows.
    
    Args:
    n (int): Number of rows of Pascal's triangle.
    
    Returns:
    List[List[int]]: List of lists where each inner list represents a row of Pascal's triangle.
    """
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Build the triangle row by row
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        # Compute the values in between the first and last element
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)
    
    return triangle
