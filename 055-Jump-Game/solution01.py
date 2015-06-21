#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 8, 2015
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
# Method: Recursion
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Note: 
# 1. terrible time and space complexity
# 2. I am wondering whether this solution is OK regardless of complexity.
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if not nums:
            return True
        elif len(nums) == 1:
            return nums[0] > 0
        else:
            flag = False
            for i in range(nums[0], 0, -1):
                print nums[:10]
                flag = flag or self.canJump(nums[i:])
            return flag

if __name__ == '__main__':
    test1 = [2,3,1,1,4]
    test2 = [3,2,1,0,4]
    test3 = []
    test4 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    test5 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,2, 0,1,1, 1]
    test6 = [1,2,2,3,2,0,0,0, 1]
    test7 = [6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0]
    print Solution().canJump(test7)