#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Aug 9, 2015
Question: 250-Count-Univalue-Subtrees
Link:     https://leetcode.com/problems/count-univalue-subtrees/
==============================================================================
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
==============================================================================
Method: one recursion
Time Complexity: O(n)
Space Complexity: O(1)
Note: failed in some cases, dont know why
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
    # @return {integer}
    def countUnivalSubtrees(self, root):
        counter = 0
        self.helper(counter, root)
        return counter

    def helper(self, counter, root):
        if not root: return False
        leftIsUniSubtree = self.helper(counter, root.left)
        rightIsUniSubtree = self.helper(counter, root.right)
        

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    print Solution().countUnivalSubtrees(root)