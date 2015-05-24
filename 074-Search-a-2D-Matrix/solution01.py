#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 24, 2015
# Question: 074-Search-a-2D-Matrix
# Link:     https://leetcode.com/problems/search-a-2d-matrix/
# ==============================================================================
# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
# 
# Consider the following matrix:
# 
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.
# ==============================================================================
# Method: Traverse
# Time complexity: O(n^2)
# Space complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        flag = False
        for row in matrix:
            flag = flag or target in row
        return flag

if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    print Solution().searchMatrix(matrix, 15)