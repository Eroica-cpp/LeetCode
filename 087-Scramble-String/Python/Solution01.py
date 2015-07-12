#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 12, 2015
Question: 087-Scramble-String
Link:     https://leetcode.com/problems/scramble-string/
====================================================================================
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
====================================================================================
Method: Recursion; pruning
====================================================================================
"""

class Solution:
    # @param s1, a string
    # @param s2, a string
    # @return a boolean
    def isScramble(self, s1, s2):
        size = len(s1)
        if size != len(s2) or sorted(s1) != sorted(s2): return False
        if size < 4 or s1 == s2: return True

        for i in xrange(1, size):
            if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]) ):
                return True

        return False
