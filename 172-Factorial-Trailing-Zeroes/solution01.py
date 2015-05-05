#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 172-Factorial-Trailing-Zeroes
# Link:     https://leetcode.com/problems/factorial-trailing-zeroes/
# ==============================================================================
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note: Your solution should be in logarithmic time complexity.
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {integer}
	def trailingZeroes(self, n):
		if n < 5: 
			return 0
		x = 5
		res = 0
		while n >= x:
			res += n / x
			x *= 5
		return res