#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 19, 2015
# Question: 143-Reorder-List
# Link:     https://leetcode.com/problems/reorder-list/
# ==============================================================================
# Given a singly linked list L: L0->L1->...->Ln-1->Ln,
# reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2→…
# 
# You must do this in-place without altering the nodes' values.
# 
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
# ==============================================================================
# Method: Use extra space
# Time Complexity: O(n)
# Space Complexity: O(n)
# ==============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head:
            return

        stack = []
        size = 0
        while head:
            stack.append(head)
            head = head.next
            size += 1

        new = []
        counter = size 
        while counter >= 2:
            new.append(stack.pop(0))
            new.append(stack.pop())
            counter -= 2

        if stack:
            new.append(stack.pop())

        for i in xrange(size-1):
            new[i].next = new[i+1]
        new[-1].next = None
