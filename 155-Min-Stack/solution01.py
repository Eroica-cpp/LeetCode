#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 15, 2015
# Question: 155-Min-Stack
# Link:     https://leetcode.com/problems/min-stack/
# ==============================================================================
# Design a stack that supports push, pop, top, and retrieving the minimum 
# element in constant time.
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# ==============================================================================
# Method: Maintain two stacks: one of it records minVal info
# ==============================================================================

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.minVal = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.minVal or x <= self.minVal[-1]:
            self.minVal.append(x)

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if self.minVal[-1] == x:
            self.minVal.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minVal[-1]
