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
Method: Recursion
Time Complexity: Exp
Space Complexity: O(1) # tail recursion
Note: ok but TLE
====================================================================================
"""

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3

        if s1[0] != s3[0] and s2[0] != s3[0]:
            return False
        elif s1[0] == s3[0] and s2[0] == s3[0]:
            return self.isInterleave(s1[1:],s2,s3[1:]) or self.isInterleave(s1,s2[1:],s3[1:])
        elif s1[0] == s3[0]:
            return self.isInterleave(s1[1:],s2,s3[1:])
        elif s2[0] == s3[0]:
            return self.isInterleave(s1,s2[1:],s3[1:])

if __name__ == '__main__':
    s1,s2,s3 = "aabcc","dbbca","aadbbcbcac"
    s1,s2,s3 = "aabcc","dbbca","aadbbbaccc"
    s1,s2,s3 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    print Solution().isInterleave(s1,s2,s3)