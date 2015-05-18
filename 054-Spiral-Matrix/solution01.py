#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 18, 2015
# Question: 054-Spiral-Matrix
# Link:     https://leetcode.com/problems/spiral-matrix/
# ==============================================================================
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# 
# For example,
# Given the following matrix:
# 
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 
# You should return [1,2,3,6,9,8,7,4,5].
# ==============================================================================
# Method: Hash Table; If statements for four situations
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# ==============================================================================

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        elif len(matrix) == 1:
            return matrix[0]

        dic = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dic[i, j] = 0

        counter = 0
        stack = []
        i = j = 0
        direction = 0
        while counter < len(matrix) * len(matrix[0]):
            stack.append(matrix[i][j])
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
        return stack

if __name__ == '__main__':
    matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    # matrix = [[1,2, 3, 4], [5, 6, 7, 8]]
    # matrix = [[1,2,3]]
    print Solution().spiralOrder(matrix)