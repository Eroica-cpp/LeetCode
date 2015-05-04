#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 4, 2015
# Question: 136-Single-Number
# Link:     https://leetcode.com/problems/single-number/
# ==============================================================================
# Given an array of integers, every element appears twice except for one. Find 
# that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it 
# without using extra memory?
# ==============================================================================
# Method: XOR
# Time Complexity: O(N)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res

if __name__ == '__main__':
    print Solution().singleNumber([1,1,2,2,3,3,4,5,5])
