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
Method: math formula
Time Complexity: O(log n)
Space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        counter, i = 0, 1
        while i <= n:
            a, b = n/i, n%i
            counter += (a+8)/10*i + int(a%10==1)*(b+1)
            i *= 10
        return counter
