#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 3, 2015
# Question: 060-Permutation-Sequence
# Link:     https://leetcode.com/problems/permutation-sequence/
# ==============================================================================
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
# 
# Note: Given n will be between 1 and 9 inclusive.
# ==============================================================================
# Method: Treat as a n!-carry number system
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        if n <= 0:
            return ""

        carry = []
        i = fac = 1
        while i < n:
            carry.append(fac)
            i += 1
            fac *= i

        if k <= 0 or k > fac:
            return ""

        permutation = []
        digits = range(1, n+1)
        k -= 1
        
        while n > 1:
            n -= 1
            div = carry.pop()
            idx = k/div
            digit = digits[idx]
            digits.remove(digit)
            permutation.append(digit)
            k %= div

        permutation.append(digits[-1])

        return "".join([str(i) for i in permutation])

if __name__ == '__main__':
    n, k = 6,719
    print Solution().getPermutation(n, k)
