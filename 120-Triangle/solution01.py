#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 30, 2015
# Question: 120-Triangle
# Link:     https://leetcode.com/problems/triangle/
# ==============================================================================
# Given a triangle, find the minimum path sum from top to bottom. Each step 
# you may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# Bonus point if you are able to do this using only O(n) extra space, 
# where n is the total number of rows in the triangle.
# ==============================================================================
# Method: DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        size = len(triangle)
        if size == 0:
            return 0
        elif size == 1:
            return triangle[0][0]

        lastMin = [triangle[0][0]]
        for i in xrange(1, size):
            new = [triangle[i][0] + lastMin[0]]
            j = 1
            while j < i:
                new.append(triangle[i][j] + min(lastMin[j-1], lastMin[j]))
                j += 1
            new.append(triangle[i][-1] + lastMin[-1])
            lastMin = new

        return min(lastMin)

if __name__ == '__main__':
    triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
    print Solution().minimumTotal(triangle)