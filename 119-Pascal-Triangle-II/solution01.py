#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 119-Pascal-Triangle-II
# Link:     https://leetcode.com/problems/pascals-triangle-ii/
# ==============================================================================
# Given an index k, return the kth row of the Pascal's triangle.
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
# ==============================================================================

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0: 
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            thisRow = [1]
            lastRow = self.getRow(rowIndex-1)
            lastLength = len(lastRow)
            for i in range(0, lastLength-1):
                thisRow.append(lastRow[i]+lastRow[i+1])
            thisRow.append(1)
            return thisRow