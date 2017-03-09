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
# Method: Bit operation with no extra space
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
    	