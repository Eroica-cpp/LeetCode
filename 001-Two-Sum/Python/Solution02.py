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
# Method: Sorted, Two pointers
# Time Complexity: O(n logn)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        new = sorted(nums)
        low, high = 0, len(nums)-1

        while low < high:
            tmp = new[low] + new[high]
            if tmp == target: break
            elif tmp > target: high -= 1
            else: low += 1

        res, bag = [], [new[low], new[high]]
        i = 0
        while len(res) < 2 and i < len(nums):
            if nums[i] in bag:
                res.append(i+1)
            i += 1

        return res

if __name__ == '__main__':
    nums, target = [150,24,79,50,88,345,3], 200
    print Solution().twoSum(nums, target)
