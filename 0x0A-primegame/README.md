# **0x0A. Prime Game**

## **Overview**
This project involves solving a competitive game scenario using **prime numbers**, **game theory**, and **algorithm optimization**. Players Maria and Ben take turns removing prime numbers and their multiples from a set of integers. The winner is the player who makes the last move.

Your task is to determine the winner across multiple rounds of the game, assuming both players play optimally.

---

## **Table of Contents**
1. [Project Details](#project-details)
2. [Requirements](#requirements)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Example Input and Output](#example-input-and-output)
6. [Files in the Repository](#files-in-the-repository)

---

## **Project Details**
- **Game Rules:**
  1. The game is played with integers from `1` to `n` (inclusive).
  2. Players take turns picking a prime number and removing it along with its multiples from the set.
  3. The player unable to make a move loses the game.
  4. Maria always starts, and both players play optimally.

- **Inputs:**
  - `x`: Number of game rounds.
  - `nums`: An array where each element specifies the upper limit of the integers for that round.

- **Output:**
  - The name of the player who wins the most rounds (`Maria` or `Ben`).
  - If neither player wins the majority, return `None`.

---

## **Requirements**
- **Languages and Tools:**
  - Python 3.4.3 or later.
  - No external libraries or packages allowed.
- **Coding Standards:**
  - Follow PEP 8 style guidelines.
  - Include the shebang `#!/usr/bin/python3` in all scripts.
  - Ensure all files are executable.
- **System Environment:**
  - Ubuntu 20.04 LTS.

---

## **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alx-interview.git
   ```

2. Navigate to the project directory:
   ```bash
   cd alx-interview/0x0A-primegame
   ```

3. Make the script executable:
   ```bash
   chmod +x 0-prime_game.py
   ```

---

## **Usage**
Run the script to determine the winner of the game:
```bash
./0-prime_game.py
```

To test with custom input:
1. Modify the input values in the script `main_0.py`:
   ```python
   isWinner = __import__('0-prime_game').isWinner
   print("Winner: {}".format(isWinner(3, [4, 5, 1])))
   ```

2. Execute the script:
   ```bash
   ./main_0.py
   ```

---

## **Example Input and Output**
### **Input:**
```python
x = 3
nums = [4, 5, 1]
```

### **Execution:**
```bash
./main_0.py
```

### **Output:**
```
Winner: Ben
```

---

## **Files in the Repository**
- **`0-prime_game.py`:** Contains the implementation of the `isWinner` function.
- **`main_0.py`:** Example script for testing the `isWinner` function.

---
