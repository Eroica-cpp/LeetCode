#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 21, 2015
Question: 029-Divide-Two-Integers
Link:     https://leetcode.com/problems/divide-two-integers/
====================================================================================
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
====================================================================================
Method: Naive Method
Time Complexity: O(n)
Space Complexity: O(1)
Note: TLE
====================================================================================
"""

MAX_INT = 2**31-1

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if dividend >= MAX_INT or divisor >= MAX_INT or divisor == 0:
            return MAX_INT

        flag = 1 if dividend*divisor >= 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)

        counter = 0
        while dividend >= divisor:
            dividend -= divisor
            counter += 1

        return flag * counter

if __name__ == '__main__':
    dividend, divisor = -5, 1
    print Solution().divide(dividend,divisor)