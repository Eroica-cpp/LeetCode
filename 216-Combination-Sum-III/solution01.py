#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 30, 2015
# Question: 216-Combination-Sum-III
# Link:     https://leetcode.com/problems/combination-sum-iii/
# ==============================================================================
# Find all possible combinations of k numbers that add up to a number n, 
# given that only numbers from 1 to 9 can be used and each combination 
# should be a unique set of numbers.
# 
# Ensure that numbers within the set are sorted in ascending order.
# 
# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# ==============================================================================
# Method: Brutal force
# Note: An ok version but apprently, time limits exceeded.
# ==============================================================================

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        combine = []
        
        minVal = 0
        for i in xrange(1, k):
            minVal += i
            minVal *= 10
        minVal += i+1

        maxVal = 0
        for i in xrange(9-k+1, 9):
            maxVal += i
            maxVal *= 10
        maxVal += 9

        for i in xrange(minVal, maxVal+1):
            new = self.helper(i, k, n)
            if new:
                combine.append(new)

        return combine

    def helper(self, i, k, n):
        digits = [int(d) for d in str(i)]
        for j in xrange(1, k):
            if digits[j-1] >= digits[j]:
                return []

        return digits if sum(digits) == n else []

if __name__ == '__main__':
    k, n = 6, 30
    print Solution().combinationSum3(k, n)