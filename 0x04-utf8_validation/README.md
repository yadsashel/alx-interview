# 0x04. UTF-8 Validation

This project focuses on validating UTF-8 encoding in Python. Through bitwise operations and the UTF-8 encoding scheme, the goal is to determine if a dataset accurately represents a valid UTF-8 encoding. This project will enhance understanding of data representation, bitwise manipulation, and Python programming skills.

## Project Details
- **Project Start**: Oct 28, 2024, 4:00 AM
- **Deadline**: Nov 1, 2024, 4:00 AM
- **Languages**: Python (interpreted on Ubuntu 20.04 LTS, Python 3.4.3)
- **Concepts Used**:
  - Bitwise operations
  - UTF-8 encoding
  - Boolean logic
  - List manipulation
  - Data representation

## Learning Objectives
- Apply bitwise operations to determine the structure of byte-level data.
- Validate data against the UTF-8 encoding scheme.
- Build Python functions using list manipulations and logical operations.

## Requirements
- **Editor**: vi, vim, emacs
- **Interpreter**: Python 3.4.3 on Ubuntu 20.04 LTS
- **File Requirements**:
  - Files must end with a new line.
  - First line: `#!/usr/bin/python3`
  - Style: Follow PEP 8 (version 1.7.x)
  - Executable files
- **Repository Structure**:
  - GitHub repository: `alx-interview`
  - Directory: `0x04-utf8_validation`
  - File: `0-validate_utf8.py`

## Function Description
The project includes one mandatory function:

### `def validUTF8(data):`
- **Parameters**:
  - `data`: A list of integers representing bytes of data.
- **Returns**:
  - `True` if `data` represents a valid UTF-8 encoding, else `False`.
- **UTF-8 Encoding Rules**:
  - A character can be 1 to 4 bytes long.
  - Only the 8 least significant bits of each integer need to be handled.
  
## Example Usage

Given `data = [65]`, the function should return `True` because `65` (binary: `01000001`) is valid UTF-8.

```python
data = [65]
print(validUTF8(data))  # Output: True
```

For a list like `data = [229, 65, 127, 256]`, the function should return `False` since `256` is not a valid byte (exceeds 8 bits).

```python
data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## Concepts and Resources
- **Bitwise Operations**:
  - Learn bitwise operations such as `&`, `|`, `^`, `~`, `<<`, `>>` in Python to manipulate binary data effectively.
- **UTF-8 Encoding**:
  - Refer to [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8) and **Unicode Character Sets** for encoding patterns.
- **Data Representation and List Manipulation**:
  - Python lists and integer handling allow byte-level data simulation.

## Additional Resources
- Mock technical interviews and guides on bitwise operations.
  
## Testing
You can test the function with the provided `0-main.py` file:
```python
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
```
