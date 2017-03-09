#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 26, 2015
# Question: 209-Minimum-Size-Subarray-Sum
# Link:     https://leetcode.com/problems/minimum-size-subarray-sum/
# ==============================================================================
# Given an array of n positive integers and a positive integer s, find the 
# minimal length of a subarray of which the sum >= s. If there isn't one, 
# return 0 instead.
# 
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
# 
# More practice:
# If you have figured out the O(n) solution, try coding another solution of 
# which the time complexity is O(n log n).
# ==============================================================================
# Method: Binary Search
# Time complexity: O(n log n)
# Space complexity: O(1)
# Note: TODO
# ==============================================================================

import time

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        minLen = float('inf')

        for start in xrange(size):
            
        return minLen


if __name__ == '__main__':
    print Solution().minSubArrayLen(6, [2,3,1,2,4,3])