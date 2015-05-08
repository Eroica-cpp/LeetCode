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
# Method: Rotate matrix in place
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Note:
# 1. matrix[i][j] -> matrix[j][-i-1] -> matrix[-i-1][-j-1] -> matrix[-j-1][i]
# 2. odd and even cases are different, treat them seperately
# ==============================================================================

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        size = len(matrix)
        center = size / 2
        flag = 0 if size%2 == 0 else 1
        for i in range(center+flag):
            for j in range(center):
                matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i], matrix[i][j] = matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i]

if __name__ == '__main__':
    test1 = [[1,2],[3,4]]
    test2 = [[11,12], [21, 22]]
    test3 = [[1,2,3],[4,5,6],[7,8,9]]
    test4 = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
    for i in test3:
        print i
    print 
    Solution().rotate(test3)
    for i in test3:
        print i