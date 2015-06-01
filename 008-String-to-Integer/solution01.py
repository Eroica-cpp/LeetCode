#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 1, 2015
# Question: 008-String-to-Integer
# Link:     https://leetcode.com/problems/string-to-integer-atoi/
# ==============================================================================
# Implement atoi to convert a string to an integer.
# 
# Hint: Carefully consider all possible input cases. If you want a challenge, 
# please do not see below and ask yourself what are the possible input cases.
# 
# Notes: It is intended for this problem to be specified vaguely 
# (ie, no given input specs). You are responsible to gather all 
# the input requirements up front.
# ==============================================================================
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: Stupid question, stupid test cases.
# ==============================================================================

class Solution:
    # @param {string} string
    # @return {integer}
    def myAtoi(self, string):
        string = string.strip()
        if not string or string[0] not in ['+', '-'] + [str(j) for j in xrange(10)]:
            return 0

        symbolCounter = 0
        for i in xrange(len(string)-1):
            if string[i] in ['+', '-']:
                symbolCounter += 1
            if symbolCounter >= 2:
                return 0
            if string[i+1] not in ['+', '-'] + [str(j) for j in xrange(10)]:
                string = string[:i+1]
                break

        if len(string) == 1 and string[0] in ['-', '+']:
            return 0

        res = int(string)
        
        if res >= 2**31:
            res = 2**31 - 1
        elif res < -2**31:
            res = -2**31
        return res

if __name__ == '__main__':
    string = ""
    string = "+-2"
    string = "-+1"
    string = "  -0012a42"
    string = "   +0 123"
    string = " ---2"
    string = "-+1"
    string = "abc"
    string = "010"
    string = "    010"
    string = "123  456"
    string = " ++1"
    string = " --2"
    string = "-abc"
    string = " ++c"
    print Solution().myAtoi(string)