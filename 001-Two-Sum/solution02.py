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
# Time Complexity: O(NlogN)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        new = sorted(nums)
        low = 0
        high = len(nums) - 1
        while low < high:
            if new[low] + new[high] == target:
                break
            elif new[low] + new[high] > target:
                high -= 1
            else:
                low += 1

        idx1 = 0
        idx2 = 1
        while new[low] != nums[idx1]:
            idx1 += 1
        while new[high] != nums[-idx2]:
            idx2 += 1
        return sorted([idx1+1, len(nums)-idx2+1])


if __name__ == '__main__':
    print Solution().twoSum([-1,-2,-3,-4,-5], -8) #([0,4,3,0], 0)