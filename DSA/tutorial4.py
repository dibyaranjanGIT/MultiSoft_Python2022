"""
Array conatins a collection of homogeneous items
"""

import array
arr = array.array('i', [1,2,3,4])
arr1 = array.array('f', [1,2,3,4])


# print(arr)
# print(arr1)

# adding one element to the array
arr.append(20)
print(arr)

# To remvoe one element in the array
arr.pop()
print(arr)

# slicing
print(arr[2:4])


##################
"""
Stack 
it works on the concept of Lifo
LIFO - Last in first out 
"""

class Stack:
    def __init__(self):
        self.my_stack = array.array('i', [])

    def is_empty(self):
        if len(self.my_stack) == 0:
            return False
        else:
            return True

    def push(self, element):
        self.my_stack.append(element)

    def pop(self, element):
        self.my_stack.pop(element)