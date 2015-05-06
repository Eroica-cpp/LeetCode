#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 7, 2015
# Question: 075-Sort-Colors
# Link:     https://leetcode.com/problems/sort-colors/
# ==============================================================================
# Given an array with n objects colored red, white or blue, sort them so that 
# objects of the same color are adjacent, with the colors in the order red, 
# white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, 
# and blue respectively.

# Note:
# You are not suppose to use the library's sort function for this problem.
# ==============================================================================
# Method: Loop
# Time Complexity: O(N)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        nums[:] = [0] * nums.count(0) + [1] * nums.count(1) + [2] * nums.count(2)

if __name__ == '__main__':
    nums = [1,2,1,1,2,2,2,2,0,0]
    Solution().sortColors(nums)
    print nums