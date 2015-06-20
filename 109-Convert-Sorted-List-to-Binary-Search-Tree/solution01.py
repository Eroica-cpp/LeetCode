#!/usr/bin/python
"""
====================================================================================
Author:   Tao Li (taoli@ucsd.edu)
Date:     Jun 20, 2015
Question: 109-Convert-Sorted-List-to-Binary-Search-Tree
Link:     https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
====================================================================================
Given a singly linked list where elements are sorted in ascending order, convert it 
to a height balanced BST.
====================================================================================
Method: Recursion; binary construction; use extra space
Time Complexity: O(n)
Space Complexity: O(n)
Note: almost the same as question #108-Convert-Sorted-Array-to-Binary-Search-Tree
====================================================================================
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.createTree(nums, 0, len(nums)-1)
    
    def createTree(self, nums, left, right):
        if left > right:
            return None

        mid = (left + right) / 2
        node = TreeNode(nums[mid])
        node.left = self.createTree(nums,left,mid-1)
        node.right = self.createTree(nums,mid+1,right)

        return node
