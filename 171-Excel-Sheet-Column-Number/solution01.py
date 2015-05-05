#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 171-Excel-Sheet-Column-Number
# Link:     https://leetcode.com/problems/excel-sheet-column-number/
# ==============================================================================
# Related to question Excel Sheet Column Title
# 
# Given a column title as appear in an Excel sheet, return its corresponding 
# column number.
# 
# For example:
# 
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {integer}
	def __init__(self):
		self.alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	def titleToNumber(self, s):
		length = len(s)
		return sum([26**i*(self.alpha.index(s[length-1-i])+1) for i in range(length)])
		