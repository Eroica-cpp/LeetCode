#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 7, 2015
Question: 231-Power-of-Two
Link:     https://leetcode.com/problems/power-of-two/
==============================================================================
Given an integer, write a function to determine if it is a power of two.
==============================================================================
Method: loop
==============================================================================
"""

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        while n >= 2:
            if n % 2 == 1:
                return False
            n /= 2

        return True
