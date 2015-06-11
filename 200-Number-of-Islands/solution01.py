#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 11, 2015
# Question: 200-Number-of-Islands
# Link:     https://leetcode.com/problems/number-of-islands/
# ==============================================================================
# Given a 2d grid map of '1's (land) and '0's (water), count the number of 
# islands. An island is surrounded by water and is formed by connecting adjacent 
# lands horizontally or vertically. You may assume all four edges of the grid 
# are all surrounded by water.
# 
# Example 1:
# 
# 11110
# 11010
# 11000
# 00000
# Answer: 1
# 
# Example 2:
# 
# 11000
# 11000
# 00100
# 00011
# Answer: 3
# ==============================================================================
# Method: tag in-place
# ==============================================================================

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        counter = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == "1":
                    counter += 1
                    self.tag(grid, i, j, m, n, counter)

        return counter

    def tag(self, grid, i, j, m, n, counter):
        grid[i][j] = -counter
        if i-1 >= 0 and grid[i-1][j] == "1":
            self.tag(grid, i-1, j, m, n, counter)
        if i+1 < m and grid[i+1][j] == "1":
            self.tag(grid, i+1, j, m, n, counter)
        if j-1 >= 0 and grid[i][j-1] == "1":
            self.tag(grid, i, j-1, m, n, counter)
        if j+1 < n and grid[i][j+1] == "1":
            self.tag(grid, i, j+1, m, n, counter)

if __name__ == '__main__':
    grid = ["11110","11010","11000","00000"]
    grid = ["11000","11000","00100","00011"]
    grid = [[j for j in i] for i in grid]
    print Solution().numIslands(grid)