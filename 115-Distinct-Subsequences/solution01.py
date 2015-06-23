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
Method: Recursion
Time Complexity: Exp
Space Complexity: Exp
Note: ok but TLE
==============================================================================
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        dic = {}
        sLength, tLength = len(s), len(t)
        sCounter, tCounter, sUnique, tUnique = [], [], [], []

        i = 0
        while i < sLength:
            j = i+1
            while j < sLength and s[j] == s[i]:
                j += 1
            sCounter.append(j-i)
            sUnique.append(s[i])
            i = j

        i = 0
        while i < tLength:
            j = i+1
            while j < tLength and t[j] == t[i]:
                j += 1
            tCounter.append(j-i)
            tUnique.append(t[i])
            i = j

        sUniqLength, tUniqLength = len(sUnique), len(tUnique)
        global res
        res = 0
        self.helper(1, sCounter, tCounter, sUnique, tUnique)
        return res

    def helper(self, tmpTimes, sCounter, tCounter, sUnique, tUnique):
        global res
        if not tUnique:
            res += tmpTimes
            return
        elif not sUnique:
            return

        if sUnique[0] == tUnique[0]:
            self.helper(tmpTimes*self.combination(sCounter[0], tCounter[0]), sCounter[1:], tCounter[1:], sUnique[1:], tUnique[1:])
            self.helper(tmpTimes, sCounter[1:], tCounter, sUnique[1:], tUnique)
        else:
            self.helper(1, sCounter[1:], tCounter, sUnique[1:], tUnique)

    def combination(self, m, n):
        val = 1
        end = m - n
        while m > end:
            val *= m
            m -= 1
        while n > 0:
            val /= n
            n -= 1
        return val

if __name__ == '__main__':
    s, t = "rabbbit||rabbit", "rabbit"
    s, t = "aacaacca", "ca"
    s, t = "aaa||aaaa", "ab"
    s, t = "", ""
    s, t = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe", "bddabdcae"
    print Solution().numDistinct(s, t)
