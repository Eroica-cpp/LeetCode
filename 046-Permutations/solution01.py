#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 3, 2015
# Question: 046-Permutations
# Link:     https://leetcode.com/problems/permutations/
# ==============================================================================
# Given a collection of numbers, return all possible permutations.
# 
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
# ==============================================================================
# Method: DFS
# Time Complexity: Exp
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        collection = []
        self.dfs(collection, [], nums)
        return collection

    def dfs(self, collection, combine, left):
        if not left:
            collection.append(combine)
            return

        for i in xrange(len(left)):
            self.dfs(collection, combine+[left[i]], left[:i]+left[i+1:])

if __name__ == '__main__':
    # nums = [1,2,3]
    nums = [1,2]
    print Solution().permute(nums)
