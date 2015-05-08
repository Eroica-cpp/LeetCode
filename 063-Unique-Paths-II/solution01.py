#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 8, 2015
# Question: 063-Unique-Paths-II
# Link:     https://leetcode.com/problems/unique-paths-ii/
# ==============================================================================
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths 
# would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.
# ==============================================================================
# Method: Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Note: 
# 1. Try better DP methods with low space use.
# 2. Almost the same as question #062-Unique-Paths
# ==============================================================================

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 1 and n == 1:
            return int(obstacleGrid[0][0] != 1)
        
        dp = [[1] * n]
        dp += [[0]*n for i in range(m-1)]
        if 1 in obstacleGrid[0]:
            idx = obstacleGrid[0].index(1)
            dp[0] = [1]*idx + [0]*(n-idx)

        flag = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1: flag = 0
            dp[i][0] = flag

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]        

if __name__ == '__main__':
    test1 = [[0,0,0],[0,1,0],[0,0,0]]
    test2 = [[1]]
    test3 = [[0,0,1]]
    test4 = [[0]]
    print Solution().uniquePathsWithObstacles(test2)