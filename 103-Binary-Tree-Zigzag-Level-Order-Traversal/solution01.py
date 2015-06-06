#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 6, 2015
# Question: 103-Binary-Tree-Zigzag-Level-Order-Traversal
# Link:     https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# ==============================================================================
# Given a binary tree, return the zigzag level order traversal of its nodes' 
# values. (ie, from left to right, then right to left for the next level and 
# alternate between).

# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
# ==============================================================================
# Method: BFS
# Time Complexity: Exp
# Space Complexity: O(n)
# ==============================================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        counter = 0
        level = [root]
        res = []

        while level:
            counter += 1
            
            if counter%2 == 1:
                res.append([level[i].val for i in xrange(0, len(level))])
            else:
                res.append([level[i].val for i in xrange(len(level)-1, -1, -1)])
            
            new = []
            for i in level:
                if i:
                    if i.left:
                        new.append(i.left)
                    if i.right:
                        new.append(i.right)
            level = new

        return res

if __name__ == '__main__':
    root = None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print Solution().zigzagLevelOrder(root)