#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 1, 2015
Question: 241-Different-Ways-to-Add-Parentheses
Link:     https://leetcode.com/problems/different-ways-to-add-parentheses/
==============================================================================
Given a string of numbers and operators, return all possible results from 
computing all the different possible ways to group numbers and operators. 
The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

==============================================================================
Method: DFS
Time Complexity: O(2^n)
Space Complexity: O(n)
Note: didn't AC cause unproper packing :(
==============================================================================
"""

import re

class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        res = []
        numbers = [int(i) for i in re.findall(ur"\d+", input)]
        symbols = re.findall(ur"[\+\-\*]", input)
        self.dfs(res, numbers, symbols)
        return sorted(res)

    def dfs(self, res, numbers, symbols):
        if not symbols:
            res.append(numbers[0])
            return

        for i in xrange(len(symbols)):
            if symbols[i] == "+":
                self.dfs(res, numbers[:i]+[numbers[i]+numbers[i+1]]+numbers[i+2:], symbols[:i]+symbols[i+1:])
            elif symbols[i] == "-":
                self.dfs(res, numbers[:i]+[numbers[i]-numbers[i+1]]+numbers[i+2:], symbols[:i]+symbols[i+1:])
            elif symbols[i] == "*":
                self.dfs(res, numbers[:i]+[numbers[i]*numbers[i+1]]+numbers[i+2:], symbols[:i]+symbols[i+1:])
