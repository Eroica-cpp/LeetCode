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
Method: binary search; recursion
Time Complexity: O(log(mn))
Space Complexity: O(1)
Note: still have space to improve, that is: pruning!
==============================================================================
"""

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        return self.helper(0, 0, m-1, n-1, matrix, target)

    def helper(self, i, j, m, n, matrix, target):
        if i > m or j > n: return False

        mid_x = i + (m - i) / 2
        mid_y = j + (n - j) / 2
        if matrix[mid_x][mid_y] == target:
            return True
        elif matrix[mid_x][mid_y] < target:
            return self.helper(mid_x+1, j, m, n, matrix, target) or self.helper(i, mid_y+1, m, n, matrix, target)
        else:
            return self.helper(i, j, mid_x-1, n, matrix, target) or self.helper(i, j, m, mid_y-1, matrix, target)

if __name__ == '__main__':
    matrix = [[1,   4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 8
    print Solution().searchMatrix(matrix, target)