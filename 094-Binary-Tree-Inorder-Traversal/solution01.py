#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 6, 2015
# Question: 094-Binary-Tree-Inorder-Traversal
# Link:     https://leetcode.com/problems/binary-tree-inorder-traversal/
# ==============================================================================
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
# 
# Note: Recursive solution is trivial, could you do it iteratively?
# ==============================================================================
# Method: Recursion
# Time Complexity: O(2^n)
# Space Complexity: O(1)
# Note: Try iterative method.
# ==============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)