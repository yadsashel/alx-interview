#!/usr/bin/python3

""" a method that determines if all the boxes can be opened """

=======
def canUnlockAll(boxes):
    
    opened = [False] * len(boxes)
    opened[0] = True  

    keys = boxes[0]  

    while keys:
        key = keys.pop()
        
        if key < len(boxes) and not opened[key]:
            opened[key] = True  
            keys.extend(boxes[key]) 
>>>>>>> 784eb7b08060f0fb51cc231c6cd9ec92a66ae7dc

    return all(opened)
