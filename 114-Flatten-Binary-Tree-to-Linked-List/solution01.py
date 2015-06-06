#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 6, 2015
# Question: 114-Flatten-Binary-Tree-to-Linked-List
# Link:     https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# ==============================================================================
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# 
# Hints:
# If you notice carefully in the flattened tree, each node's right child points 
# to the next node of a pre-order traversal.
# ==============================================================================
# Method: pre-order traversal; use extra queue
# Time Complexity: O(n) # n is the number of nodes
# Space Complexity: O(n)
# Note: ok but TLE
# ==============================================================================

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        queue = []
        self.preOrderTraversal(queue, root)
        for i in xrange(len(queue)-1):
            queue[i].right = queue[i+1]

    def preOrderTraversal(self, queue, root):
        if not root:
            return

        queue.append(root)
        self.preOrderTraversal(queue, root.left)
        self.preOrderTraversal(queue, root.right)
        
if __name__ == '__main__':
    root = None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    Solution().flatten(root)

    print
    while root:
        print root.val
        # if root.left:
        #     root = root.left
        # else:
        root = root.right