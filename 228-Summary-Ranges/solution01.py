#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 26, 2015
Question: 228-Summary-Ranges
Link:     https://leetcode.com/problems/summary-ranges/
==============================================================================
Given a sorted integer array without duplicates, return the summary of its 
ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
==============================================================================
Method: 
==============================================================================
"""

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        size = len(nums)
        if not size:
            return []

        res = []
        start = nums[0]
        i = 0
        while i < size:
            j = i + 1
            while j < size and nums[j] - nums[j-1] == 1:
                j += 1
            if nums[j-1] != start:
                res.append("%d->%d" % (start, nums[j-1]))
            else:
                res.append(str(start))

            if j < size:
                start = nums[j]

            i = j

        return res

if __name__ == '__main__':
    nums = [1,2,4]
    print Solution().summaryRanges(nums)