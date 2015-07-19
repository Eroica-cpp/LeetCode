#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 19, 2015
Question: 161-One-Edit-Distance
Link:     https://leetcode.com/problems/one-edit-distance/
==============================================================================
Given two strings S and T, determine if they are both one edit distance apart.
==============================================================================
Method: use two stacks
Time Complexity: O(n)
Space Complexity: O(n) 
==============================================================================
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isOneEditDistance(self, s, t):
        stack1 = [i for i in s]
        stack2 = [j for j in t]

        while stack1 and stack2 and stack1[-1] == stack2[-1]:
            stack1.pop()
            stack2.pop()

        stack1.reverse()
        stack2.reverse()

        while stack1 and stack2 and stack1[-1] == stack2[-1]:
            stack1.pop()
            stack2.pop()

        return (len(stack1) == 1 and not stack2) or (len(stack2) == 1 and not stack1) or (len(stack1) == len(stack2) == 1)
