#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 205-Isomorphic-Strings
# Link:     https://leetcode.com/problems/isomorphic-strings/
# ==============================================================================
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while 
# preserving the order of characters. No two characters may map to the same 
# character but a character may map to itself.
# 
# For example,
# Given "egg", "add", return true.
# 
# Given "foo", "bar", return false.
# 
# Given "paper", "title", return true.
# 
# Note:
# You may assume both s and t have the same length.
# ==============================================================================

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t): return False
        dic1 = {}
        dic2 = {}
        for i in range(0, len(s)):
            if s[i] not in dic1.keys(): 
                dic1[s[i]] = t[i]
            elif dic1[s[i]] != t[i]: return False
            
            if t[i] not in dic2.keys(): 
                dic2[t[i]] = s[i]
            elif dic2[t[i]] != s[i]: return False
        return True