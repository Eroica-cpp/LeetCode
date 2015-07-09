#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 7, 2015
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
# Method: Binary Search
# Time Complexity: O(logN)
# Space Complexity: O(1)
# Note: 
# 1. An extension of question #035-Search-Insert-Position 
# 2. Carefully handle '>' or '>=' and '+ 1' or '- 1' cases
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high-low)/2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[low]:
                if target < nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
