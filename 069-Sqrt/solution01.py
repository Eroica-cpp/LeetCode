#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 3, 2015
# Question: 069-Sqrt
# Link:     https://leetcode.com/problems/sqrtx/
# ==============================================================================
# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
# ==============================================================================
# Method: Newton Formula
# ==============================================================================

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, a):
        if a < 0:
            return -1
        elif a == 0:
            return 0

        x = 1.
        last = float('inf')
        while abs(last-x) >= 0.1**10:
            last = x
            x = (x + a/x) / 2

        return int(x)

if __name__ == '__main__':
    print Solution().mySqrt(3)