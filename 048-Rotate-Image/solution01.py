#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 8, 2015
# Question: 048-Rotate-Image
# Link:     https://leetcode.com/problems/rotate-image/
# ==============================================================================
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Follow up:
# Could you do this in-place?
# ==============================================================================
# Method: Use extra space
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# ==============================================================================

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        size = len(matrix)
        new = []
        for i in range(size):
            new.append([matrix[-j-1][i] for j in range(size)])
        matrix[:] = new

if __name__ == '__main__':
    test1 = [[1,2],[3,4]]
    test2 = [[11,12], [21, 22]]
    Solution().rotate(test2)
    for i in test2:
        print i