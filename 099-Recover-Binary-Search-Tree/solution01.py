#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 20, 2015
Question: 099-Recover-Binary-Search-Tree
Link:     https://leetcode.com/problems/recover-binary-search-tree/
==============================================================================
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a 
constant space solution?
==============================================================================
Method: using O(n) space
Time Complexity: Exp
Space Complexity: O(n)
==============================================================================
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        stack = []
        self.inOrderGet(root, stack)
        print stack
        stack.reverse()
        self.inOrderPut(root, stack)

    def inOrderGet(self, root, stack):
        if not root:
            return
        self.inOrderGet(root.left, stack)
        stack.append(root.val)
        self.inOrderGet(root.right, stack)
    
    def inOrderPut(self, root, stack):
        if not root:
            return
        self.inOrderPut(root.left, stack)
        root.val = stack.pop()
        self.inOrderPut(root.right, stack)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    Solution().recoverTree(root)