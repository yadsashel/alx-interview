# **0x09. Island Perimeter**

## **Description**
This project focuses on solving a geometric problem within a 2D grid: calculating the perimeter of an island represented by `1`s in a grid filled with `0`s (water) and `1`s (land). The goal is to implement a function `def island_perimeter(grid):` that determines the total perimeter of the island while adhering to the constraints and requirements outlined.

---

## **Learning Objectives**
By completing this project, you will:
- Understand how to navigate and manipulate 2D arrays (matrices).
- Implement conditional logic to solve algorithmic problems.
- Practice Python programming techniques such as nested loops and conditional statements.
- Adhere to coding standards like PEP 8 while documenting code effectively.

---

## **Requirements**
### **General**
- Use editors like `vi`, `vim`, or `emacs`.
- Code will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3 (version 3.4.3)**.
- Files must end with a new line and start with the shebang `#!/usr/bin/python3`.
- Create a `README.md` file at the root of the project directory.
- Code must follow the **PEP 8 style guide (version 1.7)**.
- No external modules or imports are allowed.
- All modules and functions must include proper documentation.
- All files must be executable.

---

## **Task**
### **0. Island Perimeter**
**Mandatory**

Create a function `def island_perimeter(grid):` that calculates the perimeter of the island described in the grid.

#### **Specifications**
- **Input:**
  - `grid`: A list of lists of integers where:
    - `0` represents water.
    - `1` represents land.
  - Each cell is square with a side length of `1`.
  - Cells are connected horizontally or vertically (not diagonally).
  - The grid is rectangular, with a maximum width and height of `100`.
  - The grid is completely surrounded by water.
  - There is only one island or nothing.
  - The island doesn’t have "lakes" (water inside the island not connected to the surrounding water).

- **Output:**
  - An integer representing the perimeter of the island.

---

## **Example**
### **Input Grid:**
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

### **Output:**
```python
12
```

### **Test File Example (`0-main.py`):**
```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
```

### **Command Line Execution:**
```bash
$ ./0-main.py
12
```

---

## **Concepts Needed**
### 1. **2D Arrays (Matrices):**
   - Learn how to iterate over rows and columns.
   - Understand adjacent cells (top, bottom, left, right).

### 2. **Conditional Logic:**
   - Determine when a cell contributes to the island's perimeter:
     - If a cell is land (`1`), its edges contribute to the perimeter unless adjacent to another land cell.

### 3. **Counting Techniques:**
   - Count the edges of land cells contributing to the perimeter.

---

## **Implementation Strategy**
1. **Iterate through the grid:**
   - Use nested loops to access each cell in the matrix.

2. **Check for land cells:**
   - If a cell is `1`, calculate its contribution to the perimeter.

3. **Handle adjacent cells:**
   - Subtract edges shared with neighboring land cells.

4. **Return the perimeter:**
   - After iterating through the grid, return the total perimeter.

---

## **Resources**
### Documentation
- [Python Lists (Official Docs)](https://docs.python.org/3/tutorial/datastructures.html)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)

### Tutorials
- [GeeksforGeeks: Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-multi-dimensional-arrays/)
- [YouTube: Python 2D Lists and Matrices](https://www.youtube.com)

---

## **Repository Details**
- **GitHub Repository:** `alx-interview`
- **Directory:** `0x09-island_perimeter`
- **File:** `0-island_perimeter.py`
