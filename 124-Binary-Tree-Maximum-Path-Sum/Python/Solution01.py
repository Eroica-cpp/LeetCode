#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 12, 2015
Question: 124-Binary-Tree-Maximum-Path-Sum
Link:     https://leetcode.com/problems/binary-tree-maximum-path-sum/
====================================================================================
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
====================================================================================
Method: DFS
====================================================================================
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        global maxVal
        maxVal = -float('inf')
        self.dfs(root)
        return maxVal

    def dfs(self, root):
        if not root: return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        total = root.val + max(left,0) + max(right,0)
        global maxVal
        maxVal = max(maxVal, total)
        
        return max(max(left,right)+root.val, root.val)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print Solution().maxPathSum(root)