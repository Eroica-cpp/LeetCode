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
Method: binary search
Time Complexity: O(log n)
Space Complexity: O(1)
Note: MAX_INT is 2**31-1 and MIN_INT is -2**31
====================================================================================
"""

MAX_INT = 2**31-1
MIN_INT = -2**31

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if dividend*divisor == 0:
            return 0

        sign = 1 if dividend*divisor >= 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)

        total = 0
        while dividend >= divisor:
            exponent = 1
            tmp = divisor
            while tmp <= dividend:
                tmp <<= 1
                exponent <<= 1
            dividend -= tmp >> 1
            total += exponent >> 1

        res = sign*total
        if res > MAX_INT:
            return MAX_INT
        elif res < MIN_INT:
            return MIN_INT
        return res

if __name__ == '__main__':
    dividend, divisor = -1, -1 # -2147483648, -1
    print Solution().divide(dividend,divisor)