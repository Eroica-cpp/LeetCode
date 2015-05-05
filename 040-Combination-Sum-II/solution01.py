#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 5, 2015
# Question: 040-Combination-Sum-II
# Link:     https://leetcode.com/problems/combination-sum-ii/
# ==============================================================================
# Given a collection of candidate numbers (C) and a target number (T), find all 
# unique combinations in C where the candidate numbers sums to T.
# 
# Each number in C may only be used once in the combination.
# 
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. 
# (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# 
# For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
# A solution set is: 
# [1, 7] 
# [1, 2, 5] 
# [2, 6] 
# [1, 1, 6] 
# ==============================================================================
# Method: Recursion
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Note: An AC solution but not good enough. I seeking for a better approach to
# avoid duplication
# ==============================================================================

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        res, stack = self.helper(sorted(candidates), target, []), []
        for i in res:
            stack += [] if i in stack else [i]
        return stack

    def helper(self, candidates, target, combine):
        if not candidates:
            return []
        elif len(candidates) == 1:
            return [[candidates[-1]]+combine] if target == candidates[-1] else []
        elif target == candidates[-1]:
            return self.helper(candidates[:-1], target, combine) + [[candidates[-1]]+combine]
        elif target == 0:
            return [combine]
        elif target < 0:
            return []
        else:
            return self.helper(candidates[:-1], target, combine)+self.helper(candidates[:-1], target-candidates[-1], [candidates[-1]]+combine)

if __name__ == '__main__':
    print Solution().combinationSum2([2,3,5], 10)
    print Solution().combinationSum2([1,2], 2)
    print Solution().combinationSum2([1,1,1], 3)
    print Solution().combinationSum2([1,1,1], 2)
    print Solution().combinationSum2([2,5,2,1,2], 5)
    # for i in ans:
    #     print i