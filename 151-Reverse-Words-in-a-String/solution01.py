#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 15, 2015
# Question: 151-Reverse-Words-in-a-String
# Link:     https://leetcode.com/problems/reverse-words-in-a-string/
# ==============================================================================
# Given an input string, reverse the string word by word.
# 
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
# 
# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.
# 
# click to show clarification.
# 
# Clarification:
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.
# ==============================================================================
# Method: Naive method
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: using python is trivial, how about using pure C ?
# ==============================================================================

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()
        new = s.split()
        for i in xrange(len(new)/2):
            new[i], new[-i-1] = new[-i-1], new[i]
        
        return " ".join(new)
