#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 13, 2015
Question: 236-Lowest-Common-Ancestor-of-a-Binary-Tree
Link:     https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
====================================================================================
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined 
between two nodes v and w as the lowest node in T that has both v and w as descendants 
(where we allow a node to be a descendant of itself)."

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
Method: recursion; two traversals - use extra space to store root path
Time Complexity: O(n)
Space Complexity: O(n)
Note: 
1. use node's address, instead of its value to identify a node.
2. there are difference nodes sharing a same value in a test case.
====================================================================================
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        pStack, qStack = [], []
        self.findPath(pStack, root, p)
        self.findPath(qStack, root, q)
        
        size = min(len(pStack), len(qStack))
        i = 0
        while i < size and pStack[i] == qStack[i]:
            i += 1

        return pStack[i-1] if i > 0 else None
    
    def findPath(self, stack, root, node):
        if not root: return False
        
        stack.append(root)
        if id(root) == id(node):
            return True

        if self.findPath(stack, root.left, node) or self.findPath(stack, root.right, node):
            return True

        stack.pop()
        return False
