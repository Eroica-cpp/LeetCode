#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 6, 2015
# Question: 116-Populating-Next-Right-Pointers-in-Each-Node
# Link:     https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# ==============================================================================
# Given a binary tree
# 
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no 
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the 
# same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
# ==============================================================================
# Method: Level Traverse
# Time Complexity: O(2^n)
# Space Complexity: O(1)
# ==============================================================================

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
        if not root:
            return
        queue = [root]
        while True:
            new = []
            for i in range(len(queue)-1):
                if not queue[i]: return
                new.append(queue[i].left)
                new.append(queue[i].right)
                queue[i].next = queue[i+1]
            new.append(queue[-1].left)
            new.append(queue[-1].right)
            queue[-1].next = None
            queue = new