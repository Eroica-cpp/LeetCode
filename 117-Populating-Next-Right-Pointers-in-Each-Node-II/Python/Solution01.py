#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 11, 2015
Question: 117-Populating-Next-Right-Pointers-in-Each-Node-II
Link:     https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
====================================================================================
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
====================================================================================
Method: BFS; use next point instead of a stack to maintain O(1) space complexity
Time Complexity: O(n)
Space Complexity: O(1)
====================================================================================
"""

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return

        dummy = TreeLinkNode(0)
        prev = dummy
        while root:
            if root.left:
                prev.next = root.left
                prev = prev.next
            if root.right:
                prev.next = root.right
                prev = prev.next
            root = root.next

        self.connect(dummy.next)
