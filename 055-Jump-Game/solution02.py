#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 21, 2015
# Question: 055-Jump-Game
# Link:     https://leetcode.com/problems/jump-game/
# ==============================================================================
# Given an array of non-negative integers, you are initially positioned at 
# the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Determine if you are able to reach the last index.
# 
# For example:
# A = [2,3,1,1,4], return true.
# 
# A = [3,2,1,0,4], return false.
# ==============================================================================
# Method: DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        size = len(nums)
        if size <= 1:
            return True
        elif nums[0] <= 0:
            return False

        nums[-1] = 1
        dp = [False] * size
        dp[0] = True
        maxVal = 0
        i = 0
        while i < size-1:
            if i+nums[i] > maxVal and dp[i]:
                for j in xrange(maxVal,min(i+nums[i]+1,size)):
                    dp[j] = True
                maxVal = i+nums[i]
            i += 1

        return all(dp)

if __name__ == '__main__':
    test = [2,3,1,1,4]
    test = [3,2,1,0,4]
    test = []
    test = [2,0,0]
    test = [1,0,1,0]
    print Solution().canJump(test)