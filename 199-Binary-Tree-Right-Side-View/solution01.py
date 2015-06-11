#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 11, 2015
# Question: 199-Binary-Tree-Right-Side-View
# Link:     https://leetcode.com/problems/binary-tree-right-side-view/
# ==============================================================================
# Given a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.
# 
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
# ==============================================================================
# Method: BFS
# Time Complexity: O(n), n is the height of the tree
# Space Complexity: O(n)
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
    def rightSideView(self, root):
        if not root:
            return []

        res = []
        line = [root]
        while line:
            res.append(line[-1].val)
            new = []
            for i in line:
                if i.left:
                    new.append(i.left)
                if i.right:
                    new.append(i.right)
            line = new

        return res