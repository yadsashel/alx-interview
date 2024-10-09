# 0x01. Lockboxes

## Project Overview
In this project, you have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1`, and each box may contain keys to open other boxes. The goal is to write a function that determines if all the boxes can be unlocked.

### Key Points:
- **Boxes** are numbered from `0` to `n - 1`.
- Each box may contain keys to other boxes.
- The first box (`boxes[0]`) is unlocked by default.
- The task is to determine if all boxes can be unlocked using the available keys in the boxes.

## Requirements
- Write a method `canUnlockAll(boxes)` that determines if all boxes can be unlocked.
- The `boxes` parameter is a list of lists.
- Return `True` if all boxes can be opened, otherwise return `False`.
  
### Example:
```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Concepts and Techniques Used
- **Graph Traversal**: The boxes and keys can be represented as nodes and edges in a graph. This project involves traversing the graph to find if all boxes can be opened.
- **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** algorithms may be used to explore the available keys and boxes.
- **Set Operations**: Sets can be used to keep track of visited boxes and available keys.
- **List Manipulation**: The solution will involve dynamically accessing and modifying lists.

## Getting Started
### Prerequisites:
- Python 3.x (Tested on Python 3.4.3)
- Ubuntu 20.04 LTS or compatible system

### Installation:
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/YOUR_USERNAME/alx-interview.git
cd alx-interview/0x01-lockboxes
```

### Running the Program:
You can run the project with a `main` script as follows:
```bash
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

### Running Tests:
You can test your implementation by running test cases in Python:
```bash
python3 main_0.py
```

### Project Structure:
```bash
alx-interview
|--0x01-lockboxes
  |--0-lockboxes.py         # The main solution file
  |--README.md              # The readme file
  |--main_0.py              # Test file
```

## Code Style
Your code must follow the **PEP 8** style guidelines:
- Indentation: 4 spaces.
- Use meaningful variable names and comments.
  
To check for PEP 8 compliance, use the `pycodestyle` tool:
```bash
pycodestyle 0-lockboxes.py
```
