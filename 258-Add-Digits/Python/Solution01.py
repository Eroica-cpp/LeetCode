#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 16, 2015
Question: 258-Add-Digits
Link:     https://leetcode.com/problems/binary-tree-paths/
==============================================================================
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods?
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
==============================================================================
Method: python build-in
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
"""

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        while num >= 10:
            num = sum([int(i) for i in str(num)])
        return num
