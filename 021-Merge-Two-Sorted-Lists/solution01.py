#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 3, 2015
# Question: 021-Merge-Two-Sorted-Lists
# Link:     https://leetcode.com/problems/merge-two-sorted-lists/
# ==============================================================================
# Merge two sorted linked lists and return it as a new list. The new list should 
# be made by splicing together the nodes of the first two lists.
# ==============================================================================
# Method: Two pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        ptr = head
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        if l1 is None:
            ptr.next = l2
        else:
            ptr.next = l1
        return head.next