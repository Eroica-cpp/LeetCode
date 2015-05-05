#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 118-Pascal-Triangle
# Link:     https://leetcode.com/problems/pascals-triangle/
# ==============================================================================
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# For example, given numRows = 5,
# Return
# 
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# ==============================================================================

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	return [self.helper(i) for i in range(numRows)] 

    def helper(self, num):
    	if num == 0:
    		return [1]
    	elif num == 1:
    		return [1, 1]
    	else:
    		last = self.helper(num-1)
    		current = [1]
    		for i in range(num-1):
    			current.append(last[i]+last[i+1])
    		current.append(1)
    		return current