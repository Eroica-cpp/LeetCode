#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 7, 2015
# Question: 153-Find-Minimum-in-Rotated-Sorted-Array
# Link:     https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# ==============================================================================
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# ==============================================================================
# Method: Loop
# Time Complexity: O(N)
# Space Complexity: O(1)
# Note: Try binary search
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        return min(nums)