# 0x07. Rotate 2D Matrix

## Description
This project involves implementing an in-place algorithm to rotate a square \( n \times n \) 2D matrix by 90 degrees clockwise. The task challenges you to manipulate data structures efficiently without creating additional copies, emphasizing optimization of both time and space complexity.

## Learning Objectives
By completing this project, you will:
- Understand how 2D matrices are represented and manipulated in Python.
- Learn about in-place operations to optimize memory usage.
- Practice matrix transposition and row reversal techniques for rotations.
- Enhance your problem-solving skills in Python through algorithmic thinking.

## Requirements
- **Python Version**: Python 3.8.10
- **Platform**: Ubuntu 20.04 LTS
- **Style Guide**: Pycodestyle (version 2.8.0)
- **File Requirements**:
  - All files must start with `#!/usr/bin/python3`.
  - All files must be executable and end with a new line.
- **Prohibited**:
  - You are not allowed to import any modules.

## Task
### **0. Rotate 2D Matrix**
- **Prototype**: `def rotate_2d_matrix(matrix):`
- **Objective**: Modify the given \( n \times n \) matrix in-place to rotate it 90 degrees clockwise.
- **Constraints**:
  - Do not return a new matrix.
  - Assume the matrix is non-empty and always 2-dimensional.

### Example
#### Input:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

#### After Rotation:
```python
matrix = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Concepts Needed
- **Matrix Representation in Python**: Lists of lists.
- **In-place Operations**: Direct modifications to the original data structure.
- **Matrix Transposition**: Swap rows and columns of a matrix.
- **Reversing Rows**: Reverse the elements of each row for the final rotation.
- **Nested Loops**: Iterating through 2D arrays.

## Steps to Rotate the Matrix
1. **Transpose the Matrix**:
   - Convert rows into columns.
2. **Reverse Each Row**:
   - Reverse the elements in each row to achieve a clockwise rotation.

## Usage
Create a file `0-rotate_2d_matrix.py` and implement the function `rotate_2d_matrix(matrix)`. Test it using the following script:
```bash
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

#### Output:
```bash
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Resources
- **Matrix Manipulation**: [GeeksforGeeks - Inplace Rotate Matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- **Python Lists**: [Official Python Docs - Lists](https://docs.python.org/3/tutorial/datastructures.html)
- **Matrix Transposition**: [Transpose a Matrix in Python](https://www.geeksforgeeks.org/python-transpose-matrix/)

## Repository
- **GitHub Repo**: `alx-interview`
- **Directory**: `0x07-rotate_2d_matrix`
- **File**: `0-rotate_2d_matrix.py`
