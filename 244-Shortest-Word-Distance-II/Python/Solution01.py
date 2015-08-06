#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 6, 2015
Question: 244-Shortest-Word-Distance-II
Link:     https://leetcode.com/problems/shortest-word-distance-ii/
==============================================================================
This is a follow up of Shortest Word Distance. The only difference is now you 
are given the list of words and your method will be called repeatedly many 
times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and 
implements a method that takes two words word1 and word2 and return the shortest 
distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are 
both in the list.
==============================================================================
Method: hash table, where keys are words and values are their indice.
Time Complexity: 
- construct, O(n)
- search, O(1)
Space Complexity: O(n)
==============================================================================
"""

class WordDistance:
    # initialize your data structure here.
    # @param {string[]} words
    def __init__(self, words):
        self.dic = {}
        for i in xrange(len(words)):
            if self.dic.has_key(words[i]):
                self.dic[words[i]].append(i)
            else:
                self.dic[words[i]] = [i]

    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    # Adds a word into the data structure.
    def shortest(self, word1, word2):
        idx1 = self.dic[word1]
        idx2 = self.dic[word2]
        m, n = len(idx1), len(idx2)
        i, j, minVal = 0, 0, float('inf')
   
        while i < m and j < n:
            minVal = min(minVal, abs(idx1[i] - idx2[j]))
            if idx1[i] < idx2[j]: i += 1
            else: j += 1

        return minVal

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")

if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1, word2 = "coding", "practice"
    word1, word2 = "makes", "coding"

    wordDistance = WordDistance(words)
    print wordDistance.shortest(word1, word2)