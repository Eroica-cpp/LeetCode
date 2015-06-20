#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 20, 2015
Question: 098-Validate-Binary-Search-Tree
Link:     https://leetcode.com/problems/validate-binary-search-tree/
====================================================================================
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
====================================================================================
Method: Naive method
Time Complexity: O(n)
Space Complexity: O(1)
====================================================================================
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, root, minVal, maxVal):
        if not root:
            return True
        if not minVal < root.val < maxVal:
            return False

        leftVal = root.left.val if root.left else -float('inf')
        rightVal = root.right.val if root.right else float('inf')

        return self.helper(root.left, minVal, root.val) and leftVal < root.val < rightVal and self.helper(root.right, root.val, maxVal)
