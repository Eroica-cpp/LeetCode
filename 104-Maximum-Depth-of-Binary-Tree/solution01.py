#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 104-Maximum-Depth-of-Binary-Tree
# Link:     https://leetcode.com/problems/maximum-depth-of-binary-tree/
# ==============================================================================
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root 
# node down to the farthest leaf node.
# ==============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))