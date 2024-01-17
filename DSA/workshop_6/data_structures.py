# Arrays
# list() is the implementation of dynamic arrays in python
from queue import LifoQueue
from collections import deque
l = [3, 2, 5, 1]

# operations
l.append(6)  # O(1) amortized
l.remove(5)  # best case: O(1), worst case: O(n)
l.index(1)  # best case: O(1), worst case: O(n)
len(l)  # O(1)
print(l[3])  # access by index: O(1)

# Stack
# There is no built-in data structure for stack in Python, but it can be implemented by list

stack1 = []  # creating an empty stack
stack1.append(1)  # O(1)
stack1.append(3)
stack1.append(5)

stack1.pop()  # removes last element, O(1)
last_element = stack1.pop()  # can store the last element in a new variable

# stacks can also be implemented by Python modules


stack2 = deque()

stack2.append('a')
stack2.append('b')
stack2.append('c')

stack2.pop()
stack2.pop()

# using queue module


stack3 = LifoQueue()
