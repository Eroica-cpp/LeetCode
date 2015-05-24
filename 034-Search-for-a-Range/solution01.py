#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 24, 2015
# Question: 034-Search-for-a-Range
# Link:     https://leetcode.com/problems/search-for-a-range/
# ==============================================================================
# Given a sorted array of integers, find the starting and ending position of 
# a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
# ==============================================================================
# Method: Scan the whole array
# Time complexity: O(n)
# Space complexity: O(1)
# Note: Try binary search
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        idxs = []
        i = 0
        while i < len(nums):
            if nums[i] == target:
                idxs.append(i)
            i += 1
        return [idxs[0], idxs[-1]]

if __name__ == '__main__':
    print Solution().searchRange([1], 1)
    # print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)