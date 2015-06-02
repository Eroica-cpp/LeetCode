#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 2, 2015
# Question: 032-Longest-Valid-Parentheses
# Link:     https://leetcode.com/problems/longest-valid-parentheses/
# ==============================================================================
# Given a string containing just the characters '(' and ')', find the length of 
# the longest valid (well-formed) parentheses substring.
# 
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# 
# Another example is ")()())", where the longest valid parentheses substring 
# is "()()", which has length = 4.
# ==============================================================================
# Method: Two pass; use extra memory to store flags
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        leftNum = i = 0
        size = len(s)
        flag = [0] * size

        while i < size:
            if s[i] == '(':
                leftNum += 1
            elif s[i] == ')'and leftNum > 0:
                leftNum -= 1
                j = i
                while flag[j] == 1 or s[j] == ')':
                    j -= 1
                flag[i] = 1
                flag[j] = 1
            i += 1

        maxVal = currentLen = 0
        for i in flag:
            if i == 1:
                currentLen += 1
            else:
                currentLen = 0
            maxVal = max(maxVal, currentLen)

        return maxVal

if __name__ == '__main__':
    s = "()()"
    s = ")()())"
    s = "(()"
    s = "()(()"
    s = "())()"  
    s = "()(())"
    s = "((()))"
    print Solution().longestValidParentheses(s)

