#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 23, 2015
Question: 149-Max-Points-on-a-Line
Link:     https://leetcode.com/problems/max-points-on-a-line/
==============================================================================
Given n points on a 2D plane, find the maximum number of points that lie on 
the same straight line.
==============================================================================
Method: nothing but brute-force !
Time Complexity: O(n^2)
Space Complexity: O(n)
Note: test cases fail to consider one condition: vertical lines that of same k
but differs in x-axis
==============================================================================
"""

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        if not points:
            return 0
        maxVal = 1

        pointNum = {}
        for p in points:
            pointNum[p.x,p.y] = pointNum[p.x,p.y]+1 if pointNum.has_key((p.x,p.y)) else 1
        uniqPoints = [Point(p[0], p[1]) for p in pointNum.keys()]
        size = len(uniqPoints)

        for i in xrange(size):
            dic = {}
            for j in xrange(i+1,size):
                k = float(uniqPoints[j].y-uniqPoints[i].y)/(uniqPoints[j].x-uniqPoints[i].x) if uniqPoints[j].x-uniqPoints[i].x else float('inf')
                dic[k] = dic[k]+pointNum[uniqPoints[j].x,uniqPoints[j].y] if dic.has_key(k) else pointNum[uniqPoints[j].x,uniqPoints[j].y]
            maxVal = max(maxVal, pointNum[uniqPoints[i].x,uniqPoints[i].y]+max(dic.values())) if dic.values() else max(maxVal,pointNum[uniqPoints[i].x,uniqPoints[i].y])

        return maxVal

if __name__ == '__main__':
    points = [[0,0],[0,0]]
    # points = []
    # points = [[0,0],[1,1],[0,0]]
    # points = [[1,1],[1,1],[2,2],[2,2]]
    # points = [[1,1], [2,2], [3,3], [3,3],[3,3]]

    points = [Point(i[0],i[1]) for i in points]
    print Solution().maxPoints(points)
