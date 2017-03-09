#!/usr/bin/python
"""
https://leetcode.com/problems/best-meeting-point/

Time O(n^2), Space O(n)
"""

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return

        addr = []
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    addr.append([i, j])

        N = len(addr)
        x_mid = sum(i[0] for i in addr) / N
        y_mid = sum(i[1] for i in addr) / N

        return sum(abs(i[0] - x_mid)+abs(i[1] - y_mid) for i in addr)

if __name__ == '__main__':
    grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    # grid = [[0,1], [1,0]]
    print Solution().minTotalDistance(grid)