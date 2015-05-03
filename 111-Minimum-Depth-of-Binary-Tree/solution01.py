#!/usr/bin/python
# ====================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 111-Minimum-Depth-of-Binary-Tree
# Link:     https://leetcode.com/problems/minimum-depth-of-binary-tree/
# ====================================================================
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# ====================================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root is None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            leftDepth = 1+self.minDepth(root.left) if root.left is not None else float("inf")
            rightDepth = 1+self.minDepth(root.right) if root.right is not None else float("inf")
            return min(leftDepth, rightDepth)

if __name__ == "__main__":
    head = TreeNode(0)
    root = head
    head.right = TreeNode(0)

    head = head.right
    head.right = TreeNode(0)    
    print Solution().minDepth(root)