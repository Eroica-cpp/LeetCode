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
Method: Naive method; maintain a window
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

        res = 0
        sUniqLength, tUniqLength = len(sUnique), len(tUnique)
        i = 0
        while i < sUniqLength:
            j = i
            if j < sUniqLength and j-i < tUniqLength and sUnique[j] == tUnique[j-i]:
                while j < sUniqLength and j-i < tUniqLength and sUnique[j] == tUnique[j-i]:
                    j += 1
                if j-i == tUniqLength:
                    stack = [self.combination(sCounter[k], tCounter[k-i]) for k in xrange(i,j)]
                    val = 1
                    while stack:
                        val *= stack.pop()
                    res += val
                i = j
            else:
                i += 1
        return res

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
    s, t = "rabbbiiitr||rabbbiiit", "rabbit"
    s, t = "aacaacca", "ca"
    print Solution().numDistinct(s, t)
    # m, n = 5,2
    # print Solution().combination(m, n)