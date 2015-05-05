#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 190-Reverse-Bits
# Link:     https://leetcode.com/problems/reverse-bits/
# ==============================================================================
# Reverse bits of a given 32 bits unsigned integer.
# 
# For example, given input 43261596 (represented in binary as 
# 	00000010100101000001111010011100), return 964176192 (represented 
# 	in binary as 00111001011110000010100101000000).
# 
# Follow up:
# If this function is called many times, how would you optimize it?
# 
# Related problem: Reverse Integer
# ==============================================================================

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	stack = []
    	counter = 0
    	while True:
    		stack.append(n % 2)
    		counter += 1
    		n /= 2
    		if n < 2:
    			stack.append(n)
    			counter += 1
    			break
    	exp = 32 - counter
    	total = 0
    	while stack:
    		total += stack.pop() * 2**exp
    		exp += 1
    	return total