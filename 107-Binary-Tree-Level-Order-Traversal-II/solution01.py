#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 4, 2015
# Question: 107-Binary-Tree-Level-Order-Traversal-II
# Link:     https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# ==============================================================================
# Given a binary tree, return the bottom-up level order traversal of its 
# nodes' values. (ie, from left to right, level by level from leaf to root).
# ==============================================================================

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
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
        return [nodes[-(i+1)] for i in range(len(nodes))]