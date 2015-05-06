#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 7, 2015
# Question: 035-Search-Insert-Position
# Link:     https://leetcode.com/problems/search-insert-position/
# ==============================================================================
# Given a sorted array and a target value, return the index if the target is 
# found. If not, return the index where it would be if it were inserted in order.
# 
# You may assume no duplicates in the array.
# 
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0
# ==============================================================================
# Method: Traverse
# Time Complexity: O(N)
# Space Complexity: O(1)
# Note: Try binary search
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if not nums or target <= nums[0]:
            return 0
        for i in range(len(nums)-1):
            if target > nums[i] and target <= nums[i+1]:
                return i+1
        return len(nums)

if __name__ == '__main__':
    print Solution().searchInsert([1,3,5,6], 5)