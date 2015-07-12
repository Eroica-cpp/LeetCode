#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 12, 2015
Question: 091-Decode-Ways
Link:     https://leetcode.com/problems/decode-ways/
====================================================================================
A message containing letters from A-Z is being encoded to numbers using the following 
mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to 
decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
====================================================================================
Method: DP
====================================================================================
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s or s[0] == "0" : return 0

        prev, curr = 0, 1
        for i in xrange(1,len(s)+1):
            if s[i-1] == "0": curr = 0
            if i < 2 or not (s[i-2]=="1" or (s[i-2]=="2" and int(s[i-1])<=6)): prev = 0
            tmp = curr
            curr += prev
            prev = tmp

        return curr

if __name__ == '__main__':
    s = "10"
    print Solution().numDecodings(s)