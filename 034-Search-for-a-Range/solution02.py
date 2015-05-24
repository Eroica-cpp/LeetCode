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
# Method: Binary search
# Time complexity: O(log n)
# Space complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):

        size = len(nums)
        low, high = 0, size - 1
        
        while low <= high:
            mid = (low + high) / 2
            print low, mid, high
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                i = j = mid
                while i >= 0 and i < size and nums[i] == target: 
                    i -= 1
                while j >= 0 and j < size and nums[j] == target: 
                    j += 1
                
                return [i+1, j-1]

        return [-1, -1]


if __name__ == '__main__':
    # print Solution().searchRange([1], 1)
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
    # print Solution().searchRange([5, 7, 7, 8, 8, 10], 12)
    # print Solution().searchRange([], 1)