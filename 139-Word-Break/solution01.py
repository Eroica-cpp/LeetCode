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
# Method: python build-in re module; DFA
# Time Complexity: O(n)
# Space Complexity: Exp
# Note: ok but TLE; the DFA building process is time consuming
# ==============================================================================

import re

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not wordDict or not s:
            return False
        p = ur"^(%s)*$" % "|".join(wordDict)
        pattern = re.compile(p)
        return re.match(pattern, s) is not None

if __name__ == '__main__':
    s, dict = "leetcode", ["leet", "code"]
    s, dict = "aaaaaaa", ["aaaa","aa"]
    s, dict = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print Solution().wordBreak(s, dict)