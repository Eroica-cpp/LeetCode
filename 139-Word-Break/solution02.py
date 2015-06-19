#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 19, 2015
# Question: 139-Word-Break
# Link:     https://leetcode.com/problems/word-break/
# ==============================================================================
# Given a string s and a dictionary of words dict, determine if s can be 
# segmented into a space-separated sequence of one or more dictionary words.
# 
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# 
# Return true because "leetcode" can be segmented as "leet code".
# ==============================================================================
# Method: DP; hash set
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not wordDict or not s:
            return False
        size = len(s)
        wordDict = set(wordDict)
        dp = [False] * (size+1)
        dp[0] = True

        for i in xrange(size+1):
            if dp[i]:
                for end in xrange(i+1, size+1):
                    if s[i:end] in wordDict:
                        dp[end] = True
        
        return dp[-1]

if __name__ == '__main__':
    s, dict = "leetcode", ["leet", "code"]
    s, dict = "aaaaaaa", ["aaaa","aa"]
    s, dict = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print Solution().wordBreak(s, dict)