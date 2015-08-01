#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Aug 1, 2015
# Question: 024-Swap-Nodes-in-Pairs
# Link:     https://leetcode.com/problems/swap-nodes-in-pairs/
# ==============================================================================
# Implement strStr().
# 
# Returns the index of the first occurrence of needle in haystack, or -1 if 
# needle is not part of haystack.
# ==============================================================================
# Method: brute force
# Time Complexity: O(mn)
# Space Complexity: O(1)
# Note: Try KMP algo next time
# ==============================================================================

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not needle: return 0
        elif not haystack: return -1

        idx = -1
        size = len(needle)
        for i in xrange(len(haystack)):
            if haystack[i:i+size] == needle:
                idx = i
                break

        return idx
