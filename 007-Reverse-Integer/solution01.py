#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 007-Reverse-Integer
# Link:     https://leetcode.com/problems/reverse-integer/
# ==============================================================================
# Reverse digits of an integer.
# 
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# ==============================================================================

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < 0:
        	return -self.reverse(-x)
        else:
        	res = 0
        	while x:
        		res = 10 * res + x % 10
        		x = x / 10

        	if res >= 2147483648:
        		return 0
        	else:
        		return res