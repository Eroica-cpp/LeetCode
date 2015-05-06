#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 141-Linked-List-Cycle
# Link:     https://leetcode.com/problems/binary-tree-preorder-traversal/
# ==============================================================================
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
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
    def preorderTraversal(self, root):
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)