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
# Method: modify in-place, use first column and first row
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])

        firstColumnIsZero = False
        firstRowIsZero = False

        for i in xrange(m):
            if matrix[i][0] == 0:
                firstColumnIsZero = True
                break

        for i in xrange(n):
            if matrix[0][i] == 0:
                firstRowIsZero = True
                break

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in xrange(1, m):
            if matrix[i][0] == 0:
                for j in xrange(1, n):
                    matrix[i][j] = 0

        for j in xrange(1, n):
            if matrix[0][j] == 0:
                for i in xrange(1, m):
                    matrix[i][j] = 0

        if firstColumnIsZero:
            for i in xrange(m):
                matrix[i][0] = 0

        if firstRowIsZero:
            for j in xrange(n):
                matrix[0][j] = 0

if __name__ == '__main__':
    matrix = [[1,2,3], [0,5,6]]
    # matrix = [[0,1]]
    Solution().setZeroes(matrix)
    print matrix