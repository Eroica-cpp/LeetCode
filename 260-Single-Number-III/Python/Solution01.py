#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 29, 2015
Question: 260-Single-Number-III
Link:     https://leetcode.com/problems/single-number-iii/
==============================================================================
Given an array of numbers nums, in which exactly two elements appear only once 
and all the other elements appear exactly twice. Find the two elements that 
appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
1. The order of the result is not important. So in the above example, [5, 3] is also correct. 
2. Your algorithm should run in linear runtime complexity. 
3. Could you implement it using only constant space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
==============================================================================
Method: hash table
Time Complexity: O(n)
Space Complexity: O(n)
==============================================================================
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            dic[i] = dic[i] + 1 if dic.has_key(i) else 1

        res = []
        for key, val in dic.items():
            if val == 1:
                res.append(key)

        return res
