#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 10, 2015
Question: 084-Largest-Rectangle-in-Histogram
Link:     https://leetcode.com/problems/largest-rectangle-in-histogram/
==============================================================================
Given n non-negative integers representing the histogram's bar height where 
the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
==============================================================================
Method: brute force; scan two sides of each column
Time Complexity: O(n^2)
Space Complexity: O(1)
Note: OK but apparently TLE
==============================================================================
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        size = len(height)
        maxVal = 0
        for i in xrange(size):
            h = height[i]
            left = right = i
            while left >= 0 and height[left] >= h:
                left -= 1
            while right < size and height[right] >= h:
                right += 1
            maxVal = max(maxVal, (right-left-1)*h)
        return maxVal

if __name__ == '__main__':
    height = [2,1,5,6,2,3]
    print Solution().largestRectangleArea(height)