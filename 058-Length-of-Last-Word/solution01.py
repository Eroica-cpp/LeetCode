#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 058-Length-of-Last-Word
# Link:     https://leetcode.com/problems/length-of-last-word/
# ==============================================================================
# Given a string s consists of upper/lower-case alphabets and empty space 
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space 
# characters only.
# 
# For example, 
# Given s = "Hello World",
# return 5.
# ==============================================================================

class Solution:
	# @param {string} s
	# @return {integer}
	def lengthOfLastWord(self, s):
		last, current = 0, 0
		c = ''
		for c in s:
			if c != ' ':
				current += 1
				last = current
			else:
				current = 0
	
		if c == ' ':
			return last
		else:
			return current