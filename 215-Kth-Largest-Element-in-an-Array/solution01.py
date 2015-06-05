#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 5, 2015
# Question: 215-Kth-Largest-Element-in-an-Array
# Link:     https://leetcode.com/problems/kth-largest-element-in-an-array/
# ==============================================================================
# ind the kth largest element in an unsorted array. Note that it is the kth 
# largest element in the sorted order, not the kth distinct element.
# 
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# ==============================================================================
# Method: Sort, python build-in
# Time Complexity: O(n logn)
# Space Complexity: O(1)
# Note: Try better solution 
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        nums.sort()
        res = 0
        while k > 0:
            res = nums.pop()
            k -= 1
            
        return res