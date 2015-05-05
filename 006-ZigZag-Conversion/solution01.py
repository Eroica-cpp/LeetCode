#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 006-ZigZag-Conversion
# Link:     https://leetcode.com/problems/zigzag-conversion/
# ==============================================================================
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number 
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string text, int nRows);
# 
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# ==============================================================================

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
		if numRows == 1 or len(s) <= numRows: 
			return s
		div = 2 * numRows - 2
		dic = {}
		for i in range(numRows):
			dic[i] = ""
		for j in range(len(s)):
			mod = j % div
			if mod <= (numRows-1):
				dic[mod] += s[j]
			else:
				dic[numRows-1-(mod-(numRows-1))] += s[j]
		newStr = ""
		for k in range(numRows):
			newStr += dic[k]
		return newStr