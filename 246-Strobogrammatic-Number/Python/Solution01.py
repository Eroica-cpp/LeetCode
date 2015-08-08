#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 8, 2015
Question: 246-Strobogrammatic-Number
Link:     https://leetcode.com/problems/strobogrammatic-number/
==============================================================================
A strobogrammatic number is a number that looks the same when rotated 180 
degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number 
is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
==============================================================================
Method: trivial
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        properSet = {"0", "1", "8"}

        for i in xrange(len(num) / 2 + 1):
            if num[i] == "6":
                if num[-i-1] != "9": return False
            elif num[i] == "9":
                if num[-i-1] != "6": return False
            elif num[i] not in properSet or num[-i-1] not in properSet: 
                return False
            elif num[i] != num[-i-1]:
                return False

        return True
