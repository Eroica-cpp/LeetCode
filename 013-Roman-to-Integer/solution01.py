#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 1, 2015
# Question: 013-Roman-to-Integer
# Link:     https://leetcode.com/problems/roman-to-integer/
# ==============================================================================
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
# ==============================================================================
# Method: Naive method
# Note:
# 1. Reference1: http://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97
# 2. Reference2: http://fisherlei.blogspot.com/2012/12/leetcode-roman-to-integer.html
# ==============================================================================

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        for i in xrange(len(s)):
            if i > 0 and dic[s[i]] > dic[s[i-1]]:
                res += dic[s[i]] - 2*dic[s[i-1]]
            else:
                res += dic[s[i]]
                
        return res

if __name__ == '__main__':
    roman = "MDLXXII"
    roman = "MDCLXXXIV"
    roman = "MMCXXXI"
    print Solution().romanToInt(roman)
    # print Solution().intToRoman(89)