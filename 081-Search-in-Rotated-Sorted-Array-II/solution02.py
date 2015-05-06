#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 7, 2015
# Question: 081-Search-in-Rotated-Sorted-Array-II
# Link:     https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# ==============================================================================
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# Write a function to determine if a given target is in the array.
# ==============================================================================
# Method: Binary Search
# Time Complexity: O(N)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        return target in nums