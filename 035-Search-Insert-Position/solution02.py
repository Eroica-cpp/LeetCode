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
# Method: Binary Search
# Time Complexity: O(logN)
# Space Complexity: O(N)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high-low)/2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        return low

if __name__ == '__main__':
    print Solution().searchInsert([1,3,5,6], 5)
