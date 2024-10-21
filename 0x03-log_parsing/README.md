# 0x03. Log Parsing

## Description
This project focuses on **log parsing** using **Python**. You will write a Python script that reads lines from standard input (stdin), parses the input logs, and computes statistics in real-time. The script will aggregate data such as file size and status codes, handling interruptions (CTRL + C) gracefully.

---

## Learning Objectives
By the end of this project, you will be able to:
- Read and parse input data from `sys.stdin` line by line.
- Use **regular expressions** to validate and extract data from strings.
- Compute aggregate statistics such as total file size and counts of HTTP status codes.
- Handle exceptions and interruptions in Python scripts.
- Work with **Python dictionaries** to store and update counts.
- Implement real-time data processing in Python.

---

## Key Concepts and Resources

- **File I/O in Python**:
  - [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- **Signal Handling**:
  - [Python Signal Handling](https://docs.python.org/3/library/signal.html)
- **Regular Expressions**:
  - [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- **Dictionaries in Python**:
  - [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- **Exception Handling**:
  - [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

---

## Requirements

- All your Python scripts will be interpreted on **Ubuntu 20.04 LTS** using Python 3.4.3.
- Your scripts should start with `#!/usr/bin/python3` on the first line.
- All your files should end with a new line.
- Your code should follow **PEP 8** style guidelines (version 1.7.x).
- Each Python file must be executable.
- A `README.md` file is mandatory at the root of the project folder.
- You will be tested on the file length using `wc`.

---

## Instructions

### Task: Log Parsing

Write a Python script `0-stats.py` that reads from **stdin** and computes metrics:

- **Input format**:
  ```
  <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
  ```
- **Metrics to compute**:
  - **Total file size**: Sum of all `<file size>` values.
  - **Status codes**: Count of each status code (200, 301, 400, 401, 403, 404, 405, 500).

- After every 10 lines or after a keyboard interruption (CTRL + C), print:
  - **File size**: `File size: <total size>`
  - **Status code counts**: `<status code>: <count>` (in ascending order).

---

### Example Usage

1. Run the generator script:
   ```bash
   ./0-generator.py | ./0-stats.py
   ```

2. Example output:
   ```
   File size: 5213
   200: 2
   401: 1
   403: 2
   404: 1
   405: 1
   500: 3
   ```

3. If interrupted with `CTRL + C`:
   ```
   ^CFile size: 17146
   200: 4
   301: 3
   400: 4
   401: 2
   403: 6
   404: 6
   405: 4
   500: 4
   ```

---

## How to Test

- You can simulate log data using the provided `0-generator.py` and pipe it to your script:
  ```bash
  $ ./0-generator.py | ./0-stats.py
  ```

---

## Repository

- **GitHub Repository**: `alx-interview`
- **Directory**: `0x03-log_parsing`
- **File**: `0-stats.py`

---

### License
This project is part of the **ALX SE Program**.
