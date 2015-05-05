#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 5, 2015
# Question: 129-Sum-Root-to-Leaf-Numbers
# Link:     https://leetcode.com/problems/sum-root-to-leaf-numbers/
# ==============================================================================
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path 
# could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# ==============================================================================
# Method: Recursion
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
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
    def sumNumbers(self, root):
        return self.helper(root, 0) if root else 0

    def helper(self, root, total):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 10*total + root.val
        else:
            total = 10*total + root.val
            return self.helper(root.left, total) + self.helper(root.right, total)

if __name__ == '__main__':
    head = TreeNode(4)
    head.left = TreeNode(9)
    head.right = TreeNode(0)
    head.left.right = TreeNode(1)
    print Solution().sumNumbers(head)
