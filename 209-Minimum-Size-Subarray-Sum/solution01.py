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
# Method: Two Pointers; Shrinkagble Window
# Time complexity: O(n)
# Space complexity: O(1)
# Note: Try binary search
# ==============================================================================

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        start = end = 0
        total = 0
        minLen = float('inf')

        while end < size and start <= end:

            while end < size and total < s:
                total += nums[end]
                end += 1

            while total >= s:
                minLen = min(minLen, end - start)
                total -= nums[start]
                start += 1

        return 0 if minLen == float('inf') else minLen

if __name__ == '__main__':
    print Solution().minSubArrayLen(50, [2,3,1,2,4,3])

