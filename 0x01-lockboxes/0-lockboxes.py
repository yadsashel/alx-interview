#!/usr/bin/python3

def canUnlockAll(boxes):
    
    opened = [False] * len(boxes)
    opened[0] = True  

    keys = boxes[0]  

    while keys:
        key = keys.pop()
        
        if key < len(boxes) and not opened[key]:
            opened[key] = True  
            keys.extend(boxes[key]) 

    return all(opened)

boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1)) 

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
