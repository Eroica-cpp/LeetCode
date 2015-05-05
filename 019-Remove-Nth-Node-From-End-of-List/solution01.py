#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     May 2, 2015
# Question: 019-Remove-Nth-Node-From-End-of-List
# Link:     https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# ==============================================================================
# Given a linked list, remove the nth node from the end of list and return its head.
# 
# For example,
# 
#    Given linked list: 1->2->3->4->5, and n = 2.
# 
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
# Note:
# Given n will always be valid.
# Try to do this in one pass.
# ==============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        p1 = head
        p2 = head
        if n <= 0:
            return head
        while n > 0:
            if p1 is None: return head
            p1 = p1.next 
            n -= 1
        if p1 is None:
            head = head.next
            return head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head