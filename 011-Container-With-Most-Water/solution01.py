#!/usr/bin/python
# ===============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 4, 2015
# Question: 011-Container-With-Most-Water
# Link:     https://leetcode.com/problems/container-with-most-water/
# ===============================================================================
# Given n non-negative integers a1, a2, ..., an, where each represents a point at 
# coordinate (i, ai). n vertical lines are drawn such that the two endpoints of 
# line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms 
# a container, such that the container contains the most water.
# 
# Note: You may not slant the container.
# ===============================================================================
# Method: the naive and straightforward one
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# ===============================================================================

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        maxVal = 0 
        maxHeigh = 0
        maxWidth = 0
        size = len(height)
        for i in range(size):
        	for j in range(size-i-1):
        		w = j - i
        		h = min(height[i], height[-(j+1)])
        		if (maxWidth >= w and maxHeigh >= h) or h * w <= maxVal:
        			continue
        		else:
        			maxWidth = w
        			maxHeigh = h
        			maxVal = h * w
        return maxVal