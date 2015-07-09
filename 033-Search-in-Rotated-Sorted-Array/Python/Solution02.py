#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jul 9, 2015
# Question: 033-Search-in-Rotated-Sorted-Array
# Link:     https://leetcode.com/problems/search-in-rotated-sorted-array/
# ==============================================================================
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its 
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# ==============================================================================
# Method: brute force; python build-in
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        return nums.index(target) if target in nums else -1
