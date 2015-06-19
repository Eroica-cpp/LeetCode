#!/usr/bin/python
# ==============================================================================
# Author:   Tao Li (taoli@ucsd.edu)
# Date:     Jun 19, 2015
# Question: 142-Linked-List-Cycle-II
# Link:     https://leetcode.com/problems/linked-list-cycle-ii/
# ==============================================================================
# Given a linked list, return the node where the cycle begins. If there is no 
# cycle, return null.

# Follow up:
# Can you solve it without using extra space?
# ==============================================================================
# Method: without extra space; two pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# ==============================================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head or not head.next:
            return

        p1= p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if id(p1) == id(p2):
                break

        if not p2 or not p2.next:
            return

        p1 = head
        while id(p1) != id(p2):
            p1 = p1.next
            p2 = p2.next
        
        return p1
