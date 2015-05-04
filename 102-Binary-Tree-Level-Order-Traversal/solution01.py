#!/usr/bin/python
# ====================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 4, 2015
# Question: 102-Binary-Tree-Level-Order-Traversal
# Link:     https://leetcode.com/problems/binary-tree-level-order-traversal/
# ====================================================================
# Given a binary tree, return the level order traversal of its nodes' 
# values. (ie, from left to right, level by level).
# ====================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if root is None:
            return []
        nodes = []
        last = [root]

        while len(last) > 0:
            nodes.append([x.val for x in last])
            new = []
            for i in last:
                if i.left:
                    new.append(i.left)
                if i.right:
                    new.append(i.right)
            last = new
        return nodes