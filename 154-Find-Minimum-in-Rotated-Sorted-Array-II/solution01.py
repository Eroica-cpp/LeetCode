#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 4, 2015
# Question: 154-Find-Minimum-in-Rotated-Sorted-Array-II
# Link:     https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# ==============================================================================
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
# ==============================================================================
# Method: Python build-in
# Time Complexity: O(n)
# Space complexity: O(1)
# Note: Try binary search next time LOL~
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        return min(nums)