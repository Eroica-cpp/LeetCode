#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 1, 2015
# Question: 083-Remove-Duplicates-from-Sorted-List
# Link:     https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# ==============================================================================
# Given a sorted linked list, delete all duplicates such that each element 
# appear only once.
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
# ==============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        ptr = head
        while ptr:
            ptr.next = self.findNext(ptr)
            ptr = ptr.next
        return head

    def findNext(self, head):
        if not head or not head.next:
            return None
        elif head.val != head.next.val:
            return head.next
        else:
            return self.findNext(head.next)