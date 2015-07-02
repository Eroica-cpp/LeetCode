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
Method: randomly pick up a number and figure out whether it appears more than
floor(n/3) times
Time Complexity: O(n)
Space Complexity: O(1)
Reference: http://www.cnblogs.com/fanyabo/p/4178993.html
==============================================================================
"""

import random

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        size = len(nums)
        bag = list(set(nums))
        res = []
        while bag and len(res) < 2:
            i = random.choice(bag)
            if nums.count(i) > size/3:
                res.append(i)
            bag.remove(i)
        return res
