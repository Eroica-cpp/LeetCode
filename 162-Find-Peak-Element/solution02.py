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
# Method: Binary Search
# Time Complexity: O(N)
# Space Complexity: O(1)
# Note: According to multiple callS in python, this method O(logN) is slower than 
# the one line O(N) method in leetcode.
# ==============================================================================

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        return self.helper(0, len(nums)-1, nums)

    def helper(self, start, end, nums):
        mid = (start+end)/2
        print mid
        if abs(start-end) <= 1:
            return start if nums[start] > nums[end] else end
        elif mid == 0:
            return mid if nums[mid] > nums[mid+1] else self.helper(mid, end, nums)
        elif mid == len(nums)-1:
            return mid if nums[mid] > nums[mid-1] else self.helper(start, mid, nums)
        elif nums[mid] > nums[mid-1]:
            return self.helper(mid, end, nums)
        else:
            return self.helper(start, mid, nums)




