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
# Method: Python build-in function
# Time Complexity: Don't know
# Space Complexity: Don't know
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

if __name__ == '__main__':
    print Solution().containsDuplicate([1,2,3,3,4,5])
