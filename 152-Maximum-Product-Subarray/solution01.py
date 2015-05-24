#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 24, 2015
# Question: 152-Maximum-Product-Subarray
# Link:     https://leetcode.com/problems/maximum-product-subarray/
# ==============================================================================
# Find the contiguous subarray within an array (containing at least one number) 
# which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# ==============================================================================
# Method: Simple DP implement
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: 
# 1. Refer question #053-Maximum-Subarray
# 2. Store maxVal and minVal
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        res = minVal = maxVal = nums[0]

        for i in nums[1:]:
            lastMax = maxVal
            lastMin = minVal
            maxVal = max(i, max(lastMax*i, lastMin*i))
            minVal = min(i, min(lastMax*i, lastMin*i))
            res = max(res, maxVal)
        
        return res

if __name__ == '__main__':
    array = [2,-5,-2,-4,3]
    # array = [2,3,-2,4, 0, -2000, 100]
    print Solution().maxProduct(array)