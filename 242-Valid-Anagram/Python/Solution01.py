#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 1, 2015
Question: 242-Valid-Anagram
Link:     https://leetcode.com/problems/valid-anagram/
==============================================================================
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
==============================================================================
Method: two passes; use ascii number
Time Complexity: O(n)
Space Complexity: O(1)
Note: only 26 lowercase alphabets, thus having O(1) space complexity
==============================================================================
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        counter_s = [0] * 26
        counter_t = [0] * 26

        for i in s:
            counter_s[ord(i) - ord('a')] += 1

        for j in t:
            counter_t[ord(j) - ord('a')] += 1

        return not any([counter_s[k]-counter_t[k] for k in range(26)])
