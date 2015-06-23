#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 23, 2015
Question: 106-Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal
Link:     https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
==============================================================================
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
==============================================================================
Method: Recursion
Time Complexity: O(n)
Space Complexity: O(1)
Note: ok but Memory Limit Exceeded
==============================================================================
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not postorder:
            return

        root = TreeNode(postorder[-1])
        idx = inorder.index(root.val)

        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])

        return root
