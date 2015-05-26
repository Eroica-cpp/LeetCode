#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 26, 2015
# Question: 064-Minimum-Path-Sum
# Link:     https://leetcode.com/problems/minimum-path-sum/
# ==============================================================================
# Given a m x n grid filled with non-negative numbers, find a path from top 
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# ==============================================================================
# Method: Simple DP
# Time Complexity: O(n^2)
# Space Complexity: O(n^2) 
# ==============================================================================

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])

        if m == 0 or n == 0:
            return 0
        elif m == 1 and n == 1:
            return grid[0][0]

        res = [[0 for j in xrange(n)] for i in xrange(m)]
        res[0][0] = grid[0][0]

        for i in xrange(1, m):
            res[i][0] = res[i-1][0] + grid[i][0]

        for i in xrange(1, n):
            res[0][i] = res[0][i-1] + grid[0][i]

        for i in xrange(1, m):
            for j in xrange(1, n):
                res[i][j] = grid[i][j] + min(res[i-1][j], res[i][j-1])

        return res[-1][-1]

if __name__ == '__main__':
    print Solution().minPathSum([[1,2,5],[3,2,1]])

