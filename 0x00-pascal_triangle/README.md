# pascal's Triangle

## Description

This project implements Pascal's Triangle in Python. Pascal's Triangle is a triangular array of the binomial coefficients. Each number is the sum of the two numbers directly above it. The purpose of this project is to develop a Python function that returns a list of lists, where each list represents a row of Pascal's Triangle.

## Requirements

Python 3.x
You must create a function pascal_triangle(n) that returns a list of lists of integers representing Pascal's triangle of n rows.
The project includes some basic Python concepts like:
Lists and list comprehensions.
Loops (nested loops).
Conditional statements.

## Tasks

### Task 0: Pascal's Triangle

Write a function def pascal_triangle(n): that returns a list of lists of integers representing Pascal's triangle of n rows.

Returns: An empty list if n <= 0.
Assumption: n will always be an integer.

### Example

```python
pascal_triangle(5)
```

### Output:

```python
[
  [1],
  [1, 1],
  [1, 2, 1],
  [1, 3, 3, 1],
  [1, 4, 6, 4, 1]
]
```
Repository
GitHub repository: alx-interview
Directory: 0x00-pascal_triangle
File: 0-pascal_triangle.py

### Solution

Here's the solution to implement Pascal’s Triangle in Python:

```python
def pascal_triangle(n):
    """
    Function to return Pascal's triangle of n rows.
    
    Args:
    n: Number of rows of Pascal's triangle
    
    Returns:
    List of lists where each inner list represents a row of Pascal's triangle.
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
```

### Explanation

Input validation:

If n <= 0, return an empty list.

### Building the triangle:

Start with the first row [1].
For each new row, begin and end with 1.
For the middle values, calculate the sum of the two numbers from the previous row that are directly above the current position.

### Output:

The function returns a list of lists, where each inner list represents a row of Pascal's Triangle.

### Example Usage

Here is  how you can use the function to generate and print Pascal's Triangle:

```python
def print_triangle(triangle):
    """
    Utility function to print Pascal's Triangle.
    """
    for row in triangle:
        print("[{}]".format(", ".join([str(x) for x in row])))

if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    print_triangle(triangle)
```

### Output:

```c##
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## Testing

To test the function, simply call pascal_triangle(n) where n is the number of rows you want. You can print the result using the print_triangle function.

## Author
Yazide Salhi

rt default function guardrail(mathFunction) {
  const queue = [];
  let value;

  try {
    value = mathFunction();
  } catch (err) {
    value = err.toString();
  }

  queue.push(value);
  queue.push('Guardrail was processed');

  return queue;
}

rt default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) {
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
e.

rt 

rt default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
}

rt default function createEmployeesObject(departmentName, employees) {
  return {
    [departmentName]: employees
  };
}

