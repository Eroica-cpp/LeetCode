#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 4, 2015
# Question: 162-Find-Peak-Element
# Link:     https://leetcode.com/problems/find-peak-element/
# ==============================================================================
# A peak element is an element that is greater than its neighbors.
# 
# Given an input array where num[i] != num[i+1], find a peak element and return 
# its index.
# 
# The array may contain multiple peaks, in that case return the index to any one 
# of the peaks is fine.
# 
# You may imagine that num[-1] = num[n] = -oo.
# 
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should 
# return the index number 2.
# 
# Note:
# Your solution should be in logarithmic complexity.
# ==============================================================================
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        return nums.index(max(nums))
