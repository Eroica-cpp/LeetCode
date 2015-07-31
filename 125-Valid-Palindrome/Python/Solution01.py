#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 125-Valid-Palindrome
# Link:     https://leetcode.com/problems/valid-palindrome/
# ==============================================================================
# Given a string, determine if it is a palindrome, considering only 
# alphanumeric characters and ignoring cases.
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# Note:
# Have you consider that the string might be empty? This is a good question 
# to ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
# ==============================================================================
# Method: Two passes
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        new = "".join([i.lower() for i in s if i.isalpha() or i.isdigit()])
        size = len(new)
        i = 0
        while i < size/2:
            if new[i] != new[-i-1]:
                return False
            i += 1
        return True
