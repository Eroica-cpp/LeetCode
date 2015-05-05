#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 191-Number-of-1-Bits
# Link:     https://leetcode.com/problems/number-of-1-bits/
# ==============================================================================
# Write a function that takes an unsigned integer and returns the number of ’1' 
# bits it has (also known as the Hamming weight).
# 
# For example, the 32-bit integer ’11' has binary representation 
# 00000000000000000000000000001011, so the function should return 3.
# ==============================================================================

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
    	if n == 0:
    		return 0
    	res = 0
    	while n > 1:
    		res += n % 2
    		n /= 2
    	return res + 1