#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 6, 2015
Question: 245-Shortest-Word-Distance-III
Link:     https://leetcode.com/problems/shortest-word-distance-iii/
==============================================================================
This is a follow up of Shortest Word Distance. The only difference is now word1 
could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance 
between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "makes", word2 = "coding", return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
==============================================================================
Method: treat two cases - same words and different words - seperately
Time Complexity: O(n)
Space Complexity: O(1)
Note: extend from #243-Shortest-Word-Distance directly,
try to find a conciser solution !!
==============================================================================
"""

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        return self.sameWord(words, word1) if word1 == word2 else self.diffWord(words, word1, word2)

    def diffWord(self, words, word1, word2):
        idx1, idx2, minVal = -float('inf'), float('inf'), float('inf')

        for i in xrange(len(words)):
            if words[i] == word1: idx1 = i
            if words[i] == word2: idx2 = i
            minVal = min(minVal, abs(idx1 - idx2))

        return minVal

    def sameWord(self, words, word1):
        idx = [i for i in xrange(len(words)) if words[i] == word1]
        minVal = float('inf')
        for i in xrange(len(idx) - 1):
            minVal = min(minVal, abs(idx[i + 1] - idx[i]))
        return minVal

if __name__ == '__main__':
    words, word1, word2 = ["a","a"], "a", "a"
    print Solution().shortestWordDistance(words, word1, word2)
