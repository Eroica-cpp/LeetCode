#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Sept. 26, 2015
Question: 286-Walls-and-Gates
Link:     https://leetcode.com/problems/walls-and-gates/
==============================================================================
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
==============================================================================
Method: naive method
Time Complexity: O(m * n)
Space Complexity: O(1)
==============================================================================
"""

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return
        INF = 2**31 - 1
        m, n = len(rooms), len(rooms[0])

        for i in xrange(m):
            if rooms[i][0] == 0: self.helper(i, 0, 0)
            if rooms[i][n-1] == 0: self.helper(i, n-1, 0)

        for j in xrange(n):
            if rooms[0][j] == 0: self.helper(0, j, 0)
            if rooms[n-1][i] == 0: self.helper(n-1, j, 0)

    def helper(self, i, j, step):
        global rooms
        global m, n
        if (not 0 <= i < m) or (not 0 <= j < n) or rooms[i][j] == -1: return
        rooms[i][j] = min(rooms[i][j], step)
        self.helper(i + 1, j, step + 1)
        self.helper(i - 1, j, step + 1)
        self.helper(i, j + 1, step + 1)
        self.helper(i, j - 1, step + 1)

if __name__ == '__main__':
    rooms = [0]
