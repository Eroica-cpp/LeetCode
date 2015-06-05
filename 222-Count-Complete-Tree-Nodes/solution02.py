#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 5, 2015
# Question: 222-Count-Complete-Tree-Nodes
# Link:     https://leetcode.com/problems/count-complete-tree-nodes/
# ==============================================================================
# Given a complete binary tree, count the number of nodes.
# 
# Definition of a complete binary tree from Wikipedia:
# 
# In a complete binary tree every level, except possibly the last, is 
# completely filled, and all nodes in the last level are as far left 
# as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# ==============================================================================
# Method: Recursion
# Time Complexity: Exp
# Space Complexity: 1
# Note: an ok version but TLE
# ==============================================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    print Solution().countNodes(root)