#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 168-Excel-Sheet-Column-Title
# Link:     https://leetcode.com/problems/excel-sheet-column-title/
# ==============================================================================
# Given a positive integer, return its corresponding column title as appear in 
# an Excel sheet.
# 
# For example:
# 
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
# 
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {string}
	def __init__(self):
		self.alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	def convertToTitle(self, n):
		div = 26
		stack = []
		while n > div:
			stack.append(self.alpha[(n % div) - 1])
			if n % div == 0: n -= div
			n /= div
		stack.append(self.alpha[(n % div) - 1])
		title = ""
		while stack:
			title += stack.pop()
		return title