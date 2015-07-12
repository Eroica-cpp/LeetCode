#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 12, 2015
Question: 041-First-Missing-Positive
Link:     https://leetcode.com/problems/first-missing-positive/
==============================================================================
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
==============================================================================
Method: bucket sort
Time Complexity: O(n)
space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        size = len(nums)

        for i in xrange(size):
            while nums[i] != i + 1:
                if nums[i] <= 0 or nums[i] > size or nums[i] == nums[nums[i] - 1]: break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in xrange(size):
            if nums[i] != i + 1:
                return i + 1

        return size + 1
