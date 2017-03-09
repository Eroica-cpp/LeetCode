#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 23, 2015
Question: 127-Word-Ladder
Link:     https://leetcode.com/problems/word-ladder/
====================================================================================
Given two words (beginWord and endWord), and a dictionary, find the length of 
shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
====================================================================================
Method: 
====================================================================================
"""

class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        if not beginWord or not endWord or not wordDict:
            return 0

        size = len(beginWord)
        if len(endWord) != size or not all([len(i)==size for i in wordDict]):
            return 0

        res = self.helper(beginWord, endWord, wordDict, size)
        return res if res < float('inf') else 0

    def helper(self, beginWord, endWord, wordDict, size):
        if [beginWord[i]!=endWord[i] for i in xrange(size)].count(True) == 1:
            return 0

        new = []
        for w in wordDict:
            if [beginWord[i]!=w[i] for i in xrange(size)].count(True) == 1:
                new.append(w)

        if not new:
            return float('inf')

        for w in new:
            minVal = float('inf')
            idx = wordDict.index(w)
            minVal = min(minVal, self.helper(w, endWord, endWord, wordDict[:idx]+wordDict[idx+1:]), size)

        return minVal

if __name__ == '__main__':
    beginWord, endWord, wordDict = "hit", "cog", ["hot","dot","dog","lot","log"]
    print Solution().ladderLength(beginWord, endWord, wordDict)