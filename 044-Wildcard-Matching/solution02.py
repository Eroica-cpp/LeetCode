#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 1, 2015
# Question: 044-Wildcard-Matching
# Link:     https://leetcode.com/problems/wildcard-matching/
# ==============================================================================
# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "*") -> true
# isMatch("aa", "a*") -> true
# isMatch("ab", "?*") -> true
# isMatch("aab", "c*a*b") -> false
# ==============================================================================
# Method: Greedy Algorithm
# Time Complexity: Exp 
# Space Complexity: O(1)
# Note: 
# 1. Refer Question #010-Regular-Expression-Matching
# 2. Reference: http://simpleandstupid.com/2014/10/26/wildcard-matching-leetcode-%E8%A7%A3%E9%A2%98%E7%AC%94%E8%AE%B0/
# ==============================================================================

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):

if __name__ == '__main__':
    s, p = "aa","a" # false
    # s, p = "aa","aa" # true
    # s, p = "aaa","aa" # false
    # s, p = "aa", "*" # true
    # s, p = "aa", "a*" # true
    # s, p = "ab", "?*" # true
    # s, p = "aab", "c*a*b" # false
    # s, p = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"  
    # s, p = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******"
    # s, p = "", ""
    # s, p = "abbbaaaaaaaabbbabaaabbabbbaabaabbbbaabaabbabaabbabbaabbbaabaabbabaabaabbbbaabbbaabaaababbbbabaaababbaaa", "ab**b*bb*ab**ab***b*abaa**b*a*aaa**bba*aa*a*abb*a*a"
    # s, p = "abbbaaaaaaaabbbabaaabbabbbaabaabbbbaabaabbabaabbabbaabbbaabaabbabaabaabbbbaabbbaabaaababbbbabaaababbaaa", "ab*abaa*b*a*aaa*bba*aa*abb*a"
    s, p = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
    print Solution().isMatch(s, p)