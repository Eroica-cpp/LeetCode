#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 6, 2015
# Question: 113-Path-Sum-II
# Link:     https://leetcode.com/problems/path-sum-ii/
# ==============================================================================
# Given a binary tree and a sum, find all root-to-leaf paths where each path's 
# sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# ==============================================================================
# Method: DFS
# Time Complexity: Exp
# Space Complexity: O(1)
# ==============================================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, summ):
        if not root:
            return []
        collection = []
        self.dfs(collection, [], root, summ)
        return collection

    def dfs(self, collection, combine, root, summ):
        if not root:
            return
        elif not root.left and not root.right:
            if root.val == summ:
                collection.append(combine+[root.val])
            return
        else:
            self.dfs(collection, combine+[root.val], root.left, summ-root.val)
            self.dfs(collection, combine+[root.val], root.right, summ-root.val)
            return

if __name__ == '__main__':
    root = None

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(10)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    summ = 6
    
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    summ = 22

    print Solution().pathSum(root, summ)