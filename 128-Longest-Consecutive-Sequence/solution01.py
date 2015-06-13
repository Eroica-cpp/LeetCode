#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 13, 2015
# Question: 128-Longest-Consecutive-Sequence
# Link:     https://leetcode.com/problems/longest-consecutive-sequence/
# ==============================================================================
# Given an unsorted array of integers, find the length of the longest 
# consecutive elements sequence.
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# 
# Your algorithm should run in O(n) complexity.
# ==============================================================================
# Method: Hash Table; visited array
# Time complexity: O(n)
# Space complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        size = len(nums)
        dic = dict([[nums[i], i] for i in xrange(size)])
        visited = [False] * size
        maxVal = 0

        for n in xrange(size):
            if not visited[n]:
                i = j = nums[n]
                while dic.get(i) is not None:
                    visited[dic.get(i)] = True
                    i -= 1
                while dic.get(j) is not None:
                    visited[dic.get(j)] = True
                    j += 1
                maxVal = max(maxVal, j-i-1)

        return maxVal

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2, 300, 5]
    nums = [1,2,2,200]
    print Solution().longestConsecutive(nums)