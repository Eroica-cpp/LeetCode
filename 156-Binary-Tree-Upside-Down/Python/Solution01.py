#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 19, 2015
Question: 156-Binary-Tree-Upside-Down
Link:     https://leetcode.com/problems/binary-tree-upside-down/
==============================================================================
Given a binary tree where all the right nodes are either leaf nodes with a 
sibling (a left node that shares the same parent node) or empty, flip it upside 
down and turn it into a tree where the original right nodes turned into left 
leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
==============================================================================
Method: almost the same as reverse linked list; trivial
Time Complexity: O(n)
Space Complexity: O(1)
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
    # @return {TreeNode}
    def upsideDownBinaryTree(self, root):
        prev, prevRight, curr = None, None, root

        while curr:
            tmpLeft, tmpRight = curr.left, curr.right
            curr.left, curr.right = prevRight, prev
            prev = curr
            curr, prevRight = tmpLeft, tmpRight

        return prev
