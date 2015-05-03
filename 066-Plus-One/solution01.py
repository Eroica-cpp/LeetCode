#!/usr/bin/python
# ====================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 066-Plus-One
# Link:     https://leetcode.com/problems/plus-one/
# ====================================================================
# Given a non-negative number represented as an array of digits, plus one to the number.
# 
# The digits are stored such that the most significant digit is at the head of the list.
# ====================================================================
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        size = len(digits)
        i = 1
        while True:
            if i > size:
                return [1] + digits
            if digits[-i] != 9:
                digits[-i] += 1
                return digits
            else:
                digits[-i] = 0
            i += 1 

if __name__ == "__main__":
    print Solution().plusOne([9,9,9,9,9])