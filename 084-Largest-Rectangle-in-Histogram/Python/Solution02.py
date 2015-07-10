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
Method: use a stack
Time Complexity: O(n)
Space Complexity: O(n)
Note: it is tricky. Refer: http://blog.csdn.net/abcbc/article/details/8943485
==============================================================================
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        stack = []
        height.append(0)
        i, maxVal = 0, 0
        while i < len(height):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tmp = stack.pop()
                maxVal = max(maxVal, height[tmp] * (i if not stack else i - stack[-1] - 1))
            
        return maxVal

if __name__ == '__main__':
    height = [2,1,5,6,2,3]
    height = [1]
    print Solution().largestRectangleArea(height)