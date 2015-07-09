#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 30, 2015
# Question: 080-Remove-Duplicates-from-Sorted-Array-II
# Link:     https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
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
# Method: maintain a counter variable
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        size = len(nums)
        if size <= 2: return size

        index = 2
        for i in xrange(2,size):
            if nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index += 1

        return index

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    print Solution().removeDuplicates(nums)
    print nums
