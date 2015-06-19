#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 13, 2015
# Question: 089-Gray-Code
# Link:     https://leetcode.com/problems/gray-code/
# ==============================================================================
# The gray code is a binary numeral system where two successive values differ 
# in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the 
# code, print the sequence of gray code. A gray code sequence must begin with 0.
# 
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.
# 
# For example, [0,2,3,1] is also a valid gray code sequence according to the 
# above definition.
# 
# For now, the judge is able to judge based on one instance of gray code 
# sequence. Sorry about that.
# ==============================================================================
# Method: there is a math formula to generate gracode
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: about the formula: http://www.cnblogs.com/springfor/p/3889222.html?utm_source=tuicool
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        res = ["0"]
        counter = 0
        while counter < n:
            new = ["0"+i for i in res]
            for i in xrange(1,len(res)+1):
                new.append(str(int(res[-i])+10**counter))
            res = new
            counter += 1

        return [int(i, 2) for i in res]

if __name__ == '__main__':
    print Solution().grayCode(3)