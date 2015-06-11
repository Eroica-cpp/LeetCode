#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 11, 2015
# Question: 201-Bitwise-AND-of-Numbers-Range
# Link:     https://leetcode.com/problems/bitwise-and-of-numbers-range/
# ==============================================================================
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise 
# AND of all numbers in this range, inclusive.
# 
# For example, given the range [5, 7], you should return 4.
# ==============================================================================
# Method: Math trick.
# Time Complexity: O(N), N is number (m-n)'s digit number
# Space Complexity: O(1)
# Note: Reference: http://www.cnblogs.com/aboutblank/p/4442193.html
# ==============================================================================

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        offset = 0
        while m != n:
            m >>= 1
            n >>= 1
            offset += 1
        return m << offset

if __name__ == '__main__':
    m, n = 5, 7
    m, n = 0, 2147483647
    m, n = 600000000, 2147483645
    print Solution().rangeBitwiseAnd(m, n)