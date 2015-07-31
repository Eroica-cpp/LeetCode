#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 020-Valid-Parentheses
# Link:     https://leetcode.com/problems/valid-parentheses/
# ==============================================================================
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" are all valid 
# but "(]" and "([)]" are not.
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif i in [')', ']', '}'] and stack and pairs[stack[-1]] == i:
                stack.pop()
            else:
                return False

        return not stack