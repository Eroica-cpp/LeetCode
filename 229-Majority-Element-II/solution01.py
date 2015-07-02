#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 2, 2015
Question: 229-Majority-Element-II
Link:     https://leetcode.com/problems/majority-element-ii/
==============================================================================
Given an integer array of size n, find all elements that appear more than 
floor(n/3) times. The algorithm should run in linear time and in O(1) space.
==============================================================================
Method: Hash Table; use extra space
Time Complexity: O(n)
Space Complexity: O(n)
==============================================================================
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        size = len(nums)
        dic = {}
        for i in nums:
            dic[i] = dic[i]+1 if dic.get(i) else 1

        return [j[0] for j in dic.items() if j[1] > size/3]