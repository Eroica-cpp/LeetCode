#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 5, 2015
# Question: 050-Pow
# Link:     https://leetcode.com/problems/powx-n/
# ==============================================================================
# Implement pow(x, n).
# ==============================================================================
# Method: Binary Search
# Time Complexity: O(logN)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1/float(self.myPow(x, -n))
        elif n == 1:
            return x
        else:
            tmp = self.myPow(x, n/2)
            return tmp*tmp if n%2 == 0 else tmp*tmp*x