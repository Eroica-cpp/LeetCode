#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 18, 2015
# Question: 059-Spiral-Matrix-II
# Link:     https://leetcode.com/problems/spiral-matrix-ii/
# ==============================================================================
# Given an integer n, generate a square matrix filled with elements from 1 to 
# n2 in spiral order.
# 
# For example,
# Given n = 3,
# 
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
# ==============================================================================
# Method: Hash Table; If statements for four situations
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Note: 
# 1. Refer to Question #054-Spiral-Matrix; almost the same
# 2. Difference between "[[0] * n for i in range(n)]" and "[[0] * n] * n"
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [[1]]

        matrix = [[0] * n for i in range(n)]
        dic = {}
        for i in range(n):
            for j in range(n):
                dic[i, j] = 0

        counter = 1
        stack = []
        i = j = 0
        direction = 0
        while counter <= n**2:
            matrix[i][j] = counter
            dic[i, j] = 1
            if direction == 0:
                if dic.get((i, j+1)) is not None and dic.get((i, j+1)) != 1:
                    j += 1
                else:
                    direction += 1
                    i += 1
            elif direction == 1:
                if dic.get((i+1, j)) is not None and dic.get((i+1, j)) != 1:
                    i += 1
                else:
                    direction += 1
                    j -= 1
            elif direction == 2:
                if dic.get((i, j-1)) is not None and dic.get((i, j-1)) != 1:
                    j -= 1
                else:
                    direction += 1
                    i -= 1                
            elif direction == 3:
                if dic.get((i-1, j)) is not None and dic.get((i-1, j)) != 1:
                    i -= 1
                else:
                    direction += 1
                    j += 1
            counter += 1
            direction %= 4
        return matrix

if __name__ == '__main__':
    print Solution().generateMatrix(3)