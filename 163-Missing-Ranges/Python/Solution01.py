#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 19, 2015
Question: 163-Missing-Ranges
Link:     https://leetcode.com/problems/missing-ranges/
==============================================================================
Given a sorted integer array where the range of elements are [lower, upper] 
inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return 
["2", "4->49", "51->74", "76->99"].
==============================================================================
Method: trivial; add two sides
Time Complexity: O(n)
Space Complexity: O(n)
==============================================================================
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} lower
    # @param {integer} upper
    # @return {string[]}
    def findMissingRanges(self, nums, lower, upper):
        if lower == upper: return [str(lower)] if lower not in nums else []
        if not nums: return [str(lower)+"->"+str(upper)]

        if lower < nums[0]: nums = [lower-1] + nums
        if upper > nums[-1]: nums = nums + [upper+1]

        res = []
        for i in xrange(len(nums)-1):
            diff = nums[i+1] - nums[i]
            if diff == 2:
                res.append(str(nums[i]+1))
            elif diff > 2:
                res.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))

        return res

if __name__ == '__main__':
    nums, lower, upper = [0, 1, 3, 50, 75], 0, 99
    nums, lower, upper = [], 1, 1
    nums, lower, upper = [-1], -1, -1
    print Solution().findMissingRanges(nums, lower, upper)