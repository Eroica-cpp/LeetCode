#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jul 2, 2015
Question: 230-Kth-Smallest-Element-in-a-BST
Link:     https://leetcode.com/problems/kth-smallest-element-in-a-bst/
==============================================================================
Given a binary search tree, write a function kthSmallest to find the kth 
smallest element in it.

Note: 
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to 
find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
==============================================================================
Method: inorder traverse
Time Complexity: O(n)
Space Complexity: O(n)
==============================================================================
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        return self.inOrder(root)[k-1]

    def inOrder(self, root):
        if not root:
            return []

        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
