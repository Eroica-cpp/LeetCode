#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 11, 2015
# Question: 078-Subsets
# Link:     https://leetcode.com/problems/subsets/
# ==============================================================================
# Given a set of distinct integers, nums, return all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:
# 
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# ==============================================================================
# Method: Iteration, use binary digit as flag.
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Note: Try recursive method
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        stack = []
        size = len(nums)
        i = 0
        while i <= 2**size - 1:
            tmpStr = '{0:b}'.format(i)
            stack.append([nums[j] for j in range(len(tmpStr)) if tmpStr[-j-1] == '1'])
            i += 1
        return stack

if __name__ == '__main__':
    print Solution().subsets([1,2])