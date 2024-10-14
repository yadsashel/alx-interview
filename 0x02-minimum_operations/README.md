# Minimum Operations

## Overview

In this project, we will solve the problem of calculating the fewest number of operations needed to reach exactly `n` characters using only two operations: **Copy All** and **Paste**. The goal is to determine how many steps are required to generate a text with exactly `n` characters starting from one character (`H`).

## Operations

1. **Copy All**: This operation copies all the current content in the file.
2. **Paste**: This operation pastes the copied content into the file, effectively doubling the characters.

### Problem Statement

Given an integer `n`, the method `minOperations(n)` returns the minimum number of operations required to reach exactly `n` characters starting from a single `H` character.

- If `n` is impossible to achieve, return `0`.

### Example

```python
n = 9

# Sequence of operations:
H -> Copy All -> Paste -> HH -> Paste -> HHH -> Copy All -> Paste -> HHHHHH -> Paste -> HHHHHHHHH

# Number of operations: 6
```

### Prototype

```python
def minOperations(n: int) -> int:
    """Calculate the minimum number of operations required to reach exactly `n` characters."""
```

### Logic and Approach

To solve the problem, we leverage the concept of **prime factorization**:

- The problem can be broken down into multiplying and copying groups of characters to match the prime factors of the target `n`.
- If `n` is divisible by a number `i`, then the fewest operations needed for `n` includes `i` operations to replicate the characters in groups.

### Example of Operations Count:

For `n = 12`:

- Prime factorization of 12: 2 × 2 × 3.
- Steps:
  1. Copy All (1st operation), Paste (2nd operation) to get 2 characters.
  2. Paste (3rd operation) to get 4 characters.
  3. Copy All (4th operation), Paste (5th operation) to get 8 characters.
  4. Paste (6th operation) to get 12 characters.

Total number of operations: 7.

### Requirements

- Python 3.4.3+
- Your code should be PEP 8 compliant.
- All files should be executable.

### Installation

To run this project:

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/alx-interview.git
```

2. Navigate to the project directory:

```bash
cd 0x02-minimum_operations
```

3. Run the test file:

```bash
./0-main.py
```
