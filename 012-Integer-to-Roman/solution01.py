#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 1, 2015
# Question: 012-Integer-to-Roman
# Link:     https://leetcode.com/problemset/algorithms/
# ==============================================================================
# Given an integer, convert it to a roman numeral.
# 
# Input is guaranteed to be within the range from 1 to 3999.
# ==============================================================================
# Note:
# 1. What the hell...
# 2. Reference1: http://zh.wikipedia.org/wiki/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97
# 3. Reference2: http://blog.csdn.net/havenoidea/article/details/11848921
# ==============================================================================

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        string = ""

        i = 0
        while num > 0:
            while num >= values[i]:
                num -= values[i]
                string += symbols[i]
            i += 1

        return string

if __name__ == '__main__':
    test = range(1,50)
    for i in test:
        print Solution().intToRoman(i)