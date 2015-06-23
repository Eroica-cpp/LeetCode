#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 23, 2015
Question: 115-Distinct-Subsequences
Link:     https://leetcode.com/problems/distinct-subsequences/
==============================================================================
Given a string S and a string T, count the number of distinct subsequences of 
T in S.

A subsequence of a string is a new string which is formed from the original 
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters. (ie, "ACE" is a subsequence 
of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
==============================================================================
Method: DP
Time Complexity: O(n^2)
Space Complexity: O(n)
Note: 
1.Reference: http://blog.csdn.net/linhuanmars/article/details/23589057
2. extremely concise code!
==============================================================================
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        if not t:
            return 1
        if not s:
            return 0

        res = [0] * (len(t)+1)
        res[0] = 1
        for i in xrange(len(s)):
            for j in xrange(len(t)-1,-1,-1):
                res[j+1] += res[j] if s[i] == t[j] else 0

        return res[-1]

if __name__ == '__main__':
    s, t = "rabbbit||rabbit", "rabbit"
    s, t = "aacaacca", "ca"
    s, t = "aaa||aaaa", "ab"
    s, t = "", ""
    s, t = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe", "bddabdcae"
    print Solution().numDistinct(s, t)
