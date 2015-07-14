#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 038-Count-and-Say
# Link:     https://leetcode.com/problems/count-and-say/
# ==============================================================================
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        res = str(1)
        while n > 1:
            n -= 1
            res = self.say(res)
        return res

    def say(self, s):
        if len(s) == 1:
            return '1'+s
        last = s[0]
        newStr = ""
        counter = 1
        for i in s[1:]:
            if last == i:
                counter += 1
            else:
                newStr += str(counter)+last
                last = i
                counter = 1
        newStr += str(counter)+last
        return newStr