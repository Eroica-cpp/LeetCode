#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 16, 2015
Question: 238-Product-of-Array-Except-Self
Link:     https://leetcode.com/problems/product-of-array-except-self/
==============================================================================
Given an array of n integers where n > 1, nums, return an array output such 
that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array 
does not count as extra space for the purpose of space complexity analysis.)
==============================================================================
Method: two passes - font to end & end to font
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        size = len(nums)
        res = [0] * size

        prod = 1
        for i in xrange(size):
            res[i] = prod
            prod *= nums[i]

        prod = 1
        for j in xrange(size-1,-1,-1):
            res[j] *= prod
            prod *= nums[j]

        return res
