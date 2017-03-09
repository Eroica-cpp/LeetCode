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
# Method: Recursion
# Time Complexity: Exp 
# Space Complexity: O(1)
# Note: 
# 1. Refer Question #010-Regular-Expression-Matching
# 2. Preprocess input string to remove duplicates
# 3. too many branches so that time limit exceeded
# 4. Try greedy algorithm
# ==============================================================================

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if len(p) <= 1:
            return self.helper(s, p)

        new = ""
        i = 0
        while i < len(p) - 1:
            if p[i] != '*' or p[i+1] != '*':
                new += p[i]
            i += 1
        new += p[-1]

        i = 0
        p = new
        new = ""
        while i < len(p) - 3:
            if '*' in p[i:i+2] and p[i:i+2] == p[i+2:i+4]:
                i += 2
            else:
                new += p[i]
                i += 1
        if i == len(p)-2:
            new += p[-2:]
        else:
            new += p[-3:]

        i = 0
        p = new
        new = ""
        while i < len(p) - 4:
            if '*' in p[i:i+3] and p[i:i+3] == p[i+3:i+6]:
                i += 3
            else:
                new += p[i]
                i += 1
        if i == len(p)-3:
            new += p[-3:]
        else:
            new += p[-4:]

        print new
        return self.helper(s, new)

    def helper(self, s, p):
        if not p:
            return s == ""
        elif not s:
            return p.count('*') == len(p)

        if p[0] != '*':
            return (s[0] == p[0] or p[0] == '?') and self.helper(s[1:], p[1:])
        elif self.helper(s[1:], p[1:]):
            return True
        else:
            return self.helper(s[1:], p)

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