#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 11, 2015
# Question: 016-3Sum-Closest
# Link:     https://leetcode.com/problems/3sum-closest/
# ==============================================================================
# Given an array S of n integers, find three integers in S such that the sum 
# is closest to a given number, target. Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
# 
#     For example, given array S = {-1 2 1 -4}, and target = 1.
# 
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# ==============================================================================
# Method: Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Note: Refer to question #015-3Sum
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        size = len(nums)
        summ = 0
        closeSum = nums[0] + nums[1] + nums[-1]

        for i in range(size):
            low = i + 1
            high = size - 1
            while low < high:
                summ = nums[i] + nums[low] + nums[high]
                if target-summ == 0:
                    return summ
                elif abs(target-summ) < abs(target-closeSum):
                    closeSum = summ
                if target - summ > 0:
                    low += 1
                else:
                    high -= 1

        return closeSum

if __name__ == '__main__':
    print Solution().threeSumClosest([1,2,3, 4], 7)