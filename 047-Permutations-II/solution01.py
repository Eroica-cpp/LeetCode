#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 3, 2015
# Question: 047-Permutations-II
# Link:     https://leetcode.com/problems/permutations-ii/
# ==============================================================================
# Given a collection of numbers that might contain duplicates, return 
# all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
# ==============================================================================
# Method: DFS; hash table to remove duplcates
# Time Complexity: Exp
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        collection = []
        self.dfs(collection, [], nums)
        return collection

    def dfs(self, collection, combine, left):
        if not left:
            collection.append(combine)
            return

        dic = {}
        for i in xrange(len(left)):
            if not dic.get(left[i]):
                self.dfs(collection, combine+[left[i]], left[:i]+left[i+1:])
                dic[left[i]] = 1

if __name__ == '__main__':
    nums = [1,2,3]
    nums = [1,2]
    nums = [1,1]
    nums = [1,1,1]
    nums = [1,1,2]
    nums = [1,1,1,2]
    print Solution().permuteUnique(nums)
