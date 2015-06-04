#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 4, 2015
# Question: 077-Combinations 
# Link:     https://leetcode.com/problems/combinations/
# ==============================================================================
# Given two integers n and k, return all possible combinations of k numbers 
# out of 1 ... n.
# 
# For example,
# If n = 4 and k = 2, a solution is:
# 
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# ==============================================================================
# Method: DFS
# Time Complexity: Exp
# Space Complexity: Exp
# ==============================================================================

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
    	if n <= 0 or k <= 0 or k > n:
    		return []
    		
        collection = []
        left = range(1,n+1)
        self.dfs(collection, left, k, [])
        return collection

    def dfs(self, collection, left, k, combination):
        if k <= 0:
            collection.append(combination)
            return

        for i in xrange(len(left)):
            if not combination or left[i] > combination[-1]:
	            self.dfs(collection, left[:i]+left[i+1:], k-1, combination+[left[i]])

        return

if __name__ == '__main__':
    n, k = 4, 2
    print Solution().combine(n, k)
