#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 014-Longest-Common-Prefix
# Link:     https://leetcode.com/problems/longest-common-prefix/
# ==============================================================================
# Write a function to find the longest common prefix string amongst an array of 
# strings.
# ==============================================================================

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        idx = 0
        res = ""
        if len(strs) == 0: return res
        length = min([len(s) for s in strs])
        while idx < length:
            c = strs[0][idx]
            for s in strs:
                if s[idx] != c:
                    return res
            res += c
            idx += 1
        return res