#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 5, 2015
# Question: 039-Combination-Sum
# Link:     https://leetcode.com/problems/combination-sum/
# ==============================================================================
# Given a set of candidate numbers (C) and a target number (T), find all unique 
# combinations in C where the candidate numbers sums to T.
# 
# The same repeated number may be chosen from C unlimited number of times.
# 
# Note:
# 1. All numbers (including target) will be positive integers.
# 2. Elements in a combination (a1, a2, ... , ak) must be in non-descending order. 
# (ie, a1 <= a2 <= ... <= ak).
# 3. The solution set must not contain duplicate combinations.
# 
# For example, given candidate set 2,3,6,7 and target 7, 
# A solution set is: 
# [7] 
# [2, 2, 3] 
# ==============================================================================
# Method: Recursion, a approximate TEN lines implementation.
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Note: Do not 'print' anything in LeetCode! It is a hard-to-fix bug that waste
# me huge amount of time.
# ==============================================================================

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        return self.helper(sorted(list(set(candidates))), target, [])

    def helper(self, candidates, target, combine):
        if not candidates:
            return []
        elif len(candidates) == 1:
            return [] if target%candidates[-1] else [[candidates[-1]]*(target/candidates[-1])+combine]  
        elif target == 0:
            return [combine]
        elif target < 0:
            return []
        else:
            return self.helper(candidates[:-1], target, combine)+self.helper(candidates, target-candidates[-1], [candidates[-1]]+combine)

if __name__ == '__main__':
    ans = Solution().combinationSum([3,4,10], 10)
    print 
    for i in ans:
        print i