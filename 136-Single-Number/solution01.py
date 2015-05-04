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
# Method: Hash Table
# Time Complexity: O(N)
# Space Complexity: O(N)
# ==============================================================================
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            dic[i] = 2 if dic.get(i) else 1
        for i in dic.keys():
            if dic[i] == 1:
                return i

if __name__ == '__main__':
    print Solution().singleNumber([3])
