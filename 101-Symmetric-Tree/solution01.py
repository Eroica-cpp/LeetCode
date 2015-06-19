#!/usr/bin/python
"""
==============================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 19, 2015
Question: 101-Symmetric-Tree
Link:     https://leetcode.com/problems/symmetric-tree/
==============================================================================
Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
==============================================================================
Method: BFS
Time Complexity: Exp
Space Complexity: O(n)
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
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True

        line = [root]
        while line and line.count(None) != len(line):
            new = []
            for i in line:
                if i:
                    new += [i.left, i.right]
            for i in xrange(len(new)/2):
                if new[i] == new[-i-1] == None:
                    continue
                elif not new[i] or not new[-i-1] or new[i].val != new[-i-1].val:
                    return False
            line = new

        return True

if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(2)
    tree1.right.right = TreeNode(3)
    tree1.left.left = TreeNode(3)
    print Solution().isSymmetric(tree1)
