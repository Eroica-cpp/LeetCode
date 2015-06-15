#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 15, 2015
# Question: 179-Largest-Number
# Link:     https://leetcode.com/problems/largest-number/
# ==============================================================================
# Given a list of non negative integers, arrange them such that they form the 
# largest number.
# 
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# 
# Note: The result may be very large, so you need to return a string instead 
# of an integer.
# ==============================================================================
# Method: bubble sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Note: 
# 1. reference: http://blog.csdn.net/ljiabin/article/details/42676433
# 2. Try difference sorting Method (say quick sort) for better performance
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        size = len(nums)
        nums = [str(k) for k in nums]
        for i in xrange(size,-1,-1):
            for j in xrange(0, i-1):
                if int(nums[j]+nums[j+1]) < int(nums[j+1]+nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(nums)))

if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    nums = [120,12]
    nums = [0,0,1]
    print Solution().largestNumber(nums)