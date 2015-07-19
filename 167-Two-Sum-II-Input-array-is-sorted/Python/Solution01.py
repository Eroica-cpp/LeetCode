#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 19, 2015
Question: 167-Two-Sum-II-Input-array-is-sorted
Link:     https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
==============================================================================
Given an array of integers that is already sorted in ascending order, find two 
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they 
add up to the target, where index1 must be less than index2. Please note that 
your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
==============================================================================
Method: two pointers
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param {integer[]} numbers
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, numbers, target):
        low, high = 0, len(numbers)-1
        while low < high:
            summ = numbers[low] + numbers[high]
            if summ < target:
                low += 1
            elif summ > target:
                high -= 1
            else:
                return [low+1, high+1]
