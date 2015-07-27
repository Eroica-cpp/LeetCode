#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jul 27, 2015
# Question: 001-Two-Sum
# Link:     https://leetcode.com/problems/two-sum/
# ==============================================================================
# Given an array of integers, find two numbers such that they add up to a 
# specific target number.
# 
# The function twoSum should return indices of the two numbers such that 
# they add up to the target, where index1 must be less than index2. Please 
# note that your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution.
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# ==============================================================================
# Method: brute force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Note: obvious TLE solution; adding this is only for completeness
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        size = len(nums)
        for i in xrange(size-1):
            for j in xrange(i+1,size):
                if nums[i] + nums[j] == target:
                    return [i+1, j+1]

if __name__ == '__main__':
    print Solution().twoSum([-1,-2,-3,-4,-5], -8)
