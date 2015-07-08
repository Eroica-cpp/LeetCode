#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 8, 2015
Question: 233-Number-of-Digit-One
Link:     https://leetcode.com/problems/number-of-digit-one/
==============================================================================
Given an integer n, count the total number of digit 1 appearing in all 
non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
==============================================================================
Method: brute force
Time Complexity: Exp
Space Complexity: Exp
Note: OK but apparently "Memory Limit Exceeded"
==============================================================================
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        stack = [str(i) for i in xrange(1,n+1)]
        return "".join(stack).count("1")
