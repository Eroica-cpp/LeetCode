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
# Method: uses two pointers, converges from two sides of the height array
# Time Complexity: O(n)
# Space Complexity: O(1)
# ===============================================================================

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):

        maxVal = 0
        i, j = 0, len(height)-1

        while i < j:
            area = (j-i) * min(height[i], height[j])
            maxVal = max(area, maxVal)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return maxVal