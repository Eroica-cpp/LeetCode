#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 4, 2015
# Question: 043-Multiply-Strings
# Link:     https://leetcode.com/problems/multiply-strings/
# ==============================================================================
# Given two numbers represented as strings, return multiplication of the 
# numbers as a string.
# 
# Note: The numbers can be arbitrarily large and are non-negative.
# ==============================================================================
# Method: build-in multiplication method
# Note: Lazy boy~ simulate the multiplication operation in regits next time
# ==============================================================================

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))