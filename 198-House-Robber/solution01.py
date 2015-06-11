#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 11, 2015
# Question: 198-House-Robber
# Link:     https://leetcode.com/problems/house-robber/
# ==============================================================================
# You are a professional robber planning to rob houses along a street. Each 
# house has a certain amount of money stashed, the only constraint stopping 
# you from robbing each of them is that adjacent houses have security system 
# connected and it will automatically contact the police if two adjacent 
# houses were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of 
# each house, determine the maximum amount of money you can rob tonight without 
# alerting the police.
# ==============================================================================
# Method: simple DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        elif size <= 2:
            return max(nums)

        dp = [0 for i in xrange(size)]
        dp[0], dp[1] = nums[0], max(nums[:2])
        for i in xrange(2, size):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return max(dp[-1], dp[-2])

if __name__ == '__main__':
    nums = [10,1,1,3,1]
    nums = [2,1,1,2]
    print Solution().rob(nums)