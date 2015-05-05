#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 5, 2015
# Question: 137-Single-Number-II
# Link:     https://leetcode.com/problems/single-number-ii/
# ==============================================================================
# Given an array of integers, every element appears three times except for one. 
# Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it 
# without using extra memory?
# ==============================================================================
# Method: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: Try bit operation method
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            dic[i] = dic[i]+1 if dic.get(i) else 1
        for i in dic.keys():
            if dic[i] != 3:
                return i