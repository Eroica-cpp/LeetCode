#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 009-Palindrome-Number
# Link:     https://leetcode.com/problems/palindrome-number/
# ==============================================================================
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# Some hints:
# Could negative integers be palindromes? (ie, -1)
# 
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# 
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
# 
# There is a more generic way of solving this problem.
# ==============================================================================

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        tmp_str = str(x)
        for i in range(0, len(tmp_str)/2):
            if tmp_str[i] != tmp_str[-(i+1)]:
                return False
        return True
