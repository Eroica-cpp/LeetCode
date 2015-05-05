#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 169-Majority-Element
# Link:     https://leetcode.com/problems/majority-element/
# ==============================================================================
# Given an array of size n, find the majority element. The majority element is 
# the element that appears more than floor(n/2) times.
# 
# You may assume that the array is non-empty and the majority element always 
# exist in the array.
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def __init__(self):
        self.dic = {}

    def majorityElement(self, nums):
        num = len(nums)
        for i in nums:
            if self.dic.get(i):
                self.dic[i] += 1
            else:
                self.dic[i] = 1
        
        for i in self.dic.keys():
            if self.dic[i] > num / 2:
                return i