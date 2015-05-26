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
# Method: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dic = {}
        for i in nums:
            if dic.get(i) is not None:
                return True
            else:
                dic[i] = 1
        return False

if __name__ == '__main__':
    print Solution().containsDuplicate([1,2,3,4,5])
