#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 6, 2015
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
# Method: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: Pay attention to the get() method of a python dictionary. In case 
# of element i is not a dictionary key OR i's value dic[i] is exact 0, the if 
# statement would fail.
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dic = {}
        for i in nums:
            dic[i] = target - i
        for i in nums:
            if dic.get(dic[i]) is not None:
                idx1 = nums.index(i)
                if dic[i] != i:
                    return sorted([idx1+1, nums.index(dic[i])+1])
                elif nums.count(i) >= 2:
                    return [idx1 + 1, idx1 + nums[idx1+1:].index(i) + 2]
