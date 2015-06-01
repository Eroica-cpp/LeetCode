#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 1, 2015
# Question: 010-Regular-Expression-Matching
# Link:     https://leetcode.com/problems/regular-expression-matching/
# ==============================================================================
# Implement regular expression matching with support for '.' and '*'.
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# The matching should cover the entire input string (not partial).
# 
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
# 
# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true
# ==============================================================================
# Method: Recursion
# Time Complexity: Exp
# Space Complexity: O(1)
# Note: 
# 1. An ok version but apparently time limit exceeded.
# 2. Discriminate to python! C++ and java code can pass even though Exp complexity.
# 3. preprocess "p" (eliminate duplications) for efficiency
# ==============================================================================

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if len(p) <= 3:
            return self.helper(s, p)

        new = ""
        i = 0
        while i < len(p) - 3:
            if p[i+1] == '*' and p[i:i+2] == p[i+2:i+4]:
                i += 2
            else:
                new += p[i]
                i += 1
        if i == len(p)-2:
            new += p[-2:]
        else:
            new += p[-3:]
        return self.helper(s, new)

    def helper(self, s, p):
        if not p:
            return s == ""
        elif not s:
            flag = True
            for i in xrange(len(p)/2):
                flag = flag and p[2*i+1] == '*'
            return p == "" or (len(p) % 2 == 0 and flag)
        elif len(p) == 1:
            return len(s) == 1 and (p[0] == '.' or p[0] == s[0])
        
        if p[1] == '*':
            while len(s) > 0 and (p[0] == '.' or p[0] == s[0]):
                if self.helper(s, p[2:]):
                    return True
                s = s[1:]
            return self.helper(s, p[2:])
        else:
            return (p[0] == '.' or p[0] == s[0]) and self.helper(s[1:], p[1:])

if __name__ == '__main__':
    # s, p = "aa","a"
    # s, p = "aa","aa"
    # s, p = "aaa","aa"
    # s, p = "aa", "a*"
    # s, p = "aaaaa", "aa*"
    # s, p = "aa", ".*"
    # s, p = "abc", "ab.*cd"
    # s, p = "aabbc", "a*.*c"
    # s, p = "aab", ".*b"
    # s, p = "c", "cd"
    # s, p = "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*b"
    # s, p = "a", "."
    # s, p = "a", "ab*"
    # s, p = "bb", ".bab"
    # s, p = "", "a*b*c*"
    # s, p = "", "b*b*a*a*"
    s, p = "aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"
    print Solution().isMatch(s, p)

