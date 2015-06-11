#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 11, 2015
# Question: 225-Implement-Stack-using-Queues
# Link:     https://leetcode.com/problems/implement-stack-using-queues/
# ==============================================================================
# Implement the following operations of a stack using queues.
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# 
# Notes:
# 
# 1. You must use only standard operations of a queue -- which means only push 
# to back, peek/pop from front, size, and is empty operations are valid.
# 
# 2. Depending on your language, queue may not be supported natively. You may 
# simulate a queue by using a list or deque (double-ended queue), as long 
# as you use only standard operations of a queue.
# 
# 3. You may assume that all operations are valid (for example, no pop or top 
# operations will be called on an empty stack).
# ==============================================================================
# Method: Naive method
# ==============================================================================

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.items = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.items.append(x)

    # @return nothing
    def pop(self):
        self.items.pop()

    # @return an integer
    def top(self):
        return self.items[-1]

    # @return an boolean
    def empty(self):
        return len(self.items) == 0
