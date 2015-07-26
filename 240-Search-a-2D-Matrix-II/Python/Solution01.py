#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 26, 2015
Question: 240-Search-a-2D-Matrix-II
Link:     https://leetcode.com/problems/search-a-2d-matrix-ii/
==============================================================================
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
==============================================================================
Method: brute force
Time Complexity: O(mn)
Space Complexity: O(1)
Note: Though having high time Complexity, it is AC in LeetCode.
==============================================================================
"""

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == target: return True

        return False
