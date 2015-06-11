#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 11, 2015
# Question: 223-Rectangle-Area
# Link:     https://leetcode.com/problems/rectangle-area/
# ==============================================================================
# Find the total area covered by two rectilinear rectangles in a 2D plane.
# 
# Each rectangle is defined by its bottom left corner and top right corner 
# as shown in the figure.
# 
# Assume that the total area is never beyond the maximum possible value of int.
# ==============================================================================
# Method: simple math
# Time Complexity: O(1)
# Space Complexity: O(1)
# ==============================================================================

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area = abs(A-C)*abs(B-D) + abs(E-G)*abs(F-H)
        area -= self.interact(A,C,E,G) * self.interact(B,D,F,H)
        return area

    def interact(self, x1, y1, x2, y2):
        if y1 < x1:
            x1, y1 = y1, x1
        if y2 < x2:
            x2, y2 = y2, x2

        if x1 < x2:
            if y1 <= x2:
                return 0
            elif y1 > x2 and y1 <= y2:
                return y1 - x2
            elif y1 > y2:
                return y2 - x2
        if x1 >= x2 and x1 <= y2:
            if y1 <= y2:
                return y1 - x1
            elif y1 > y2:
                return y2 - x1
        if x1 > y2:
            return 0

if __name__ == '__main__':
    A, B, C, D, E, F, G, H = -2, -2, 2, 2, -1, -1, 1, 1
    print Solution().computeArea(A, B, C, D, E, F, G, H)