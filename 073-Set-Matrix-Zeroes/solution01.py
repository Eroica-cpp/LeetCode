#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 26, 2015
# Question: 073-Set-Matrix-Zeroes
# Link:     https://leetcode.com/problems/set-matrix-zeroes/
# ==============================================================================
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
# Do it in place.
# 
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# ==============================================================================
# Method: extra space
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# ==============================================================================

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        old = []
        for i in xrange(m):
            line = [0] * n
            line[:] = matrix[i]
            old.append(line)
        
        for i in xrange(m):
            for j in xrange(n):
                if old[i][j] == 0:
                    for k in xrange(m):
                        matrix[k][j] = 0
                    for k in xrange(n):
                        matrix[i][k] = 0

if __name__ == '__main__':
    matrix = [[1,2,3], [0,5,6]]
    Solution().setZeroes(matrix)
    print matrix