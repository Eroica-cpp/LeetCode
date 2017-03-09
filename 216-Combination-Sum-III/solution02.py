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

# ==============================================================================

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        return self.helper(k, n, 1)

    def helper(k, n, cur):
        

if __name__ == '__main__':
    k, n = 6, 30
    print Solution().combinationSum3(k, n)