#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 21, 2015
Question: 097-Interleaving-String
Link:     https://leetcode.com/problems/interleaving-string/
====================================================================================
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
====================================================================================
Method: two-dimensional DP
Time Complexity: O(n^2)
Space Complexity: O(n^2)
====================================================================================
"""

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        size1, size2 = len(s1), len(s2)
        if size1+size2 != len(s3):
            return False
        elif not s1 or not s2:
            return s1+s2 == s3

        dp = [[False]*(size2+1) for _ in xrange(size1+1)]
        dp[0][0] = True
        for i in xrange(1,size1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]      
        for j in xrange(1,size2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in xrange(1,size1+1):
            for j in xrange(1, size2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]

if __name__ == '__main__':
    s1,s2,s3 = "aabcc","dbbca","aadbbcbcac"
    s1,s2,s3 = "aabcc","dbbca","aadbbbaccc"
    s1,s2,s3 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    s1,s2,s3 = "aa", "ab", "abaa"
    print Solution().isInterleave(s1,s2,s3)