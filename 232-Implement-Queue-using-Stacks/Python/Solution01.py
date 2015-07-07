#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 7, 2015
Question: 232-Implement-Queue-using-Stacks
Link:     https://leetcode.com/problems/implement-queue-using-stacks/
==============================================================================
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Notes:

1. You must use only standard operations of a stack -- which means only push to 
top, peek/pop from top, size, and is empty operations are valid.

2. Depending on your language, stack may not be supported natively. You may 
simulate a stack by using a list or deque (double-ended queue), as long as 
you use only standard operations of a stack.

3. You may assume that all operations are valid (for example, no pop or peek 
operations will be called on an empty queue).
==============================================================================
Method: naive method; python build-in
==============================================================================
"""

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.items = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.items.append(x)        

    # @return nothing
    def pop(self):
        self.items.pop(0)

    # @return an integer
    def peek(self):
        return self.items[0]

    # @return an boolean
    def empty(self):
        return not self.items
