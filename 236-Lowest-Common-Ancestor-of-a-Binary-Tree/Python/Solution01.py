#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 13, 2015
Question: 236-Lowest-Common-Ancestor-of-a-Binary-Tree
Link:     https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
====================================================================================
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
between two nodes v and w as the lowest node in T that has both v and w as descendants 
(where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example 
is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to 
the LCA definition.
====================================================================================
Method: brute force; recursion
Time Complexity: O(n^2)
Space Complexity: O(n^2)
Note: 
1. OK but apparently TLE
2. cpp version AC while py version TLE ...
====================================================================================
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if not root: return
        if id(root) == id(p) or id(root) == id(p): return root

        pInLeft = self.inSubtree(root.left, p)
        qInLeft = self.inSubtree(root.left, q)
        if pInLeft == qInLeft == True:
            return self.lowestCommonAncestor(root.left, p, q)
        elif pInLeft == qInLeft == False:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def inSubtree(self, root, node):
        if not root: return False
        
        if id(root) == id(node): 
            return True
        else:
            return self.inSubtree(root.left, node) or self.inSubtree(root.right, node)
