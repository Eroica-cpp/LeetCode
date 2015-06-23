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
Note: Note: pass indices instead of whole lists to fix MLE problems
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
        size = len(inorder)
        return self.construct(inorder, postorder, 0, size-1, 0, size-1)

    def construct(self, inorder, postorder, s1, e1, s2, e2):
        if s1 > e1 or s2 > e2:
            return

        root = TreeNode(postorder[e2])
        idx = inorder.index(root.val)

        root.left = self.construct(inorder,postorder,s1,idx-1,s2,s2+idx-s1-1)
        root.right = self.construct(inorder,postorder,idx+1,e1,s2+idx-s1,e2-1)

        return root
