#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Oct 1, 2015
Question: 275-H-Index-II
Link:     https://leetcode.com/problems/h-index-ii/
==============================================================================
Follow up for H-Index: What if the citations array is sorted in ascending order? 
Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.

==============================================================================
Method: sort
Time Complexity: log n
Space Complexity: O(1)
==============================================================================
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size = len(citations)
        h = 0
        
        while h < size and citations[-h-1] > h:
            h += 1

        return h
