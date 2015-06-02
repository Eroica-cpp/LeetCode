#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 2, 2015
# Question: 024-Swap-Nodes-in-Pairs
# Link:     https://leetcode.com/problems/swap-nodes-in-pairs/
# ==============================================================================
# Implement strStr().
# 
# Returns the index of the first occurrence of needle in haystack, or -1 if 
# needle is not part of haystack.
# ==============================================================================
# Method: Python's build-in function
# Note: Try KMP algo next time
# ==============================================================================

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        return haystack.index(needle) if needle in haystack else -1