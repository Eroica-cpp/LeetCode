#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 29, 2015
Question: 259-3Sum-Smaller
Link:     https://leetcode.com/problems/3sum-smaller/
==============================================================================
Given an array of n integers nums and a target, find the number of index 
triplets i, j, k with 0 <= i < j < k < n that satisfy the condition 
nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?
==============================================================================
Method: sort first
Time Complexity: O(n^2)
Space Complexity: O(1)
==============================================================================
"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        counter = 0
        for i in xrange(size-2):
            begin, end = i + 1, size - 1
            while begin < end:
                if nums[i] + nums[begin] + nums[end] < target:
                    counter += end - begin
                    begin += 1
                else:
                    end -= 1

        return counter
