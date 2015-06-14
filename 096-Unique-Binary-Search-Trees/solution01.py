#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 13, 2015
# Question: 096-Unique-Binary-Search-Trees
# Link:     https://leetcode.com/problems/unique-binary-search-trees/
# ==============================================================================
# Given n, how many structurally unique BST's (binary search trees) 
# that store values 1...n?
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# ==============================================================================
# Method: DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n <= 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in xrange(2, n+1):
            for j in xrange(0, i):
                dp[i] += dp[j] * dp[i-j-1]

        return dp[-1]

if __name__ == '__main__':
    n = 3
    print Solution().numTrees(n)