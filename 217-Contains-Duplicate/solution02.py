#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 26, 2015
# Question: 217-Contains-Duplicate
# Link:     https://leetcode.com/problems/contains-duplicate/
# ==============================================================================
# Given an array of integers, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice in 
# the array, and it should return false if every element is distinct.
# ==============================================================================
# Method: Sort
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        nums.sort()
        size = len(nums)

        if size <= 1:
            return False

        for i in xrange(1, size):
            if nums[i-1] == nums[i]:
                return True

        return False

if __name__ == '__main__':
    print Solution().containsDuplicate([1,2,3,4,5])
