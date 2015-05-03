#!/usr/bin/python
# ====================================================================
# Question 067-Add-Binary:
# Given two binary strings, return their sum (also a binary string).
# 
# For example,
# a = "11"
# b = "1"
# Return "100".
# ====================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# ====================================================================

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        total = 0
        a_size, b_size = len(a), len(b)
        for i in range(a_size):
            total += int(a[i]) * 2**(a_size-i-1)
        for j in range(b_size):
            total += int(b[j]) * 2**(b_size-j-1)
        return self.int2binary(total)

    def int2binary(self, n):
        stack = []
        while n >= 2:
            stack.append(n%2)
            n /= 2
        stack.append(n)
        binary = ""
        while stack:
            binary += str(stack.pop())
        return binary

if __name__ == "__main__":
    print Solution().addBinary("100", "1")