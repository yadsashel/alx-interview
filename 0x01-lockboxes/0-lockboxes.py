#!/usr/bin/python3

def canUnlockAll(boxes):
    # A list to keep track of which boxes are opened
    opened = [False] * len(boxes)
    opened[0] = True  # The first box is always opened

    # A list to keep track of keys to check
    keys = boxes[0]  # Start with keys from the first box

    while keys:
        key = keys.pop()  # Take a key from the list
        # If the key is valid and the box is not already opened
        if key < len(boxes) and not opened[key]:
            opened[key] = True  # Mark the box as opened
            keys.extend(boxes[key])  # Add keys from the newly opened box

    # Check if all boxes are opened
    return all(opened)

# Example usage
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # False
