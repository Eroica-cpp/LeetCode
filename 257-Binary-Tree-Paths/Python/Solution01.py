#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 16, 2015
Question: 257-Binary-Tree-Paths
Link:     https://leetcode.com/problems/binary-tree-paths/
==============================================================================
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
==============================================================================
Method: DFS
Time Complexity: O(n)
Space Complexity: O(1)
==============================================================================
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        s = ""
        self.dfs(res, s, root)
        return res
        
    def dfs(self, res, s, root):
        if not root: return
        if not root.left and not root.right:
            res.append(s+str(root.val))
            return
        
        self.dfs(res, s+str(root.val)+"->", root.left)
        self.dfs(res, s+str(root.val)+"->", root.right)
