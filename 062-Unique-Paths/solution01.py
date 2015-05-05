#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 062-Unique-Paths
# Link:     https://leetcode.com/problems/unique-paths/
# ==============================================================================
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the
# diagram below).
# 
# How many possible unique paths are there?
# ==============================================================================
# Method: Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Note: Try better DP methods with low space use.
# ==============================================================================

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        return [self.helper(i) for i in range(numRows)] 

    def helper(self, num):
        if num == 0:
            return [1]
        elif num == 1:
            return [1, 1]
        else:
            last = self.helper(num-1)
            current = [1]
            for i in range(num-1):
                current.append(last[i]+last[i+1])
            current.append(1)
            return current