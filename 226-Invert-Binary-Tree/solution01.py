#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 13, 2015
# Question: 226-Invert-Binary-Tree
# Link:     https://leetcode.com/problems/invert-binary-tree/
# ==============================================================================
# Invert a binary tree.
# 
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 
# to
# 
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# ==============================================================================
# Method: traverse (any traverse methods: pre/mid/post-order is ok)
# Time Complexity: O(n), n is the number of nodes
# Space Complexity: O(1), no stack is used
# ==============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        head = root
        self.traverse(root)
        return head

    def traverse(self, root):
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        self.traverse(root.left)
        self.traverse(root.right)

