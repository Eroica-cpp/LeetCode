#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 20, 2015
Question: 220-Contains-Duplicate-III
Link:     https://leetcode.com/problems/contains-duplicate-iii/
==============================================================================
Given an array of integers, find out whether there are two distinct indices i 
and j in the array such that the difference between nums[i] and nums[j] is at 
most t and the difference between i and j is at most k.
==============================================================================
Method: Hash Table
Time Complexity: O(n)
Space Complexity: O(n)
Note: Reference: http://bookshadow.com/weblog/2015/06/03/leetcode-contains-duplicate-iii/
==============================================================================
"""

import collections

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) <= 1 or k < 1 or t < 0:
            return False

