#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 27, 2015
Question: 095-Unique-Binary-Search-Trees-II
Link:     https://leetcode.com/problems/unique-binary-search-trees-ii/
==============================================================================
Given n, generate all structurally unique BST's (binary search trees) that 
store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
==============================================================================
Method: refer from question #096-Unique-Binary-Search-Trees
Reference: http://www.cnblogs.com/springfor/p/3884029.html?utm_source=tuicool
==============================================================================
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self.construct(1, n)

    def construct(self, left, right):
        res = []
        if left > right:
            res.append(None)
            return res

        for i in xrange(left, right+1):
            leftSubTree = self.construct(left, i-1)
            rightSubTree = self.construct(i+1,right)
            for l in leftSubTree:
                for r in rightSubTree:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)

        return res
