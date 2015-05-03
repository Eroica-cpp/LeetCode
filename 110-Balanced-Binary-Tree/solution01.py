#!/usr/bin/python
# ====================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 110-Balanced-Binary-Tree
# Link:     https://leetcode.com/problems/balanced-binary-tree/
# ====================================================================
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# ====================================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if root is None:
            return True
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.heigh(root.left) - self.heigh(root.right)) <= 1

    def heigh(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return 1 + max(self.heigh(root.left), self.heigh(root.right))

if __name__ == "__main__":
    head = TreeNode(1)
    root = head

    head.right = TreeNode(2)
    head = head.right
    
    head.right = TreeNode(3)
    head = head.right

    head.left = TreeNode(4)
    head = head.right

    print Solution().heigh(root)