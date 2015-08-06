#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 6, 2015
Question: 243-Shortest-Word-Distance
Link:     https://leetcode.com/problems/shortest-word-distance/
==============================================================================
Given a list of words and two words word1 and word2, return the shortest 
distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are 
both in the list.
==============================================================================
Method: one pass
Time Complexity: O(n) 
Space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        idx1, idx2, minVal = -float('inf'), float('inf'), float('inf')

        for i in xrange(len(words)):
            if words[i] == word1: idx1 = i
            if words[i] == word2: idx2 = i
            minVal = min(minVal, abs(idx1 - idx2))

        return minVal
