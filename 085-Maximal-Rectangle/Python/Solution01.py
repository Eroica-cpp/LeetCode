#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 12, 2015
Question: 085-Maximal-Rectangle
Link:     https://leetcode.com/problems/maximal-rectangle/
==============================================================================
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle 
containing all ones and return its area.
==============================================================================
Method: use a stack
Time Complexity: O(n^2)
Space Complexity: O(n)
Note: it is tricky. Refer: http://blog.csdn.net/abcbc/article/details/8943485
==============================================================================
"""

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0

        m, n = len(matrix), len(matrix[0])
        H, L, R = [0]*n, [0]*n, [n]*n

        res = 0
        for i in xrange(m):
            left, right = 0, n
            
            for j in xrange(n):
                if matrix[i][j] == "1":
                    H[j] += 1
                    L[j] = max(L[j], left)
                else:
                    left = j + 1
                    H[j], L[j], R[j] = 0, 0, n

            for j in xrange(n-1,-1,-1):
                if matrix[i][j] == "1":
                    R[j] = min(R[j], right)
                    res = max(res, H[j]*(R[j]-L[j]))
                else:
                    right = j

        return res

if __name__ == '__main__':
    matrix = [["1", "1"], ["0", "1"]]
    print Solution().maximalRectangle(matrix)