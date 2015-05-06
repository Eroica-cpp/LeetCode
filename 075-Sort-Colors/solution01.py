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
# Method: Library method (quick sort is used I suppose)
# Time Complexity: O(NlogN)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        nums.sort()