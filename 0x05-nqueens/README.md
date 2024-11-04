# 0x05. N Queens

## Description
The **N Queens** problem is a classic challenge in computer science and mathematics, where the goal is to place N non-attacking queens on an N×N chessboard. This project utilizes the **backtracking** algorithm to find all possible arrangements of queens on the board such that no two queens threaten each other.

This project demonstrates the application of backtracking, recursion, and efficient data manipulation, and provides experience with Python command-line arguments and coding to meet specific project requirements.

## Requirements
- **Python Version**: Python 3.4.3 (compiled on Ubuntu 20.04 LTS)
- **PEP 8 Style Guide**: Follow PEP 8 style guidelines (version 1.7.\*)
- **Executable files**: All scripts must be executable
- **File Header**: The first line of each file should be `#!/usr/bin/python3`

## Concepts and Skills
To succeed in this project, you'll need to be familiar with:
- **Backtracking Algorithms**: Exploring possible solutions and backtracking when necessary.
- **Recursion in Python**: Using recursive functions to implement the backtracking logic.
- **List Manipulations**: Storing and managing the positions of queens.
- **Command-Line Arguments**: Parsing command-line input with the `sys` module.

### Resources
- [Backtracking Introduction](https://www.geeksforgeeks.org/backtracking-introduction/)
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Command-Line Arguments in Python](https://docs.python.org/3/library/sys.html)

## Usage
To solve the N Queens problem for a board size \( N \), run the program as follows:
```bash
./0-nqueens.py N
```

### Input Conditions
- `N` must be an integer greater than or equal to 4.
- If `N` is not an integer or is less than 4, the program will print an appropriate error message and exit.

### Output
Each solution is printed on a new line in the format:
```plaintext
[[row, col], ...]
```
For example:
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Example
```bash
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
...
```

## Tasks
### Task 0: N Queens
- **Objective**: Write a program to solve the N Queens problem.
- **Constraints**: Handle command-line arguments and validate input to ensure \( N \) is an integer \(\geq 4\).
- **Implementation Details**: The program should only import the `sys` module.

## Project Directory
- **GitHub Repository**: [alx-interview](https://github.com/alx-interview)
- **Project Directory**: `0x05-nqueens`
- **File**: `0-nqueens.py`
