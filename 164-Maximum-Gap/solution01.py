#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 15, 2015
# Question: 164-Maximum-Gap
# Link:     https://leetcode.com/problems/maximum-gap/
# ==============================================================================
# Given an unsorted array, find the maximum difference between the successive 
# elements in its sorted form.
# 
# Try to solve it in linear time/space.
# 
# Return 0 if the array contains less than 2 elements.
# 
# You may assume all elements in the array are non-negative integers and fit 
# in the 32-bit signed integer range.
# ==============================================================================
# Method: quick sort
# Time Complexity: O(n logn)
# Space Complexity: O(1)
# Note: 
# 1. seemingly TLE, but not found by LeetCode ==||
# 2. try bucket sort next time :-)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        size = len(nums)
        if size < 2:
            return 0

        nums.sort()
        maxVal = 0
        for i in xrange(size-1):
            maxVal = max(maxVal, nums[i+1]-nums[i])

        return maxVal

