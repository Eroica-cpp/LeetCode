#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 6, 2015
Question: 251-Flatten-2D-Vector
Link:     https://leetcode.com/problems/flatten-2d-vector/
==============================================================================
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements 
returned by next should be: [1,2,3,4,5,6].

Hint:

1. How many variables do you need to keep track?
2. Two variables is all you need. Try with x and y.
3. Beware of empty rows. It could be the first few rows.
4. To write correct code, think about the invariant to maintain. What is it?
5. The invariant is x and y must always point to a valid point in the 2d vector. 
   Should you maintain your invariant ahead of time or right when you need it?
6. Not sure? Think about how you would implement hasNext(). Which is more complex?
7. Common logic in two different places should be refactored into a common method.

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.
==============================================================================
Method: use a linked list
Note: trivial in python
==============================================================================
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Vector2D:

    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.dummy = ListNode(-float('inf'))
        p = self.dummy
        for i in vec2d:
            for j in i:
                p.next = ListNode(j)
                p = p.next
        self.curr = self.dummy.next

    # @return {integer}
    def next(self):
        tmp = self.curr.val
        self.curr = self.curr.next
        return tmp

    # @return {boolean}
    def hasNext(self):
        return self.curr

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    vec2d = [[1,2], [3], [4,5,6]]
    i, v = Vector2D(vec2d), []
    while i.hasNext(): v.append(i.next())
    print v