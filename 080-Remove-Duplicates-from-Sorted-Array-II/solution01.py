#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 30, 2015
# Question: 219-Contains-Duplicate-II
# Link:     https://leetcode.com/problems/contains-duplicate-ii/
# ==============================================================================
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# 
# Your function should return length = 5, with the first five elements of nums 
# being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
# ==============================================================================
# Method: hash table; pointer
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: Try not use hash table next time, try a new method of space complexity O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        size = len(nums)
        
        if size <= 2:
            return size
        
        dic = {}
        counter = 0
        ptr = 0
        for i in xrange(size):
            if dic.get(nums[i]) >= 2:
                continue
            elif dic.get(nums[i]) is None:
                dic[nums[i]] = 1
            elif dic.get(nums[i]) == 1:
                dic[nums[i]] = 2
            nums[ptr] = nums[i]
            ptr += 1
            counter += 1

        return counter

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    print Solution().removeDuplicates(nums)
    print nums