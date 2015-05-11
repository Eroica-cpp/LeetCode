#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 11, 2015
# Question: 090-Subsets-II
# Link:     https://leetcode.com/problems/subsets-ii/
# ==============================================================================
# Given a collection of integers that might contain duplicates, nums, return 
# all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,2], a solution is:
# 
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# ==============================================================================
# Method: Iteration, use binary digit as flag.
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Note: 
# 1. Almoat the same as question #078-Subsets if use this method.
# 2. Use hash table to remove duplications
# 3. Try recursive method
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        dic = {}
        stack = []
        size = len(nums)
        i = 0
        while i <= 2**size - 1:
            tmpStr = '{0:b}'.format(i)
            subset = [nums[j] for j in range(len(tmpStr)) if tmpStr[-j-1] == '1']
            if dic.get(",".join([str(j) for j in subset])) is None:
                stack.append(subset)
                dic[",".join([str(j) for j in subset])] = 0
            i += 1
        return stack

if __name__ == '__main__':
    print Solution().subsetsWithDup([1,2,2])