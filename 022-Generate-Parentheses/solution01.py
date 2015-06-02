#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 30, 2015
# Question: 022-Generate-Parentheses
# Link:     https://leetcode.com/problems/generate-parentheses/
# ==============================================================================
# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:
# 
# "((()))", "(()())", "(())()", "()(())", "()()()"
# ==============================================================================
# Method: Deep First Search (dfs)
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n <= 0:
            return []

        collect = []
        self.dfs(collect, "", n, n)
        return collect

    def dfs(self, collect, string, leftNum, rightNum):
        if leftNum < rightNum:
            return

        if leftNum == 0 and rightNum == 0:
            collect.append(string)
        if leftNum > 0:
            self.dfs(collect, string+')', leftNum-1, rightNum)
        if rightNum > 0:
            self.dfs(collect, string+'(', leftNum, rightNum-1)

if __name__ == '__main__':
    n = 3
    print Solution().generateParenthesis(n)