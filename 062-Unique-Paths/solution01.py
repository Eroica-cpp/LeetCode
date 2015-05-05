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
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        if m < 1 and n < 1:
            return 0
        elif m == 1 and n == 1:
            return 1
        
        tmp_row = [1] * n
        dp = [tmp_row] * m
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

if __name__ == '__main__':
    print Solution().uniquePaths(1, 2)